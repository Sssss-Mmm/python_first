# -*- coding: utf-8 -*-

"""
Step03_Indexing_Selection_Loc.py
데이터 선택과 인덱싱 (Indexing & Selection with loc/iloc)
"""
import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 22],
    "City": ["Seoul", "Busan", "Incheon", "Seoul", "Daegu"],
    "Score": [88, 92, 75, 80, 95]
}
df = pd.DataFrame(data)
# 인덱스를 이름으로 사용해보기 (가독성 위해)
df = df.set_index("Name") 

print(f"DataFrame:\n{df}\n")


print("=== 1. Column Selection ===")
# 단일 컬럼 -> Series 반환
print(f"Age Series:\n{df['Age']}\n")
# 복수 컬럼 -> DataFrame 반환
print(f"Name & Score:\n{df[['City', 'Score']]}\n")


print("=== 2. loc (Label-based Indexing) ===")
# 이름(Label)을 기준으로 행/열 선택
print(f"loc['Alice']:\n{df.loc['Alice']}\n") # Series 반환

# 행, 열 동시 선택
print(f"loc['Bob', 'Score']: {df.loc['Bob', 'Score']}\n")

# 슬라이싱 (끝 포함!)
print(f"loc['Alice':'Charlie']:\n{df.loc['Alice':'Charlie']}\n")


print("=== 3. iloc (Integer-based Indexing) ===")
# 위치(0부터 시작하는 숫자)를 기준으로 선택
print(f"iloc[0] (First Row):\n{df.iloc[0]}\n")

# [행, 열] 인덱스
print(f"iloc[1, 2] (Row 1, Col 2): {df.iloc[1, 2]}\n")

# 슬라이싱 (끝 제외, Python 기본과 동일)
print(f"iloc[0:3]:\n{df.iloc[0:3]}\n")


print("=== 4. Boolean Indexing (Filtering) ===")
# 조건에 맞는 행만 추출
mask = df['Age'] >= 30
print(f"Mask (Age >= 30):\n{mask}\n")

print(f"Filtered DataFrame:\n{df[mask]}\n")

# 복합 조건 (&, |)
cond = (df['Age'] >= 30) & (df['City'] == 'Seoul')
print(f"Age >= 30 AND City == 'Seoul':\n{df[cond]}")
