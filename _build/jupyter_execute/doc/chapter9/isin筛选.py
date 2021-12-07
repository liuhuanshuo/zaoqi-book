#!/usr/bin/env python
# coding: utf-8

# # isin - 筛选
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
# 
# 在 `pandas` 中有没有类似 `SQL` 中 `IN` 和 `NOTIN` 的筛选方法？
# 
# `isin` 就可以实现，通过 `isin` 可以快速筛选出包含某个值的结果

# ## 根据列表筛选
# 
# 筛选出 `country` 包含 `'China','UK'` 的行

# In[2]:


import pandas as pd
df3 = pd.DataFrame({'country': ['China','US', 'UK', 'Germany', 'Japan'],
             'rank':[1,2,3,4,5]})

df3


# In[4]:


df3[df3.country.isin(['China','UK'])]


# ## 逆筛选
# 
# 对上一题的结果取逆

# In[5]:


df3[~df3.country.isin(['China','UK'])]

