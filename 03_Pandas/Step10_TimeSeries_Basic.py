# -*- coding: utf-8 -*-

"""
Step10_TimeSeries_Basic.py
시계열 데이터 기초 (Time Series Basics)
"""
import pandas as pd
import numpy as np

print("=== 1. Creating Date Objects ===")
date_str = "2025-01-01"
date_obj = pd.to_datetime(date_str)
print(f"String '{date_str}' to Datetime: {date_obj} (Type: {type(date_obj)})\n")

# Date Range 생성
dates = pd.date_range("2025-01-01", periods=6, freq='D') # D: 일, M: 월, H: 시간
print(f"Date Range (6 days):\n{dates}\n")


print("=== 2. Time Series DataFrame ===")
df = pd.DataFrame(np.random.randn(6, 2), index=dates, columns=['A', 'B'])
print(f"Time-Indexed DataFrame:\n{df}\n")

print(f"Select by Year-Month ('2025-01'):\n{df['2025-01']}\n")

# slicing with string dates
print(f"Slice '2025-01-02':'2025-01-04':\n{df['2025-01-02':'2025-01-04']}\n")


print("=== 3. Resampling ===")
# 빈도 변경 (일 -> 2일 간격 합계)
resampled = df.resample('2D').sum()
print(f"Resample (2D Sum):\n{resampled}")
