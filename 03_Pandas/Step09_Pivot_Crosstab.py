# -*- coding: utf-8 -*-

"""
Step09_Pivot_Crosstab.py
피벗 테이블과 교차표 (Pivot Table & Crosstab)
"""
import pandas as pd
import numpy as np

data = {
    "Date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-01"],
    "Region": ["Seoul", "Busan", "Seoul", "Busan", "Seoul"],
    "Product": ["Apple", "Apple", "Banana", "Banana", "Apple"],
    "Sales": [100, 200, 150, 250, 100]
}
df = pd.DataFrame(data)
print(f"Original DataFrame:\n{df}\n")


print("=== 1. Pivot Table ===")
# 엑셀의 피벗 테이블과 유사 기능
# 인덱스: Date, 컬럼: Region, 값: Sales (합계)
pivot_res = df.pivot_table(index="Date", columns="Region", values="Sales", aggfunc="sum")
print(f"Pivot Table (Sum of Sales):\n{pivot_res}\n")

# 여러 집계 함수 적용
pivot_multi = df.pivot_table(index="Date", columns="Product", values="Sales", aggfunc=["sum", "mean"])
print(f"Pivot Table (Sum & Mean):\n{pivot_multi}\n")


print("=== 2. Crosstab (교차표) ===")
# 두 범주형 변수의 빈도수나 집계
# Region별 Product 판매 횟수
cross_count = pd.crosstab(index=df["Region"], columns=df["Product"])
print(f"Crosstab (Count):\n{cross_count}\n")

# Region별 Product Sales 합계
cross_sum = pd.crosstab(index=df["Region"], columns=df["Product"], values=df["Sales"], aggfunc="sum")
print(f"Crosstab (Sum of Sales):\n{cross_sum}")
