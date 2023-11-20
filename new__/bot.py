import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import psycopg2

# Database connection parameters
DB_PARAMS = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '1',
    'host': 'localhost',
    'port': 5432,
}

con = psycopg2.connect(**DB_PARAMS)
cur = con.cursor()

BOT_TOKEN = "6665230931:AAHZMyuQoZulWiNUhpBe3GdztVob82K_mMk"
dp = Dispatcher(storage=MemoryStorage())


class UserState(StatesGroup):
    name = State()
    age = State()
    phone_number = State()
    request = State()


def phone_button():
    phone_btn = KeyboardButton(text="Phone ☎️", request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[phone_btn]], resize_keyboard=True, one_time_keyboard=True)


def request_button():
    save = InlineKeyboardButton(text="SAVE 🟢", callback_data="save")
    edit = InlineKeyboardButton(text="EDIT 📝", callback_data="edit")
    design = [
        [save, edit]
    ]
    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    await msg.answer("Ismizni kiriting : ")
    await state.set_state(UserState.name)


@dp.message(UserState.name)
async def name_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"name": msg.text})
    await state.set_data(data)
    await msg.answer("Yoshizni kiriting EXAMPLE (25-24-45): ")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def age_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    data.update({"age": msg.text})
    await state.set_data(data)
    await msg.answer("Telefon raqamni yuborish uchun quydagi buttondi bosing : ", reply_markup=phone_button())
    await state.set_state(UserState.phone_number)


@dp.message(UserState.phone_number, F.contact)
async def phone_number_handler(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    phone = msg.contact.phone_number

    if not is_user_exist(name, age, phone):
        save_to_database(name, age, phone)
        text = f"name : {name}\nage : {age}\nphone ☎️: {phone}"
        await msg.answer(text, reply_markup=request_button())
        await state.set_state(UserState.request)
    else:
        await msg.answer("Foydalanuvchi ma'lumotlari allaqachon mavjud. Agar kerak bo'lsa, uni tahrirlashingiz mumkin.")


@dp.callback_query(UserState.request)
async def request_handler(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'save':
        await call.message.answer("Mofaqaiyatli saqlandi !")
    elif call.data == "edit":
        await call.message.answer("Ismizni kiriting : ")
        await state.set_state(UserState.name)


# Function to save user data to the database
def save_to_database(name, age, phone):
    insert_query = """
        INSERT INTO users (name, age, phone_number)
        VALUES (%s, %s, %s)
    """
    params = (name, age, phone)
    cur.execute(insert_query, params)
    con.commit()


# Function to check if the user already exists in the database
def is_user_exist(name, age, phone):
    select_query = """
        SELECT * FROM users
        WHERE name = %s AND age = %s AND phone_number = %s
    """
    params = (name, age, phone)
    cur.execute(select_query, params)
    return bool(cur.fetchone())


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())