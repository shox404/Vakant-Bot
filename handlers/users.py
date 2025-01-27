from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.filters import Command
from loader import dp
from general import generals # Ensure this imports a valid structure
from states import User
from keyboards.inline import general_kb  # Ensure User states are properly defined

# Step 1: Send the vacancy list
@dp.message_handler(commands=["vakansy"])
async def send_vacancy_list(message: types.Message):
    start_text = "Список вакансий:"
    keyboard = InlineKeyboardMarkup(row_width=1)
    for item in generals:
        keyboard.add(
            InlineKeyboardButton(
                text=item.get("topic", "Без названия"),
                callback_data=f"general_{item['id']}"
            )
        )
    await message.answer(text=start_text, reply_markup=keyboard)

# Step 2: Handle vacancy selection
@dp.callback_query_handler(lambda call: call.data.startswith("general_"))
async def handle_vacancy_selection(call: types.CallbackQuery, state: FSMContext):
    vacancy_id = call.data.split("_")[1]
    selected_vacancy = next((item for item in generals if item["id"] == vacancy_id), None)
    if selected_vacancy:
        await state.update_data(selected_vacancy=selected_vacancy["topic"])
        await call.message.answer(f"Вы выбрали: {selected_vacancy['topic']}\nТеперь пройдите регистрацию.")
        await User.name.set()  # Proceed to the name collection step
    await call.answer()

# Step 3: Get user name
@dp.message_handler(state=User.name)
async def get_user_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично! Теперь введите вашу фамилию:")
    await User.surname.set()

# Step 4: Get user surname
@dp.message_handler(state=User.surname)
async def get_user_surname(message: types.Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await message.answer("Хорошо! Теперь укажите ваш возраст:")
    await User.age.set()

# Step 5: Get user age
@dp.message_handler(state=User.age)
async def get_user_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()
    name = data.get("name")
    surname = data.get("surname")
    age = data.get("age")
    selected_vacancy = data.get("selected_vacancy")

    # Display the collected data
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
