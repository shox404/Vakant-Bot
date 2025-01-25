from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from datetime import datetime
from data.config import ADMINS  # Список админов из конфигурации
from app import db  # Подключение к базе данных (убедитесь, что это работает)

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    # Текущее время
    current_time = datetime.now()
    user_id = str(message.from_user.id)  # Преобразование ID в строку для сравнения с ADMINS

    # Приветствие для админов
    if user_id in ADMINS:
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
        # Проверка пользователя в базе данных
        user = await db.find_user(user_id)  # Предполагается, что `find_user` возвращает данные или None

        if not user:
            # Если пользователь новый, можно добавить в базу данных
            await db.add_user(user_id, message.from_user.full_name)

        await message.answer(
            f"Hello, Welcome to the bot <b>{message.from_user.full_name}</b>!"
        )