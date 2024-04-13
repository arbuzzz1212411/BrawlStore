from aiogram.fsm.state import State, StatesGroup


class OrderForm(StatesGroup):
    order = State()
    pay_method = State()
    summary = State()
