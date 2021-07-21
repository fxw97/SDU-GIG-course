# 导入pandas库
import pandas as pd

data = pd. read_csv('Huairou.csv')
# print(data)
# print(data.info())

# 新建一列时间序列，将年、月、日、小时等时间信息整合到一起。
time = pd.PeriodIndex(year=data['year'],month=data['month'],day=data['day'],hour=data['hour'],freq='H')
#print(time)

# 将新建的时间序列列插入到原始数据
data.insert(1,'time',time)

# 取出我们所需要的数据所在的列
data_finally = data.loc[:,'time':'O3']
# print(data_finally)

# 保存到新的csv文件
data_finally.to_csv('1.huairou.csv',index=None)