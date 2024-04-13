from aiogram.types import CallbackQuery, Message
from utils.get_responses import get_responses
from aiogram import Router, F
from keyboards.keyboard import InCallBack, buy_inline, pay_method_inline, main_inline, order_info_inline
from aiogram.fsm.context import FSMContext
from utils.statesorder import OrderForm
from typing import Dict, Any

buy_router = Router()


@buy_router.callback_query(InCallBack.filter(F.action == 'buy'))
async def buy_action(call: CallbackQuery, state: FSMContext):
    await state.set_state(OrderForm.order)
    await call.message.answer_photo(
        get_responses('photo_teg'),
        caption=get_responses('buy_step1'),
        reply_markup=buy_inline()
    )
    await call.answer()


@buy_router.callback_query(InCallBack.filter(F.action.casefold().in_(
    ['sum33', 'sum88', 'sum187', 'sum396', 'sum1045', 'sum2200', 'pass_plus']
        )
    )
 , OrderForm.order)
async def buy_step1(call: CallbackQuery, state: FSMContext):
    action = call.data[3:]
    if action == 'sum33':
        await state.update_data(order='33 гема')
        await call.message.answer_photo(
            get_responses('photo_teg_33'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum88':
        await state.update_data(order='88 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_88'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum187':
        await state.update_data(order='187 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_187'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum396':
        await state.update_data(order='396 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_396'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum1045':
        await state.update_data(order='1045 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_1045'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'sum2200':
        await state.update_data(order='2200 гемов')
        await call.message.answer_photo(
            get_responses('photo_teg_2200'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    elif action == 'pass_plus':
        await state.update_data(order='Бравл пасс+')
        await call.message.answer_photo(
            get_responses('photo_teg_pass_plus'),
            get_responses('buy_step2'),
            reply_markup=pay_method_inline()
        )
    await state.set_state(OrderForm.pay_method)
    await call.answer()


@buy_router.callback_query(OrderForm.order)
async def incorrect_order(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        get_responses('inc_order'),
        reply_markup=buy_inline()
    )
    await call.answer()


@buy_router.callback_query(OrderForm.pay_method, InCallBack.filter(F.action.casefold().in_(
    ['sbp', 'qiwi', 'card']
        )
    )
, OrderForm.pay_method)
async def buy_step2(call: CallbackQuery, state: FSMContext):
    action = call.data[3:]
    if action == 'sbp':
        await state.update_data(pay_method='СБП')
    elif action == 'qiwi':
        await state.update_data(pay_method='Qiwi')
    elif action == 'card':
        await state.update_data(pay_method='Карта')
    data = await state.get_data()
    await state.set_state(OrderForm.summary)
    await show_summary(call=call, data=data)
    await call.answer()


@buy_router.callback_query(OrderForm.pay_method)
async def incorrect_pay(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        get_responses('inc_order'),
        reply_markup=pay_method_inline()
    )
    await call.answer()


@buy_router.callback_query(InCallBack.filter(F.action.casefold() == 'ok_order'), OrderForm.summary)
async def ok_order(call: CallbackQuery, state: FSMContext):
    await call.message.answer(
        get_responses('ok_order'),
        reply_markup=main_inline()
    )
    await call.message.forward(chat_id='-1002110191577')
    await call.answer()
    await state.clear()


@buy_router.callback_query(InCallBack.filter(F.action == 'negative_order'), OrderForm.summary)
async def incor_order(call: CallbackQuery, state: FSMContext ):
    await call.message.answer(
        get_responses('incorrect_order'),
        reply_markup=main_inline()
    )
    await call.answer()
    await state.clear()


@buy_router.message()
async def unknown_cmd(message: Message):
    await message.reply(get_responses('unknown_cmd'))


async def show_summary(call: CallbackQuery, data: Dict[str, Any]):
    order = data.get('order')
    pay_method = data.get('pay_method')
    summ = str(order)
    pay = str(pay_method)
    msg = f"Пользователь: @{call.from_user.username}\nСумма заказа: {summ}\nМетод оплаты: {pay}\nВсё верно?"
    await call.message.answer(
        msg,
        reply_markup=order_info_inline()
    )
    await call.answer()
