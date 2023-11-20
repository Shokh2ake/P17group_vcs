# class Animal:
#     def __init__(self, name, gender, habitat):
#         self.name = name
#         self.gender = gender
#         self.habitat = habitat
#
#
# class Bird:
#     def __init__(self, name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
#
# class Fish:
#     def __init__(self, name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
#
# class Mammal:
#     def __init__(self, name, gender, habitat):
#         super().__init__(name, gender, habitat)
#
# bird1 = Bird("Shoh", "Zor", "")
# fish1 = Fish()
# mammal = Mammal()


# def counter(words):
#     word_count = {}
#     for char in words:
#         if char not in word_count:
#             word_count[char] = 1
#         else:
#             word_count[char] += 1
#     return word_count
#
# words = "Hello world"
# print(counter(words))



# words = "Hello world"
# c = {}
# for i in words:
#     c[i] = c.setdefault(i, 0) + 1
# print(c)


# def son(nums):
#     n = len(nums)
#     total_sum = (n * (n + 1)) // 2
#     for num in nums:
#         total_sum -= num
#     return total_sum
#
# nums = [3, 0, 2]
# print(son(nums))





