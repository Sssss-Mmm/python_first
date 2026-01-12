# -*- coding: utf-8 -*-

"""
Step05_Conditionals.py
조건문 (Conditionals): if, elif, else
"""

print("=== 1. Basic if-else ===")
age = 20
if age >= 18:
    print(f"Age {age}: Adult")
else:
    print(f"Age {age}: Minor")

print("\n=== 2. if-elif-else ===")
score = 85
grade = ""

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

print("\n=== 3. Nested if (중첩 if) ===")
num = 15
if num > 10:
    print("Number is greater than 10")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

print("\n=== 4. Ternary Operator (삼항 연산자) ===")
# 변수 = 참일때값 if 조건 else 거짓일때값
is_raining = False
status = "Take Umbrella" if is_raining else "Go Outside"
print(f"Raining: {is_raining}, Status: {status}")

print("\n=== 5. Truthy & Falsy ===")
# 값이 비어있거나 0이면 False로 취급
values = [0, "", [], None, 1, "Hello"]
for v in values:
    if v:
        print(f"'{v}' is True")
    else:
        print(f"'{v}' is False")
