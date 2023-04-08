from aiogram import types
from filters.is_admin import IsAdmin

from aiogram.dispatcher import FSMContext



from handlers.users.send_ads import start_service, service



from loader import dp

from keyboards.default.admin_keys import admin, ready


from states.admin_states import Admin



@dp.message_handler(IsAdmin(),commands=['admin'])
async def adminForm(message: types.Message):
    await message.answer('Hello admin!', reply_markup=admin)


@dp.message_handler(IsAdmin(),text='Reklama')
async def request_ads(message: types.Message):
    await message.answer("Menga reklama uchun xabar yuboring. Istalgan formatda bo'lishi mumkin", reply_markup=ready)
    await Admin.Q1.set()




@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.Q1)
async def Q1form(message: types.Message, state: FSMContext):
    # first message received
    await message.answer("Reklama qabul qilindi! \n\
                         Reklama uchun 2-xabarni yboring. Agar boshqa yuboradigan reklamangiz bo'lmasa, \"Tayyor\" tugmasini bosing.",
                         reply_markup=ready)
    await state.update_data(count = 1)
    await state.update_data(message_1 = message)
    await Admin.Q2.set()




@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.Q2)
async def Q2form(message: types.Message, state: FSMContext):
    if message.text == "Tayyor":
        await call_service(state=state)
        await message.answer('Reklama muvaffaqqiyatli yuborildi.')
        await message.answer("Xabar yuborishni to'xtatish uchun /stop buyrugini bering.", reply_markup=admin)
        await state.finish()
        return
    # second message received
    await message.answer("Reklama qabul qilindi! \n\
                         Reklama uchun 3-xabarni yboring. Agar boshqa yuboradigan reklamangiz bo'lmasa, \"Tayyor\" tugmasini bosing.")
    await state.update_data(message_2 = message)
    await state.update_data(count = 2)
    await Admin.Q3.set()




@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.Q3)
async def Q3form(message: types.Message, state: FSMContext):
    if message.text == "Tayyor":
        await call_service(state=state)
        await message.answer('Reklama muvaffaqqiyatli yuborildi.')
        await message.answer("Xabar yuborishni to'xtatish uchun /stop buyrugini bering.", reply_markup=admin)
        await state.finish()
        return
    # third message received
    await message.answer("Reklama qabul qilindi! \n\
                         Reklama uchun 4-xabarni yboring. Agar boshqa yuboradigan reklamangiz bo'lmasa, \"Tayyor\" tugmasini bosing.")
    await state.update_data(message_3 = message)
    await state.update_data(count = 3)
    await Admin.Q4.set()




@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.Q4)
async def Q4form(message: types.Message, state: FSMContext):
    if message.text == "Tayyor":
        await call_service(state=state)
        await message.answer('Reklama muvaffaqqiyatli yuborildi.')
        await message.answer("Xabar yuborishni to'xtatish uchun /stop buyrugini bering.", reply_markup=admin)
        await state.finish()
        return
    # fourth message received
    await message.answer("Reklama qabul qilindi! \n\
                         Reklama uchun 5-xabarni yboring. Agar boshqa yuboradigan reklamangiz bo'lmasa, \"Tayyor\" tugmasini bosing.")
    await state.update_data(message_4 = message)
    await state.update_data(count = 4)
    await Admin.Q5.set()


@dp.message_handler(IsAdmin(),content_types=types.ContentTypes.ANY,state=Admin.Q5)
async def Q5form(message: types.Message, state: FSMContext):
    await message.answer("Reklama qabul qilindi! \n\
                         Boshqa reklama qabul qilinmaydi.", reply_markup=admin)
    # fifth message received
    await state.update_data(message_5 = message)
    await state.update_data(count = 5)
    # final step
    await call_service(state=state)
    await message.answer('Reklama muvaffaqqiyatli yuborildi.\n\
                         Xabar yuborishni to\'xtatish uchun /stop buyrugini bering.', reply_markup=admin)
    await state.finish()


    






async def call_service(state: FSMContext):
    data = await state.get_data()
    count = data['count']
    messages = []
    for x in range(1,count+1):
        messages.append(data[f'message_{x}'])
    try:
        await service(messages=messages)
        await start_service(data=messages)
    except Exception as e:
        print(e)
    
