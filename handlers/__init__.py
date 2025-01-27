from aiogram import Dispatcher
from handlers.start import start_router
from handlers.users import profile_router
from handlers.new_vakant import new_vakant


async def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(profile_router)
    dp.include_router(new_vakant)
