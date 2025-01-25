from aiogram import types
from aiogram.filters import Command
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
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

@dp.message_handler(state=User.vacancy)
async def send_vacancy_to_admin(message: types.Message, state: FSMContext):
    vacancy = message.text
    await state.update_data(vacancy=vacancy)
    await state.update_data(age=age)  # Сохраняем возраст в состоянии
    data = await state.get_data()  # Получаем все данные из состояния
    name = data.get('name')
    surname = data.get('surname')
    age = data.get('age')

    # Сообщение с персональными данными
    admin_message = (
        "Your personal data has been saved successfully!\n\n"
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Age: {age}"
    )

    for admin_id in ADMINS:
            await dp.bot.send_message(admin_id, admin_message, reply_markup=get_approval_keyboard())
        # Подтверждение пользователю
    await message.answer("Your data has been sent to the admin for approval. Please wait.")
    await state.finish()
