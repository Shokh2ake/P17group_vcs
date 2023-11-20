from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import psycopg2
import asyncio
import logging
import sys

con = psycopg2.connect(dbname = 'postgres',
                       user = 'postgres',
                       password = '1',
                       host = 'localhost',
                       port = 5432)

cur = con.cursor()

user_table = """
    create table if not exists users(
    id serial primary key,
    name varchar(255),
    age integer ,
    phone_number varchar (13) check (phone_number ilike '+%'),
    created_at timestamp default current_timestamp 
    )
"""

cur.execute(user_table)
con.commit()


def users_save_db(name, age, phone_number):
    insert_query = """
        insert into users (name, age, phone_number)
        values (%s, %s, %s)"""

    params = (name, age, phone_number)
    cur.execute(insert_query, params)
    con.commit()

BOT_TOKEN = "6577787774:AAHuz9S2cTEBKvf3jzTF-tPMMBED7rcjFLI"
dp = Dispatcher(storage=MemoryStorage)


class UserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    request = State()

def phone_number():
    phone_btn = InlineKeyboardButton(text='Phone☎️', request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[phone_btn], resize_keyboard=True)

def request_btn():
    save = InlineKeyboardButton(text='Save🟢', callback_data="save")
    edit = InlineKeyboardButton(text='Edit📝', callback_data="edit")
    design = [
        [save, edit]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)

@dp.message(CommandStart())

async def start_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Ismingizni kiriting: ")
    await state.set_state(UserState.name)


@dp.message(UserState())
async def name_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"name": msg.text})
    await state.set_data(data)
    await msg.answer("Yoshingizni kiriting: ")
    await state.set_state(UserState.age)

@dp.message(UserState())
async def age_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"age": msg.text})
    await state.set_state(data)
    await msg.answer("Telefon raqam yuborish uchun pastdagi tugmani bosing: ", reply_markup=phone_number())
    