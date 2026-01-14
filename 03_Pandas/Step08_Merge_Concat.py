# -*- coding: utf-8 -*-

"""
Step08_Merge_Concat.py
데이터 병합 (Merge & Concat)
"""
import pandas as pd

# 데이터 준비
df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
df2 = pd.DataFrame({"ID": [2, 3, 4], "Score": [80, 90, 85]})

print(f"df1:\n{df1}")
print(f"df2:\n{df2}\n")


print("=== 1. Merge (Join) ===")
# 공통 컬럼(ID)을 기준으로 병합

# Inner Join (교집합): ID 2, 3만 남음
inner_join = pd.merge(df1, df2, on="ID", how="inner")
print(f"Inner Join:\n{inner_join}\n")

# Left Join (df1 기준): ID 1, 2, 3 (4는 누락, 1의 Score는 NaN)
left_join = pd.merge(df1, df2, on="ID", how="left")
print(f"Left Join:\n{left_join}\n")

# Outer Join (합집합): ID 1, 2, 3, 4 모두 포함
outer_join = pd.merge(df1, df2, on="ID", how="outer")
print(f"Outer Join:\n{outer_join}\n")


print("=== 2. Concat (Stacking) ===")
df3 = pd.DataFrame({"ID": [5, 6], "Name": ["David", "Eva"]})
print(f"df3:\n{df3}\n")

# 위아래로 붙이기 (axis=0)
concat_res = pd.concat([df1, df3], ignore_index=True)
print(f"Concat (Stack Vertical):\n{concat_res}")
