import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置全局字体为新罗马
plt.rcParams['font.sans-serif'] = ['Times New Roman']

data = pd.read_csv('../Data analysis/2.huairou_year.csv') # 读入年均值数据
data = data.loc[:,'PM2.5':'O3'] # 取出污染物浓度数据
data['year'] = ['2013','2014','2015','2016','2017'] #将年份写入数据表
data.set_index('year',inplace=True)
data['CO'] = data['CO']/10


plt.figure(figsize=(10,6))

x1 = np.arange(6)-0.3
x2 = np.arange(6)-0.15
x3 = np.arange(6)
x4 = np.arange(6)+0.15
x5 = np.arange(6)+0.3

colors=['#53AC74','#5CB8CC','#7559B5','#CCB57A','#C45759','#4778BA','#C0C0C0']

plt.bar(x1,data.loc['2013'],width=0.15,label='2013year',alpha=0.8,color=colors[0])
plt.bar(x2,data.loc['2014'],width=0.15,label='2014year',alpha=0.8,color=colors[1])
plt.bar(x3,data.loc['2015'],width=0.15,label='2015year',alpha=0.8,color=colors[2])
plt.bar(x4,data.loc['2016'],width=0.15,label='2016year',alpha=0.8,color=colors[3])
plt.bar(x5,data.loc['2017'],width=0.15,label='2017year',alpha=0.8,color=colors[4])
plt.xticks(range(6),['PM2.5','PM10','SO2','NO2','CO(×10)','O3'],fontsize=10)
plt.yticks(fontsize=10)
plt.ylabel('Concentration(μg·m-3)',fontsize=12)
plt.grid(axis='y',alpha=0.5,linestyle='--')
plt.tick_params(axis='x',length=0)

plt.legend(fontsize=12,frameon=False)
plt.tight_layout()
plt.savefig('4.plot3.svg',dpi=900)
plt.show()