from aiogram.dispatcher.filters.state import State, StatesGroup




class Admin(StatesGroup):
    admin = State()
    Q1 = State()
    Q2 = State()
    Q3 = State()
    Q4 = State()
    Q5 = State()
    send_ads = State()