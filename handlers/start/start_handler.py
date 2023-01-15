from builder import dp
from aiogram.types import Message
from keyboards import start_menu
from logger import command_logger


@dp.message_handler(commands=['start'])
async def start(message: Message):
    command_logger(message)
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    text = f'Приветствую тебя, {user_name}'
    await dp.bot.send_message(user_id, text=text)


@dp.message_handler(commands=['show'])
async def start(message: Message):
    command_logger(message)
    user_id = message.from_user.id
    photo = open('database/__materials/logo.png', 'rb')
    await dp.bot.send_photo(user_id,
                            photo=photo,
                            reply_markup=start_menu)
    chat_id = message.chat.id
    message_id = message.message_id
    await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
