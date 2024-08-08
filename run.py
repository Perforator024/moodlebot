import asyncio
import logging

# Подключаем нужные библиотеки
from aiogram import Bot, Dispatcher

# шифруем токен бота
from config import TOKEN
from app.handlers import router
# Подключаем бота


bot = Bot(token=TOKEN)
dp = Dispatcher()

# функция, чтобы телеграм не зациклился и не сдох
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
