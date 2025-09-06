from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Помощь")],
            [KeyboardButton(text="Вопрос по механике")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )

def get_back_keyboard():
    return ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Назад")]
            ],
            resize_keyboard=True
    )
