from builder import dp
from aiogram.types import CallbackQuery
from models import Unit
from keyboards import show_menu
from data import files_read


@dp.callback_query_handler(text='contentSHOW')
async def go_to_show(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        unit = Unit(user_id=user_id,
                    content_name='content_1')
        if unit.get_type() == 'link':
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            await dp.bot.delete_message(chat_id=chat_id,
                                        message_id=message_id)
            await dp.bot.send_message(user_id,
                                      unit.get_content_address(),
                                      reply_markup=show_menu)
        else:
            media = unit.get_content_callback()
            await call.message.edit_media(media=media,
                                          reply_markup=show_menu)
    except:
        unit = Unit(None, None)
        if unit.get_type() == 'link':
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            await dp.bot.delete_message(chat_id=chat_id,
                                        message_id=message_id)
            await dp.bot.send_message(user_id,
                                      unit.get_content_address(),
                                      reply_markup=show_menu)
        else:
            media = unit.get_content_callback()
            await call.message.edit_media(media=media,
                                          reply_markup=show_menu)


@dp.callback_query_handler(text='showCLOSE')
async def go_to_show_close(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await dp.bot.delete_message(chat_id=chat_id,
                                message_id=message_id)


@dp.callback_query_handler(text='showLEFT')
async def go_to_show_left(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        current_content_name = str(call.message.caption).split(': ')[0]
        file_list = files_read(user_id=user_id)
        for i in range(len(file_list)):
            if file_list[i] == current_content_name:
                current_content_name = file_list[i - 1]
                break
        unit = Unit(user_id=user_id,
                    content_name=current_content_name)
        if unit.get_type() == "link":
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_message(user_id, f'{unit.get_name()}: {unit.get_content_address()}',
                                      reply_markup=show_menu)
        else:
            media = unit.get_content_callback()
            await call.message.edit_media(media=media,
                                          reply_markup=show_menu)
    except:
        current_content_name = str(call.message.text).split(':')[0]
        file_list = files_read(user_id=user_id)
        for i in range(len(file_list)):
            if file_list[i] == current_content_name:
                current_content_name = file_list[i - 1]
                break
        unit = Unit(user_id=user_id,
                    content_name=current_content_name)
        if unit.get_type() == "link":
            text = f'{unit.get_name()}: {unit.get_content_address()}'
            await call.message.edit_text(text=text, reply_markup=show_menu)
        elif unit.get_type() == 'photo':
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            photo = unit.get_content_standard()
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_photo(user_id, photo=photo, reply_markup=show_menu, caption=f'{unit.get_name()}: photo')
        else:
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            video = unit.get_content_standard()
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_video(user_id, video=video, reply_markup=show_menu, caption=f'{unit.get_name()}: video')


@dp.callback_query_handler(text='showRIGHT')
async def go_to_show_right(call: CallbackQuery):
    user_id = call.from_user.id
    try:
        current_content_name = str(call.message.caption).split(': ')[0]
        file_list = files_read(user_id=user_id)
        file_list.reverse()
        for i in range(len(file_list)):
            if file_list[i] == current_content_name:
                current_content_name = file_list[i - 1]
                break
        unit = Unit(user_id=user_id,
                    content_name=current_content_name)
        if unit.get_type() == "link":
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_message(user_id, f'{unit.get_name()}: {unit.get_content_address()}',
                                      reply_markup=show_menu)
        else:
            media = unit.get_content_callback()
            await call.message.edit_media(media=media,
                                          reply_markup=show_menu)
    except:
        current_content_name = str(call.message.text).split(': ')[0]
        file_list = files_read(user_id=user_id)
        file_list.reverse()
        for i in range(len(file_list)):
            if file_list[i] == current_content_name:
                current_content_name = file_list[i - 1]
                break
        unit = Unit(user_id=user_id,
                    content_name=current_content_name)
        if unit.get_type() == "link":
            text = f'{unit.get_name()}: {unit.get_content_address()}'
            await call.message.edit_text(text=text, reply_markup=show_menu)
        elif unit.get_type() == 'photo':
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            photo = unit.get_content_standard()
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_photo(user_id, photo=photo, reply_markup=show_menu, caption=f'{unit.get_name()}: photo')
        else:
            chat_id = call.message.chat.id
            message_id = call.message.message_id
            video = unit.get_content_standard()
            await dp.bot.delete_message(chat_id=chat_id, message_id=message_id)
            await dp.bot.send_video(user_id, video=video, reply_markup=show_menu, caption=f'{unit.get_name()}: video')
