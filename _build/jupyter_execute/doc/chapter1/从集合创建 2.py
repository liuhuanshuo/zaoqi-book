#!/usr/bin/env python
# coding: utf-8

# # 从集合创建 DataFrame

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 常规方法
# 
# 
# 将下面的元组转换为 dataframe 且行列索引均为 `1,2,3,4`

# In[1]:


import pandas as pd


# In[2]:


t =((1,0,0,0,),(2,3,0,0,),(4,5,6,0,),(7,8,9,10,))


# In[3]:


pd.DataFrame(t, columns=[1,2,3,4], index=[1,2,3,4])

