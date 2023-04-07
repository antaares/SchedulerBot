from aiogram import Dispatcher
from filters.is_group import IsGroup

from loader import dp
from .is_admin import IsAdmin


if __name__ == "filters":
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    pass
