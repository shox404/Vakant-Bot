from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from datetime import datetime
from data.config import ADMINS
from utils.commands import set_commands, set_admin_commands
from loader import bot

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):

    current_time = datetime.now()
    user_id = message.from_user.id 

    if user_id in ADMINS:
        await set_admin_commands(message.bot)

        if current_time.hour < 12:
            greeting = "Good morning"
        elif 12 <= current_time.hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        await message.answer(
            f"{greeting}. Welcome to the bot, ADMIN <b>{message.from_user.full_name}</b>!"
        )
    else:
        await set_commands(message.bot)
        await message.answer(
            f"Hello, Welcome to the bot <b>{message.from_user.full_name}</b>!"
        )
