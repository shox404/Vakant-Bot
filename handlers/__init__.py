from app import dp
from handlers.start import start_router
dp.include_router(start_router)