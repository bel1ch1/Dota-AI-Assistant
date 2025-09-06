import asyncio
from aiogram import Bot, Dispatcher

from config.config import tg_config
from bot.handlers import router as bot_router

async def main():
    # Инициализация бота и диспетчера
    bot = Bot(token=tg_config.bot_token)
    dp = Dispatcher()

    # Регистрация роутеров
    dp.include_router(bot_router)

    # Запуск polling
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
