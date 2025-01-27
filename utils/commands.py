from aiogram.types import BotCommand
from aiogram import Bot


async def set_admin_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start"),
            BotCommand(command="new_vakant", description="Create Vakant"),
        ]
    )

async def set_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Start"),
            BotCommand(command="profile", description="Profile"),
            BotCommand(command="new_vakant", description="Create Vakant"),
        ]
    )
