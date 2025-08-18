import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from langchain_openai import ChatOpenAI
import asyncio

load_dotenv()
TELEGRAM_TOKEN = os.getenv("bot_api")
OPENROUTER_API_BASE = os.getenv("openai_api_base")
OPENAI_API_KEY = os.getenv("openai_api_key")
MODEL = os.getenv("model_name")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

llm = ChatOpenAI(
    model=MODEL,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENROUTER_API_BASE,
)

# обработка команды: start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Я бот задай вопрос")

# обработка любого текста не являющегося start
@dp.message()
async def handle_message(message: types.Message):
    try:
        # Асинхронный запрос к модели
        response = await llm.ainvoke(message.text)
        await message.answer(response.content)
    except Exception as e:
        await message.answer(f"🚫 Ошибка: {str(e)}")

# Запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
