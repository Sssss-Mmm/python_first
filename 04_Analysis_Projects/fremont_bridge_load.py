import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/FremontBridge.csv",
                    index_col='Date', parse_dates=True)
print(data.head())
cols = ["East", "West"]
data.columns = cols
data['Total'] = data.eval('East+West')
data.info()
print(data.describe())

import seaborn
# seaborn.set()
# data.plot()
# plt.ylabel('Hourly Bicle Count')
# plt.show()

weekly = data.resample("W").sum()
# weekly.plot(style=[':', "--", "-"])
# plt.ylabel('Weekly Bicle Count')
# plt.show()

daily = data.resample("D").sum()
# daily.rolling(30, center=True).sum().plot(style=[':', "--", "-"])
# plt.ylabel('mean daily Count')
# plt.show()
# daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', "--", "-"])
# plt.show()
byTime = data.groupby(data.index.time).mean()
hourlyTicks = 4*60*60*np.arange(6)
# byTime.plot(xticks=hourlyTicks, style=[':', "--", "-"])
# plt.show()

byWeekday = data.groupby(data.index.dayofweek).mean()
byWeekday.index = ['Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
# byWeekday.plot(style=[':', "--", "-"])
# plt.show()

weekend = np.where(data.index.weekday < 5, "Weekday", "Weekend")
byTime = data.groupby([weekend, data.index.time]).mean()
fgs, ax = plt.subplots(1,2, figsize=(14, 5))
byTime.loc["Weekday"].plot(ax=ax[0], title="Weekday", \
                          xticks=hourlyTicks, style=[':', "--", "-"])
byTime.loc["Weekend"].plot(ax=ax[1], title="Weekend", \
                          xticks=hourlyTicks, style=[':', "--", "-"])
plt.show()