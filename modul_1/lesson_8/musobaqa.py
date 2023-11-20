# def buildArry(self, nums: list[int]) -> list[int]:
#     n = []
#     for i in nums:
#         n.append(nums[i])
#     return n



# nums = [1,2,3,4,5]
# s = []
#
# c = 0
# for num in nums:
#     c += num
#     s.append(c)
#
# print(s)

# import random
#
# s = [1, 2, 3]
#
# print(random.choice(s))

# def restoreString(s, indices):
#     new_string = [''] * len(s)
#     for i in range(len(s)):
#         new_string[indices[i]] = s[i]
#     return ''.join(new_string)
#
# s = "codeleet"
# indices = [4, 5, 6, 7, 0, 2, 1, 3]
# output = restoreString(s, indices)
# print(output)

#
# def countMatches(items, ruleKey, ruleValue):
#     count = 0
#     for item in items:
#         if item[["type", "color", "name"].index(ruleKey)] == ruleValue:
#             count += 1
#     return count
#
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# output = countMatches(items, ruleKey, ruleValue)
# print(output)


# def generateCombinations(s):
#     output = []
#     letters, numbers = s.split(":")
#     for letter in letters:
#         for number in numbers:
#             output.append(letter + number)
#     return output
#
# s = "K1:L2"
# output = generateCombinations(s)
# print(output)



# def generateOutput(key, message):
#     output = ""
#     for char in message:
#         if char == " ":
#             output += " "
#         else:
#             index = key.index(char)
#             output += key[index]
#     return output
#
# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"
# output = generateOutput(key, message)
# print(output)


# d = {
#     "t" : "a",
#
# }
# print(d)







