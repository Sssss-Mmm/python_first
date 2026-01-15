# -*- coding: utf-8 -*-

"""
Step06_Fremont_Analysis.py
패턴 분석 (Analysis: Weekday vs Weekend)
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

if not os.path.exists("fremont_clean.pkl"):
    exit()

df = pd.read_pickle("fremont_clean.pkl")

print("=== 1. Weekday vs Weekend ===")
# 요일별 구분 (0=Mon, 6=Sun)
# 주중(0~4)과 주말(5~6) 데이터 분리
where_weekend = df.index.dayofweek >= 5
by_time = df.groupby([where_weekend, df.index.time]).mean()

# 시각화
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_time.loc[False].plot(ax=ax[0], title='Weekday', xticks=4*3600*np.arange(6))
by_time.loc[True].plot(ax=ax[1], title='Weekend', xticks=4*3600*np.arange(6))
plt.show()

print("주중에는 출퇴근 시간(8시, 17시)에 피크가 있고,")
print("주말에는 낮 시간대에 완만한 분포를 보임 -> 레저용으로 추정")
