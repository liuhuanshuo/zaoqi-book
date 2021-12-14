#!/usr/bin/env python
# coding: utf-8

# # 直方图
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


# ## 默认
# 
# 重新生成数据 df3 ，并制作直方图

# In[2]:


df3 = pd.DataFrame(
    {
        "a": np.random.randn(1000) + 1,
        "b": np.random.randn(1000),
        "c": np.random.randn(1000) - 1,
    },
    columns=["a", "b", "c"],
)


# In[3]:


df3.plot(kind = 'hist', figsize=(10, 6))
plt.show()


# ## 修改透明度
# 
# 在上一题的基础上，设置透明度为 0,5

# In[4]:


df3.plot(kind = 'hist', figsize=(10, 6),alpha = 0.5)
plt.show()


# ## 修改小区间
# 
# 在上一题的基础上，堆叠直方图，并设置小区间为20个

# In[5]:


df3.plot(kind = 'hist', figsize=(10, 6),alpha = 0.5,bins = 20,stacked=True)
plt.show()


# ## 拆分子图
# 在上一题的基础上，将3个直方图拆分为3个子图

# In[6]:


df3.diff().hist(alpha=0.5, bins=20, figsize=(10, 6))
plt.show()

