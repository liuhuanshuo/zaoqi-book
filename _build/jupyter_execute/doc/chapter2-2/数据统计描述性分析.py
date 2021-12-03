#!/usr/bin/env python
# coding: utf-8

# # 数据探索与统计分析
# 
# 
# 在利用 `Pandas` 进行对数据进行**缺失值**、**重复值**进行检查与相关处理后
# 
# 接下来一般是对数据进行简单的**探索与统计描述性分析**，进一步观察数据特征，为后续的分析提供大致方向。

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# In[1]:


import pandas as pd
df = pd.read_excel("2020年中国大学排名.xlsx",index_col=0)
import warnings
warnings.filterwarnings("ignore")


# ## 数据查看

# ### 查看指定行
# 
# 查看数据前 10 行

# In[2]:


df.head(10)


# ### 查看数据量
# 
# 也就是数据框的 行 * 列，总共单元格的数量

# In[3]:


df.size


# ## 数据排序

# ### 升序
# 
# 将数据按照总分升序排列，并展示前20个学校
# 
# 备注：也就是看倒数20名啦

# In[4]:


df.sort_values(by='总分', ascending=True).head(20)


# ### 指定列排序
# 
# 将数据按照 高端人才得分 降序排序，展示前 10 位

# In[5]:


df.nlargest(10, '高端人才得分')


# ### 分列排名
# 
# 查看各项得分最高的学校名称

# In[6]:


df.iloc[:,3:].idxmax()


# ## 数据统计

# ### 统计信息｜均值
# 
# 计算总分列的均值

# In[7]:


df.总分.mean()


# ### 统计信息｜中位数
# 
# 
# 计算总分列的中位数

# In[8]:


df.总分.median()


# ###  统计信息｜众数
# 
# 
# 计算总分列的众数

# In[9]:


df.总分.mode()


# ### 统计信息｜部分
# 
# 计算 总分、高端人才得分、办学层次得分的最大最小值、中位数、均值

# In[10]:


df.agg({
        "总分": ["min", "max", "median", "mean"],
        "高端人才得分": ["min", "max", "median", "mean"],
        "办学层次得分":["min", "max", "median", "mean"]})


# ### 统计信息｜完整
# 
# 查看数值型数据的统计信息（均值、分位数等），并保留两位小数

# In[11]:


df.describe().round(2).T


# ###  统计信息｜分组
# 
# 计算各省市总分均值

# In[12]:


df.groupby("省市")['总分'].mean()


# ### 统计信息｜相关系数
# 
# 
# 也就是相关系数矩阵，也就是每两列之间的相关性系数

# In[13]:


df.corr() 


# ###  相关系数｜热力图
# 
# 
# 将上一题的相关性系数矩阵制作为热力图

# In[14]:


### 方法一

df.corr().style.background_gradient(cmap='coolwarm').set_precision(2)

### 方法二

#借助 `matplotlib` 和 `seaborn` 

#其中中文设置可以参考[我的这篇文章](https://mp.weixin.qq.com/s/WKOGvQP-6QUAP00ZXjhweg)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (9,6),dpi=100)
sns.set(font='Songti SC')
sns.heatmap(df.corr().round(2),annot=True,cmap='RdBu')
plt.show()


# ### 统计信息｜频率
# 
# 计算各省市出现的次数

# In[15]:


df.省市.value_counts()


# ### 统计信息｜热力地图
# 
# 结合 `pyecharts` 将各省市高校上榜数量进行地图可视化

# In[16]:


from pyecharts import options as opts
from pyecharts.charts import Map
list1 = list(pd.DataFrame(df.省市.value_counts()).index)
list2 = list(pd.DataFrame(df.省市.value_counts()).省市)


c = (
    Map()
    .add('', [list(z) for z in zip(list1,list2)], "china",is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="排名前100高校各省市占比"),
        visualmap_opts=opts.VisualMapOpts(max_=20),
       

    )
)
c.render_notebook()


# ### 统计信息｜直方图
# 
# 绘制总分的直方图、密度估计图

# In[17]:


import seaborn as sns
plt.figure(figsize = (9,6),dpi=100)
sns.set(font='Songti SC')
sns.distplot(df['总分'])
plt.show()


# In[ ]:




