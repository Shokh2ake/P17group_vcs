# class A:
#     def __init__(self, num):
#         self.num = num
#
#     def __truediv__(self, other):
#         return self.num / other
#
#     def __floordiv__(self, other):
#         return self.num // other
#
#     def __mod__(self, other):
#         return self.num % other
#
#
# o = A(10) / 4
# r = A(10) // 4
# p = A(10) % 4
# print(o)
# print(r)
# print(p)


# class A:
#     def __init__(self, st):
#         self.st = st
#
#     def __add__(self, other):
#         return f"{self.st} {other}"
# a = A("Hello") + "Shokh"
# print(a)


# class A:
#     def __init__(self, num):
#         self.num = num
#
#     def __lt__(self, other):
#         return self.num < other
#
#     def __gt__(self, other):
#         return self.num > other
#
# u = A(4) > 6
# o = A(5) < 6
# print(o)
# print(u)


# class A:
#     def __init__(self, num):
#         self.num = num
#     def __neg__(self):
#         return f"-{self.num}"
#     def __pos__(self):
#         return f"+{self.num}"

# ==================================================================================

# class A:
#     def __init__(self, num):
#         self.num = num
#
#     def __add__(self, other):
#         return self.num + other
#
#     def __sub__(self, other):
#         return self.num - other
#
#     def __mul__(self, other):
#         return self.num * other
#
#     def __truediv__(self, other):
#         return self.num / other
#
# a = A(3) + 2
# print(a)
# b = A(9) - 2
# print(b)
# c = A(2) * 2
# print(c)
# d = A(6) / 2
# print(d)




