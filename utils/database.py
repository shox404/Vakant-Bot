import asyncpg
from typing import Union
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config


async def connect():
    """Initialize a connection pool."""
    return await asyncpg.create_pool(
        user=config.DB_NAME,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        database=config.DB_DATABASE,
    )


async def find_user(chat_id):
    """Find a user by their chat ID."""
    db = await connect()
    sql = "SELECT * FROM users WHERE chat_id = $1;"
    return await db.fetchrow(sql, chat_id)


async def add_user(user_id: int, name: str, surname: str, age: int) -> bool:
    db = await connect()
    sql = """
        INSERT INTO users (chat_id, name, surname, age)
        VALUES ($1, $2, $3, $4);
    """
    result = await db.execute(sql, user_id, name, surname, age)
    return result == "INSERT 0 1"
