import asyncio
import handlers
from utils.database import Database, connect
from loader import dp, bot

connection = connect()
db = Database(connection)


async def start():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
