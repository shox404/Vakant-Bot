import asyncio
from handlers import register_routes
from loader import dp, bot


async def start():
    try:
        await register_routes(dp)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
