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
        print(song)
        search_request: SearchRequest = await client.searches.search(song)
        await asyncio.sleep(5)
        if search_request.results:
            print(search_request.results[0].shared_items[0])

async def downloadFiles(songs):
    client: SoulSeekClient = SoulSeekClient(settings)

    await client.start()
    await client.login()

    await asyncio.sleep(5)

    await client.stop()

    ##todo format search, figure out login
"""
    tasks = [download_song(song, client) for song in songs]
    await asyncio.gather(*tasks)

    await client.stop()
"""