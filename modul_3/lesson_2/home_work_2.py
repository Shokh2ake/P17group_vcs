""""
Home Work

    1) login_valid()
    2) key_valid()
    3) datetime_valid()
    4) strip_case()

    5) algo - (1-172)
    6) leetcode - string 10 ta misol!
"""

#login valid

# user = {
#     "username": input("Username: "),
#     "password": input("Password: ")
# }
#
#
# def login_valid(function):
#     def wrapper(data: dict):
#         if len(data.get("username").split()) < 2:
#             raise Exception("Usernameda xatolik !")
#         if len(data.get("password")) <= 8:
#             raise Exception("Passwordda kamchik bor !")
#         result = function(data)
#         return result
#
#     return wrapper
#
#
# @login_valid
# def login():
#     return "Muvaffaqiyatni saqlang !"
#
#
# try:
#     print(login(user))
# except Exception as e:
#     print(e)


#date time

from datetime import datetime

def check_datetime(function):
    def wrapper(datetime_):
        pass



