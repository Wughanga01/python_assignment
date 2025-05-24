# call.py

from function import greet, add, subtract, multiply
from classes import Animal, Car, Student

# Testing functions
print(greet("Wughanga"))
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))

print("\n")

# Testing classes
dog = Animal("Dog")
print(dog.bark())
print(dog.size())

jeep = Car("Jeep")
print(jeep.buy())
print(jeep.her())

student = Student("Wughanga")
print(student.code())
print(student.home())
