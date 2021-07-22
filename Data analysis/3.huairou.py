import pandas as pd

data = pd.read_csv('1.huairou.csv')
# print(data)

# 将时间列改为pandas可以识别的格式
data['time'] = pd.to_datetime(data['time'])

# 将时间序列与对应的星期数一一对应
data['dayofweek'] = data['time'].dt.day_name()
# print(data)

# 将时间序列与对应的季度一一对应
data['Q'] = data['time'].dt.quarter

# 周变化数据：按星期数分组求平均，并保存数据
data_week = data.groupby('dayofweek')[['PM2.5','PM10','SO2','NO2','CO','O3']].mean()
# print(data_week)
data_week.to_csv('3.data_week.csv')

# 月变化数据：按月份分组求平均，并保存数据
data_month = data.groupby('month')[['PM2.5','PM10','SO2','NO2','CO','O3']].mean()
# print(data_month)
data_month.to_csv('3.data_month.csv')

# 季节变化数据：按季度分组求平均，并保存数据
data_quarter = data.groupby('Q')[['PM2.5','PM10','SO2','NO2','CO','O3']].mean()
# print(data_quarter)
data_quarter.to_csv('3.data_quarter.csv')