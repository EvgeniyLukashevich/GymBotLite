from aiogram.types import Message
import os
import datetime


def command_logger(message: Message):
    user_id = message.from_user.id
    user_name = f'{message.from_user.first_name} {message.from_user.username} {message.from_user.last_name}'
    command = message.text
    time = datetime.datetime.now()
    text = f'{time} :: {user_id} :: {user_name} :: ВВЕЛ КОМАНДУ :: {command}\n\n'
    with open('database/general_logger.txt', 'a', encoding='UTF-8') as file:
        file.write(text)
    try:
        os.mkdir(f"database/{user_id}")
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
    except:
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)


def try_logger(message: Message):
    user_id = message.from_user.id
    user_name = f'{message.from_user.first_name} {message.from_user.username} {message.from_user.last_name}'
    content_type = message.content_type
    time = datetime.datetime.now()
    text = f'{time} :: {user_id} :: {user_name} :: пытается добавить :: {content_type}\n'
    with open('database/general_logger.txt', 'a', encoding='UTF-8') as file:
        file.write(text)
    try:
        os.mkdir(f"database/{user_id}")
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
    except:
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)


def add_video_logger(message: Message):
    user_id = message.from_user.id
    content = message.video.file_id
    time = datetime.datetime.now()
    text = f'{time} :: {user_id} :: ДОБАВИЛ :: {content}\n\n'
    with open('database/general_logger.txt', 'a', encoding='UTF-8') as file:
        file.write(text)
    try:
        os.mkdir(f"database/{user_id}")
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
    except:
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)


def add_photo_logger(message: Message):
    user_id = message.from_user.id
    content = message.photo[0].file_id
    time = datetime.datetime.now()
    text = f'{time} :: {user_id} :: ДОБАВИЛ :: {content}\n\n'
    with open('database/general_logger.txt', 'a', encoding='UTF-8') as file:
        file.write(text)
    try:
        os.mkdir(f"database/{user_id}")
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
    except:
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)


def add_text_logger(message: Message):
    user_id = message.from_user.id
    content = message.text
    time = datetime.datetime.now()
    text = f'{time} :: {user_id} :: ДОБАВИЛ :: {content}\n\n'
    with open('database/general_logger.txt', 'a', encoding='UTF-8') as file:
        file.write(text)
    try:
        os.mkdir(f"database/{user_id}")
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
    except:
        with open(f'database/{user_id}/{user_id}_logger.txt', 'a', encoding='UTF-8') as file:
            file.write(text)
