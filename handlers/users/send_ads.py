import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import types

from typing import List

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


from loader import dp, db

scheduler = AsyncIOScheduler()


async def start_service(data):
    try:
        scheduler.remove_job("id4556")
    except Exception as e:
        pass
    scheduler.add_job(service, trigger= 'interval', minutes=25, id="id4556", max_instances=20, args=[data])
    try:
        scheduler.start()
    except Exception as e:
        pass


async def service(messages: List[types.Message]):
    allgroups = db.select_all_groups()
    for group in allgroups:
        try:
            for message in messages:
                await message.copy_to(group, reply_markup=message.reply_markup)
                await asyncio.sleep(0.3)
        except Exception as e:
            print(e)













    # try:
    #     scheduler.remove_job("id4556")
    #     print("removed")
    # except Exception as e:
    #     print(e)
    # try:
    #     scheduler.add_job(service, 'interval', seconds=10, id="id4556", args=[data])
    #     print("added")
    # except Exception as e:
    #     print(e)
    # try:
    #     scheduler.start()
    #     print("started")
    #     scheduler.print_jobs()
    # except Exception as e:
    #     print(e)


# , jobstore='default', executor='processpool',



# async def service(message: types.Message):
#     allgroups = [5950193177, 1393139047]
#     for group in allgroups:
#         await message.copy_to(group, reply_markup=message.reply_markup)










# from apscheduler.schedulers.background import BackgroundScheduler

# def start_service(data):
#     scheduler = BackgroundScheduler()
#     scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
#     scheduler.add_job(service, 'interval', seconds=10, id="id4556", args=[data])
#     scheduler.start()




