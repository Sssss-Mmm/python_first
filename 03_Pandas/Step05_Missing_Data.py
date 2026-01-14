# -*- coding: utf-8 -*-

"""
Step05_Missing_Data.py
결측치 처리 (Handling Missing Data)
"""
import pandas as pd
import numpy as np

# 결측치(NaN: Not a Number)가 포함된 데이터 생성
df = pd.DataFrame({
    "A": [1, 2, np.nan, 4],
    "B": [5, np.nan, np.nan, 8],
    "C": [10, 11, 12, 13]
})
print(f"Original:\n{df}\n")


print("=== 1. Checking Missing Values ===")
# True이면 결측치
print(f"isna():\n{df.isna()}\n")

# 각 컬럼별 결측치 개수 확인
print(f"Missing count per column:\n{df.isna().sum()}\n")


print("=== 2. Dropping Missing Values ===")
# 하나라도 NaN이 있으면 해당 행 삭제
df_dropped = df.dropna() 
print(f"dropna (any row with nan):\n{df_dropped}\n")

# 모든 값이 NaN인 행만 삭제 (subset 지정 가능)
# df.dropna(how='all')


print("=== 3. Filling Missing Values ===")
# 특정 값으로 채우기
df_filled_0 = df.fillna(0)
print(f"fillna(0):\n{df_filled_0}\n")

# 평균값으로 채우기 (컬럼별 평균 사용)
mean_val = df['A'].mean()
df_filled_mean = df.copy()
df_filled_mean['A'] = df['A'].fillna(mean_val)
print(f"fillna(mean) for Col A (Mean={mean_val}):\n{df_filled_mean}")
