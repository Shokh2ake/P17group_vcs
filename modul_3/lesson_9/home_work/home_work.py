""""
1)# enum
DayOfWeek                           ✔
UserRole                            🗿
Color                               ✔
PizzaSize                           🗿
HTTPStatus                          🗿
Gender                              ✔
Coin                                🗿
FileType                            ✔
PaymentMethod                       ✔
Language                            ✔
MusicGenre                          🗿
ComputerComponent                   ✔

=====================

2)berilgan 2 ta rasmni -> DTO       ✔

=====================

3)algo -> matrix(130-147)           ✔

=====================

4)leetcode -> matrix(10ta)          🗿

=====================

5)leetcode -> string(25 ta)         🗿

=====================

5)leetcode -> array(25 ta)          🗿

=====================

6) BALLI sistema(project)           🗿




"""
from enum import Enum

# class DayOfWeek(Enum):
#     DUSHANBA = "1"
#     SESHANBA = "2"
#     CHORSHANBA = "3"
#     PAYSHANBA = "4"
#     JUMA = "5"
#     SHANBA = "6"
#     YAKSHANBA = "7"
#
# menu = """
#     1) Dushanba
#     2) Seshanba
#     3) Chorshanba
#     4) Payshanba
#     5) Juma
#     6) Shanba
#     7) Yakshanba
#     >>>"""
# key = input(menu)
# print(DayOfWeek(key).name)

# ======================================================================

# class Color(Enum):
#     QIZIL = "1"
#     SARIQ = "2"
#     YASHIL = "3"
#     OQ = "4"
#     KOK = "5"
#     QORA = "6"
#     OLTIN = "8"
#     YORQIN = "9"
#
# menu = """
#     1) Qizil
#     2) Sariq
#     3) Yashil
#     4) Oq
#     5) Kok
#     6) Qora
#     8) Oltin
#     9) Yorqin
#     >>>"""
# print(Color(input(menu)).name)

# ======================================================================

# class Gender(Enum):
#     MALE = "1"
#     WOMAN = "2"
#
# gender = """
#     1) MALE
#     2) WOMAN
#     >>>"""
# print(Gender(input()).name)

# ======================================================================

# class Language(Enum):
#     RUSSKIY = "1"
#     UZBEK = "2"
#     ENGLISH = "3"
#     TURETISKIY = "4"
#     KAZAK = "5"
#     TJK = "6"
#     KRGIZ = "7"
#     TURKMAN = "8"
#     AZARBAYJAN = "9"
#     POKISTAN = "10"
#
# menu = """
#     1) RUSSKIY
#     2) UZBEK
#     3) ENGLISH
#     4) TURETISKIY
#     5) KAZAK
#     6) TJK
#     7) KRGIZ
#     8) TURKMAN
#     9) AZARBAYJAN
#     10) POKISTAN
#     >>>"""
# print(Language(input(menu)).name)

# ======================================================================

# class ComputerComponent(Enum):
#     HP = "1"
#     ACER = "2"
#     VICTUS = "3"
#     LENOVO = "4"
#     ASUS = "5"
#
# menu = """
#
#     1) HP
#     2) ACER
#     3) VICTUS
#     4) LENOVO
#     5) ASUS
#     >>>"""
# print(ComputerComponent(input(menu)).name)

# ======================================================================

# class PaymentMethod(Enum):
#     PAYNET = "1"
#     PAYME = "2"
#     CLICK = "3"
#     UZUM_BANK = "4"
#
# menu = """
#
#     1) PAYNET
#     2) PAYME
#     3) CLICK
#     4)UZUM BANK
#     >>>"""
#
# print(PaymentMethod(input(menu)).name)

# ======================================================================

# class FileType(Enum):
#     JSON = "1"
#     SCV = "2"
#     EXCEL = "3"
#     LONG = "4"
#
# menu = """
#
#     1) JSON
#     2) SCV
#     3) EXCEL
#     4) LOG
#     >>>"""
#
# print(FileType(input(menu)).name)

# ======================================================================

# class Gender(Enum):
#     MALE = "1"
#     WOMAN = "2"
#
# menu = """
#
#     1) MALE
#     2) WOMAN
#     >>>"""
#
# print(Gender(input(menu)).name)









# from collections import namedtuple
"""1-rasm"""
# Orders = namedtuple('OrderDTO', ('order_id', 'order_data', '.customer_id'))
# Customers = namedtuple('CustomersDTO', ('customer_id', 'customer_phone', 'customer_email'))
# Orders_items = namedtuple('Orders_itmsDTO', ('order_id', 'item_id'))
# Items = namedtuple('ItemsDTO', ('item_id', 'item_price'))
"""2-rasm"""
# Users = namedtuple('UsersDTO', ('user_id', 'first_name', 'last_name', 'address', 'email'))
# Orders = namedtuple('OrdersDTO', ('order_id', 'user', 'product_ordered', 'total_paid'))
# Products = namedtuple('ProductsDTO', ('product_id', 'product_name', 'description', 'price'))
#
# user = Users("1", "Saitqulov", "Shohjahon", "Samarkand","jahonsaitqulov@gmail.com")
# order = Orders('1', 'Shokh', 'Iphone', '50000')
# product = Products('3', 'Monza', "Zo'rlekin", '20000$')
# print(product)











