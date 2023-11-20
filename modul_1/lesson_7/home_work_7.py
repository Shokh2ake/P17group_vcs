
# 1
#
# n: int = int(input(">>>"))
# yigindi = 0
#
# while n > 0:
#     yigindi += n % 10
#
#     n //= 10
# print(yigindi)

# 2

# user_names = {
#                 1: "Alisher" ,
#                 2: "Kamol" ,
#                 3: "Botirjon",
#                 4: "Hamidillo",
#                 5: "John"
#             }
# s = list(user_names)
# user = sorted(user_names.items(), key=lambda x:x[1])
# print(user)

# 3

# s = "2is 4sentence 1This 3a"
# str = s.split()
# s = sorted(str)
# str3 = []
#
# for i in s:
#     str3.append(i[1:])
# print(str3)
# print(" ".join(str3))


# 4

# def uzb_companya(tel_nomber):
#     menyu_dict = {
#         "99899" : "UzMobile",
#         "99895" : "UzMobile",
#         "99877" : "UzMobile",
#         "99890" : "Beeline",
#         "99891" : "Beeline",
#         "99893" : "Ucell",
#         "99894" : "Ucell",
#         "99850" : "Ucell",
#         "99897" : "MobiUz",
#         "99888" : "MobiUz",
#         "99898" : "Perfectum"
#
#     }
#
#     if tel_nomber in menyu_dict:
#         return menyu_dict[tel_nomber]
#     else:
#         return "Bunday kompanya yoq!"
#
# nomer = input("Nomer kodini kiriting: ")
# re = uzb_companya(nomer)
# print(re)

# 5

# input1 = input("Yilni kiriting: ")
# str = input1.replace('-', ' ').split()
# if len(str[1]) == 1:
#     str[1] = '0' + str[1]
# if len(str[2]) == 1:
#     str[2] = '0' + str[2]
# print("-".join(str))




# data1 = {}
# for i in range(1, 3):
#     name = input(f"{i}: Name= ")
#     date = {
#         i: name
#     }
#     data1.update(date)
# print(data1)




