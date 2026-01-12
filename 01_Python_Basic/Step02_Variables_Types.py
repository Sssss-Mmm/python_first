# -*- coding: utf-8 -*-

"""
Step02_Variables_Types.py
변수와 자료형 (Variables and Data Types)
"""

print("=== 1. Variables and Assignment ===")
x = 10
y = 3.14
name = "Python"
is_active = True

print("x:", x)
print("y:", y)
print("name:", name)
print("is_active:", is_active)

print("\n=== 2. Dynamic Typing (동적 타이핑) ===")
# Python은 변수의 자료형을 자유롭게 바꿀 수 있습니다.
current_val = 100
print(f"Current val: {current_val}, type: {type(current_val)}")

current_val = "Now I am a String"
print(f"Current val: {current_val}, type: {type(current_val)}")


print("\n=== 3. Multiple Assignment (다중 할당) ===")
# 여러 변수에 한 번에 값을 대입할 수 있습니다.
a, b, c = 1, 2, "Three"
print(f"a: {a}, b: {b}, c: {c}")

x = y = z = 0
print(f"x: {x}, y: {y}, z: {z}")


print("\n=== 4. None Type ===")
# 값이 없음을 나타내는 특별한 상수입니다.
unknown = None
print(f"unknown: {unknown}, type: {type(unknown)}")


print("\n=== 5. Data Types (type() function) ===")
# type() 함수를 사용하여 변수의 자료형을 확인할 수 있습니다.
print("Type of x:", type(x))         # <class 'int'>
print("Type of a:", type(a))         # <class 'int'>
print("Type of name:", type(name))   # <class 'str'>
print("Type of is_active:", type(is_active)) # <class 'bool'>

print("\n=== 6. Type Conversion ===")
# 자료형 변환 (Casting)
num_str = "100"
num_int = int(num_str)  # 문자열 -> 정수
print(f"String '{num_str}' to Int: {num_int}, type: {type(num_int)}")

float_val = 3.99
int_val = int(float_val) # 실수 -> 정수 (소수점 버림)
print(f"Float {float_val} to Int: {int_val}")

val = 123
str_val = str(val)      # 정수 -> 문자열
print(f"Int {val} to String: '{str_val}', type: {type(str_val)}")

bool_val = bool(1)      # 1 -> True
print(f"Bool(1): {bool_val}")
print(f"Bool(0): {bool(0)}") # 0 -> False
print(f"Bool(''): {bool('')}") # 빈 문자열 -> False
print(f"Bool('Hello'): {bool('Hello')}") # 값이 있으면 -> True
