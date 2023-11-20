# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# c = 0
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if row + col == len(matrix) - 1 or row == col:
#             c += matrix[row][col]
# print(c)

# c = sum(matrix[0]) + sum(matrix[-1])
# for row in matrix[1:-1]:
#     c += row[0] + row[-1]
# print(c)
# print(sum(matrix[0]) + sum(matrix[-1]) + sum([row[0]] + row[-1] for row in matrix[1:-1]))


# for i in range(len(matrix[0])):
#     for j in matrix:
#         print(j[i], end = " ")
#     print()

# n, m = map(int, input().split())
# matrix = []
# c = 1
# for i in range(n):
#     inner = []
#     for j in range(m):
#         inner.append(c)
#         c += 1
#     matrix.append(inner)
# print(matrix)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# c = 0
# for row in range(len(matrix)):
#     for col in range(len(matrix[0])):
#         if row + col == len(matrix) - 1 or row == col:
#             # c += matrix[row][col]
#             print(matrix[row][col])
#     print()
# # print(c)

# input = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# output = []
#
# for row in input:
#     new_row = row[:1] + row[2:]
#     output.append(new_row)
#
# print(output)





# row = 5
# col = 5
#
# for i in range(row):
#     for j in range(col):
#
#         if i != 0 and i != row - 1 and j != 0 and j != col - 1:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()

row: int = int(input("row: "))
col: int = int(input("col: "))

for i in range(row):
    for j in range(col):
        if j == 0 or j == col - 1 or row // 2 == i :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# row: int = int(input("row: "))
# col: int = int(input("col: "))
#
# for i in range(row):
#     for j in range(col):
#         if i == j or i + j == col-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# row: int = int(input("row: "))
# col: int = int(input("col: "))
#
# for i in range(row):
#     for j in range(col):
#         if i % 2 == 0 or j % 2 == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




