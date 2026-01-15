"""
[Step 04] Fremont Bridge Data Load & Analysis
---------------------------------------------
Fremont Bridge 자전거 통행량 데이터를 로드하고 
시계열 데이터 처리(Resampling) 및 시각화를 수행하는 예제입니다.

주요 내용:
- CSV 데이터 로드 및 날짜 인덱스 설정
- 주간(Weekly), 일간(Daily) 데이터 리샘플링
- 시간대별, 요일별 통행량 패턴 분석 및 시각화
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드 및 전처리
data = pd.read_csv("../data/FremontBridge.csv",
                    index_col='Date', parse_dates=True)
print(data.head())
cols = ["East", "West"]
data.columns = cols # 컬럼명 변경
data['Total'] = data.eval('East+West') # 전체 통행량 계산 (동쪽 + 서쪽)
data.info()
print(data.describe())

import seaborn
# seaborn.set()
# data.plot()
# plt.ylabel('Hourly Bicle Count')
# plt.show()

# 주간 단위로 리샘플링하여 합계 계산
weekly = data.resample("W").sum()
# weekly.plot(style=[':', "--", "-"])
# plt.ylabel('Weekly Bicle Count')
# plt.show()

# 일간 데이터 리샘플링 및 이동 평균 시각화
daily = data.resample("D").sum()
# daily.rolling(30, center=True).sum().plot(style=[':', "--", "-"])
# plt.ylabel('mean daily Count')
# plt.show()
# daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', "--", "-"])
# plt.show()
# 시간대별(Hourly) 평균 통행량 계산
byTime = data.groupby(data.index.time).mean()
hourlyTicks = 4*60*60*np.arange(6)
# byTime.plot(xticks=hourlyTicks, style=[':', "--", "-"])
# plt.show()

# 요일별 평균 통행량
byWeekday = data.groupby(data.index.dayofweek).mean() # 요일별 평균 통행량
byWeekday.index = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
# byWeekday.plot(style=[':', "--", "-"])
# plt.show()

# 주말과 주중 데이터 분리
weekend = np.where(data.index.weekday < 5, "Weekday", "Weekend")
# 주말/주중 및 시간대별 평균 통행량 그룹화
byTime = data.groupby([weekend, data.index.time]).mean()
fgs, ax = plt.subplots(1,2, figsize=(14, 5))
byTime.loc["Weekday"].plot(ax=ax[0], title="Weekday", \
                          xticks=hourlyTicks, style=[':', "--", "-"])
byTime.loc["Weekend"].plot(ax=ax[1], title="Weekend", \
                          xticks=hourlyTicks, style=[':', "--", "-"])
plt.show()