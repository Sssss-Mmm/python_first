"""
[20250417_02.py]
Fremont Bridge 자전거 통행량 데이터를 이용한 시계열 데이터 시각화 및 분석 예제입니다.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
# 1. [데이터 로드 및 전처리]
data = pd.read_csv("FremontBridge.csv",index_col="Date",parse_dates=True)
print(data.head(5))
cols =['East',"West"]
data.columns = cols
data['Total']=data.eval('East+West')# data['Total']= data['East']+data['West']
print(data.head(5))
print(data.describe())
data.info()
# seaborn.set()
# data.plot()
# plt.ylabel('Hourly Bicycle Count')
# plt.show()

# 2. [주간 데이터 리샘플링]
# weekly = data.resample('W').sum()
# weekly.plot(style=[':','--','-']) 
# plt.ylabel('Weekly bicycle count')

# 3. [일간 데이터 리샘플링 및 이동 평균 시각화]
daily = data.resample('D').sum()
# daily.rolling(30,center=True).sum().plot(style=[':','--','-'])
# plt.ylabel('mean hourly count')
# daily.rolling(50, center=True,win_type='gaussian').sum(std=10).plot(style=[':','--','-'])

# 4. [시간대별 평균 통행량 분석]
byTime = data.groupby(data.index.time).mean()
hourlyTicks= 4*60*60*np.arange(6)
# byTime.plot(xticks=hourlyTicks,style=[':','--','-'])

# 5. [요일별 평균 통행량 분석]
byWeekday = data.groupby(data.index.dayofweek).mean()
# byWeekday.index=['Mon',"Tues","Wed","Thurs","Fri","Sat","Sun"]
# byWeekday.plot(style=[':','--','-'])


# 6. [주중 vs 주말 시간대별 통행량 비교]
weekend=np.where(data.index.weekday<5,"Weekday","Weekend")
byTime = data.groupby([weekend,data.index.time]).mean()
fgs,ax=plt.subplots(1,2,figsize=(14,5)) 
byTime.loc['Weekday'].plot(ax=ax[0],title='Weekdays',
                           xticks=hourlyTicks, 
                           style=[':','--','-'])
byTime.loc['Weekend'].plot(ax=ax[1],title='Weekends',
                           xticks=hourlyTicks, 
                           style=[':','--','-'])
# plt.show()


