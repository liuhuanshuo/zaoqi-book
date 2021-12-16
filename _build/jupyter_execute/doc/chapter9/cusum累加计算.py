#!/usr/bin/env python
# coding: utf-8

# # cumsum - 累加计算
# 
# cumsum 可以对数据按照指定方式进行累加，[👉官方文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 按列累加
# 
# 将 df7 按列进行累加

# In[2]:


import pandas as pd
import numpy as np
df7 = pd.DataFrame(np.arange(1,37).reshape([9,4]), columns=["A", "B","C","D"])
df7['item'] = ['Apple','Xiaomi','Huawei'] * 3
df7


# In[3]:


df7[list('ABCD')].cumsum()


# ## 按行累加
# 
# 将 df7 按行进行累加

# In[4]:


df7[list('ABCD')].cumsum(axis = 1)


# ## 分组累加
# 
# 将 df7 按照 `item` 按不同组对第 A 列进行累加

# In[7]:


df7 = df7.sort_values(['item']).reset_index(drop=True)
df7['cusum']=df7.groupby('item')['A'].cumsum(axis=0)
df7

