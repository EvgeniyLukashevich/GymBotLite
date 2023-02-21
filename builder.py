import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

memory = MemoryStorage()
bot = Bot(token=os.getenv('GYMBOT_TOKEN'), parse_mode='HTML')
dp = Dispatcher(bot, storage=memory)


async def activate(_):
    print('GymBotLite is activated')


async def turn_off(_):
    print('GymBotLite is deactivated')
