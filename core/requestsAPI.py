import aiohttp
from dotenv import load_dotenv
import os
load_dotenv

async def get_weather(region: str) -> dict:
    async with aiohttp.ClientSession() as session:
        params = {
            'q': region,
            'units': 'metric',
            'lang': 'ru',
            'appid': os.getenv('API_KEY')
        }
        try:

            async with session.get('https://api.openweathermap.org/data/2.5/weather?', params=params) as response:
                if response.ok:
                    return await response.json()
                else:
                    return '404'

        except Exception as r:
            print(f'Error: {r}')
            return None