from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_menu = InlineKeyboardMarkup(resize_keyboard=True)
show_btn = InlineKeyboardButton(text='СМОТРЕТЬ', callback_data='contentSHOW')
start_menu.row(show_btn)
