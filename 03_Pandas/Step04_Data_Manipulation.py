# -*- coding: utf-8 -*-

"""
Step04_Data_Manipulation.py
데이터 조작 (Manipulation: Add/Delete/Sort)
"""
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
}, index=['x', 'y', 'z'])
print(f"Original:\n{df}\n")


print("=== 1. Adding Columns ===")
# 스칼라 값 할당: 모든 행에 동일 값
df['C'] = 10
print(f"Add 'C' (Scalar):\n{df}\n")

# 리스트/배열 할당: 행 개수 일치해야 함
df['D'] = [100, 200, 300]
print(f"Add 'D' (List):\n{df}\n")

# 파생 변수 생성
df['Sum'] = df['A'] + df['B']
print(f"Add 'Sum' (A+B):\n{df}\n")


print("=== 2. Deleting Columns/Rows ===")
# 컬럼 삭제 (axis=1)
df_drop_col = df.drop('C', axis=1) # 원본 유지, 반환값 저장
print(f"Drop 'C':\n{df_drop_col}\n")

# 원본에서 바로 삭제 (inplace=True)
df.drop('C', axis=1, inplace=True)
print(f"Dropped 'C' inplace:\n{df}\n")

# 행 삭제 (axis=0, 기본값)
df_drop_row = df.drop('x', axis=0)
print(f"Drop 'x':\n{df_drop_row}\n")


print("=== 3. Sorting ===")
# 값 기준 정렬
# ascending=False (내림차순)
df_sorted = df.sort_values(by='Sum', ascending=False)
print(f"Sort by 'Sum' (Desc):\n{df_sorted}\n")

# 인덱스 기준 정렬
df_idx_sorted = df.sort_index(ascending=False)
print(f"Sort by Index (Desc):\n{df_idx_sorted}")
