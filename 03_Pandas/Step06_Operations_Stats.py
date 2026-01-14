# -*- coding: utf-8 -*-

"""
Step06_Operations_Stats.py
기본 연산과 통계 함수 (Basic Operations & Statistics)
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Key": ["A", "B", "C", "A", "B"],
    "Data1": [10, 20, 30, 40, 50],
    "Data2": [5, 4, 3, 2, 1]
})
print(f"DataFrame:\n{df}\n")


print("=== 1. Basic Statistics ===")
# 요약 정보 (개수, 평균, 표준편차, 4분위수 등)
print(f"describe():\n{df.describe()}\n")

print(f"Mean (Data1): {df['Data1'].mean()}")
print(f"Sum (Data2): {df['Data2'].sum()}")
print(f"Correlation:\n{df[['Data1', 'Data2']].corr()}\n")


print("=== 2. Unique & Value Counts ===")
# 고유값 확인
print(f"Unique Keys: {df['Key'].unique()}")
print(f"Nunique (Count): {df['Key'].nunique()}")

# 값의 빈도수 (Data Distribution)
print(f"Value Counts (Key):\n{df['Key'].value_counts()}\n")


print("=== 3. Data Transformation (apply) ===")
# 함수 적용 (Mapping)
def square(x):
    return x ** 2

# Series에 적용
df['Data1_Sq'] = df['Data1'].apply(square)
print(f"Apply square to Data1:\n{df}")

# Lambda 사용
df['Data2_x10'] = df['Data2'].apply(lambda x: x * 10)
print(f"Apply lambda (*10) to Data2:\n{df}")
