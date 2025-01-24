from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from datetime import datetime
from data.config import ADMINS
from app import db

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message):

    current_time = datetime.now()
    user_id = message.from_user.id

    if str(user_id) in ADMINS:

        if current_time.hour < 12:
            await message.answer(
                f"Good morning. Welcome to the bot ADMIN <b>{message.from_user.full_name}</b>! "
            )
        elif current_time.hour < 18 and current_time > 12:
            await message.answer(
                f"Good afternoon. Welcome to the bot ADMIN <b>{message.from_user.full_name}</b>! "
            )
        else:
            await message.answer(
                f"Good evening. Welcome to the bot ADMIN <b>{message.from_user.full_name}</b>! "
            )
    else:
        user = await db.find_user(user_id)
        print("hi", user)

        await message.answer(
            f"Hello, Welcome to the bot <b>{message.from_user.full_name}</b>!"
        )
