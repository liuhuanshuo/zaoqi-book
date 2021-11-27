#!/usr/bin/env python
# coding: utf-8

# # 从列表创建 DataFrame

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
# 将下面的 `list` 转换为 `dataframe`，并指定列名为`"早起Python"`

# In[1]:


import pandas as pd


# In[2]:


l = [1,2,3,4,5]


# In[3]:


pd.DataFrame(l,columns=['早起Python'])


# ## 嵌套列表转换
# 
# 
# 将下面的 `list` 转换为 `dataframe`，并指定行索引为`"公众号","早起Python"`

# In[4]:


l = [[1,2,3],[4,5,6]]


# In[5]:


pd.DataFrame(l,index=['公众号','早起Python'])

