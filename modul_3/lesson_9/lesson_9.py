# import openpyxl
#
# path = "Book2_unit10.xlsx"
# obj = openpyxl.load_workbook(path)
# sheet_obj = obj.active
# max_col =


#===========================================

# from enum import Enum

# class Season(Enum):
#     SPTRING = 0
#     SUMMER = 1
#     AUTUMN = 2
#     WINTER = 3


# class Gener(Enum):
#     MALE = "1"
#     WOMEN = "2"
#
#
# menu = """
#     1) MALE
#     2) WOMAN
#     >>>"""
# key = input(menu)
# print(Gener(key).name)


# class Customers:
#     def __init__(self, customerID,
#                  firstName,
#                  lastName,
#                  birthDate,
#                  moneySpent,
#                  anniversary
#                  ):
#         self.customerID = customerID
#         self.firstName = firstName
#         self.lastName = lastName
#         self.birthDate = birthDate
#         self.moneySpent = moneySpent
#         self.anniversary = anniversary


# from collections import namedtuple

# Customers = namedtuple("CustomersDTO", ('customerID', 'firstName', 'birthDate', 'moneySpent', 'anniversary'))
# Employees = namedtuple("EmployeesDTO", ('employeeID', 'firstName', 'birthDate'))
# Products = namedtuple("CustomersDTO", ('productID', 'category', 'price'))
# Orders = namedtuple("OrdersDTO", ('orderID', 'customerID', 'employeeID', 'productID', 'orderTotal', 'orderDate'))




from collections import UserString



#
# class MyString(UserString):
#
#     pass





"""QR code"""
# import qrcode
#
# manzil = "https://t.me/c/1919667762/38"
#
# qrcode.make(manzil).save("Qondaye.png")





from datetime import datetime
#
Sana1 = "1997-03-09"
Sana2 = "2021-08-05"

tarih1 = datetime.strptime(Sana1, "%Y-%m-%d")
tarih2 = datetime.strptime(Sana2, "%Y-%m-%d")

gun_farki = (tarih2 - tarih1).days

print("İki tarih arasındaki gün farkı:", gun_farki)





# ====================================================================================














