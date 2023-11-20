# import json
# import random
#
#
# class File:
#     def __init__(self, filename: str = None):
#         self.filename = filename
#
#     def read(self):
#         with open(self.filename, "r") as f:
#             return json.load(f)
#
#     def write(self, data: list[dict]):
#         with open(self.filename, "w") as f:
#             json.dump(data, f, indent=3)
#
#
# # ///////////////////////////////////////////////
# class User:
#     def __init__(self,
#                  id: int = None,
#                  fullname: str = None,
#                  passport_id: int = None,
#                  password: int = None,
#                  card_number: int = None,
#                  balance: int = 0
#                  ):
#         self.id = id
#         self.fullname = fullname
#         self.passport_id = passport_id
#         self.password = password
#         self.card_number = card_number
#         self.balance = balance
#
#     def register(self):
#         file = File("users.json")
#         users = file.read()
#         user = self.__dict__
#         users.append(user)
#         file.write(users)
#
#     def login(self, data):
#         self.check_login(data)
#         UI().account(data)
#
#     def check_login(self, data):
#         file = File("users.json")
#         users = file.read()
#         for user in users:
#             if user.get("card_number") == data.get("card_number") and user.get("password") == data.get("password"):
#                 UI().account(data)
#         else:
#             print("Card nuber yoki password hato!")
#             UI().main()
#
#     def check_passport_id(self, data: dict):
#         file = File("users.json")
#         users = file.read()
#         for user in users:
#             if user.get("passport_id") == data.get("passport_id"):
#                 print("Munday passport ID kiritilgan !")
#                 UI().main()
#
#     def random_id(self):
#         id = random.randrange(1, 10_000_000)
#         return self.check_id(int(id))
#
#     def check_id(self, id: int = None):
#         file = File("users.json")
#         users = file.read()
#         for user in users:
#             if user.get("id") == id:
#                 self.random_id()
#         return id
#
#     def random_card_number(self):
#         new_card_number = random.randrange(1, 10_000)
#         return self.check_card_number(new_card_number)
#
#     def check_card_number(self, new_card_number: int = None):
#         file = File("users.json")
#         users = file.read()
#         for user in users:
#             if user.get("card_number") == new_card_number:
#                 self.random_id()
#         else:
#             return new_card_number
#
#     def login_card_nuber(self, search_card):
#         file = File("users.json")
#         users = file.read()
#         for i, user in enumerate(users):
#             if user.get("card_number") == search_card:
#                 return i
#         else:
#             print("munday card topilmadi !")
#
#     def check_balance(self, data, summa):
#         file = File("users.json")
#         users = file.read()
#         for i, user in enumerate(users):
#             if user.get("card_number") == data.get("card_number"):
#                 if user.get("balance") >= summa:
#                     users[i]["balance"] = user.get("balance") - summa
#                     file.write(users)
#                 else:
#                     print("Mablag yetarli emas")
#                     UI().account(data)
#
#                 # ///////////////////////////////////////////////////
#
#
# class UI:
#     def main(self):
#         menu = """
#         1) Register
#         2) Login
#         3) Exit
#         >>>"""
#         key = input(menu)
#         match key:
#             case "1":
#                 new_card_number = User().random_card_number()
#
#                 data = {
#                     "id": User().random_id(),
#                     "fullname": input("Fulname : "),
#                     "passport_id": input("Passport id : "),
#                     "password": int(input("Password : ")),
#                     "card_number": new_card_number
#                 }
#                 User().check_passport_id(data)
#                 data = User(**data)
#                 data.register()
#                 print(f"Sizning card nomeringiz {new_card_number} ")
#                 print("Siz Royhatan otingiz.")
#                 self.main()
#             case "2":
#                 data = {
#                     "card_number": int(input("Card number : ")),
#                     "password": int(input("Password : "))
#                 }
#                 User().login(data)
#             case "3":
#                 return
#
#     def account(self, data):
#         menu = """
#         1) Transfer mony
#         2) Balanse
#         3) logaut
#         >>>"""
#         key = input(menu)
#         match key:
#             case "1":
#                 search_card = int(input("card_number"))
#                 file = File("users.json")
#                 index = User().login_card_nuber(search_card)
#                 summa = int(input("Summa : "))
#                 User().check_balance(data, summa)
#                 users = file.read()
#                 users[index]["balance"] = users[index]["balance"] + summa
#                 file.write(users)
#                 print("Tolovingiz uchun Raxmat")
#                 self.account(data)
#             case "2":
#                 file = File("users.json")
#                 users = file.read()
#                 for user in users:
#                     if user.get("card_number") == data.get("card_number"):
#                         print(user.get("balance"))
#                         return self.account(data)
#             case "3":
#                 self.main()
#
#
# run = UI()
# run.main()




















