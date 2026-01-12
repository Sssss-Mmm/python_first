# -*- coding: utf-8 -*-

"""
Step03_Operators.py
연산자 (Operators): 산술, 비교, 논리, 멤버십, 식별 연산자
"""

print("=== 1. Arithmetic Operators (산술 연산자) ===")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")       # 결과는 항상 float
print(f"Floor Division (a // b): {a // b}") # 몫 (정수 나누기)
print(f"Modulus (a % b): {a % b}")        # 나머지
print(f"Exponentitation (a ** b): {a ** b}") # 거듭제곱

print("\n=== 2. Comparison Operators (비교 연산자) ===")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= 10: {a >= 10}")
print(f"b <= 1: {b <= 1}")
print(f"a == 10: {a == 10}")
print(f"a != b: {a != b}")

print("\n=== 3. Logical Operators (논리 연산자) ===")
t = True
f = False
print(f"True and False: {t and f}")
print(f"True or False: {t or f}")
print(f"not True: {not t}")

print("\n=== 4. Membership Operators (멤버십 연산자) ===")
# in / not in
lst = [1, 2, 3, 4, 5]
print(f"List: {lst}")
print(f"3 in lst: {3 in lst}")
print(f"10 not in lst: {10 not in lst}")
print(f"'P' in 'Python': {'P' in 'Python'}")

print("\n=== 5. Identity Operators (식별 연산자) ===")
# is / is not (객체의 주소 비교)
x = 10
y = 10
z = x
print(f"x is y: {x is y}") # 작은 정수는 메모리 캐싱되어 True (구현에 따라 다름, 보통 True)
print(f"x is z: {x is z}")

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(f"lst1 == lst2: {lst1 == lst2}") # 값은 같음 -> True
print(f"lst1 is lst2: {lst1 is lst2}") # 객체는 다름 -> False
