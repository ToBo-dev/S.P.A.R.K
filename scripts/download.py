import asyncio
from aioslsk.client import SoulSeekClient
from aioslsk.settings import Settings, CredentialsSettings
from aioslsk.search.model import SearchRequest
import csv
import pprint


# Create default settings and configure credentials
settings: Settings = Settings(
    credentials=CredentialsSettings(
        username='tobiaaa',
        password='2007'
    )
)

async def download_song(song, client):
        query = " - ".join([song["artist"], song["song"], song["album"]])
        print("Searching with query:" + query)
        search_request: SearchRequest = await client.searches.search(query)
        await asyncio.sleep(5)
        download_target = await searchResults(search_request.results)
        print(download_target)
        #todo: download
        
                          
async def searchResults(results):
     if (results):
            for result in results:
                for item in result.shared_items:
                     if (item.filename.lower().endswith(".mp3") and item.attributes[0].value == 320):
                          return {"filename": item.filename, "user": result.username}

async def downloadFiles(songs):
    client: SoulSeekClient = SoulSeekClient(settings)

    await client.stop()

    await client.start()
    await client.login()

    await asyncio.sleep(5)

    await download_song(songs[1], client)

    await client.stop()

    ##todo format search, figure out login
"""
    tasks = [download_song(song, client) for song in songs]
    await asyncio.gather(*tasks)

    await client.stop()
"""