from aiogram import types

from filters import IsGroup
from loader import dp, bot, db


@dp.message_handler(IsGroup(), content_types=types.ContentTypes.ANY)
async def new_member(message: types.Message):
    chat_id = message.chat.id
    db.add_group(chat_id)