# classes.py

class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"The{self.name} is barking a lot."

    def size(self):
        return f"The {self.name} is small."

class Car:
    def __init__(self, brand):
        self.brand = brand

    def buy(self):
        return f"The {self.brand} has been bought."

    def her(self):
        return f"The {self.brand} is her's."

class Student:
    def __init__(self, name):
        self.name = name

    def code(self):
        return f"{self.name} is coding."

    def home(self):
        return f"{self.name} is going home."
