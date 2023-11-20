# def groupby(str_: str):
#     group = []
#     for i in str_:
#
#         if i == group[-1][0]:
#             group[-1][1] += i
#         else:
#             group.append((i, i))
#
# print(groupby("AAAAAAAAAA"))

# from datetime import date, datetime
# import time

# print(date.today())
# date_input = input("date: ")
# date.fromisoformat(date_input)
# datetime_input = input("datetime: ")
# d = datetime.fromisoformat(datetime_input)
# d = datetime.now()
# print(d.month)
# print(d.day)
# print(d.hour)
# print(d.minute)
# print(d.second)

# print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# import calendar

# print(calendar.month(2023, 9))

"""======================decorator=========================="""


# def plus_one(number):
#     return number + 1
#
# add_one = plus_one
# print(add_one(5))

# def plus_one(number):
#     def add_one(number):
#         return number + 1
#
#     result = add_one(number)
#     return result
#
#
# print(plus_one(4))


# def plus_one(number):
#     return number + 1
#
#
# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)
#
#
# print(function_call(plus_one))

# def hello_function():
#     def say_hi():
#         return "Hi"
#
#     return say_hi
#
#
# hello = hello_function()
# print(hello())


# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
# def say_hi():
#     return "hello there"
# decorater = uppercase_decorator(say_hi)
# print(decorater())
# import time
#
#
# def uppercase_decorator(function):
#     def wrapper(name):
#         name = name.title()
#         func = function(name)
#         # make_uppercase = func.upper()
#         return func
#
#     return wrapper
#
# def time_decoratr(function):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         re = function(*args, **kwargs)
#         print(time.time() - start)
#         return re
#     return wrapper
# @time_decoratr
# def say_hi(name):
#     # time.sleep(5)
#     return f"Salom {name}"
# @time_decoratr
# def send_massage():
#     time.sleep(3)
#     return "nimadir"
#
# print(send_massage())
# print(say_hi("botiraka"))

# import os
#
# print(os.cpu_count())
#
# user = {
#     "fullname": "Shokhjahon",
#     "age": 19,
#     "username": "Shokh",
#     "password": 1234
# }
#
# def user_valid(function):
#     def wrapper(data: dict):
#         pass
#
#
# def register():
#     return "Success save!"






def user_valid(function):
    def wrapper(data: dict):
        if len(data.get("fullname").split()) < 2:
            raise Exception("Invalid fullname")
        if data.get("age") < 1:
            raise Exception("Invalid age !")
        if len(data.get("password")) < 4:
            raise Exception("Must password 4 chars")
        result = function(data)
        return result
    return wrapper

user = {
    "fullname": "Botirjon Qodirov",
    "age": 15,
    "username": "botir",
    "password": "12345"
}

@user_valid
def register(data: dict):
    return "Success save!"

try:
    print(register(user))
except Exception as e:
    print(e)






