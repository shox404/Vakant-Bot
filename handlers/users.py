<<<<<<< HEAD
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
=======
from aiogram import types
from aiogram.filters import Command
from aiogram.dispatcher import FSMContext 
>>>>>>> c0a468c0e363d62c0ade77b81636f696777af743
from states.users import User

profile_router = Router()

<<<<<<< HEAD

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
=======
@dp.message_handler(Command('registration'))
async def get_user_name(message: types.Message):
    text = f"Please enter your name: "
    await User.name.set()
    await message.answer(text)  

@dp.message_handler(state=User.surname)   
async def get_user_surname(message: types.Message,state:FSMContext):
    text = f"Well! Now please enter your surname"
    await state.update_data(
        {"Name" : message.text}
        )   
    await User.surname.set()
    await message.answer(text)       

@dp.message_handler(state=User.age)   
async def get_user_age(message: types.Message,state:FSMContext):
    text = f"Got it! FInally enter your age: "
    await state.update_data(
        {"Surname" : message.text}
        )   
    await User.age.set()


@dp.message_handler(state=User.age)   
async def get_personal_data(message: types.Message,state:FSMContext):
    await state.update_data(
        {"Age" : message.text}
        )   
    text = f"Data has been added succesfully"
    data = await state.get_data()
    name = data.get('name')
    surname = data.get('surname')
    age = data.get('age')
    text1 = f"This is your personal data \n"\
           f"Name: {name},\n Surname: {surname},\nAge:{age}" 
    await state.finish()
    await message.answer(text)
    await message.answer(text1)
>>>>>>> c0a468c0e363d62c0ade77b81636f696777af743
