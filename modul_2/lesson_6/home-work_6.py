# from abc import ABC, abstractmethod
"""HOMEWORK-0"""
# class BatteryPowered(ABC):
#     def __init__(self, battery_type):
#         self.battery_type = battery_type
#
#     @abstractmethod
#     def power_source(self):
#         pass
#
#
# class PlugPowered(BatteryPowered):
#     def __init__(self, battery_type, voltage):
#         super().__init__(battery_type)
#         self.voltage = voltage
#
#     def power_source(self):
#         pass
#
#
# class HybridDevice(BatteryPowered, PlugPowered):
#     def __init__(self, name, battery_type, voltage):
#         self.name = name
#         super().__init__(battery_type, voltage)
#
#     def power_source(self):
#         pass
#
#
# obj = HybridDevice("nmadr", "yana nmadr", "220")
# print(obj.voltage)
"""HOMEWORK-1"""
# class Person(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         pass
#
# class Customer(Person):
#     def __init__(self, name, age, customer_id):
#         self.customer_id = customer_id
#         super().__init__(name, age)
#
#     def purchase(self):
#         pass
#
# class Manager(Person):
#     def __init__(self, name, age, department, salary):
#         self.department = department
#         self.salary = salary
#         super().__init__(name, age)
#
#     def manage(self):
#         pass
#
#     def display_salary(self):
#         pass
#
# class Developer(Person):
#     def __init__(self, name, age, programming_language):
#         self.programming_language =programming_language
#         super().__init__(name, age)
#
#     def code(self):
#         pass
"""HOMEWORK-2"""
# class ZooAnimal(ABC):
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#
# class FlyingAnimal(ZooAnimal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#
#     @abstractmethod
#     def fly(self):
#         pass
#
#
# class SwimmingAnimal(ZooAnimal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#
#     @abstractmethod
#     def swim(self):
#         pass
#
#
# class Bird(FlyingAnimal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#     @abstractmethod
#     def fly(self):
#         pass
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Fish(SwimmingAnimal, Bird):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#
#     def swim(self):
#         pass
#
#     def make_sound(self):
#         pass
#
#
# class Duck(SwimmingAnimal, Bird):
#     def __init__(self, name, species):
#         super().__init__(name, species)
#
#     def swim(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def make_sound(self):
#         pass
"""HOMEWORK-3"""
# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name
#     @abstractmethod
#     def display_info(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self, name, width, height):
#         self.width = width
#         self.height = height
#         super().__init__(name)
#     @abstractmethod
#     def display_info(self):
#         pass
#     @abstractmethod
#     def area(self):
#         pass
#
# class Square(Rectangle):
#     def __init__(self, name, width, height):
#         super().__init__(name, width, height)
#
#     def display_info(self):
#         pass
#
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, name, radius):
#         self.radius = radius
#         super().__init__(name)
#
#     def display_info(self):
#         pass
#
#     def area(self):
#         pass
"""HOMEWORK-4"""
# class Vehicle(ABC):
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     @abstractmethod
#     def display_info(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self, brand, model, fuel_type):
#         super().__init__(brand, model)
#         self.fuel_type = fuel_type
#
#     def display_car_info(self):
#         pass
#
#
#     def display_info(self):
#         pass
#
# class ElectricCar(Vehicle):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity
#
#     def battery_capacity(self):
#         pass
#
#     def display_info(self):
#         pass
"""HOMEWORK-5"""
# class LibraryItem(ABC):
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     @abstractmethod
#     def display_info(self):
#         pass
#
# class Book(LibraryItem):
#     def __init__(self, title, author, genre):
#         super().__init__(title, author)
#         self.genre = genre
#     @abstractmethod
#     def display_info(self):
#         pass
#     @abstractmethod
#     def display_genre(self):
#         pass
#
# class AudioBook(Book):
#     def __init__(self, title, author, genre, narrator):
#         super().__init__(title, author, genre)
#         self.narrator = narrator
#
#     def display_info(self):
#         pass
#
#     def display_genre(self):
#         pass
#
#     def display_narrator(self):
#         pass
