from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import dp, db

class IsGroup(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        if message.chat.type in (
            types.ChatType.GROUP,
            types.ChatType.SUPERGROUP):
            db.add_group(message.chat.id)
            return True
        else:
            return False