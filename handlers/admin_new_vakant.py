from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters.command import Command
from keyboards.inline.general_kb import send_vacancy_list
from general import chats
from data.config import ADMINS, SUPERGROUP_CHAT_ID
from utils.database import find_user

new_vakant = Router()

