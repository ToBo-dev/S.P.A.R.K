import asyncio
from aioslsk.client import SoulSeekClient
from aioslsk.settings import Settings, CredentialsSettings
from aioslsk.search.model import SearchRequest
import csv


# Create default settings and configure credentials
settings: Settings = Settings(
    credentials=CredentialsSettings(
        username='tobia',
        password='2007'
    )
)

async def main():
    client: SoulSeekClient = SoulSeekClient(settings)

    songs = []

    with open('./playlist_data.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            songs.append({'artist': row[0], 'song': row[1]})

        print(songs)

"""
    await client.start()
    await client.login()
    global_request: SearchRequest = await client.searches.search('tyler, the creator - sweet / i thought you wanted to dance')

    await asyncio.sleep(5)

    print(global_request.results[0].shared_items[0])

    await client.stop()
"""
asyncio.run(main())