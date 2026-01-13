# -*- coding: utf-8 -*-

"""
Step06_Broadcasting.py
브로드캐스팅 (Broadcasting)
: 모양(Shape)이 다른 배열 간의 연산을 자동으로 수행하는 규칙
"""
import numpy as np

print("=== 1. Scalar Broadcasting ===")
arr = np.array([1, 2, 3])
print(f"Array: {arr}")
print(f"Array + 10: {arr + 10}") # [11, 12, 13]


print("\n=== 2. Array Broadcasting (Matrix + Vector) ===")
# 3x3 행렬
matrix = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])
# 1x3 벡터 (또는 길이 3인 1차원 배열)
vector = np.array([0, 1, 2])

print(f"Matrix (3x3):\n{matrix}")
print(f"Vector (3,): {vector}")

# (3x3) + (3,) => 벡터가 각 행마다 더해짐
result = matrix + vector
print(f"Result:\n{result}")


print("\n=== 3. Column Vector Broadcasting ===")
# 3x1 벡터
col_vector = np.array([[10], [20], [30]])
print(f"Col Vector (3x1):\n{col_vector}")

# (3x3) + (3x1) => 벡터가 각 열마다 더해짐
result_col = matrix + col_vector
print(f"Result:\n{result_col}")
