import asyncpg
from typing import Union
from asyncpg import Connection
from asyncpg.pool import Pool
from data import config

_pool: Union[Pool, None] = None

async def connect():
    """Initialize a connection pool."""
    return await asyncpg.create_pool(
        user=config.DB_NAME,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        database=config.DB_DATABASE,
    )

async def get_pool():
    """Get or create the connection pool."""
    global _pool
    if not _pool:
        _pool = await connect()
    return _pool

class Database:
    def __init__(self, pool: Pool):
        self.pool: Union[Pool, None] = pool

    async def close(self):
        """Close the connection pool."""
        if self.pool:
            await self.pool.close()

    async def execute(
        self,
        command: str,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ) -> Union[None, list, str, dict]:
        """Execute a database command with various fetch options."""
        if not any([fetch, fetchval, fetchrow, execute]):
            raise ValueError("No execution mode specified. Use one of fetch, fetchval, fetchrow, or execute.")

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                try:
                    if fetch:
                        result = await connection.fetch(command, *args)
                    elif fetchval:
                        result = await connection.fetchval(command, *args)
                    elif fetchrow:
                        result = await connection.fetchrow(command, *args)
                    elif execute:
                        result = await connection.execute(command, *args)
                    return result
                except Exception as e:
                    # Log the exception (replace with a proper logging mechanism in production)
                    print(f"Database query error: {e}")
                    return None

    async def find_user(self, chat_id: int) -> Union[dict, None]:
        """Find a user by their chat ID."""
        sql = "SELECT * FROM users WHERE chat_id = $1;"
        return await self.execute(sql, chat_id, fetchrow=True)

# Example usage (should be used in an async context):
# pool = await get_pool()
# db = Database(pool)
# user = await db.find_user(123456)
# await db.close()
