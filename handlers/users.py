from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from general import generals  
from states import User 





@dp.callback_query_handler(lambda call: call.data.startswith("general_"))
async def handle_vacancy_selection(call: types.CallbackQuery, state: FSMContext):
    vacancy_id = call.data.split("_")[1]
    selected_vacancy = next((item for item in generals if item["id"] == vacancy_id), None)
    if selected_vacancy:
        await state.update_data(selected_vacancy=selected_vacancy["topic"])
        await call.message.answer(f"Вы выбрали: {selected_vacancy['topic']}\nТеперь пройдите регистрацию.")
        await User.name.set()  # Proceed to the name collection step
    await call.answer()


@dp.message_handler(state=User.name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично! Теперь введите вашу фамилию:")
    await User.surname.set()


@dp.message_handler(state=User.surname)
async def get_user_surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Хорошо! Теперь укажите ваш возраст:")
    await User.age.set()


@dp.message_handler(state=User.age)
async def get_user_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    name = data.get("name")
    surname = data.get("surname")
    age = data.get("age")
    selected_vacancy = data.get("selected_vacancy")


    text = (
        f"Регистрация завершена!\n\n"
        f"Ваши данные:\n"
        f"Имя: {name}\n"
        f"Фамилия: {surname}\n"
        f"Возраст: {age}\n"
        f"Выбранная вакансия: {selected_vacancy}"
    )
    await state.finish()
    await message.answer(text)
