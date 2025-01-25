from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import dp
from general import general  # Ensure this imports a valid structure

# Sample data for generals (list of dictionaries with topics and IDs)
generals = general

@dp.message_handler(commands=["vakansy"])  # Example handler
async def send_vacancy_list(message: types.Message):
    # Start text
    start_text = f"Список вакансий:"

    keyboard = InlineKeyboardMarkup(row_width=1)
    for item in chats:
        keyboard.add(
            InlineKeyboardButton(
                text=item.get("topic", "Без названия"),
                callback_data=f"general_{item['id']}",
            )
        )

    await message.answer(text=start_text, reply_markup=keyboard)
