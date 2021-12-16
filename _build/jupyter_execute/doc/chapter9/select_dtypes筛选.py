#!/usr/bin/env python
# coding: utf-8

# # select_dtypes - 筛选
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# 

# ## 单类型
# 
# `select_dtypes`  可以筛选制定数据类型的列，例如，筛选 df4 数据类型为整数的列

# In[2]:


import pandas as pd
df4 = pd.DataFrame({'a': [1, 2] * 3,
                   'b': [True, False] * 3,
                   'c': [1.0, 2.0] * 3})

df4


# In[3]:


df4.select_dtypes(include=['int64'])


# ## 多类型
# 
# 筛选 df4 数据类型为和浮点数的列

# In[4]:


df4.select_dtypes(include=['int','float64'])


# ## 逆筛选
# 
# 筛选 df4 数据类型为布尔值的列

# In[5]:


df4.select_dtypes(exclude=['int','float64'])

