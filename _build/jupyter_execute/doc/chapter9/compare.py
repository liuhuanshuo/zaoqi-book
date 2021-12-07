#!/usr/bin/env python
# coding: utf-8

# # compare - 数据比较
# 
# 
# `compare` 用于比较两个数据框之间的差异，[👉官方文档](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html)
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 默认比较
# 
# 输出 df9 和 df10 的差异

# In[1]:


import pandas as pd
import numpy as np
df9 = pd.DataFrame(
    {
        "col1": ["a", "a", "b", "b", "a"],
        "col2": [1.0, 2.0, 3.0, np.nan, 5.0],
        "col3": [1.0, 2.0, 3.0, 4.0, 5.0]
    },
    columns=["col1", "col2", "col3"],
)


df10 = df9.copy()
df10.loc[0, 'col1'] = 'c'
df10.loc[2, 'col3'] = 4.0


# In[2]:


df9.compare(df10)


# ## 保留数据框
# 
# 在上一题的要求下，保留原数据框

# In[3]:


df9.compare(df10, keep_shape=True)


# ## 保留值
# 
# 在上一题的基础上，再保留原始相同的值

# In[4]:


df9.compare(df10, keep_shape=True, keep_equal=True)

