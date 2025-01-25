import asyncpg
from typing import Union
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config


async def connect():
    return await asyncpg.create_pool(
        user=config.DB_NAME,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        database=config.DB_DATABASE,
    )


class Database:
    def __init__(self, connect):
        self.pool: Union[Pool, None] = connect

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def find_user(self, chat_id):
        """Find a user by their chat ID."""
        sql = "SELECT * FROM users WHERE chat_id = $1;"
        return await self.fetchrow(sql, chat_id)
