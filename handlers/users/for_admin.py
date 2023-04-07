from aiogram import types
from filters.is_admin import IsAdmin

from aiogram.dispatcher import FSMContext



from handlers.users.send_ads import start_service, service



from loader import dp

from keyboards.default.admin_keys import admin


from states.admin_states import Admin



@dp.message_handler(IsAdmin(),commands=['admin'])
async def adminForm(message: types.Message):
    await message.answer('Hello admin!', reply_markup=admin)


@dp.message_handler(IsAdmin(),text='Reklama')
async def request_ads(message: types.Message):
    await message.answer('Menga reklama uchun xabar yuboring.')
    await Admin.send_ads.set()


@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.send_ads)
async def send_ads(message: types.Message,state: FSMContext):
    try:
        await service(message)
        await start_service(message)
    except Exception as e:
        print(e)
    await message.answer('Reklama muvaffaqqiyatli yuborildi.')
    await message.answer("Xabar yuborishni to'xtatish uchun /stop buyrugini bering.")
    await state.finish()

    