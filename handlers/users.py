from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from aiogram.filters import Command
from aiogram.dispatcher import FSMContext 
from states.users import User
from loader import dp

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
    await message.answer(text)


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