from aiogram import Router, F
from aiogram.types import Message


photo_router = Router()


@photo_router.message(F.photo)
async def process_photo(message: Message):
    photo_data = message.photo[-1]
    await message.answer(f'{photo_data}')