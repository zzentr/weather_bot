from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from asyncio import to_thread

from core.requestsAPI import get_weather

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer('Добрый день! Я помогу вам быстро узнать всю нужную информацию о погоде в любом городе. ' \
                          '\nДостаточно написать название города, а все остальное я сделаю сам!')
    
@router.message(F.text)
async def send_weather(message: Message):
    region = message.text
    response = await get_weather(region)

    if type(response) == dict:
        mess = await to_thread(create_message_with_weather, response)
        await message.answer(mess, parse_mode='html')

    elif response == '404':
        await message.answer('Такой город я не смог найти, попробуйте ввести город неподалеку!')

    else:
        await message.answer('Извините, но сервис отправляющий погоду не отвечает, попробуйте чуть позже')

@router.message()
async def other(message: Message):
    await message.answer('Отправьте название города, чтобы я смог найти информацию о его погоде!')

def create_message_with_weather(response: dict) -> str:
    main = response['main']
    temp = int(main['temp'])
    feels_like = int(main['feels_like'])
    humidity = main['humidity']
    weather = response['weather'][0]['description']
    wind = int(response['wind']['speed'])

    message = f'В выбранном регионе сейчас <b>{weather}</b>\n\nТемпература <b>{round(temp)}°С</b>, '\
                f'но ощущается как <b>{round(feels_like)}°С</b>\nВлажность: <b>{humidity} %</b>\n' \
                f'Скорость ветра: <b>{round(wind)} м/с</b>'
    
    return message

