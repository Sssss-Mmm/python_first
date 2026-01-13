# -*- coding: utf-8 -*-

"""
Step01_Creation_Attributes.py
Numpy 배열 생성과 속성 확인 (Array Creation & Attributes)
"""
import numpy as np

print("=== 1. Creating Arrays ===")
# 리스트로부터 생성
arr_list = np.array([1, 2, 3, 4, 5])
print(f"From List: {arr_list}")

# 2차원 배열 생성
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr_2d}")


print("\n=== 2. Initialization Functions ===")
# 0으로 초기화
zeros = np.zeros((2, 3))
print(f"Zeros (2x3):\n{zeros}")

# 1로 초기화
ones = np.ones((2, 3))
print(f"Ones (2x3):\n{ones}")

# 특정 값으로 초기화
full = np.full((2, 3), 7)
print(f"Full (2x3, val=7):\n{full}")

# 연속된 값 생성 (arange)
seq = np.arange(0, 10, 2) # 0부터 10전까지 2간격
print(f"Arange (0, 10, 2): {seq}")

# 구간 등분 (linspace)
lin = np.linspace(0, 1, 5) # 0부터 1까지 5등분
print(f"Linspace (0, 1, 5): {lin}")


print("\n=== 3. Array Attributes ===")
print(f"Shape: {arr_2d.shape}")       # 차원의 크기 (2, 3)
print(f"NDim: {arr_2d.ndim}")         # 차원 수 (2)
print(f"Size: {arr_2d.size}")         # 전체 원소 개수 (6)
print(f"Dtype: {arr_2d.dtype}")       # 데이터 타입 (int64 등)
print(f"Itemsize: {arr_2d.itemsize}") # 각 원소의 바이트 크기
