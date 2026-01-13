# -*- coding: utf-8 -*-

"""
Step08_LinearAlgebra.py
선형대수 기초 (Linear Algebra Basics)
"""
import numpy as np

print("=== 1. Matrix Multiplication (Dot Product) ===")
# 2x2 행렬
A = np.array([[1, 2],
              [3, 4]])
# 2x2 행렬
B = np.array([[5, 6],
              [7, 8]])

print(f"Matrix A:\n{A}")
print(f"Matrix B:\n{B}")

# 행렬 곱 (A @ B)
dot_res = np.dot(A, B)
matmul_res = np.matmul(A, B) # A @ B 와 동일
print(f"Dot Product (A.B):\n{dot_res}")
print(f"Matmul (A @ B):\n{matmul_res}")


print("\n=== 2. Identity Matrix & Inverse ===")
# 단위 행렬 (대각 성분이 1인 정사각 행렬)
I = np.eye(2)
print(f"Identity Matrix (2x2):\n{I}")

print(f"A @ I:\n{np.dot(A, I)}") # 자기 자신이 나와야 함

# 역행렬 (Inverse Matrix)
try:
    inv_A = np.linalg.inv(A)
    print(f"Inverse of A:\n{inv_A}")
    print(f"A @ inv_A (Should be Identity):\n{np.dot(A, inv_A)}")
except np.linalg.LinAlgError:
    print("Inverse does not exist (Singular Matrix).")


print("\n=== 3. Determinant ===")
# 행렬식 (Determinant)
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A:.2f}")
