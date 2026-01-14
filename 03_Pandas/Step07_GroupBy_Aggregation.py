# -*- coding: utf-8 -*-

"""
Step07_GroupBy_Aggregation.py
그룹화와 집계 (GroupBy & Aggregation)
"""
import pandas as pd

df = pd.DataFrame({
    "Category": ["A", "A", "B", "B", "C", "C"],
    "Sub": ["x", "y", "x", "y", "x", "y"],
    "Score1": [10, 20, 30, 40, 50, 60],
    "Score2": [100, 200, 300, 400, 500, 600]
})
print(f"DataFrame:\n{df}\n")


print("=== 1. Basic GroupBy ===")
# Category별 Score1의 평균
grouped = df.groupby("Category")
print(f"Mean per Category (Score1):\n{grouped['Score1'].mean()}\n")

# 여러 컬럼 평균
print(f"Mean per Category (All Numeric):\n{grouped.mean(numeric_only=True)}\n")


print("=== 2. Multi-level GroupBy ===")
# (Category, Sub) 두 가지 기준으로 그룹화
multi_group = df.groupby(["Category", "Sub"]).sum()
print(f"Sum per Category & Sub:\n{multi_group}\n")


print("=== 3. Aggregation (agg) ===")
# 다양한 집계 함수를 한 번에 적용
# 총합, 평균, 최댓값
agg_res = grouped['Score1'].agg(['sum', 'mean', 'max'])
print(f"Agg result:\n{agg_res}")
