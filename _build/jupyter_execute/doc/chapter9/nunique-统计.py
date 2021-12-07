#!/usr/bin/env python
# coding: utf-8

# # nunique - 统计
# 
# 
# `nunique` 可以统计指定轴上不唯一的元素数量，[👉对应官方文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html)
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 按列统计

# In[1]:


import pandas as pd
df6 = pd.DataFrame({'A': [4, 5, 6], 'B': [4, 1, 1]})
df6


# In[2]:


df6.nunique()


# ## 按行统计

# In[3]:


df6.nunique(axis=1)

