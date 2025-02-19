import asyncio
import logging.config
from aioslsk.client import SoulSeekClient
from aioslsk.transfer.model import Transfer
from aioslsk.settings import Settings, CredentialsSettings, SharesSettings
from aioslsk.search.model import SearchRequest
from rich.progress import Progress, BarColumn, TextColumn
from aioslsk.protocol.messages import FileSearch
from aioslsk.log_utils import MessageFilter, DistributedSearchMessageFilter
from aioslsk.events import SearchResultEvent
import logging
import time

# Create default settings and configure credentials
settings: Settings = Settings(
    credentials=CredentialsSettings(username="tobia", password="2007"),
    shares=SharesSettings(download="music"),
)

download_semaphore = asyncio.Semaphore(1)

async def limited_download_song(song, client, progress, overall_task_id):
    async with download_semaphore:
        # Only 3 tasks can be active here at once.
        return await download_song(song, client, progress, overall_task_id)#
    
async def search_result_listener(event: SearchResultEvent):
    print(f"got a search result for query: {event.query.query} : {event.query.result}")

async def download_song(song, client, progress: Progress, overall_task_id):

    query = " - ".join([song["artist"], song["song"], song["album"]])
    print("Searching with query:" + query)
    search_request: SearchRequest = await client.searches.search(query)
    await asyncio.sleep(10)
    # todo: instead of sleeping do it with evenlistener to maybe make it more efficient idk its kinda slow
    # CHECK NOTION
    download_target = await searchResults(search_request.results)

    if not download_target:
        await emergency_download_yt()
        return

    transfer: Transfer = await client.transfers.download(
        download_target["user"], download_target["filename"]
    )

    while transfer.filesize == None:
        await asyncio.sleep(0.1)

    while not transfer.is_finalized():
        await asyncio.sleep(0.5)

    progress.update(overall_task_id, advance=1)    

    print(f"Download completed: {transfer.local_path}")


async def emergency_download_yt():
    print("Downloading from youtube")


async def searchResults(results):
    if results:
        for result in results:
            for item in result.shared_items:
                if (
                    item.filename.lower().endswith(".mp3")
                    and item.attributes[0].value == 320
                ):
                    return {"filename": item.filename, "user": result.username, "filesize": item.attributes}


async def downloadFiles(songs):
    total_files = len(songs)

    client: SoulSeekClient = SoulSeekClient(settings)
    
    #disable logging, not really needed atm, could be helpful if eli has problems and we can look at logs ig idk pookie, just cleaning the console right now
    logging.disable()

    await client.stop()

    await client.start()
    await client.login()

    print("Logging in...")

    await asyncio.sleep(5)

    with Progress(
        TextColumn("[bold blue]{task.description}[/bold blue]"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        # 1) Create an OVERALL task to track how many files are done
        overall_task_id = progress.add_task(
            "Overall", total=total_files,
            # We'll manually update the "completed" count
        )

        # 2) Kick off a separate async job for each file
        tasks = []
        for song in songs:
            tasks.append(limited_download_song(song, client, progress, overall_task_id))

        await asyncio.gather(*tasks)


    await client.stop()
