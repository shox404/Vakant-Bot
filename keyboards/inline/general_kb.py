from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from general import chats  # Ensure this imports a valid structure


async def send_vacancy_list():
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=chat.get("topic", "Без названия"),  # Button text
                callback_data=f"general_{chat['id']}",  # Callback data
            )
        ]
        for chat in chats
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
