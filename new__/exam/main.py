"""1 - misol"""

# range(start end step) clone generatorda yaratish


# def rangee(*args):
#     l = len(args)
#     start = 0
#     step = 1
#     end = args[0]
#     if l == 1:
#         end = args[0]
#     elif l == 2:
#         start = args[0]
#         end = args[1]
#     elif l == 3:
#         start = args[0]
#         end = args[1]
#         step = args[2]
#     while start < end:
#         yield start
#         start += step
#
# for i in rangee(1, 100, 7):
#     print(i)


"""2 - misol"""

# Sana1 = "1997-03-09", Sana2 = "2021-08-05"
# Shu oraliqda necha kun farq borliginin topuvchi dastur tuzish


# from datetime import datetime

# date1 = input("Yil oy kun kiriting: ")
# date2 = input("Yil oy kun kiriting: ")
# try:
#     date1 = datetime.strptime(date1, "%Y-%m-%d")
#     date2 = datetime.strptime(date2, "%Y-%m-%d")
#
#     difference = date2 - date1
#
#     difference_in_days = difference.days
#
#     print(f"Ikki sana orasidagi kunlardagi farq {abs(difference_in_days)} days.")
# except:
#     print("Xato sana kiritdingiz! ")


"""3 - misol"""

# 4 ta function yaratilsin
# 1-chi function 3 sekond, 2-chi function 4 sekond, 3-chi funtion 6 sekond, 4-chi function 8 sekond
# va bu yaratilgan functionlarni bir vaqtda minimu vaqtda ishini tugatadingan dastur tuzulsin


# import threading
# import time
#
#
# def a1():
#     time.sleep(3)
# def a2():
#     time.sleep(4)
# def a3():
#     time.sleep(6)
# def a4():
#     time.sleep(8)
#
# threads = []
#
# datas = [a1, a2, a3, a4]
# start = time.time()
# for url in datas:
#     thread = threading.Thread(target=url)
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print("Ish bajarildi vaqt:", time.time() - start)


"""4 - savol"""

# async, Multithreading, Multiprocessing bir biridan farqi aniqroq yaratilsin
# async request yuboradigan function yaratilsin (aiohttp) :
# https://jsonplanceholder.typicode.com/  posts, comments,  users, albums, photos todos


# import aiohttp
# import asyncio
#
# async def fetch_data():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
#             data = await response.json()
#             return data
#
# async def main():
#     data = await fetch_data()
#     print(data)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())


"""5 - misol"""
# LinkedList" Node class yarating
# https://jsonplanceholder.typicode.com/comments   shu linkdan malumotlarni olib LinkedList hosil qilinsin


# import requests
#
#
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# data = requests.get("https://jsonplaceholder.typicode.com/comments")
# head = Node(0)
# tmp = head
# for i in data.json():
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head.next
# while tmp:
#     print(tmp.value)
#     print()
#     tmp = tmp.next

"""==============================================================================================================="""

# import logging
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
#
#
# def send_email(receiver_email, file_address):
#
#     sender_email = "shokhake6690@gmail.com"
#     sender_password = "qskahdybmhhqysja"
#     receiver_email = receiver_email
#     subject = "Test E-pochta"
#
#     msg = MIMEMultipart()
#     msg["From"] = sender_email
#     msg["To"] = receiver_email
#     msg["Subject"] = subject
#
#     text = f"Sizga file yuborildi: {file_address}"
#     msg.attach(MIMEText(text, "plain"))
#
#     filename = file_address
#     attachment = open(filename, "rb")
#     part = MIMEBase('application', 'octet-stream')
#     part.set_payload((attachment).read())
#     encoders.encode_base64(part)
#     part.add_header('Content-Disposition', f"attachment; filename={filename}")
#     msg.attach(part)
#
#     try:
#         smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
#         smtp_server.starttls()
#         smtp_server.login(sender_email, sender_password)
#         smtp_server.sendmail(sender_email, receiver_email, msg.as_string())
#         smtp_server.quit()
#         logging.info("E-pochta muvaffaqiyatli yuborildi!")
#         return file_address
#     except Exception as e:
#         logging.error(f"Error sending email: {str(e)}")
#         return None
#
#
# receiver_email = "jahonsaitqulov@gmail.com"
# file_address = "/home/shokhake/PycharmProjects/P17group/modul_3/lesson_11/main.py"
# send_email(receiver_email, file_address)

