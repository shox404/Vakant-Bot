from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
from loader import dp
from general import chat  # Ensure this imports a valid structure

# Sample data for generals (list of dictionaries with topics and IDs)
chats = chat
@dp.message_handler(commands=["vakansy"])  # Example handler for the "/vakansy" command
async def send_vacancy_list(message: types.Message):
    # Start text
    start_text = "Список вакансий:"
    # Create the inline keyboard
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


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)