# -*- coding: utf-8 -*-

"""
Step04_Shape_Manipulation.py
배열의 형태 변경 (Shape Manipulation)
"""
import numpy as np

print("=== 1. Reshape ===")
# 0~11까지의 1D 배열
arr = np.arange(12)
print(f"Original (12,): {arr}")

# 3x4로 변경
arr_3x4 = arr.reshape(3, 4)
print(f"Reshape (3x4):\n{arr_3x4}")

# -1 사용 (자동 계산)
arr_auto = arr.reshape(4, -1) # 행은 4, 열은 자동 계산(3)
print(f"Reshape (4, -1):\n{arr_auto}")


print("\n=== 2. Flatten & Ravel ===")
# 다차원 배열을 1차원으로 펼치기
print(f"Flatten (Copy): {arr_3x4.flatten()}") # 복사본 반환
print(f"Ravel (View): {arr_3x4.ravel()}")     # 참조(View) 반환 (가능한 경우)


print("\n=== 3. Transpose (전치) ===")
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original (2x3):\n{mat}")

mat_t = mat.T # 또는 np.transpose(mat)
print(f"Transpose (3x2):\n{mat_t}")


print("\n=== 4. Concatenate & Split ===")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 연결 (Concatenate)
v_cat = np.concatenate((a, b), axis=0) # 수직 연결 (= vstack)
h_cat = np.concatenate((a, b), axis=1) # 수평 연결 (= hstack)

print(f"Vertical Concat:\n{v_cat}")
print(f"Horizontal Concat:\n{h_cat}")

# 분할 (Split)
# v_cat(4x2)을 2개로 분할
s1, s2 = np.split(v_cat, 2, axis=0) # (= vsplit)
print(f"Split result 1:\n{s1}")
