# # class Animal:
# #     def speak(self):
# #         return "nmadr"
# #
# #
# # class Dog(Animal):
# #     def speak(self):
# #         return "Woof!"
# #
# #
# # class Cat(Animal):
# #     def speak(self):
# #         return "Meow!"
# #
# # animal = Animal()
# # dog = Dog()
# # cat = Cat()
# # data = [animal, dog, cat]
# # for i in data:
# #     print(i.speak())
#
# # import math
#
# # class Shape:
# #     def area(self):
# #         pass
# #
# #
# # class Circle(Shape):
# #     def __init__(self, radius: float) -> None:
# #         self.radius = radius
# #
# #     def area(self):
# #         return math.pi * self.radius ** 2
# #
# #
# # class Square(Shape):
# #     def __init__(self, side: float) -> None:
# #         self.side = side
# #
# #     def area(self):
# #         return self.side ** 2
# #
# #
# # class Triangle(Shape):
# #     def __init__(self, base: float, hight: float) -> None:
# #         self.base = base
# #         self.hight = hight
# #
# #     def area(self):
# #         return (self.base * self.hight)/2
# #
# # circle = Circle(10.0)
# # square = Square(10.0)
# # triangle = Triangle(5.0 , 10.0)
# # data = [circle, square, triangle]
# # for i in data:
# #     print(i.area())
#
# users = []
# todo = []
#
#
# class CRUD:
#     def create(self):
#         pass
#
#     def update(self):
#         pass
#
#     def get(self):
#         return self
#
#     def delete(self):
#         pass
#
#
# class User(CRUD):
#     def __init__(self, fullname, age):
#         self.fullname = fullname
#         self.age = age
#
#     def create(self):
#         users.append(self)
#         print("Seccessfully created")
#
#     def update(self, new_fullname):
#         index = users.index(self)
#         users[index].fullname = new_fullname
#
#     def delete(self):
#         users.remove(self)
#
#     def __str__(self):
#         return f"{self.fullname} {self.age}"
#
#     def __repr__(self):
#         return f"{self.fullname} {self.age}"
#
#
# obj = User("Botirjon", 19)
# obj1 = User("Shokh", 18)
# obj.create()
# obj1.create()
# obj1.delete()
#
# print(users)
#
#
# class ToDo(CRUD):
#
#     def __init__(self, title, description, time):
#         self.title = title
#         self.description = description
#         self.time = time
#
#     def create(self):
#         todo.append(self)
#         print("Seccessfully created")
#
#
#     def update(self, new_title):
#         index = todo.index(self)
#         todo[index].title = new_title
#
#     def delete(self):
#         pass


# class MathOperations:
#     def add(self, a, b):
#         return a + b
#
#     def add(self, a):
#         return a
#
# m = MathOperations
# print(m.add(3, 5))
