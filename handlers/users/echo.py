from aiogram import types
from filters.is_admin import IsAdmin

from loader import dp
from handlers.users.send_ads import scheduler

# Echo bot
@dp.message_handler(IsAdmin(),commands='stop', state='*')
async def bot_echo(message: types.Message):
    scheduler.remove_job("id4556")
    await message.answer("Xabar yuborish to'xtatildi")    
