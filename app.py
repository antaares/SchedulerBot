from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers


async def on_startup(dispatcher):
    db.create_table_users()
    my_bot = await dp.bot.get_me()
    print(f"{my_bot.username} is running...")

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
