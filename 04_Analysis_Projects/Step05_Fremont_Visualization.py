# -*- coding: utf-8 -*-

"""
Step05_Fremont_Visualization.py
데이터 시각화 (Visualization: Trends)
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("fremont_clean.pkl"):
    print("Error: 'fremont_clean.pkl' not found. Run Step04 first.")
    exit()

df = pd.read_pickle("fremont_clean.pkl")
print("=== Data Loaded ===")
print(df.head())

print("\n=== 1. Rolling Mean (30 Days) ===")
# 30일 이동 평균 (추세 확인)
daily = df.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=['--', '-', ':'], figsize=(10, 6))
plt.ylabel('Mean Hourly Count')
plt.title('30-day Rolling Mean')
plt.show()


print("\n=== 2. Average Traffic by Time of Day ===")
# 시간대별 평균 통행량
by_time = df.groupby(df.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)

by_time.plot(xticks=hourly_ticks, style=[':', '--', '-'], figsize=(10, 6))
plt.ylabel('Traffic according to time')
plt.title('Average Traffic by Time of Day')
plt.show() 
