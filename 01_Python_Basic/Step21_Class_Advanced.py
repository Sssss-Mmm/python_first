# -*- coding: utf-8 -*-

"""
Step21_Class_Advanced.py
클래스 심화 (Inheritance, Overriding, Magic Methods)
"""

print("=== 1. Inheritance (상속) ===")
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass # 추상 메서드처럼 사용

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Kitty")
print(f"{dog.name} says {dog.speak()}")
print(f"{cat.name} says {cat.speak()}")


print("\n=== 2. Method Overriding & super() ===")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age) # 부모 클래스 생성자 호출
        self.student_id = student_id
    
    def introduce(self): # 메서드 오버라이딩 (재정의)
        super().introduce()
        print(f"I am a student with ID: {self.student_id}")

s = Student("Alice", 20, "S12345")
s.introduce()


print("\n=== 3. Magic Methods (Special Methods) ===")
# __str__, __repr__, __add__, __len__ 등
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        # + 연산자 오버로딩
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        # == 연산자 오버로딩
        return self.x == other.x and self.y == other.y

v1 = Vector(2, 4)
v2 = Vector(3, -1)
v3 = v1 + v2

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2 = {v3}")
print(f"v1 == Vector(2, 4): {v1 == Vector(2, 4)}")
