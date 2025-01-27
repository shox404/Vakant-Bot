import asyncio
import handlers
from loader import dp, bot
from utils.commands import set_commands


async def start():
    try:
        await dp.start_polling(bot)
        await set_commands()
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
