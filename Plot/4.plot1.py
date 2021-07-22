# 导入pandas和matplotlib库
import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体为新罗马
plt.rcParams['font.sans-serif'] = ['Times New Roman']

# 读入绘图数据
data = pd.read_csv('../Data analysis/2.huairou_1day.csv')

# 时间尺度作为绘图x轴数据
x = data.index

# 获取2013-03-01、2014-01-01、2015-01-01、2016-01-01及2017-01-01的索引位置，从而确定这些时间点在x轴上的标签位置
xticks_loc = data[data['time'].isin(['2013-03-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01'])].index.values
print(xticks_loc)

# 取出绘图需要的y轴数据，分别为PM2.5、SO2、NO2和O3的浓度数据
y1 = data['PM2.5']
y2 = data['SO2']
y3 = data['NO2']
y4 = data['O3']

# 新建画布和两行两列共4个坐标轴
fig, ax = plt.subplots(2,2,figsize=(12,6))

# 在第一个坐标轴绘制PM2.5浓度变化的折线图
ax[0][0].plot(x,y1)
ax[0][0].set_xticks([0,306,671,1036,1402])  #将x轴标签位置设置为每年数据的起始位置
ax[0][0].set_xticklabels(['2013-03-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01']) #将标签值传入到x轴标签位置
ax[0][0].set_xlabel('Time')
ax[0][0].set_ylabel('PM2.5(μg·m-3)')

# 在第二个坐标轴绘制SO2浓度变化折线图
ax[0][1].plot(x,y2,c='C1')
ax[0][1].set_xticks([0,306,671,1036,1402])  #将x轴标签位置设置为每年数据的起始位置
ax[0][1].set_xticklabels(['2013-03-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01']) #将标签值传入到x轴标签位置
ax[0][1].set_xlabel('Time')
ax[0][1].set_ylabel('SO2(μg·m-3)')

# 在第三个坐标轴绘制SO2浓度变化折线图
ax[1][0].scatter(x,y3,c='C2',s=10)
ax[1][0].set_xticks([0,306,671,1036,1402])  #将x轴标签位置设置为每年数据的起始位置
ax[1][0].set_xticklabels(['2013-03-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01']) #将标签值传入到x轴标签位置
ax[1][0].set_xlabel('Time')
ax[1][0].set_ylabel('NO2(μg·m-3)')

#在第四个坐标轴绘制O3浓度变化曲线
ax[1][1].bar(x,y4,color='C3')
ax[1][1].set_xticks([0,306,671,1036,1402])  #将x轴标签位置设置为每年数据的起始位置
ax[1][1].set_xticklabels(['2013-03-01','2014-01-01','2015-01-01','2016-01-01','2017-01-01']) #将标签值传入到x轴标签位置
ax[1][1].set_xlabel('Time')
ax[1][1].set_ylabel('O3(μg·m-3)')


plt.tight_layout() # 让图形最大贴合画布，减少周围留下的空白
plt.savefig('4.plot1.svg',dpi=900) # 保存图片一定要在展示图片-plt.show()代码之前
plt.show() # 在pycharm中展示所绘图片