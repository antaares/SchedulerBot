from aiogram.dispatcher.filters.state import State, StatesGroup




class Admin(StatesGroup):
    admin = State()
    send_ads = State()