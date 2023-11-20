from aiogram.types import KeyboardButton, ReplyKeyboardMarkup




# def numer_button():
#
#     n1 = KeyboardButton(text='1')
#     n2 = KeyboardButton(text='Phone number', request_contact=True)
#     n3 = KeyboardButton(text='Location', request_location=True)
#     n4 = KeyboardButton(text='4')
#     n5 = KeyboardButton(text='5')
#     n6 = KeyboardButton(text='6')
#     n7 = KeyboardButton(text='7')
#     n8 = KeyboardButton(text='8')
#
#
#     design = [
#         # [KeyboardButton(text='1'), KeyboardButton(text='2'), KeyboardButton(text='3'), KeyboardButton(text='4')],
#         # [KeyboardButton(text='5'), KeyboardButton(text='6'), KeyboardButton(text='7'), KeyboardButton(text='8')]
#         [n1, n2, n3, n4],
#         [n5, n6, n7, n8]
#     ]
#
#     rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
#     return rkm


def number_butn():
    n1 = KeyboardButton(text='🏢О КОМПАНИИ')
    n2 = KeyboardButton(text='📍Филиалы')
    n3 = KeyboardButton(text='💼Вакансии')
    n4 = KeyboardButton(text='📱Меню')
    n5 = KeyboardButton(text='🗣Новости')
    n6 = KeyboardButton(text='📞Контакты/Адрес')
    n7 = KeyboardButton(text='🇺🇿/🇷🇺Язык')


    desgn = [
        [n1, n2],
        [n3],
        [n4, n5],
        [n6, n7]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=desgn, resize_keyboard=True)
    return rkm


# from modul_5.lesson_1.language import uzb_lang, eng_lang, lang
#
#
# def level_btn(data):
#     design = [
#         [data.get("level1"), data.get("level2")],
#         [data.get("level3"), data.get("level4")],
#         [data.get("back")]
#     ]
#
#     markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
#     return markup
#
#
# def lang_btn():
#     design = [
#         [uzb_lang, eng_lang]
#     ]
#
#     markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
#     return markup