import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体为新罗马
plt.rcParams['font.sans-serif'] = ['Times New Roman']

# 导入绘图数据
data1 = pd.read_csv('../Data analysis/3.data_month.csv') # 月均值数据
data2 = pd.read_csv('../Data analysis/3.data_week.csv',index_col='dayofweek') # 星期均值数据
data2 = data2.loc[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']] # 将星期数据按照周一到周日排序

# x轴绘图数据
x1 = range(12)
x2 = range(7)

# 第一个坐标系中y轴绘图数据
y1 = data1['PM2.5']
y12 = data1['PM10']

# 第二个坐标系中y轴绘图数据
y2 = data2['NO2']
y22 = data2['O3']


fig, ax = plt.subplots(1,2,figsize=(12,5)) # 新建一个画布，有一行两列共两个坐标轴

# 在第一个坐标轴绘制月均值变化双y图
l1 = ax[0].bar(x1,y1,label='PM2.5')    # 绘制PM2.5柱状图
ax[0].set_ylim(0,140) # 设置y轴范围
ax[0].set_xticks(range(12)) # 设置x刻度位置
ax[0].set_xticklabels(range(1,13)) # 设置x刻度标签
ax[0].set_xlabel('Month') #设置x轴标题
ax[0].set_ylabel('PM2.5') # 设置y轴标题

p1 = ax[0].twinx()  #建立第一个坐标系的副y轴
l12, = p1.plot(x1,y12,color='C1',marker='o',mfc='w',linewidth = 2,label='PM10') # 绘制副y轴的PM10点线图
p1.set_ylim(0,130) #设置副y轴范围
p1.set_ylabel('PM10') #设置y轴标题

ax[0].legend([l1,l12],['PM2.5','PM10'],frameon=False) #设置图例
ax[0].grid(alpha=0.5,linestyle='--') # 设置网格


# 在第二个坐标轴绘制星期均值变化双y图
l2, = ax[1].plot(x2,y2)
ax[1].set_ylim(28,38)
ax[1].set_xticks(range(7))
ax[1].set_xticklabels(data2.index,rotation=30)
ax[1].set_ylabel('NO2')

p2 = ax[1].twinx()
l22, = p2.plot(x2,y22,c='C1',linestyle='--')
p2.set_ylim(54,64)
p2.set_yticks(range(54,66,2))
p2.set_ylabel('O3')

ax[1].legend([l2,l22],['NO2','O3'],frameon=False)
plt.tight_layout()
plt.savefig('4.plot2.svg',dpi=900)
plt.show()