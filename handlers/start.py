from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
