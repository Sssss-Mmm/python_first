# -*- coding: utf-8 -*-

"""
Step03_Indexing_Slicing.py
인덱싱과 슬라이싱 (Indexing & Slicing)
"""
import numpy as np

print("=== 1. Basic Indexing & Slicing ===")
arr = np.arange(10) # [0, 1, ..., 9]
print(f"Array: {arr}")
print(f"arr[3]: {arr[3]}")
print(f"arr[2:5]: {arr[2:5]}") # 2부터 5전까지
print(f"arr[::2]: {arr[::2]}")  # 처음부터 끝까지 2간격


print("\n=== 2. 2D Array Slicing ===")
mat = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"Matrix:\n{mat}")

# 행 선택
print(f"Row 0 (mat[0]): {mat[0]}")
print(f"Row 1 (mat[1, :]): {mat[1, :]}")

# 열 선택
print(f"Col 2 (mat[:, 2]): {mat[:, 2]}")

# 부분 행렬
print(f"Sub-matrix (mat[:2, :2]):\n{mat[:2, :2]}")


print("\n=== 3. Boolean Indexing (Masking) ===")
# 조건에 맞는 요소만 선택
data = np.array([10, 20, 30, 40, 50])
mask = data > 30
print(f"Data: {data}")
print(f"Mask (data > 30): {mask}")
print(f"Filtered (data[mask]): {data[mask]}")

# 조건부 값 변경
data[data > 30] = 0
print(f"Modified Data (val>30 -> 0): {data}")


print("\n=== 4. Fancy Indexing ===")
# 인덱스 배열을 사용하여 여러 요소를 한 번에 선택
arr = np.array([10, 20, 30, 40, 50, 60])
indices = [0, 2, 4]
print(f"Arr: {arr}")
print(f"Fancy Indexing [0, 2, 4]: {arr[indices]}")

# 2차원 Fancy Indexing
mat = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
# (0,0), (1,1), (2,0) 선택
rows = [0, 1, 2]
cols = [0, 1, 0]
print(f"Fancy Indexing 2D (rows, cols): {mat[rows, cols]}")