# ======================================================================================================================

# import json
# import time
#
# import requests
#
# def writer_datas(datas):
#     for i in datas:
#         data = requests.get(i)
#         with open("userss.json", "a") as f:
#             json.dump(data.json(), f, indent=3)
#
# start = time.time()
# datas = "https://jsonplaceholder.typicode.com/posts https://jsonplaceholder.typicode.com/comments https://jsonplaceholder.typicode.com/albums https://jsonplaceholder.typicode.com/photos https://jsonplaceholder.typicode.com/todos https://jsonplaceholder.typicode.com/users".split()
# writer_datas(datas)
# print(time.time() - start)


# ======================================================================================================================


# STUDENT_TABLE = """
#     create table if not exists student(
#         id integer primary key autoincrement,
#         fullname varchar(255) not null,
#         phone varchar(255) not null,
#         password varchar(255) not null,
#         status boolean default FALSE,
#         rank integer default 0
#     );
# """
#
# GROUP_TABLE = """
#     create table if not exists group(
#         id integer primary key autoincrement,
#         name varchar(255) not null,
#         teacher_id integer,
#         subject_id integer,
#         status boolean default FALSE,
#         time varchar(255) not null
#     );
# """
#
# SUBJECT_TABLE = """
#     create table if not exists subject(
#         id integer primary key primary key,
#         name varchar(255)
#     );
# """


# ======================================================================================================================

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# # "salom",2,3,4
#
# massiv = range(1, 100)
#
# head = Node(0)
# tmp = head
# for i in massiv:
#     tmp.next = Node(i)
#     tmp = tmp.next
# # node1 = Node("salom")
# # node2 = Node(2)
# # node3 = Node(3)
# # node4 = Node(4)
# #
# # node1.next = node2
# # node2.next = node3
# # node3.next = node4
# tmp = head.next
# while tmp:
#     print(tmp.next.next)
#     tmp = tmp.next
#
#
# # juft qiymatga ega tugunlarni remove qilish
# tmp = head
# while tmp and tmp.next:
#     if tmp.next.value % 2 == 0:
#         tmp.next = tmp.next.next
#     tmp = tmp.next
#
# tmp = head.next
# while tmp:
#     print(tmp.value)
#     tmp = tmp.next
#
#
# # ohirgi tugun qiymatini print qilish
#
# tmp = head.next
# while tmp.next.next:
#     tmp = tmp.next
#
# print(tmp.value)

# =============================================================================================


# import sqlite3
#
#
# class CreateSQL:
#     def __init__(self, filename):
#         self.filename = filename
#         self.con = sqlite3.connect(self.filename)
#         self.cur = self.con.cursor()
#
#     def create_table(self, table_name):
#         query = f"""
#             create table  if not exists {table_name}(
#             id integer primary key autoincrement,
#             fullname varchar (255) not null,
#             username varchar (255) not null unique,
#             password varchar (4) not null
#             );
#             """
#
#         self.cur.execute(query)
#         self.con.commit()
#
#     def insert(self, data: dict):
#         query = """
#         insert into userrr(fullname, username, password)
#         values (?, ?, ?) """
#         params = (data.get("fullname"), data.get("username"), data.get("password"))
#
#         self.cur.execute(query, params)
#         self.con.commit()
#
#
#     def delete(self, username):
#         query = """
#             delete from userrr where username=?"""
#         params = (username,)
#         self.cur.execute(query, params)
#         self.con.commit()
#
#     def select(self, username, password):
#         query = """
#             select * from userrr where username=? and password=?"""
#         params = (username, password)
#         self.cur.execute(query, params)
#         user = self.cur.fetchone()
#         return user
#     def update(self, field, new_value, id):
#         query = f"""
#             update userrr set {field} = ? where id =?"""
#         params = (new_value, id)
#         self.cur.execute(query, params)
#         self.con.commit()
#
#
#
#
#
#
#             # data = {
#             #     "fullname": input(),
#             #     "username": input(),
#             #     "password": input()
#             # }
#
#
# c = CreateSQL("/Users/macbookpro/PycharmProjects/p17_group/Module_3/Lesson_7/testt.sqlite")
# # c.insert(data)
# c.update("username", "L", 3)

