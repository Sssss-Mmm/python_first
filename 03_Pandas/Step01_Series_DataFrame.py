# -*- coding: utf-8 -*-

"""
Step01_Series_DataFrame.py
Pandas 자료구조 (Series & DataFrame)
"""
import pandas as pd
import numpy as np

print("=== 1. Series Creation ===")
# Series: 1차원 데이터 (인덱스 + 값)
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(f"Series:\n{s}")
print(f"Values: {s.values}")
print(f"Index: {s.index}")


print("\n=== 2. DataFrame Creation ===")
# DataFrame: 2차원 데이터 (행/열)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["Seoul", "Busan", "Incheon", "Seoul"]
}
df = pd.DataFrame(data)
print(f"DataFrame (from dict):\n{df}")


print("\n=== 3. DataFrame Attributes ===")
print(f"Shape: {df.shape}")       # (행, 열)
print(f"Columns: {df.columns}")   # 열 이름
print(f"Index: {df.index}")       # 행 인덱스
print(f"Dtypes:\n{df.dtypes}")    # 각 열의 자료형

# 기본 정보 요약
print("\n--- Info ---")
df.info()


print("\n=== 4. Creating from NumPy ===")
arr = np.random.randn(4, 3) # 4x3 난수
df_np = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(f"DataFrame (from NumPy):\n{df_np}")
