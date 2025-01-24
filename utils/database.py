import asyncpg
from typing import Union
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config


import asyncpg


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_NAME,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            database=config.DB_DATABASE,
        )

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def execute(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def fetchrow(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query, *args)

    async def fetchval(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetchval(query, *args)

    async def find_user(self, chat_id):
        """Find a user by their chat ID."""
        sql = "SELECT * FROM users WHERE chat_id = $1;"
        return await self.fetchrow(sql, chat_id)

# class Database:
#     def __init__(self):
#         self.pool: Union[Pool, None] = None

#     async def create(self):
#         self.pool = await asyncpg.create_pool(
#             user=config.DB_NAME,
#             password=config.DB_PASSWORD,
#             host=config.DB_HOST,
#             database=config.DB_DATABASE,
#         )

#     async def execute(
#         self,
#         command,
#         *args,
#         fetch: bool = False,
#         fetchval: bool = False,
#         fetchrow: bool = False,
#         execute: bool = False,
#     ):
#         async with self.pool.acquire() as connection:
#             connection: Connection
#             async with connection.transaction():
#                 if fetch:
#                     result = await connection.fetch(command, *args)
#                 elif fetchval:
#                     result = await connection.fetchval(command, *args)
#                 elif fetchrow:
#                     result = await connection.fetchrow(command, *args)
#                 elif execute:
#                     result = await connection.execute(command, *args)
#             return result

#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join(
#             [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
#         )
#         return sql, tuple(parameters.values())

#     async def find_user(self, chat_id):
#         db.create()
#         sql = f"SELECT * FROM users WHERE chat_id = $1;"
#         return await self.execute(sql, chat_id, fetch=True)

#     async def get_users(self) -> bool:
#         sql = f"SELECT * FROM users ;"
#         return await self.execute(sql, fetch=True)

#     async def add_product(
#         self, name, description, address, price, summary, product_count
#     ):
#         sql = f"INSERT INTO {self.db_name} (name, description, address, price, summary, product_count) VALUES($1, $2, $3, $4, $5, $6) returning *"
#         return await self.execute(
#             sql,
#             name,
#             description,
#             address,
#             price,
#             summary,
#             product_count,
#             fetchrow=True,
#         )


# db = Database()
