# -*- coding: utf-8 -*-

"""
Step07_Fremont_Prediction.py
통행량 예측 (Prediction: Linear Regression)
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression

if not os.path.exists("fremont_clean.pkl"):
    exit()

# 일별 합계 데이터 사용
df = pd.read_pickle("fremont_clean.pkl")
daily = df.resample('D').sum()
daily['Total'] = daily['West'] + daily['East']
data = daily[['Total']].copy()

print("=== 1. Feature Engineering ===")
# 요일 (Mon=0, Sun=6)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i in range(7):
    data[days[i]] = (data.index.dayofweek == i).astype(float)

# 휴일 (미국 공휴일 라이브러리 등이 없으므로 간단히 처리하거나 생략)
# 여기서는 '시간 흐름(연차)'만 추가
data['day_count'] = np.arange(len(data))

print(data.head())
data = data.dropna() # 결측치 제거

print("\n=== 2. Linear Regression ===")
# X: Features (요일, 경과일수)
# y: Target (Total 통행량)
X = data[days + ['day_count']]
y = data['Total']

model = LinearRegression(fit_intercept=False)
model.fit(X, y)

# 예측
daily['predicted'] = model.predict(X)

# 시각화
daily[['Total', 'predicted']].plot(alpha=0.5, figsize=(10, 6))
plt.title('Daily Bicycle Count Prediction')
plt.show()

print("\n=== 3. Validation ===")
# 계수 확인 (요일별 영향력)
params = pd.Series(model.coef_, index=X.columns)
print("Coefficient (Effect of each day):")
print(params)
