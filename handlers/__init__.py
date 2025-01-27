from handlers.start import start_router
from handlers.users import profile_router
from aiogram import Dispatcher


async def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(profile_router)
