# -*- coding: utf-8 -*-

"""
Step12_Comprehensions.py
Comprehension (리스트, 딕셔너리, 셋 내포)
"""

print("=== 1. List Comprehension ===")
# [표현식 for 항목 in 이터러블 if 조건]
nums = [1, 2, 3, 4, 5]

# 기존 방식
squared = []
for n in nums:
    squared.append(n ** 2)
print(f"Squared (Loop): {squared}")

# Comprehension 방식
squared_comp = [n ** 2 for n in nums]
print(f"Squared (Comp): {squared_comp}")

# 조건문 포함 (짝수만 제곱)
even_squares = [n ** 2 for n in nums if n % 2 == 0]
print(f"Even Squares: {even_squares}")


print("\n=== 2. Dictionary Comprehension ===")
# {키: 값 for ...}
names = ["Alice", "Bob", "Charlie"]
name_len = {name: len(name) for name in names}
print(f"Name Lengths: {name_len}")

# 키와 값 바꾸기
reversed_dict = {v: k for k, v in name_len.items()}
print(f"Reversed Dict: {reversed_dict}")


print("\n=== 3. Set Comprehension ===")
# {표현식 for ...} -> 중복 제거
raw_data = [1, 2, 2, 3, 3, 3, 4, 5]
unique_squares = {x ** 2 for x in raw_data}
print(f"Unique Squares Set: {unique_squares}")
