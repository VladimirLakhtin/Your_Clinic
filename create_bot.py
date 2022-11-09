from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN_BOT = "5565576290:AAHBrzftlKvhYrjSx81Q_um084d-L7-KF7M"

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot, storage=storage)
