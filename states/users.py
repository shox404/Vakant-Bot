from aiogram.filters.state import State, StatesGroup

class User(StatesGroup):
    name = State()
    surname = State()
    age = State()