#==================================================================

# import json
#
# async def write_to_json_file(filename, data):
#     with open(filename, 'w') as file:
#         json.dump(data, file)
#
# # Misol uchun ma'lumotlar
# data = {
#     'name': 'John Doe',
#     'age': 25,
#     'city': 'Tashkent'
# }
#
# # Asosiy ishni bajarish uchun asosiy funksiya
# async def main():
#     await write_to_json_file('data.json', data)
#     print("Ma'lumot JSON faylga yozildi.")
#
# # Asosiy funksiyani chaqirish
# asyncio.run(main())




#===================================================







"""
Asinxron
dasturlash (Asinxron) : Asinxron dasturlash bloklanmaydigan kiritish-chiqarish operatsiyalarini bajara oladigan
va tizim resurslaridan samarali foydalana oladigan bir vaqtda kodni loyihalash imkonini beradi. U odatda mustaqil
ravishda bajarilishi mumkin bo'lgan tarmoq so'rovlari yoki fayl kiritish/chiqarish kabi potentsial uzoq muddatli
operatsiyalar mavjud bo'lgan stsenariylarda qo'llaniladi. Asinxron dasturlash yordamida siz avvalgi operatsiya
tugashini kutmasdan operatsiyani boshlashingiz va boshqa vazifalarni bajarishni davom ettirishingiz mumkin.
Bunga koroutinlar, hodisalar tsikllari va asinxron funktsiyalar kabi usullardan foydalanish orqali erishiladi.
Async dasturlash odatda Python'da asyncio kabi ramkalarda qo'llaniladi.


Multithreading :
Multithreading bir jarayon ichida bir vaqtning o'zida bir nechta iplarni bajarishni o'z ichiga oladi.
 Mavzular engil va bir xil xotira maydoniga ega bo'lib, ularga osongina ma'lumot almashish va almashish imkonini beradi.
  Multithreading stsenariylar uchun javob beradi, bu erda vazifalar parallel bajarilishi mumkin va ko'plab CPU bilan
  bog'liq operatsiyalarni o'z ichiga oladi. Biroq, Python-da bir vaqtning o'zida Python bayt-kodini bajarishga faqat
  bitta ipni ta'minlaydigan Global Interpreter Lock (GIL) tufayli, ko'p ish zarralari Python-da CPU bilan bog'langan
   vazifalar uchun haqiqiy parallellikni ta'minlamasligi mumkin. Bu kirish/chiqarish bilan bog'liq vazifalar yoki
protsessor unumdorligi muammosi bo'lmagan stsenariylar uchun samaraliroq.

"""


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# data = requests.get("https://jsonplaceholder.typicode.com/comments")
# head = Node(0)
# tmp = head
# for i in data.json():
#     tmp.next = Node(i)
#     tmp = tmp.next
#
# tmp = head.next
# while tmp:
#     print(tmp.value)
#     print()
#     tmp = tmp.next



# import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler
# from telegram.ext.filters import Filters
# from telegram.ext import Updater, CommandHandler, MessageHandler#, Filters
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Assalomu alaykum!")
#
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
# def main():
#     updater = Updater(token='6479418150:AAEgFePPv1OjMeRO2GRtMhHxwtFVl6xcvrQ', use_context=True)
#     dispatcher = updater.dispatcher
#
#     start_handler = CommandHandler('start', start)
#     echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#
#     dispatcher.add_handler(start_handler)
#     dispatcher.add_handler(echo_handler)
#
#     updater.start_polling()
#
# if __name__ == '__main__':
#     main()












