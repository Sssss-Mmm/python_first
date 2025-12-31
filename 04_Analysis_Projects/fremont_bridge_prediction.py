"""
[20250418_01.py]
Fremont Bridge 자전거 통행량 데이터를 날씨 데이터와 결합하여 선형 회귀 모델로 트래픽을 예측하고 평가하는 예제입니다.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar
from sklearn.metrics import r2_score, mean_squared_error

counts= pd.read_csv('../data/FremontBridge.csv',index_col='Date', parse_dates=True)
weather =pd.read_csv('../data/BicycleWeather.csv',index_col='DATE',parse_dates=True)
print(counts.head(3))
weather.info()
print(weather.head(3))
daily= counts.resample('d').sum()
daily['Total'] =daily.sum(axis=1)
daily = daily[['Total']]

print(daily.head(3))
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for i in range(len(days)):
    daily[days[i]]=(daily.index.dayofweek ==i).astype(float) # 요일별 원-핫 인코딩 (월~일)
# for i in dir(daily.index):
#     print(i)
print(daily.head(7))
cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012','2016') # 미국 공휴일 데이터 가져오기
daily= daily.join(pd.Series(1, index= holidays, name='holiday')) # 휴일 여부 추가
# print("2012 holiday",daily.loc['2012'].sample(5))
daily['holiday'].fillna(0, inplace=True) # 휴일이 아닌 날은 0으로 채움
print(daily.head(3))
# 일조시간(낮의 길이) 계산 함수: 날씨가 좋을 때 자전거를 더 많이 타는지 파악하기 위함
def hours_of_daylight(date, axis=23.44, latitude=47.61):
    """
    해당 날짜의 일조시간(낮의 길이)을 계산합니다.
    
    Args:
        date: 날짜
        axis: 자전축 기울기 (기본값: 23.44도)
        latitude: 위도 (기본값: 47.61도 - 시애틀)
    Returns:
        일조시간 (시간 단위)
    """
    # 해당 날짜의 일조시간 계산
    days = (date - pd.to_datetime('2000, 12, 21')).days
    m = (1. -np.tan(np.radians(latitude))
    * np.tan(np.radians(axis) * np.cos(days * 2 * np.pi / 365.25)))
    return 24 * np.degrees(np.arccos(1 - np.clip(m, 0, 2))) / 180.
daily['daylight_hrs'] = list(map(hours_of_daylight, daily.index))
daily[['daylight_hrs']].plot()
plt.ylim(8, 17)
# plt.show()
weather['TMIN'] /= 10 # 온도 단위??
weather['TMAX'] /= 10
weather['Temp(F)'] = 0.5 * (weather['TMIN'] + weather['TMAX']) # 평균 온도
weather['PRCP'] /= 254 # 강수량 단위 변환
weather['dry day'] = (weather['PRCP']== 0).astype(int) # 비가 오지 않은 날 (건조한 날)
daily =daily.join(weather[['PRCP','Temp(F)','dry day']]) # 날씨 데이터 병합
print(daily.head(10))
daily['annual']= (daily.index - daily.index[0]).days /365. # 연도별 증가 추세를 반영하기 위한 변수
print(daily.sample())
daily.dropna(axis=0,how='any',inplace=True)
column_names = ['Mon','Tue','Wed',"Thu","Fri",'Sat',"Sun","holiday",'daylight_hrs','PRCP',"dry day",'Temp(F)','annual']
X= daily[column_names]
y=daily['Total']
print(X.head(3))
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False) #인공지능 학생
model.fit(X,y) #학습시키다
daily['predicted'] = model.predict(X) # 검증, 모의고사, 테스트...(맞춰봐)
daily[['Total','predicted']].plot(alpha=0.5)
params= pd.Series(model.coef_,index=X.columns)
print("params:",params)
# plt.show() 
from sklearn.utils import resample
np.random.seed(1)
err = np.std([model.fit(*resample(X,y)).coef_ for i in range(1000)],0)
print(pd.DataFrame({'effect': params.round(0), 'error':err.round(0)}))

# --- Added Features ---

# 1. Model Evaluation
r2 = r2_score(y, daily['predicted'])
rmse = np.sqrt(mean_squared_error(y, daily['predicted']))
print(f"\n[Model Evaluation]")
print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 2. Save Results
output_filename = 'predicted_bicycle_traffic.csv'
daily.to_csv(output_filename)
print(f"\n[Result Saving]")
print(f"Results saved to '{output_filename}'")

# 3. Visualization
plt.figure(figsize=(14, 6))

# Subplot 1: Actual vs Predicted Scatter
plt.subplot(1, 2, 1)
plt.scatter(y, daily['predicted'], alpha=0.3)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Traffic')
plt.ylabel('Predicted Traffic')
plt.title('Actual vs Predicted (Scatter)')

# Subplot 2: Detailed View of First 50 Days
plt.subplot(1, 2, 2)
daily['Total'].iloc[:50].plot(label='Actual', style='-')
daily['predicted'].iloc[:50].plot(label='Predicted', style='--')
plt.legend()
plt.title('Actual vs Predicted (First 50 Days)')

plt.tight_layout()
plt.show()