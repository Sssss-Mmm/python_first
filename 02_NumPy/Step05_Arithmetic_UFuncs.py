# -*- coding: utf-8 -*-

"""
Step05_Arithmetic_UFuncs.py
산술 연산과 유니버설 함수 (Arithmetic & Universal Functions)
"""
import numpy as np

print("=== 1. Basic Arithmetic ===")
a = np.array([10, 20, 30, 40])
b = np.arange(4) # [0, 1, 2, 3]

print(f"a: {a}")
print(f"b: {b}")

print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}") # 요소별 곱셈 (Element-wise)
print(f"a / 10: {a / 10}") # 스칼라 나눗셈


print("\n=== 2. Universal Functions (UFuncs) ===")
# 배열의 모든 요소에 대해 함수 적용
arr = np.array([1, 4, 9, 16])
print(f"Original: {arr}")

# 제곱근
print(f"sqrt: {np.sqrt(arr)}")

# 지수함수 (e^x)
print(f"exp: {np.exp(arr)}")

# 로그함수 (log)
print(f"log: {np.log(arr)}")

# 합계, 누적 합계
data = np.arange(1, 6)
print(f"Data: {data}")
print(f"Sum: {np.sum(data)}")
print(f"Cumsum: {np.cumsum(data)}") # [1, 3, 6, 10, 15]
