from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



admin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Reklama"),
        ],
    ],
    resize_keyboard=True
)


ready = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tayyor"),
        ],
    ],
    resize_keyboard=True
)