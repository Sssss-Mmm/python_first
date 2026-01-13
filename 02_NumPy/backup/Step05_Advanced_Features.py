"""
NumPy Advanced Operations Example
---------------------------------
이 파일은 NumPy의 심화 연산 기능을 다룹니다.
1. Broadcasting: 크기가 다른 배열 간의 자동 연산.
2. Logical Indexing (Masking): 조건에 맞는 데이터만 선택하거나 변경.
3. Linear Algebra Basics: 내적(Dot Product) 등 선형대수 기본 연산.
"""

import numpy as np

def run_numpy_advanced_examples():
    print("=== 1. Broadcasting Example ===")
    # 2차원 배열 (3x3 Matrix)
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    # 1차원 배열 (Vector)
    vector = np.array([10, 20, 30])
    
    print(f"Matrix:\n{matrix}")
    print(f"Vector: {vector}")
    
    # 브로드캐스팅: (3x3) + (3,) => 각 행마다 벡터가 더해짐
    result = matrix + vector
    print(f"Broadcasting Result (Matrix + Vector):\n{result}")
    
    
    print("\n=== 2. Logical Indexing (Masking) Example ===")
    data = np.random.randint(1, 100, size=10) # 1~100 사이 난수 10개
    print(f"Original Data: {data}")
    
    # 조건: 50보다 큰 값 찾기
    mask = data > 50
    print(f"Mask (Data > 50): {mask}")
    
    # 마스크를 이용한 필터링
    filtered_data = data[mask]
    print(f"Filtered Data: {filtered_data}")
    
    # 조건부 값 변경: 50 이하는 0으로 변경
    data[data <= 50] = 0
    print(f"Modified Data (<=50 -> 0): {data}")


    print("\n=== 3. Linear Algebra Basics Example ===")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    
    # 행렬 곱 (Dot Product)
    dot_product = np.dot(A, B)
    print(f"Dot Product (A @ B):\n{dot_product}")
    
    # Transpose (전치 행렬)
    transpose_A = A.T
    print(f"Transpose of A:\n{transpose_A}")

if __name__ == "__main__":
    run_numpy_advanced_examples()
