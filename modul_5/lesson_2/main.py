import asyncio
import logging
import sys
from aiogram import Bot , Dispatcher , types , F
from aiogram.filters.command import CommandStart
from geopy.distance import geodesic

BOT_TOKEN = ""
dp = Dispatcher()

cafe_branches = [
    {"name": "Guncha", "location": (69.219087 , 41.332013)},
    {"name": "Tashkent City", "location": (69.219087 , 41.332013)},
    # Add more branches as needed
]

@dp.message(CommandStart())
async def start_handler(msg : types.Message):
    await msg.answer_location(41.327563 , 69.227053)


@dp.message(F.location)
async def location_handler(msg : types.Message):

    map_ = []
    user_location = (msg.location.latitude , msg.location.longitude)
    for branch in cafe_branches:
        branch_location = branch["location"]
        distance = geodesic(user_location, branch_location).kilometers
        map_.append({"name": branch["name"], "distance": distance , "location" : branch_location})
    near = min(map_ , key=lambda x : x.get('distance'))
    await msg.answer_location(*near.get('location')[::-1])


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())