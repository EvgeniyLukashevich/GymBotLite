from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

show_menu = InlineKeyboardMarkup()
left_btn = InlineKeyboardButton(text='<<< Влево', callback_data='showLEFT')
right_btn = InlineKeyboardButton(text='Вправо >>>', callback_data='showRIGHT')
close_btn = InlineKeyboardButton(text='Закрыть', callback_data='showCLOSE')
show_menu.row(left_btn, right_btn)
show_menu.row(close_btn)
