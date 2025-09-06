from aiogram.fsm.state import State, StatesGroup

class Question_about_game(StatesGroup):
    waiting_for_question = State()
