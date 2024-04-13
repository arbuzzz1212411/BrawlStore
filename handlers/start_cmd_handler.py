from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.get_responses import get_responses
from keyboards.keyboard import main_inline

start_router = Router()


@start_router.message(Command("start"))
async def hello_cmd(message: Message):
    await message.answer(
        get_responses('start'),
        reply_markup=main_inline()
    )
