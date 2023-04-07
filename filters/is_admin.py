
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from loader import bot 
from data.config import ADMINS


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        chat_id = message.chat.id
        if chat_id == 1393139047 or chat_id in ADMINS:
            return True
        return False