import asyncio
import aiohttp
from ukrainealarm.client import Client
from dotenv import load_dotenv
import os

load_dotenv()
KEY = os.getenv("UKRAINE_ALARM_KEY")

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, KEY)
        all_alerts = await client.get_alerts()
        print(all_alerts)

asyncio.run(main())