from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def inline_number():
    # btn1 = InlineKeyboardButton(text='1', callback_data='1')
    # btn2 = InlineKeyboardButton(text='Tavarlar', callback_data='Tavar')
    # btn3 = InlineKeyboardButton(text='Kun uz', url='https://kun.uz')
    # btn4 = InlineKeyboardButton(text='Admin', url='https://t.me/shokh_saitqulov')
    # design = [
    #     [btn1, btn2],
    #     [btn3, btn4]
    # ]

    # btn1 = InlineKeyboardButton(text='📱Меню', url='https://evos.uz/')
    # btn2 = InlineKeyboardButton(text='📱Меню', url='https://www.instagram.com/evosuzbekistan/')
    # btn3 = InlineKeyboardButton(text='📱Меню', url='https://t.me/evosdeliverybot')
    # btn4 = InlineKeyboardButton(text='📱Меню', url='https://www.facebook.com/evosuzbekistan/')
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [
        InlineKeyboardButton(text="Перейти на сайт Evos", url="https://evos.uz/"),
        InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/evosuzbekistan/"),
        InlineKeyboardButton(text="Telegram", url="https://t.me/evosdeliverybot"),
        InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/evosuzbekistan/")
    ]
    keyboard.add(*buttons)

    ikm = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return ikm