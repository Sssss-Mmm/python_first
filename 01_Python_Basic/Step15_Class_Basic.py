# -*- coding: utf-8 -*-

"""
Step15_Class_Basic.py
클래스와 객체 지향 프로그래밍 기초 (Class & OOP)
"""

# 클래스 정의
class Dog:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Canis familaris"

    # 생성자 (__init__)
    def __init__(self, name, age):
        # 인스턴스 변수 (각 객체마다 별도)
        self.name = name
        self.age = age

    # 인스턴스 메소드
    def description(self):
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"

# 객체 생성 (Instance)
dog1 = Dog("Buddy", 9)
dog2 = Dog("Miles", 4)

print("=== 1. Access Attributes ===")
print(f"{dog1.name} (Age: {dog1.age})")
print(f"{dog2.name} (Age: {dog2.age})")

print("\n=== 2. Call Methods ===")
print(dog1.description())
print(dog2.speak("Woof Woof"))

print("\n=== 3. Class Variable vs Instance Variable ===")
print(f"dog1 species: {dog1.species}")
print(f"dog2 species: {dog2.species}")

# 클래스 변수는 클래스 이름으로도 접근 가능
print(f"Dog.species: {Dog.species}")

print("\n=== 4. Inheritance (상속) ===")
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        # 부모 클래스의 메소드 오버라이딩 (Overriding)
        return super().speak(sound)

dog3 = GoldenRetriever("Jack", 3)
print(dog3.description())       # 부모 메소드 사용
print(dog3.speak())             # 자식 메소드 (오버라이딩) 사용
