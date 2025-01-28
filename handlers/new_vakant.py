from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import Command
from keyboards.inline.general_kb import send_vacancy_list
from general import chats
from data.config import ADMINS, SUPERGROUP_CHAT_ID
from utils.database import find_user

new_vakant = Router()


# States
class User(StatesGroup):
    job_name = State()
    location = State()
    requirements = State()
    contact_info = State()
    experience = State()
    salary = State()


@new_vakant.message(Command("new_vakant"))
async def vacancy_list(message: Message):
    start_text = "List of Vacancies:"
    keyboard = await send_vacancy_list()
    await message.answer(text=start_text, reply_markup=keyboard)


@new_vakant.callback_query(F.data.startswith("general_"))
async def handle_vacancy_selection(callback: CallbackQuery, state: FSMContext):
    vacancy_id = callback.data.split("_")[1]
    selected_vacancy = next((item for item in chats if item["id"] == vacancy_id), None)
    if selected_vacancy:
        await state.update_data(selected_vacancy=selected_vacancy["topic"])
        await state.update_data(vacancy_id=vacancy_id)
        await callback.answer(f"You selected: {selected_vacancy['topic']}")
        await callback.message.answer("Enter job name.")
        await state.set_state(User.job_name)  # Set state for job_name
    await callback.answer()


@new_vakant.message(User.job_name)
async def get_job_name(message: Message, state: FSMContext):
    await state.update_data(job_name=message.text)
    await message.answer("Enter the Location:")
    await state.set_state(User.location)  # Set state for location


@new_vakant.message(User.location)
async def get_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)
    await message.answer("Enter the Requirements:")
    await state.set_state(User.requirements)  # Set state for requirements


@new_vakant.message(User.requirements)
async def get_requirements(message: Message, state: FSMContext):
    await state.update_data(requirements=message.text)
    await message.answer("Enter Contact Information:")
    await state.set_state(User.contact_info)  # Set state for contact_info


@new_vakant.message(User.contact_info)
async def get_contact_info(message: Message, state: FSMContext):
    await state.update_data(contact_info=message.text)
    await message.answer("Enter Education and Experience:")
    await state.set_state(User.experience)  # Set state for experience


@new_vakant.message(User.experience)
async def get_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await message.answer("Enter the Salary:")
    await state.set_state(User.salary)  # Set state for salary


@new_vakant.message(User.salary)
async def get_salary(message: Message, state: FSMContext):
    await state.update_data(salary=message.text)
    data = await state.get_data()
    user = await find_user(message.from_user.id)
    text = (
        f"Name: {user.get('name')}\n"
        f"Surname: {user.get('surname')}\n"
        f"Age: {user.get('age')}\n"
        f"Selected Vacancy: {data.get('selected_vacancy')}\n"
        f"Job Name: {data.get('job_name')}\n"
        f"Location: {data.get('location')}\n"
        f"Requirements: {data.get('requirements')}\n"
        f"Contact Info: {data.get('contact_info')}\n"
        f"Education and Experience: {data.get('experience')}\n"
        f"Salary: {data.get('salary')}"
    )
    print(str(message.from_user.id))
    print(ADMINS)
    if str(message.from_user.id) in ADMINS:
        print("admin")
        await message.bot.send_message(
            chat_id=SUPERGROUP_CHAT_ID, text=text, message_thread_id=data["vacancy_id"]
        )
    else:
        print("user")
        for admin in ADMINS:
            await message.bot.send_message(chat_id=admin, text=text)

        await message.answer(text)
        await state.clear()
