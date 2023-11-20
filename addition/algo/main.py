"""1-misol"""
# x = int(input())
# v = x ** 3
# print(v)
"""2-misol"""
# from math import pi
#
# p = pi
# a, b, c = map(int, input().split())
# x, y, z = a ** 2 * p, b ** 2 * p, c ** 2 * p
# print(f"{x:.2f} {y:.2f}  {z:.2f}")
"""3-misol"""
# s, h = map(int, input().split())
# a = 2 * s / h
# print(f"{a:.2f}")
"""4-misol"""
# from math import pi
#
# r = int(input())
# s = 4 * pi * r ** 2
# print(f"{s:.2f}")
"""5-misol"""
# a, b, c = map(int, input().split())
# p = (a + b + c) / 2
# print(f"{p:.2f}")
"""7-misol"""
# from math import pi
#
# h, r = map(int, input().split())
# v = (1 / 3) * pi * (r ** 2) * h
# print(f"{v: .2f}")
"""8-misol"""
# v, s = map(int, input().split())
# t = s / v
# print(f"{t:.2f}")
"""9-misol"""
# from math import *
#
# h = int(input())
# g = 9.8
# t = sqrt(2 * h / g)
# print(f"{t:.2f}")
"""10-misol"""
# x = int(input())
# l = x * 365 * 24 * 60 * 60 // 1000
# print(l)
"""11-misol"""
# n = int(input())
# i = 1
# s = 0
# while i <= n:
#     s += i
#     i += 1
# print(s)
"""12-misol"""
# m = int(input())
# g = 9.8
# l = m * g
# print(f"{l:.2f}")
"""13-misol"""
# m, a = map(int, input().split())
# l = m * a
# print(l)
"""14-misol"""
# u, r = map(int, input().split())
# l = u / r
# print(f"{l:.3f}")
"""15-misol"""
# r1, r2, r3 = map(int, input().split())
# p = 1 / r1 + 1 / r2 + 1 / r3
# q = 1 / p
# print(f"{q:.2f}")
"""16-misol"""
# from math import e
# x, y = map(float, input().split())
# c = (x + y) / (y ** 2 + abs((y ** 2 + 2) / (x + x ** 3 / 5))) + e ** (y + 2)
# print(f"{c:.2f}")
"""17-misol"""
# from math import *
#
# x, y = map(float, input().split())
# f = (2 * tan(x + pi / 6) / (1 / 3 + cos(y + x ** 2) ** 2) + log2(x ** 2 + 2))
# print(f"{f:.2f}")
"""18-misol"""
# from math import *
#
# x, y = map(float, input().split())
# f2 = (1 / (x + 2 / x ** 2 + 3 / x ** 3) + exp(x * x + 3 * x)) / (
#         atan(x + y) + abs(5 + x) ** 2) - cos(y * y + x * x / 2) ** 2
# print("%.2f" % f2)
"""19-misol"""
# from math import *
#
# x, y = map(int, input().split())
# z = log(abs((x + y) ** 2 + sqrt(abs(y) + 2) - (x - (x * y) / (x * x / 2 - 5)))) + cos(x + y) ** 2 / (
#         x + y) ** (1 / 3)
# print("%.2f" % z)
"""20-misol"""
# from math import *
#
# x, y = map(float, input().split())
# l = ((x ** 2 + 1) / (x ** 2 + (x * y + y ** 2) / (y ** 2 + (y + x * y) / (abs(x * y) + 5)))) + (
#             1 / (1 + cos(x) + (1 / sin(abs(x)))))
# print(f"{l:.2f}")
"""21-misol"""
# a, b = map(float, input().split())
# l = a ** (1 / 5) + (b * (a + b) / (2 * b + a * b)) ** (1 / 4) * (a * a + b * b + 2)
# print("%.2f" % l)
"""22-misol"""
# from math import *
#
# x1, x2, c, d = map(float, input().split())
# F = abs(sin(abs(c * x2 ** 3 +d * x1 ** 3 - c * d)) ** 2 / sqrt(c * x1 ** 2 + d * x2 ** 2 + 7)) + tan(
#     x1 * x2 ** 2 + d ** 3)
# print(("%.2f" % F))
"""23-misol"""
# from math import *
#
# arr = input()
# a, b, c, d, x = map(float, arr.split())
# try:
#     print(
#         f"{((a * x * x + b * x + c) / (x * a * a * a + a * a + a ** (b - c)) + cos(abs((a * x + b) / (c * x + d + 2 ** c)))):.2f}")
# except:
#     print("1.00")
"""24-misol"""
# from math import *
#
# a, b, c, x = map(float, input().split())
# W1 = 0.75 + (8.2 * x * x + sqrt(abs(x ** 3 + 3 * x) + cos(x - 2))) / (a / 4 + b / 3 + c / 2 + 1)
# print("%.2f" % W1)
"""25-misol"""
# from math import *
#
# a, x = map(float, input().split())
# TT = (sqrt(x - 1) + sqrt(x + 2) + log10(sqrt(a * (x * x)) + 2)) / sqrt(sqrt(x + 2) + (sqrt(x + 24 )+ (x ** 5)))
# print("%.2f" % TT)
"""26-misol"""
# from math import *
#
# a, x, y = map(float, input().split())
# W2 = sqrt(exp(x * y) - x * sin(a * x) - (x * x + 2) / (abs(x) + 5)) + sqrt(log(x * x + 2) + 5)
# print("%.2f" % W2)
"""27-misol"""
# from math import *
#
# x = float(input())
#
# AA = sqrt((2 * tan(x + 2) - cos(x + 2 ** x)) / (1 + cos(x + 2) ** 2)) + sin(x ** 2) / (x ** 2 + 3)
# print("%.2f" % AA)
"""28-misol"""
# import math as mt
#
# a, x = map(float, input().split())
# l = x * mt.sin(x / 2 + x / 3 + x / 4) + (mt.log10(x * x - 2) + 3 ** a) / (mt.cos(x + 3) * mt.sin(x + 3) + 8)
# print(f"{l:.2f}")
"""29-misol"""
# import math as mt
#
# a, x, y = map(float, input().split())
# l = mt.sqrt(y * y + mt.exp(x) + mt.sqrt(mt.exp(x) + a / (x * x + 2)) + mt.cos(x) ** 2 / mt.sin(x * x)) + mt.cos(x) ** 3
# print(f"{l:.2f}")
"""30-misol"""
# from math import *
# x , y ,z = input().split()
#
# x = int(x)
# y = float(y)
# z = float(z)
#
# AF = pow(2 , -x) * sqrt(x + pow(abs(y) + 2 , 1/4)) * pow(pow(e , x - 1) / sin(z + 2) + 2, 1/3)
#
# print(f"{AF:.2f}")
"""31-misol"""
# x, y = map(float, input().split())
# max = max(x, y)
# min = min(x, y)
# print("%.2f" % max, "%.2f" % min)
# 32 - masala
# x, y, z = map(float, input().split())
# max = max(x, y, z)
# min = min(x, y, z)
# print("%.2f" % max, "%.2f" % min)
# 33  - masala
# x, y, z = map(float, input().split())
# max = max(x + y + z, x, y, z)
# min = min((x + y) / 2, x, y, z) ** 2
# print("%.2f" % max, "%.2f" % min)
"""32-misol"""
# x, y, z = map(float, input().split())
# print(max(max(x, y), z), min(min(x, y), z))
"""33-misol"""
# x, y, z = map(int, input().split())
# max_, min_ = max(x + y + z, x, y, z), min(x + y / 2, x, y, z) ** 2
# print(f"{max_:.2f} {min_:.2f}")
"""34-misol"""
# a, b, c, = map(int, input().split())
# if a < b and b < c:
#     print("YES")
# else:
#     print("NO")
"""35-misol"""
# from math import *
# a,b,c = map(int, input().split())
# if c <= b and b <= a:
#     print(a*2,b*2,c*2)
# else:
#     print(abs(a), abs(b), abs(c))
"""36-misol"""
# a,b= map(int ,input().split())
#
# if a >b:
#     print(a)
# else:
#     print(a,b)
"""37-misol"""
# a,b= map (int,input().split())
# if a <=b:
#     a=0
#     print(a,b)
# else:
#     print(a,b)
"""38-misol"""
# a,b,c = map (float,input().split())
# if a>=1 and a <=3 :
#     print(a)
# if b>=1 and b<=3:
#     print(b)
# if c>=1 and c<=3:
#     print(c)
"""39-misol"""
# x, y = map(int, input().split())
# if x > y:
#     print("%.1f" % (4 * x * y), "%.1f" % ((x + y) / 2))
# else:
#     print("%.1f" % ((x + y) / 2), "%.1f" % (4 * x * y))
"""40-misol"""
# a,b,c = map(int, input().split())
#
# if a>0:
#     a=a*a
# if b>0:
#     b=b*b
# if c>0:
#     c=c*c
# print(a,b,c)
"""41-misol"""
# x, y, z = map(float, input().split())
# if x != y and x != z and y != z:
#     if x < 1 and y < 1 and z < 1:
#         kichkina = min(x, y, z)
#         if kichkina == x:
#             print((y + z) / 2, y, z)
#         elif kichkina == y:
#             print(x, (x + z) / 2, z)
#         else:
#             print(x, y, (x + y) / 2)
#     else:
#         print(x, y, z)
"""42-misol"""
# a,b,c,d = map(float, input().split())
#
# if a<=b and b<=c and c<=d:
#     max_ = max(a,max(b,max(c,d)))
#     print(f"{max_} {max_} {max_} {max_}")
# else:
#     min_ = min(a,min(b,min(c,d)))
#     print(f"{min_} {min_} {min_} {min_}")
"""43-misol"""
# x, y = map(float, input().split())
# if x < 0 and y < 0:
#     print(-x, -y)
# elif x < 0 or y < 0:
#     print(x + 0.5, y + 0.5)
# else:
#     print(x, y)
"""44-misol"""
# x, y, z = map(int, input().split())
# if x + y > z and x + z > y and y + z > x:
#     print("YES")
# else:
#     print("NO")
"""45-misol"""
# from math import *
# a, b, c = map(int, input().split())
# d = (b * b - 4 * a * c)
# if d >= 0:
#     x1 = (- b + sqrt(d)) / (2 * a)
#     x2 = (- b - sqrt(d)) / (2 * a)
#     print(f"{x1: .2f} {x2: .2f}")
# else:
#     print("NO")
"""46-misol"""
# a = float(input())
# if a <= -1:
#     print("%.2f" % (1 / (a * a)))
# elif a >= -1 and a <= 2:
#     print("%.2f" % (a * a))
# else:
#     print("%.2f" % 4)
"""47-misol"""
# a = float(input())
# if a <= 1:
#     print("%.2f" % (abs(a)))
# elif a >= 1 and a <= 2:
#     print("%.2f" % 1)
# else:
#     print("%.2f" % (- a * 2 + 5))
"""48-misol"""
# a = float(input())
# if a <= 0:
#     print("%.2f" % - a)
# else:
#     print("%.2f" % (- a * a))
"""49-misol"""
# a = float(input())
# if a <= 0:
#     print("%.2f" % (abs(a + 1)))
# else:
#     print("%.2f" % (abs(a - 1)))
"""50-misol"""
# x, y = map(float, input().split())
# if y >= - 1 and y <= 3 * x + 2 and y <= - 3 * x + 2:
#     print("yes")
# else:
#     print("no")
"""51-misol"""
# x, y = map(float, input().split())
# if x >= - 1 and x <= 1 and y >= - 2 and y <= abs(x):
#     print("yes")
# else:
#     print("no")
"""52-misol"""
# x, y = map(float, input().split())
# if (y <= 0 and y <= 2 * x + 3 and y >= (x - 1) / 3 ) or (y >= 0 and y <= 2 * x + 3 and y <= - x):
#     print("yes")
# else:
#     print("no")
"""53-misol"""
# x, y = map(float, input().split())
# if (y >= abs(x) and y <= 1) or (x >= - 2 and x <= 2 and y >= 1 and y <= 1.5):
#     print("yes")
# else:
#     print("no")
"""54-misol"""
# x, y = map(float, input().split())
# if y >= 0 and x * x + y * y <= 4 and x * x + y * y >= 1:
#     print("yes")
# else:
#     print("no")
"""55-misol"""
# x, y = map(float, input().split())
# if x * x + y * y <= 1:
#     print("yes")
# else:
#     print("no")
"""56-misol"""
# x, y = map(float, input().split())
# if x * x + y * y <= 1 and x * x + y * y >= 0.25:
#     print("yes")
# else:
#     print("no")
"""57-misol"""
# x, y = map(float, input().split())
# if x >= - 1 and x <= 1 and y >= - 1 and y <= 1:
#     print("yes")
# else:
#     print("no")
"""58-misol"""
# x, y = map(float, input().split())
# if x * x + y * y <= 1 and y <= x / 2:
#     print("yes")
# else:
#     print("no")
"""59-misol"""
# x, y = map(float, input().split())
# if (y <= 2 * x + 1 and y <= - 2 * x + 1 and y >= 0) or (y >= - 2 * x + 1 and y >= 2 * x - 1 and y <= 0):
#     print("yes")
# else:
#     print("no")
"""60-misol"""
# x, y = map(float, input().split())
# if (y <= 0.5 * x + 1 and y >= - 0.5 * x - 1 and x <= 0) or (x >= 0 and x * x + y * y <= 1):
#     print("yes")
# else:
#     print("no")
"""61-misol"""
# from math import *
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += sin(i) / pow(2, i)
# print(f"{s:.2f}")
"""62-misol"""
# from math import *
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += pow(-1, i - 1) * sin(pow(i, i)) / pow(2, i)
# print(f"{s:.2f}")
"""63-misol"""
# from math import *
#
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += (-1) ** (i - 1) * (1 / factorial(2 * i - 1))
# print(f"{s:.4f}")
"""64-misol"""
# n , x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s = s + (-1) ** (i - 1) * (1 / (x ** (2 * i)))
# print(f"{s:.3f}")
"""65-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s = s + i / x  ** (2 * i)
# print(f"{s:.3f}")
# """67-misol"""
# from math import *
# n , x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += (x ** i) / sqrt(i)
# print(f"{s:.3f}")
"""66-misol"""
# from math import *
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s = s + (-1) ** (i - 1) / i * sin(i * x)
# print(f"{s:.3f}"
"""68-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, i + 1):
#         p = p * j
#     s = s + x ** i / p
# print(f"{s:.3f}")
"""69-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, i + 1):
#         p = p * j
#     s = s + (- 1) ** i * x ** i / p
# print(f"{s:.3f}")
"""70-misol"""
# from math import *
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s += pow(-1, i - 1) * pow(x, 2 * i - 1) / factorial(2 * i - 1)
# print(f"{s:.3f}")
"""71-misol"""
# from math import *
#
# n, x = map(int, input().split())
# S = 0
# for i in range(1, n + 1):
#     S += pow(-1, i - 1) * pow(x, 2 * i - 2) / factorial(2 * i - 2)
#
# print(f"{S:.3f}")
"""72-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, 2 * i - 1):
#         p = p * j
#     s = s + x ** (2 * i - 2) / p
# print(f"{s:.3f}")
"73-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     s = s + x ** (2 * i - 1) / (2 * i - 1)
# print(f"{s:.3f}")
"""74-misol"""
# n, x = map(int, input().split())
# s = 0
# for i in range(1, n + 1):
#     p = 1
#     for j in range(1, 2 * i):
#         p = p *j
#     s = s + x ** (2 * i - 1) / p
# print(f"{s:.3f}")
"""75-misol"""
# from math import *
# n, k = map(int, input().split())
# s = 0
# for i in range(n + 1):
#     s += (((-1) ** i) * (k ** i))/ factorial(i)
# print(f"{s:.3f}")
"""76-misol"""
# from math import *
#
# a, b, c = map(int, input().split())
# s = 0
# for i in range(a, c + 1, 3):
#     s += ((a * i + b) / (b ** 2 + cos(i) ** 2)) ** (1 / 3) - sin(i ** 2) / (a * b)
# print(f"{s:.2f}")
"""77-misol"""
# from math import *
# a, b, c, d = map(int, input().split())
# s = 0
# for i in range(c, d + 1, 2):
#     s += ((sin(a * i) + b ** (2 * c)) / (b ** 2 + cos(i) ** 2)) ** (1 / 3) - ((sin(i ** 2) / (a * b)))
# print(f"{s:.2f}")
"""78-misol"""
# a, b, c = map(int, input().split())
# s = 0
# for i in range(a, b + 1, 2):
#     s = s + (a ** b + b ** i + c ** a) / (2 * i * i + 3 * a ** i)
# print(f"{s:.2f}")
"""79-misol"""
# from math import *
#
# a = int(input())
# S = 0
# x = -pi / 2
# h = pi / 19
# while x <= pi:
#     S += pow(a, a / 3) + pow(x, 2) * cos(a * x)
#     x += h
#
# print(f"{S:.2f}")
"""80-misol"""
# from math import *
# a = int(input())
# y = 0
# i = 0
# while i <= 10:
#     y += a * cos(i) - sin(i * i)
#     i += 0.5
# print(f"{y:.2f}")
"""81-misol"""
# import math
#
# a, b = map(int, input().split())
# sum_result = 0.0
#
# for x in range(1, 13, 2):  # 1 dan 12 gacha 2 qadamda
#     numerator = b + math.sin(x)
#     denominator = a ** 3 + math.cos(x) ** 2
#     second_term = math.pow(numerator / denominator, 1 / 5)
#     y = a ** 2 + second_term
#     sum_result += y
#
# print(f"{sum_result:.2f}")
"""82-misol"""
# a, b, c = map(int, input().split())
# s = 0
# for i in range(1, 11, 3):
#     s += a * i * i / b + i / c
# print(f"{s:.2f}")
"""83-misol"""
# a, b, c = map(int, input().split())
# y = 0
# i = 5
# while i <= 10:
#     y += (a * a + b * i + i ** c) / (a * a + b * b + i ** 2)
#     i += 0.5
# print(f"{y:.2f}")
"""84-misol"""
# from math import *
# a, b, c = map(int, input().split())
# s = 0
# i = -1
# while i <= 1:
#     s += ((sin(a * i) + b ** c) / (b ** 2 + cos(i) ** 2)) ** (1 / 3) - (sin(i ** 2) / (a * b))
#     i += 0.25
# print(f"{s:.2f}")
"""85-misol"""
# a, b, c = map(int, input().split())
# s = 0
# for i in range(1, 21, 5):
#     s += (a * i ** 2 + b * i + c) / (a ** 2 + b ** 2 + i ** 2)
# print(f"{s:.2f}")
"""86-misol"""
# from math import *
# a, b, c = map(int, input().split())
# s = 0
# i = c
# while i <= b:
#     s += a ** 2 * cos(i) + ((sin(i) / 2)) + b * i ** 2
#     i += 0.25
# print(f"{s:.2f}")
"""87-misol"""
# from math import *
# a = int(input())
# s = 0
# i = - pi / 2
# while i <= pi:
#     s += 2 *(a) ** (sin(2 * i) / 3) + i * i * cos(a * i)
#     i += pi / 10
# print(f"{s:.2f}")
"""88-misol"""
# from math import *
# a, b, c, d = map(int, input().split())
# s = 0
# i = d
# while i <= c:
#     s += ((a * i + b) / (b ** 2 + cos(i) ** 2)) ** (1 / 5) - (sin(i ** 2) / (a * b))
#     i += 1.5
# print(f"{s:.2f}")
"""89-misol"""
# from math import *
# a, b, c = map(int, input().split())
# s = 0
# i = 0
# while i <= 1:
#     s += (((sin(a * i) + b ** c) / (b * b + cos(i) ** 2)) ** (1 / 2)) - (sin(i ** 2) / (a * b))
#     i += 0.25
# print(f"{s:.2f}")
"""90-misol"""
# from math import *
# a, b, c = map(int, input().split())
# s = 0
# i = -pi
# while i <= pi:
#     s += (log(a ** (2 * sin(i))) + exp(2 * i)) / (atan(i) + b) + c
#     i+= pi / 10
# print(f"{s:.2f}")
"""91-misol"""
# from math import *
#
# a, b, c, d = map(int, input().split())
# s, p, sp, = 0, 1, 0
# for m in range(1, a + 1):
#     s += (3 * m ** 3 + 4 * m + 5) / (m ** 3 + log(m))
# for k in range(1, b + 1):
#     p *= (k) / (k ** 3 + 7 * k + 5)
# for i in range(1, c + 1):
#     q = 1
#     for m in range(1, d + 1):
#         q *= (log(i) + m ** i) / (m ** i)
#     sp += q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""92-misol"""
# from math import *
# x, y, a, b = map(int, input().split())
# g, s, p = a, 0, 1
# for a in range(1, x +1):
#     s += (a * a + 2 * a) / (a * a * a + a * cos(a) ** 2 + 1)
# for i in range(1, y + 1):
#     p *= (i * i + 1) / (i ** (3 / i) + 2)
# sp = float(0)
# for i in range(1, g + 1):
#     p1 = float(1)
#     for k in range(1, b + 1):
#         p1 *= log((k ** i + k ** (1 / i)) / (k ** 3 + i **(1 / k)))
#     sp += p1
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""93-misol"""
# from math import *
#
# x, y, a, b = map(int, input().split())
# s, p, sp = 0, 1, 0
# for k in range(1, x + 1):
#     s += (k ** 2 + sin(k) + 5) / (k ** 7 + 1) ** (1 / 5)
# for n in range(1, y + 1):
#     p *= (n + n ** (1 / 2)) / (n - (n + 1) ** (1 / 5))
# for k in range(1, a + 1):
#     q = 1
#     for i in range(1, b + 1):
#         q *= (i * i + k ** (2 / i)) / ((sin(i) + cos(k)) * i ** k)
#     sp += q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""94-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s, p, sp = 0, 1, 0
# for a in range(1, x + 1):
#     s += (2 * a + cos(a)) ** 2
# for a in range(1, y + 1):
#     p *= (a + 6) / sqrt(a ** 2 + 2)
# for k in range(1, c + 1):
#     for y in range(1, d + 1):
#         sp += (k ** 2 + y) / sqrt(k ** 2 + y ** 2)
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""95-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s, p, sp, = 0, 0, 0
# for i in range(1, x + 1):
#     s += (i ** 4 + i ** 2 + 3) / ((i + exp(i)) ** (1 / 2))
# for k in range(1, y + 1):
#     p += (k + 1) / (k * k * k + 5 * k)
# for m in range(1, c + 1):
#     q = 1
#     for n in range(1, d + 1):
#         q *= sqrt(abs(m ** n - n ** m) / (m ** n + n ** m))
#     sp += q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""96-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s, p, sp = 0, 1, 1
# for i in range(1, x + 1):
#     s += ((-1) ** i * (i + 1)) / (i ** 3 + i ** 2 + 1)
# for i in range(1, y + 1):
#     p *= (i ** 3 + abs(i - 9)) / (log(i) + 7 * i)
# for i in range(1, c + 1):
#     q = 0
#     for j in range(1, d + 1):
#         q += (-1) ** j * log(j + 5)/ (j ** (i + 3) + i * j)
#     sp *= q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""97-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s, p, sp = 0, 1, 0
# for i in range(1, x + 1):
#     s += 1 / (5 - 17 * i + i ** 3)
# for i in range(1, y + 1):
#     p *= (abs(i - 5) + 1) ** (1 / 2) / (i * i + 4 * i - 1)
# for i in range(1, c + 1):
#     x = 1
#     for j in range(1, d + 1):
#         x *= (-1) ** i * ((abs(sin(j) + e ** j)) ** (1 / 7)) / (2 * abs(4 * i ** 3 - j ** 4))
#     sp += x
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""98-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s, p, sp = 0, 1, 0
# for a in range(1, x + 1):
#     s += (4 * a + 6 * log(a)) / (a ** 2 + a)
# for a in range(1, y + 1):
#     p *= (abs(a - 6 * cos(a))) / (a ** 2 + a ** log(a))
# for i in range(1, c + 1):
#     q = 1
#     for j in range(1, d + 1):
#         q *= (j * i + x) / (i ** 2 + y ** 2)
#     sp += q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""99-misol"""
# from math import *
# x , y , c , d = map(int , input().split())
#
# S = 0
# P = 1
# for k in range(1 , x + 1):
#     S += (pow(k , 3) + pow(e , k))
#
# for a in range(3 , y + 1):
#     P *= a*x/sqrt(a**2 + x ** 2)
#
# SP = 0
# for i in range(1 , c + 1):
#     tmp = 1
#     for j in range(1, d + 1):
#         tmp *= (i*x + j**2)/sqrt(i**2 + j * y)
#     SP += tmp
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")
"""100-misol"""
# from math import *
#
# x, y, c, d = map(int, input().split())
# s = 0
# p = 1
# sp = 1
# for a in range(1, x + 1):
#     s += (a * x + 4) / sqrt(a + log(6))
# for a in range(1, y + 1):
#     p *= (a * x * x + 6) / sin(a * x)
# for i in range(1, c + 1):
#     q = 1
#     for j in range(1, d + 1):
#         q *= (i * j + y * x) / sqrt((j * x + y) ** i)
#     sp *= q
# print(f"{s:.2f} {p:.2f} {sp:.2f}")
"""101-misol"""
# l = int(input())
# n = list(map(int, input().split()))
# o1 = sum(n) / l
# s = []
# for i in n:
#     if i < o1:
#         s.append(i)
# re = sum(s) / len(s)
# print(f"{re:.2f}")
"""102-misol"""
# l = int(input())
# n = list(map(int , input().split()))
# start , end = map(int , input().split())
# minn = min(n)
#
# for i in range(start-1 , end):
#     n[i] = (n[i] / minn) + 0.01
#
# for i in n:
#     print(f"{i:.1f}" , end=" ")
"""103-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# k, l = map(int, input().split())
# s = 0
# for i in range(n):
#     if i >= k - 1 and i <= l - 1:
#         s = s + a[i]
# re = (s / (l - k + 1))
# print(f"{re:.1f}")
"""105-misol"""
# n = int(input())
# s = 0
# a1 = list(map(int, input().split()))
# a, b = map(int, input().split())
# for i in range(n):
#     if not (i >= a - 1 and i <= b - 1):
#         s += a1[i]
# m = (s / (n - (b - a + 1)))
# print(f"{m:.2f}")
"""106-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     s += a[i] ** 2
# print(s)
"""107-misool"""
# n = int(input())
# a = list(map(int, input().split()))
# s = max(a)
# for i in range(n):
#     print("%.2f"% (a[i] / s), end=" ")
"""108-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s = min(a)
# for i in range(n):
#     print("%.2f"% (a[i] / s), end=" ")
"""109-misol"""
# from math import *
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# s = 1
# for i in range(n):
#     if a[i] > m:
#         s *= (a[i])
# b = log(s)
# print(f"{b:.2f}")
"""110-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# k, m = map(int, input().split())
# s = 1
# for i in range(n):
#     if a[i] == m or a[i] == k:
#         s *= (a[i])
# print(s)
"""111-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# c = int(input())
# s = 0
# for i in range(n):
#     if m[i] > c:
#         s += (m[i])
# print((s))
"""112-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# s = 0
# p = 1
# for i in range(n):
#     if i % 2 == 0:
#         p *= m[i]
#     else:
#         s += m[i]
# e = p / s
# print(f"{e:.2f}")
"""113-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# s = 0
# c = 0
# for i in range(n):
#     if m[i] < 0:
#         c += 1
#         s += m[i]
# e = s / c
# print(f"{e:.2f}")
"""114-misol"""
# from math import *
# n = int(input())
# m = list(map(int, input().split()))
# s = 1
# for i in range(n):
#     if m[i] % 2 == 0 or m[i] % 5 == 0:
#         s *= m[i]
# print("%.2f"%(sin(s)))
"""115-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# c = int(input())
# s = 0
# for i in range(n):
#     if m[i] < c:
#         s += m[i] ** 2
# print(s)
"""116misol"""
# n = int(input())
# m = list(map(int, input().split()))
# max_ = max(m)
# for i in range(n):
#     print("%.2f" % (m[i] / max_ + 0.00001), end=" ")
"""117-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     if i % 2 == 0:
#         s += a[i]
# print(s)
"""118-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# b = 0
# for i in range(n):
#     if a[i] % 2 == 1:
#         b += 1
#         s += a[i]
# if b != 0:
#     print("%.2f"%(s / b + 0.001))
"""120-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# x, y = map(int, input().split())
# s = 0
# for i in range(n):
#     if not(a[i] >= x and a[i] <= y):
#         s += 1
# print(s)
"""121-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# s = 0
# for i in range(n):
#     if i >= m:
#         s += a[i]
# print(s)
"""122-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s1, s2 = 0, 0
# for i in range(n):
#     s1 += a[i] ** 2
#     s2 += a[i]
# print(s1)
# print("%.2f"%(s2 / n));
"""123-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s = 0
# for i in range(n):
#     if i % 2 == 1:
#         s += a[i]
# for i in range(n):
#     if a[i] % 2 == 1 and a[i] > 0:
#         print("%.2f"%(a[i] / s))
#     else:
#         print("%.2f"%a[i])
"""124-misol"""
# n = int(input())
# ma = list(map(int, input().split()))
# k = int(input())
# s = 0
# m = max(ma)
#
# for i in range(n):
#     if ma[i] == m:
#         print(ma[k - 1])
#     elif i == k - 1:
#         print(m)
#     else:
#         print(ma[i])
"""125-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# k, l = map(int, input().split())
# s = 0
# for i in range(n):
#     if i >= k - 1 and i <= l - 1:
#         s += a[i] ** 3
# print(s)
"""126-misol"""
# from math import log
# if __name__ == '__main__':
#     n = int(input())
#     l = list(map(int, input().split()))
#     orlog = log(sum(l)/n)
#     for i in range(n):
#         if l[i] < 0:
#             l[i] = orlog
#         print(f"{l[i]:.2f}", end=" ")
"""127-misol"""
# input()
# massiv = list(map(int , input().split()))
# min_num = pow(min(massiv) , 2)
#
# for i , v in enumerate(massiv):
#     if v < 0:
#         massiv.pop(i)
#         massiv.insert(i , min_num)
#
# print(*massiv)
"""128-misol"""
# n = int(input())
# a = list(map(int, input().split()))
# s, s1 = 0, 0
# for i in a:
#     if i % 2 == 0:
#         s += i
#         s1 += 1
# s2 = s / s1
# print(f"{s2:.2f}")
"""129-misol"""
# n = int(input())
# masive = list(map(int , input().split()))
# sum_ = 0
# for i in masive :
#     if i % 2 == 0 or i % 3 == 0 or i %5 == 0:
#         sum_+= i
# print(sum_)
"""130-misol"""
# n , m = map(int , input().split())
# matrix = []
# for _ in range(n):
#     matrix.append(list(map(int , input().split())))
# sum_ = []
# max_ , min_ = float('-inf') , float('inf')
# for row in matrix:
#     max_ = max(max_ , max(row))
#     min_ = min(min_ , min(row))
#     print(sum(row) , end=' ')
# print()
# print(max_ , min_)
"""131-misol"""
# n, m = map(int, input().split())
# mins = float('inf')
# maxs = float('-inf')
# matrix = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     maxs = max(max(l), maxs)
#     mins = min(min(l), mins)
#     matrix.append(l)
# summa = []
# for i in zip(*matrix):
#     summa.append(sum(i))
# print(*summa)
# print(maxs, mins)
"""132-misol"""
# l = int(input())
# a = list(map(int, input().split()))
# n, m = map(int, input().split())
# d = []
# w = 0
# for i in range(n * m - l):
#     a.append(0)
# for i in range(n):
#     for j in range(m):
#         print(a[w], end=" ")
#         w += 1
#     print("")
"""134-misol"""
# n = int(input())
# d = []
# x = []
# a = n
# for i in range(n):
#     d.append(list(map(int, input().split())))
# for i in range(n):
#     x.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(2 * n):
#         if a > j:
#             print(d[i][j], end=" ")
#         else:
#             print(x[i][j-a], end=" ")
#     print()
"""134-misol"""
# n,m = map(int, input().split())
# mat = []
# for i in range(n):
#     l = list(map(int, input().split()))
#     mat.append(l)
# a = list(map(int,input().split()))
#
# p=n
# for i in range(n-1,-1,-1):
#     if a[0]>mat[i][0]:
#         p=i
#
# mat.insert(p,a)
# for i in range(n+1):
#     print(*mat[i])
"""135-misol"""
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# k = int(input())
# for i in range(n):
#     for j in range(m):
#         if k - 1 != i:
#             print(d[i][j], end=" ")
#     print()
"""136-misol"""
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# k = int(input())
# for i in range(n):
#     for j in range(m):
#         if k - 1 != j:
#             print(d[i][j], end=" ")
#     print()
"""137-misol"""
# m = int(input())
# matrix = []
# k = []
# for i in range(m):
#     l = list(map(int, input().split()))
#     matrix.append(l)
# n = int(input())
# for i in matrix:
#     for j in i:
#         if j % n == 0:
#             k.append(j)
# print(f"{sum(k) / len(k):.2f}")
"""138-misol"""
# n = int(input())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# max_ = d[0][0]
# min_ = d[0][0]
# for i in range(n):
#     for j in range(n):
#         if i == j and max_ < d[i][j]:
#             max_ = d[i][j]
#         if i + j == n - 1 and d[i][j] < min_:
#             min_ = d[i][j]
# print(max_, min_)
"""139-misol"""
# m, n = map(int, input().split())
# matrix = []
# k = []
# for i in range(m):
#     l = list(map(int,input().split()))
#     matrix.append(l)
# indexi = 0
# indexj = 0
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] < 0:
#             indexi = i
#             indexj = j
# for i in range(m):
#     for j in range(n):
#         if i == indexi:
#             continue
#         if j == indexj:
#             continue
#         print(matrix[i][j], end=' ')
#     print()
"""140-misol"""
# n , m = map(int , input().split()) # 2 3
# matrix1 = []
#
# for i in range(n):
#     matrix1.append(list(map(int , input().split())))
#
# N , M = map(int , input().split()) # 3 6
# matrix2 = []
#
# for i in range(N):
#     matrix2.append(list(map(int , input().split())))
#
# zip_mat2 = list(zip(*matrix2))
# result = []
#
# for i in matrix1:
#     inner = []
#     for j in zip_mat2:
#         tmp = 0
#         for k in range(len(i)):
#             tmp += i[k] * j[k]
#         inner.append(tmp)
#
#     print(*inner)
"""141-misol"""
# n, m = map(int,input().split())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int,input().split())))
# x, y = map(int, input().split())
# s = []
# for i in matrix:
#     for j in i:
#         if x <= j <= y:
#             s.append(j)
# print(f"{sum(s) / len(s):.2f}")
"""142-misol"""
# n = int(input())
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int , input().split())))
#
# re = []
# for i in range(n):
#     re += matrix[i][i:]
# print(*re)
# print(max(re) , min(re))
"""143-misol"""
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(m):
#         for k in range(j, m):
#             if d[i][j] > d[i][k]:
#                 t = d[i][j]
#                 d[i][j] = d[i][k]
#                 d[i][k] = t
# for i in range(n):
#     for j in range(m):
#         print(d[i][j], end=" ")
#     print()
"""144-misol"""
# n, m = map(int, input().split())
# d = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# for i in range(n):
#     for j in range(m):
#         for k in range(i, n):
#             if d[i][j] < d[k][j]:
#                 t = d[i][j]
#                 d[i][j] = d[k][j]
#                 d[k][j] = t
# for i in range(n):
#     for j in range(m):
#         print(d[i][j], end=" ")
#     print()
"""145-misol"""
# n, m = map(int, input().split())
# d = []
#
# for i in range(n):
#     d.append(list(map(int, input().split())))
# for i in range(n):
#     s = 0
#     for j in range(m):
#         print(d[i][j], end=" ")
#         s += d[i][j]
#     print(s)
"""146-misol"""
# n, m = map(int, input().split())
# d = []
# v = []
# for i in range(n):
#     d.append(list(map(int, input().split())))
# for i in range(m):
#     s = 0
#     for j in range(n):
#         s += d[j][i]
#     v.append(s)
# for i in range(n):
#     for j in range(m):
#         print(d[i][j], end=" ")
#     print()
# for i in range(m):
#     print(v[i], end=" ")
"""147-misol"""
# a = input()
# cA = 0
# cY = 0
# for i in a:
#     if i == "A":
#         cA += 1
#     if i == "Y":
#         cY += 1
# print(cA)
# print(cY)
"""148-misol"""
# a = input()
# b = a.split()
# for i in range(len(b)):
#     if b[i][0] == "A":
#         print(b[i])
"""149-misol"""
# s = input().split()
# re = []
# for i in s:
#     if i.endswith('NA'):
#         re.append(i)
#
# print(len(re))
# print(*re)
"""150-misol"""
# x = input().split(" ")
# arr = ''
# for i in x:
#     if i.find("info") >= 0 or i.find("Info") >= 0:
#         arr += " " + i
# print(arr.strip(" "))
"""151-misol"""
# call = input()
# p = 0
# for i in call:
#     if i in 'AaOoUuEeIi':
#         p += 1
# print(p)
"""152-misol"""
# call = input()
# print(str(call[::-1]))
"""153-misol"""
# a = input()
# b = a.split()
# for i in b:
#     print(i, len(i))
"""154-misol"""
# n = input().strip()
# s = 0
# for i in n:
#     s += int(i)
# print(s)
"""155-misol"""
# a = input().split()
# count = 0
# for i in a:
#     if i[0].isupper():
#         count += 1
# print(count)
"""156-misol"""
# text = input().split()
#
# i , j = map(int , input().split())
#
# text[i-1] , text[j-1] =  text[j-1] , text[i-1]
# print(*text)
"""157-misol"""
# s = input().split()
# n = int(input())
# s[n-1] = "TATU"
# print(*s)
"""158-misol"""
# s = input().split()
# j = 0
# t = 0
# for i in s:
#     if len(i) % 2 == 0:
#         j += 1
#     else:
#         t += 1
# print(j * t)
"""159-misol"""
# s = input().split()
# count = 0
# for i in s:
#     if i[0] == 'a' and i[-1] == 'b':
#         count += 1
# print(count)
"""160-misol"""
# s = input()
# print(s.swapcase())
"""161-misol"""
# input()
# a = input().split()
# hi = {'A':2 , 'S':2 , 'L':1 , 'O':1 , 'M':1}
# for k , v in hi.items():
#     if a.count(k) < v:
#         print('NO')
#         break
# else:
#     print('YES')
"""162-misol"""
# n = int(input())
# s = input()
# s = s.replace("$", '')
# print(s)
"""163-misol"""
# n = input()
# b = n.split()
# a = 0
# max_ = len(b[0])
# for i in range(len(b)):
#     if len(b[i]) > max_:
#         max_ = len(b[i])
#         a = i
# print(b[a])
"""164-misol"""
# s = input()
# a, b = map(int, input().split())
# a, b = a - 1, b - 1
# if a > b:
#     if b == 0:
#         s = s[a:: -1]
#     else:
#         s = s[a:b - 1: -1]
# else:
#     s = s[a:b + 1]
# print(s)
"""165-misol"""
# from math import sin
#
# def fungsiya(a, b, c):
#     f2 = (2 * a - b - sin(c)) / (5 + abs(c))
#     return f2
# t, s = map(float, input().split())
# natija = fungsiya(t, -2 * s, 1.17) + fungsiya(2.2, t, s - t)
# print(f"{natija:.2f}")
"""166-misol"""
# def g(a, b):
#
#
#     return (a * a + b * b) / (a * a + 2 * a * b + 3 * b * b + 4)
#
# t, s = map(float, input().split())
#
# s = g(1.2, s) + g(t, s) + g(2 * s - 1, s * t)
#
# print(f'{s:.2f}')
"""168-misol"""
# a, b, c = map(float, input().split())
# def max_(x, y):
#     if x > y:
#         return x
#     else:
#         return y
# d = (max_(a, a + b) + max_(a, b + c)) / (1 + max_(a + b * c, 1.15))
# print(f"{d:.2f}")
"""169-misol"""
# a, b = map(float, input().split())
# def min_(n, m):
#     if n < m:
#         return n
#     else:
#         return m
# def max_(x, y):
#     if x > y:
#         return x
#     else:
#         return y
# u = min_(a, b)
# v = min_(a * b, max_(a, b))
# s = min_(u + v, 3.14)
# print(f"{u:.2f} {v:.2f} {s:.2f}")
"""170-misol"""
# s, t = map(float, input().split())
# def h(a, b):
#     return a / (b ** 2 + 1) + b / (a ** 2 + 1) - (a - b) ** 3
# def max_(x, y):
#     if x > y:
#         return x
#     else:
#         return y
# s = h(s, t) + max_(h(s - t, s*t), h(s - t, s + t)) + h(1, 1)
# print(f"{s:.2f}")
"""171-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# x, y = map(int, input().split())
# s, a, b, c = 0, 0, 0, 0
# for i in range(1, y - x + 1):
#     s += m[i - 1]
# for i in range(1, x + 1):
#     a += m[i - 1]
# for i in range(1, y + 1):
#     b += m[i - 1]
# for i in range(1, 5):
#     c += m[i - 1]
# summ = (s + a) / (b - c) ** 2
# print(f"{summ:.2f}")
"""172-misol"""
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n % 2 == 0:
#         m = n // 2
#         return fibonacci(m)
#     else:
#         m = n // 2
#         return fibonacci(m) + fibonacci(m + 1)
#
#
# n = int(input())
# result = fibonacci(n)
# print(result)
"""175-misol"""
# s = input()
# for i in range(len(s)):
#     if s[i] == '(':
#         a = i
#     if s[i] == ')':
#         b = i
#         z = s.replace(s[a + 1: b], s[b - 1:a: -1])
#         s = z
# for i in range(len(s)):
#     if not (s[i] == '(' or s[i] == ')'):
#         print(s[i], end="")
"""200-misol"""
# n = int(input())
# m = list(map(int, input().split()))
# s = 0
# for i in m:
#     s += i
# print(s)
"""1102-misol"""
# n = int(input())
# a = [-1, 2]
# b = 5
# if n == 1:
#     print(-1)
# else:
#     while n!= 1:
#         n = n - 1
#         a.append(a[-1] + b)
#         b = b + 2
#     print(a[-1])
"""1208-misol"""
# salom dunyo
# python Pi_pi
