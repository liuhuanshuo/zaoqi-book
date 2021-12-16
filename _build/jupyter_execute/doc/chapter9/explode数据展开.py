#!/usr/bin/env python
# coding: utf-8

# # explode - 数据展开
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 单列展开
# 
# 有时我们的数据中会包含列表，此时便可使用  `explode` 进行展开，将一个list拆成多行。
# 
# 例如，将 df5 第 A 列进行展开

# In[1]:


import pandas as pd
import numpy as np
df5 = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                   'B': 1,
                   'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
df5


# In[2]:


df5.explode('A')


# ## 多列展开
# 
# 将 df5 第 A、C 列进行展开

# In[3]:


# pandas版本 >= 1.3 才可以完成
# df5.explode(list('AC')) 

