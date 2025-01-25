from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from general import chats


async def send_vacancy_list(message: Message):
    start_text = f"Список вакансий:"

    keyboard = InlineKeyboardMarkup(row_width=1)
    for chat in chats:
        keyboard.add(
            InlineKeyboardButton(
                text=chat.get("topic", "Без названия"),  # Button text
                callback_data=f"chat_{chat['id']}",  # Callback data
            )
        )

    # Send the message with the inline keyboard
    await message.answer(text=start_text, reply_markup=keyboard)
