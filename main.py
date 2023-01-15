from aiogram.utils import executor
from builder import activate, turn_off
from handlers import dp

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=activate,
                           on_shutdown=turn_off)
