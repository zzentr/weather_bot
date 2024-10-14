from aiogram import Bot, Dispatcher
from asyncio import run
from dotenv import load_dotenv
import os
load_dotenv()

from core.handlers import router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())