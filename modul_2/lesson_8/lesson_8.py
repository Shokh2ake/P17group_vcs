# amount = 1000
#
# if (amount > 2999):
#     print("You are elingible to ")
#
# marks = 10000
#
# a = marks / 0
# print(a)
#
# x = 5
# y = "hello"
# try:
#     z = x + y
# except TypeError:
#     print("Xato: int va str qo'shib bo'lmaydi")
# print(1 / 0)
# print("hello")
# try:
#     print(1 / 1)
# except :
#     print("Xato")
# print("hello")


a = 9
b = 0
try:
    assert b != 0 , "Assertion failed"
    print(a / b)
except AssertionError as e:
    print(e)



