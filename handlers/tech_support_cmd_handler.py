from aiogram.types import CallbackQuery
from aiogram import Router, F
from keyboards.keyboard import InCallBack
from utils.get_responses import get_responses
from keyboards.keyboard import tech_support_contacts_inline, main_inline

tech_router = Router()


@tech_router.callback_query(InCallBack.filter(F.action == 'tech'))
async def tech_support(call: CallbackQuery):
    await call.message.answer(
        get_responses('tech_support'),
        reply_markup=tech_support_contacts_inline()
    )
    await call.answer()


@tech_router.callback_query(InCallBack.filter(F.action == 'back_main_menu'))
async def back_main_menu(call: CallbackQuery):
    await call.message.answer(
        get_responses('start'),
        reply_markup=main_inline()
    )
    await call.answer()
