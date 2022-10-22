from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import CONFIG


storage = MemoryStorage()
bot = Bot(
    token=CONFIG['BOT']['TOKEN'],
    parse_mode='HTML'
)
dp = Dispatcher(
    bot=bot,
    storage=storage
)
