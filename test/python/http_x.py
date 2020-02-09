

import asyncio
import httpx

async def post_httpx():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://www.example.org/')
        print(response)


loop = asyncio.get_event_loop()
loop.run_until_complete(post_httpx())

