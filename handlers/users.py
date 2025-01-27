from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.users import User

profile_router = Router()


@profile_router.message(Command("profile"))
async def get_user_name(message: Message, state: FSMContext):
    text = "Please enter your name:"
    


@profile_router.message(User.name)
async def get_user_surname(message: Message, state: FSMContext):
    text = f"Well! Now please enter your surname"
    await state.update_data(name=message.text)
    await state.set_state(User.surname)
    await message.answer(text)


@profile_router.message(User.surname)
async def get_user_age(message: Message, state: FSMContext):
    text = f"Got it! FInally enter your age: "
    await state.update_data(surname=message.text)
    await state.set_state(User.age)
    await message.answer(text)


@profile_router.message(User.age)
async def get_personal_data(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    text = f"Data has been added succesfully"
    data = await state.get_data()
    name = data.get("name")
    surname = data.get("surname")
    age = data.get("age")
    data = (
        f"This is your personal data \n"
        f"Name: {name},\nSurname: {surname},\nAge: {age}"
    )
    await message.answer(text)
    await message.answer(data)
    await state.clear()
