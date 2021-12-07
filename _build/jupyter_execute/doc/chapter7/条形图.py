#!/usr/bin/env python
# coding: utf-8

# # 条形图
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


# ## 垂直
# 
# 重新生成数据，并对使用条形图可视化 df2 的第 3 行

# In[2]:


df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])


# In[3]:


df2.iloc[2].plot(kind = 'bar', figsize=(10, 6))
plt.show()


# ## 水平
# 
# 绘制 df2 第 3 行的条形图，并设置为水平

# In[4]:


df2.iloc[2].plot(kind = 'barh', figsize=(10, 6))
plt.show()


# ## 多行
# 
# 将df2的全部行在同一个画布上制作条形图

# In[5]:


df2.plot(kind = 'bar', figsize=(10, 6))
plt.show()


# ## 堆叠
# 
# 在上一题的基础上，对条形图进行堆叠

# In[6]:


df2.plot(kind = 'bar', figsize=(10, 6),stacked=True)
plt.show()

