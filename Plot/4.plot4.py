import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../Data analysis/1.huairou.csv')
data = data.loc[:,'PM2.5':'O3']
# print(data.info()) # 打印输出发现共35064行、6列数据

# 求个污染物浓度之间的相关性
data_corr = data.corr()

# 绘制相关性热力图
sns.heatmap(data_corr,cmap='jet',linewidths=0.5,vmin=-1,vmax=1,cbar_kws={'label':'Correlation values'},annot=True)

plt.tick_params(axis='y',rotation=0,length=0)
plt.tick_params(axis='x',length=0)
plt.tight_layout()

plt.savefig('4.plot4.svg',dpi=900)
plt.show()