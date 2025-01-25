from aiogram import types
from aiogram.filters import Command
from aiogram.dispatcher import FSMContext
from states.users import User  # Убедитесь, что User — это ваш StateGroup
from loader import dp

@dp.message_handler(Command('registration'))
async def get_user_name(message: types.Message):
    text = "Please enter your name:"
    await User.name.set()  # Устанавливаем состояние
    await message.answer(text)

@dp.message_handler(state=User.name)
async def get_user_surname(message: types.Message, state: FSMContext):
    name = message.text
    text = "Great! Now, please enter your surname:"
    await state.update_data(name=name)  # Сохраняем имя в состоянии
    await User.surname.set()  # Устанавливаем следующее состояние
    await message.answer(text)

@dp.message_handler(state=User.surname)
async def get_user_age(message: types.Message, state: FSMContext):
    surname = message.text
    text = "Got it! Finally, enter your age:"
    await state.update_data(surname=surname)  
    await User.age.set()  # Устанавливаем следующее состояние
    await message.answer(text)

@dp.message_handler(state=User.age)
async def get_personal_data(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)  # Сохраняем возраст в состоянии
    data = await state.get_data()  # Получаем все данные из состояния

    name = data.get('name')
    surname = data.get('surname')
    age = data.get('age')

    # Сообщение с персональными данными
    text = (
        "Your personal data has been saved successfully!\n\n"
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Age: {age}"
    )

    await state.finish()  # Завершаем состояние
    await message.answer(text)
