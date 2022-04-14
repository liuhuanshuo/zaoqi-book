#!/usr/bin/env python
# coding: utf-8

# # 散点图
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 导入与预设
# 
# 虽然在 `pandas` 中可以直接调用 `matplotliab` 进行可视化，但是依旧需要进行相关设置，例如字体、精度等。

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus']=False


# ## 默认方法
# 
# 重新生成数据 df4 ，并制作散点图，X轴为 a，Y轴为 b

# In[2]:


df4 = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])

df4["species"] = pd.Categorical(
    ["setosa"] * 20 + ["versicolor"] * 20 + ["virginica"] * 10
)


# In[3]:


df4.plot.scatter(x="a", y="b", figsize=(8, 6))
plt.show()


# ## 修改散点大小
# 
# 在上一题的基础上，让散点的大小随着值变化

# In[4]:


df4.plot.scatter(x="a", y="b", figsize=(8, 6), s=df4["c"] * 200)
plt.show()


# ## 进一步优化
# 
# 在上一题的基础上，进行如下设置
# 
# - 散点固定
# - 调低透明度
# - 增加黑色边缘线

# In[5]:


df4.plot.scatter(x="a", y="b", figsize=(8, 6), marker='o',
                 s=100, linewidths=1, alpha=0.8, edgecolors='black')
plt.show()


# ## 颜色渐变
# 
# 在上一题的基础上，将散点的颜色设置为渐变色

# In[6]:


df4.plot.scatter(x="a", y="b",c="c", figsize=(8, 6), marker='o',
                 s=100, linewidths=1, alpha=0.8, edgecolors='black')

plt.show()


# ## 分组绘制
# 
# 将 ab 分为一组，cd分为一组，制作三散点图

# In[7]:


ax = df4.plot.scatter(x="a", y="b", color="DarkBlue", label="Group 1", figsize=(8, 6), marker='o',
                 s=80, linewidths=1, alpha=0.8, edgecolors='black')

df4.plot.scatter(x="c", y="d", color="DarkGreen", label="Group 2", ax=ax, figsize=(8, 6), marker='o',
                 s=80, linewidths=1, alpha=0.8, edgecolors='black');

