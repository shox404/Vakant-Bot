from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states.users import User
dp = Dispatcher

@dp.message_handler(commands='registration')
async def get_name(message: types.Message):
    await message.answer("Please enter your name:")
    await User.name.set()

@dp.message_handler(state=User.surname)
async def process_age(message: types.Message, state: FSMContext):
     await message.answer("Well! Now please enter your surname: ")

@dp.message_handler(state=User.name)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer("Got it! Now, how old are you?")
    await User.age.set()

@dp.message_handler(state=User.age)
async def process_age(message: types.Message, state: FSMContext):
    await message.answer(f"")
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
