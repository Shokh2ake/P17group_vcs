#
# # nums = [3,2,3]
#
# def find_duplicate(nums):
#     seen = set()
#     duplicates = []
#
#     for num in nums:
#         if num in seen:
#             duplicates.append(num)
#         else:
#             seen.add(num)
#
#     if duplicates:
#         return duplicates[0]
#     else:
#         return None
# nums = [5, 6, 3, 2, 2]
# print(find_duplicate(nums))


# def nums(n):
#     re = []
#     for i in range(len(n)):
#         if n.count(n[i]) == 2 and n[i] not in re:
#             re.append(n[i])
#     return re
# n = [1, 2, 2, 4]
# print(nums(n))




# def count_length_sum(words, chars):
#     result = 0
#     for word in words:
#         count = 0
#         for char in set(word):
#             if char in chars:
#                 count += 1
#         result += count
#     return result
#
#
# # Test:
#
# # python
# words = ["hello", "world", "leetcode"]
# chars = "welldonehoneyr"
# print(count_length_sum(words, chars))




# n: int = int(input(">>> "))
# for i in range(2, n + 1):
#     c = 0
#     for j in range(2, i):
#         if i % j == 0:
#             c += 1
#
#     if c == 0:
#         print(i, end="-")

# a: int = int(input(">>>"))
# def tubmi(a):
#     j = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             j += 1
#     if j == 2:
#         return True
#     else:
#         return False


# def raqam(a):
#     return max(set(a), key= a.count)
# a = [2, 3, 5, 7, 5, 8, 9, 4, 7, 9, 2, 1, 9, 9, 9, 1, 1, 1, 1, 1, 1]
# print(raqam(a))


# n: int = int(input(">>>"))

# for i in range(2, n + 1):
#     c = 0
#     for j in range(2, i):
#         if i % j == 0:
#             c += 1
#     if c == 0:
#         print(i, end=" ")

# f = 0
# c = 0

# for i in range(2,  ):
#     f = 0
#     for j in range(2, i):
#         if i % j == 0:
#             f += 1
#     if f == 0:
#         print(i, end=" ")
#         c += 1
#     if (c == n):
#         break

# n: int = int(input(">>>"))
# m: int = int(input(">>>"))
#
# for i in range(n-1):
#     for j in range(m-1):
#         print(i+j, end=" ")
#
#     print()





