import asyncio
from handlers import register_routes
from loader import dp, bot
from utils.commands import set_commands


async def start():
    try:
        await set_commands(bot)
        await register_routes(dp)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
