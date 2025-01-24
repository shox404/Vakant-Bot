import asyncio
import handlers
from utils.database import Database
from loader import dp, bot

db = Database("vakant")

async def start():
    await db.create()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
