import asyncio

from aiogram.types import Message

from filters import IsAdmin
from loader import dp, bot
from models import CRUDUser
from utils import get_response, parse_html


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.delete()
    if await CRUDUser.add(user_id=message.from_user.id):
        await message.answer(
            text='Салам Алейкум! Большой Рахмет!'
        )
    else:
        await message.answer(
            text='Шалом Алехейм, манишма!'
        )


async def parse_news():
    while True:
        html = await get_response()
        news_list = await parse_html(html=html)
        if news_list:
            users = await CRUDUser.all()
            for news in news_list:
                for user in users:
                    await bot.send_message(
                        chat_id=user.id,
                        text='https://realt.onliner.by' + news
                    )
                    await asyncio.sleep(0.4)
        await asyncio.sleep(10)


@dp.message_handler(IsAdmin(), commands=['parse'])
async def start_parsing(message: Message):
    await message.delete()
    task = asyncio.create_task(parse_news())
    await task
