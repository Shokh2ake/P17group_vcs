# Telegram bot -> TeleBot,


import asyncio
import logging
import sys
from os import getenv

import ldb
from aiogram import Bot, Dispatcher  # , Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F
from aiogram.filters.command import Command
from aiogram import types
import emoji

from modul_5.lesson_1.inline import inline_number
from modul_5.lesson_1.reply import number_butn

TOKEN = "6577787774:AAHuz9S2cTEBKvf3jzTF-tPMMBED7rcjFLI"

dp = Dispatcher()


#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     await message.answer(f"Qondaye, {hbold(message.from_user.full_name)}!")


# @dp.message()
# async def echo_message_handler(msg: Message):
#     # await msg.answer("Qonday nima gap?")
#     for i in range(1):
#         await msg.copy_to(msg.from_user.id)
#
# @dp.message()
# async def echo_message(msg: Message):
#     await msg.answer("⏳")

#
# @dp.message(F.photo)
# async def photo_handler(msg: Message):
#     await msg.answer("Photo handler successful")


# @dp.message(F.document)
# async def photo_handler(msg: Message):
#     await msg.answer("Photo handler successful")
#     await msg.answer("Photo handler successful")
#
#
# @dp.message(F.video)
# async def photo_handler(msg: Message):
#     await msg.answer(f"document handler successful\n{msg.document.file_id}")
#
#
# @dp.message(F.audio)
# async def photo_handler(msg: Message):
#     await msg.answer("audio handler successful")
#     await msg.answer(f"{msg.audio.file_id}")
#
#
# @dp.message(F.sticker)
# async def photo_handler(msg: Message):
#     await msg.answer("sticker handler successful")
#     await msg.answer(f"{msg.sticker.file_id}")
#
#
# @dp.message(F.voice)
# async def photo_handler(msg: Message):
#     await msg.answer("voice handler successful")
#     await msg.answer(f"{msg.voice.file_id}")
#
#
# @dp.message(F.gif)
# async def photo_handler(msg: Message):
#     await msg.answer("GIF handler successful")
#
#
#
# @dp.message(lambda msg: emoji.emoji_count(msg.text) > 0)
# async def photo_handler(msg: Message):
#     await msg.answer("emoji handler successful")


# @dp.message(F.context.in_("photo"))
# async def photo_handler(msg : Message):
#     async msg.answer(" Photo hannle sucsefully !")

@dp.message(Command("start"))
# @dp.message(Command("admin"))
# @dp.message(Command("panel"))
# @dp.message(CommandStart)

# @dp.message(lambda msg: msg.text.isdigit() and 1 <= int(msg.text) <= 100)
# @dp.message(F.text.isdigit())

# async def digit_handler(msg: Message):
#     await msg.answer("Hello world", reply_markup=numer_button())
async def digit_handlerrr(msg: Message):
    # await msg.answer("Hello", reply_markup=inline_number())
    await msg.answer_photo("AgACAgIAAxkBAAOvZVDAgOb0ehmX265SJTareBHP_JwAAhHKMRu67IBKWiltgsaVq08BAAMCAANzAAMzBA",
                           reply_markup=number_butn())


@dp.message(lambda msg: msg.text == '🏢О КОМПАНИИ')
async def Kompany_button(msg: Message):
    await msg.answer_animation(
        animation="CgACAgIAAxkBAAPeZVDNpH5MEhNuAAEOawxTBYkZYxVWAAISDQACvbcxSYoZgspJl-sYMwQ",
        caption="""Информация о компании:

        Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц.
        Сейчас в нашей сети насчитывается более 50 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®.
        EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста.
        Начни свою карьеру в EVOS® уже сейчас!""",
        duration=5
    )


# @dp.message(F.photo)
@dp.message(lambda msg: msg.text == '📍Филиалы')
async def Filiallar_button(msg: Message):
    await msg.answer_photo(photo="AgACAgIAAxkBAAPtZVI6lMU0hPxPGMSjpxDsyzVcrhsAApbTMRvvp5FKgFpsMerAVokBAAMCAANzAAMzBA",
                           caption="""EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто 49 торговых точек и современное многопрофильное производство.

Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!""",
                           duration=5)
    # print(msg.photo[0].file_id)


@dp.message(lambda msg: msg.text == '💼Вакансии')
async def Ish_orin_button(msg: Message):
    await msg.answer(f"{msg.text} bosildi")


# @dp.message(F.photo)
@dp.message(lambda msg: msg.text == '📱Меню')
async def menu_handler(message: types.Message) -> None:
    image_url = "AgACAgIAAxkBAAIBJ2VTFze_xH9JiBYJpXr4Fiw_QaMFAAJg0DEb2FWZSnj5QJlqMX_hAQADAgADcwADMwQ"
    caption = (
        "<a href='https://evos.uz'>Перейти на сайт Evos</a>")
    await message.answer_photo(photo=image_url, caption=caption)
    caption1 ="<a href='https://www.instagram.com/evosuzbekistan/'>Instagram</a>|<a href='https://t.me/@evosdeliverybot'>Telegram</a>|<a href='https://www.facebook.com/evosuzbekistan/'>Facebook</a>"
    await message.answer(text=caption1)
    # print(message.photo[0].file_id)

@dp.message(lambda msg: msg.text == '🗣Новости')
async def Yangiliklar_button(msg: Message):
    await msg.answer(
"""
Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.""")


# @dp.message(F.photo)
@dp.message(lambda msg: msg.text == '📞Контакты/Адрес')
async def location_handler(msg: types.Message) -> None:
    image_url = "AgACAgIAAxkBAAIBDGVTDTVI9HgnU91Ex051tPGc8kkaAAJF0DEb2FWZSjt1h4LrYmrhAQADAgADcwADMwQ"
    caption = '📍Адрес:  ул. Фурката 175, 1 подъезд, 2\n этаж. 📌Ориентир: MAKRO THE TOWER\n 📲 Контакты: +998 71 203 12 12'

    await msg.answer_photo(
        photo=image_url, caption=caption)
    await msg.answer_location(latitude=41.326494, longitude=69.228355)
    # print(msg.photo[0].file_id)

@dp.message(lambda msg: msg.text == '🇺🇿/🇷🇺Язык')
async def Til_button(msg: Message):
    await msg.answer(f"{msg.text} bosildi")


@dp.message(F.document)
async def photo_handler(message: Message):
    await message.answer("GIF handler successful")
    await message.answer(f"{message.document.file_id}")


@dp.message(lambda msg: msg.text == '1')
async def onehendler(msg: Message):
    await msg.answer('Bir raqami bosildi !')


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


@dp.message(F.contact)
async def contact_handler(msg: Message):
    await msg.answer(msg.contact.phone_number)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
