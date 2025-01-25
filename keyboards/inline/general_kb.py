from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from general import chats


async def send_vacancy_list(message: Message):
    start_text = f"Список вакансий:"
    
    # Create the keyboard
    keyboard = InlineKeyboardMarkup(row_width=1)
    for item in chats:
        keyboard.add(
            InlineKeyboardButton(
                text=item.get("topic", "Без названия"),
                callback_data=f"general_{item['id']}",
            )
        )

    await message.answer(text=start_text, reply_markup=keyboard)
