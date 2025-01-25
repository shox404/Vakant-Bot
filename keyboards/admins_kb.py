from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp


def get_approval_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="Approve", callback_data="approve_user"),
        InlineKeyboardButton(text="Reject", callback_data="reject_user")
    )
    return keyboard

@dp.callback_query_handler(lambda c: c.data in ["approve_user", "reject_user"])
async def process_admin_decision(callback_query: types.CallbackQuery):
    decision = callback_query.data
    user_id = callback_query.from_user.id

    if decision == "approve_user":
        await callback_query.message.answer("User has been approved.")
        # Здесь можно отправить сообщение пользователю об одобрении
    elif decision == "reject_user":
        await callback_query.message.answer("User has been rejected.")
        # Здесь можно отправить сообщение пользователю об отказе

    await callback_query.answer()  # Уведомление, что callback обработан

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)    