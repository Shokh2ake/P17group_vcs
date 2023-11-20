"""HOMEWORK - 1"""
# with open("main_file.txt", "w") as file_obj:
#     n = int(input("n: "))
#     for i in range(1, n):
#         file_obj.write(f"{i} \n")
"""HOMEWORK - 2"""
# with open("main_file.txt", "w") as file_obj:
#     n = int(input("n: "))
#     for i in range(2, n, 2):
#         file_obj.write(f"{i} ")
"""HOMEWORK - 3"""
# with open("main_file.txt", "w") as file_obj:
#     n = int(input("n: "))
#     for i in range(1, n, 2):
#         for j in range(n):
#             if i == j:
#                 file_obj.write(f"{i}")
#             else:
#                 file_obj.write(" ")
#         file_obj.write("\n")
"""HOMEWORK - 4"""
# with open("main_file.txt", "w") as file_obj:
#     n = int(input("n: "))
#     s = 0
#     for i in range(1, n):
#         s += i
#         file_obj.write(f"{s} ")
"""HOMEWORK - 5"""
# class User:
#     def __init__(self):
#         self.users = []
#
#     def add(self):
#         n = int(input("Qancha foydalanuvchi qoʻshmoqchsiz? "))
#         for i in range(n):
#             print(f"{i + 1} user:")
#             user = f"""
#             user fullname: {input("Ism kiriting: ")} {input("Familyasini kiriting: ")}
#             """
#             self.users.append(user)
#             with open("main_file.txt", "w") as file_obj:
#                 for i in self.users:
#                     file_obj.write(f"{i}")
#         print("Foydalanuvchi ro'yxatga qo'shildi!")
# obj = User()
# obj.add()
"""HOMEWORK - 6"""
# with open("main_file.txt", "r") as file_obj:
#     if file_obj.read:
#         print(True)
#     else:
#         print(False)
"""HOMEWORK - 7"""
# with open("main_file.txt", "r") as file_obj:
#     a = file_obj.read()
# with open("main_file.txt", "w") as file:
#     for i in a.split():
#         file.write(f"{i} \n")
"""HOMEWORK - 8"""
# class File:
#     def __init__(self, filename: str = None) -> None:
#         self.filename = filename
#     def read(self):
#         with open(self.filename, "r") as file_obj:
#             return file_obj.read()
#
#     def wride(self, data):
#         with open(self.filename, "a") as file_obj:
#             file_obj.write(data)
#
#     def update(self, data):
#         with open(self.filename, "w") as file_obj:
#             file_obj.write(data)
#
#     def clear(self):
#         with open(self.filename, "w") as file_obj
#             file_obj.write(" ")
# file = File("main_file.txt")
# print(file.read())
"""HOMEWORK - 9"""



"""HOME-WORK"""
# class Vehicle:
#
#     def speed(self):
#         return f" max speed 150 "
#
#     def chage_gear(self):
#         return f" gear 5"
#
#     def show(self):
#         return F" {self.speed()} {self.chage_gear()}"
#
#
# class Car(Vehicle):
#
#     def speed(self):
#         return f" speed 240 "
#
#     def change_gear(self):
#         return f" gear 6  "
#
#     def show(self):
#         return F" {self.speed()} {self.chage_gear()}"
#
#
# class Truck(Vehicle):
#
#     def speed(self):
#         return f" speed = 200"
#
#     def chage_gear(self):
#         return F" gear = 8 "
#
#     def show(self):
#         return F" {self.speed()} {self.chage_gear()}"
#
#
# vicle = Vehicle()
# car = Car()
# truc = Truck()
# print(truc.speed())
# print(vicle.show())
# print(car.show())



