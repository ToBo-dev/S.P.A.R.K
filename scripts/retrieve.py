import asyncio
from aioslsk.client import SoulSeekClient
from aioslsk.settings import Settings, CredentialsSettings
from aioslsk.search.model import SearchRequest


# Create default settings and configure credentials
settings: Settings = Settings(
    credentials=CredentialsSettings(
        username='tobia',
        password='2007'
    )
)

async def main():
    client: SoulSeekClient = SoulSeekClient(settings)

    await client.start()
    await client.login()

    # Send a private message
    global_request: SearchRequest = await client.searches.search('tyler, the creator - sweet / i thought you wanted to dance')

    await asyncio.sleep(5)

    print(global_request.results[0].shared_items[0])

    await client.stop()

asyncio.run(main())