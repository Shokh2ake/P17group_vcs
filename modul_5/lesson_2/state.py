import asyncio
import logging
import sys
from aiogram import Bot , Dispatcher , types , F
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from geopy.distance import geodesic

BOT_TOKEN = "6577787774:AAHuz9S2cTEBKvf3jzTF-tPMMBED7rcjFLI"
dp = Dispatcher(storage=MemoryStorage())

class StepState(StatesGroup):
    step1 = State()
    step2 = State()


# def buttons():
#     btn1 = KeyboardButton(text="btn1")
#     btn2 = KeyboardButton(text="btn2")
#     btn3 = KeyboardButton(text="btn3")
#     design = [
#         [btn1, btn2, btn3]
#     ]
#     return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


@dp.message(CommandStart())
async def start_handler(msg : types.Message, state: FSMContext):
    await state.set_state(StepState.step1)
    await msg.answer("Qonday")


@dp.message(StepState.step1)
async def step1_handler(msg: types.Message, state: FSMContext):
    # if msg.text == 'btn1':
    #     await msg.answer("Button 1 bosldi")
    # elif msg.text == 'btn2':
    #     await msg.answer("Button 2 bosldi")
    # elif msg.text == 'btn3':
    #     await msg.answer("Button 3 bosldi")
    # await state.set_state(StepState.step2)
    await state.set_state(StepState.step2)
    data = await state.get_data()
    data.update({"button": msg.text})
    await state.set_state(data)


@dp.message(StepState.step2)

async def step2_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    await msg.answer(f"Saqlab qo'yilgan malumot: {data.get('button')}")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())