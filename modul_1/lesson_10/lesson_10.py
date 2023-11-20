l = ["is2", "this1", "a3", "laptop4"]
l.sort(key=lambda x: x[-1])
a = []
for i in l:
    a.append(i[:-1])
print(" ".join(a))

# print(" ".join([i[:-1]]for i in l))

# l = [1, 5, 6, 8, 3, 9]
# l.sort(key= lambda x: -x if x % 2 == 0 else x)
# print(l)

# a = [3,1,5]
# s = [2,7,4]
# d = 0
# a.sort()
# s.sort()
# for i in range(len(a)):
#     d += abs(a[i] - s[i])
# print(d)


# n = ["Mary", "John", "Emma"]
# s = [180, 165, 170]
#
# d = list(zip(n, s))
# sorted_d = sorted(d, key=lambda x: x[1], reverse=True)
# m = [n for n, _ in sorted_d]
#
# print(m)

# def qwer(arg1, arg2):
#     return arg1, arg2
# print(qwer(1, 2,))




# def factorial(n):
#     s = 1
#     for i in range(1, n+1):
#         s *= i
#     return s
#     print(s)
# n: int = int(input(">>>"))




# def fib(n):
#     if n <= 0:
#         return 0
#     if n <= 2:
#         return 1
#
#     return fib(n - 1) + fib(n - 2)
#
#
# n: int = int(input(">>>"))
#
# for i in range(0, n):
#     print(fib(i))

# name = ["Mary", "John", "Emma"]
# names = [180, 165, 170]
#
# print((list(zip(name, names))))
# #



