from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .keyboards import get_main_keyboard, get_back_keyboard
from .states import Question_about_game
from ai.llm_chains.question_about_game_chain import QuestionAboutGameChain

router = Router()
mechanics_chain = QuestionAboutGameChain()

@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = """
    🤖 Добро пожаловать в бот-помощник "Вопрос по механике"!

    Я могу помочь вам с вопросами по игре Dota 2:
    • Что сейчас в мете?
    • Как апнуть птс?
    • Что собирать на пуджа?
    • Как играть на лайне?

    Выберите действие из меню ниже:
    """

    await message.answer(
        welcome_text,
        reply_markup=get_main_keyboard()
    )

@router.message(F.text == "Помощь")
async def help_command(message: Message):
    help_text = """
    📚 Доступные команды:

    /start - Запустить бота и показать главное меню
    Помощь - Показать это сообщение
    Вопрос по механике - Задать вопрос по Dota 2

    🔧 Как пользоваться:
    1. Нажмите "Вопрос по механике"
    2. Введите ваш вопрос
    3. Получите развернутый ответ от AI-Тренера

    Примеры вопросов:
    • "Кто сейчас в мете?"
    • "Как выйграть лайн?"
    • "Покажи сборку на фантомку."
    """

    await message.answer(help_text, reply_markup=get_main_keyboard())

@router.message(F.text == "Вопрос по механике")
async def start_mechanics_question(message: Message, state: FSMContext):
    await message.answer(
        "💡 Задайте ваш вопрос по механике:\n\n"
        "Пример: 'Как играть за пуджа?'",
        reply_markup=get_back_keyboard()
    )
    await state.set_state(Question_about_game.waiting_for_question)

@router.message(F.text == "Назад")
async def back_to_main(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Главное меню:",
        reply_markup=get_main_keyboard()
    )

@router.message(Question_about_game.waiting_for_question)
async def process_mechanics_question(message: Message, state: FSMContext):
    if message.text == "Назад":
        await back_to_main(message, state)
        return

    # Показываем, что бот "думает"
    thinking_msg = await message.answer("🤔 Обрабатываю ваш вопрос...")

    try:
        # Получаем ответ от LLM
        answer = await mechanics_chain.get_answer(message.text)

        # Отправляем ответ (разбиваем на части если слишком длинный)
        if len(answer) > 4096:
            for i in range(0, len(answer), 4096):
                await message.answer(answer[i:i+4096])
        else:
            await message.answer(answer)

    except Exception as e:
        await message.answer(f"❌ Произошла ошибка: {str(e)}")

    finally:
        # Удаляем сообщение "думаю"
        await thinking_msg.delete()

    await message.answer(
        "Можете задать еще вопрос или вернуться в главное меню:",
        reply_markup=get_back_keyboard()
    )

@router.message()
async def unknown_message(message: Message):
    await message.answer(
        "Я не понимаю эту команду. Используйте кнопки меню или /start",
        reply_markup=get_main_keyboard()
    )
