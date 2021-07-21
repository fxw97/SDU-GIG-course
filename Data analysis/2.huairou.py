import pandas as pd

# 读取数据
data = pd.read_csv('1.huairou.csv')
# print(data)

# 更改时间分辨率之前，需要把时间列更改为pandas可以识别的时间格式，并设置为索引
data['time'] = pd.to_datetime(data['time'])
data.set_index('time',inplace=True)
# print(data)

# 更改数据的时间分辨率为6小时，并保存
data_6h = data.resample('6H').mean()
# print(data_6h)
data_6h.to_csv('2.huairou_6h.csv')

# 更改数据的时间分辨率为1天，并保存
data_1day = data.resample('1D').mean()
# print(data_1day)
data_1day.to_csv('2.huairou_1day.csv')

# 更改数据的时间分辨率为1个月，并保存
data_1month = data.resample('1M').mean().to_period('M')
# print(data_1month)
data_1month.to_csv('2.huairou_1month.csv')