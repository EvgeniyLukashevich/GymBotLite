from builder import dp
from aiogram.types import Message
from data import content_write
from logger import try_logger, add_text_logger, add_photo_logger, add_video_logger


@dp.message_handler(content_types='photo')
async def photo_funnel(message: Message):
    try_logger(message)
    user_id = message.from_user.id
    photo_id = message.photo[0].file_id
    content_write(user_id=user_id,
                  content_type='photo',
                  content_id=photo_id)
    add_photo_logger(message)
    chat_id = message.chat.id
    message_id = message.message_id
    await dp.bot.delete_message(chat_id=chat_id,
                                message_id=message_id)


@dp.message_handler(content_types='video')
async def photo_funnel(message: Message):
    try_logger(message)
    user_id = message.from_user.id
    video_id = message.video.file_id
    content_write(user_id=user_id,
                  content_type='video',
                  content_id=video_id)
    add_video_logger(message)
    chat_id = message.chat.id
    message_id = message.message_id
    await dp.bot.delete_message(chat_id=chat_id,
                                message_id=message_id)


@dp.message_handler()
async def link_funnel(message: Message):
    try_logger(message)
    link_checker = 'http'
    text = message.text
    if link_checker in text:
        user_id = message.from_user.id
        link_id = message.text
        content_write(user_id=user_id,
                      content_type='link',
                      content_id=link_id)
        add_text_logger(message)
    chat_id = message.chat.id
    message_id = message.message_id
    await dp.bot.delete_message(chat_id=chat_id,
                                message_id=message_id)
