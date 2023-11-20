# raqamlar = [0,1,2,3,4]
# indeks = [0,1,2,2,1]
# l = []
# for i in range(len(raqamlar)):
#     l.insert(indeks[i], raqamlar[i])
# print(l)

# nums = [1,2,3,4] # Chiqish: [2,4,4,4]
# l = []
#
# for i in range(0, len(nums), 2):
#     # print(nums[i], nums[i+1])
#     l.extend([nums[i+1], nums[i]])
# print(l)

# encoded = [1,2,3]
# first = 1
# l = [first]
# for i in encoded:
#     num = l[-1] ^ i
#     l.append(num)
# print(l)

# n, m = input(">>>").split()
# n ,m = int(n), int(m)
# matrix = []
# for i in range(n):
#     matrix.append(["*"]*m)
# print(matrix)


# row: int = int(input("row: "))
# col: int = int(input("col: "))
#
# for i in range(row):
#     for j in range(col):
#         if j == 0 or j == col -1 and i // 2 == row-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# matrix = []
#
# n, m = map(int, input(">>>").split())
# c = 1
# for i in range(n):
#     tmp = []
#     for j in range(m):
#         tmp.append(c)
#         c += 1
#     matrix.append(tmp)
#
# for i in matrix:
#     print(i)


# n, m = map(int, input(">>>").split())
#
# l = list(range(1, n*m+1))
# matrix = []
# for i in range(n):
#     matrix.append(l[i*m:i*m+m])
#
# re = []
# for i in list(zip(*matrix)):
#     re.append(i[::-1])
# print(re)


# for i in range(n):
#     matrix.append(["*"]*m)
# print(*matrix[0])
# for i in matrix[1:]:
#     print("  "*(m//2) + "*")






