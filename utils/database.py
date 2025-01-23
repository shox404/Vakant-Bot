from typing import Union

import asyncpg

from asyncpg import Connection
from asyncpg.pool import Pool



class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user='postgres',
            password='1111',
            host='localhost',
            database='ecommerce',
        )

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


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())
    
    async def get_products(self):
        sql = "SELECT * FROM products;"
        return await self.execute(sql, fetch=True)
    
    async def add_product(self, name, description, address, price, summary, product_count):
        sql = "INSERT INTO products (name, description, address, price, summary, product_count) VALUES($1, $2, $3, $4, $5, $6) returning *"
        return await self.execute(sql, name, description, address, price, summary, product_count, fetchrow=True)
