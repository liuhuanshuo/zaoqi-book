#!/usr/bin/env python
# coding: utf-8

# # merge - 数据连接
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
# 
# `merge`  是 `pandas` 中 `SQL` 风格的合并方法，虽然它有多个参数，但大多情况下我们只需要了解如何使用 `how（LEFT、RIGHT、OUTER、INNER）` 参数，下面是图解
# 
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112222202212.png
# :width: 100%
# :align: center
# ```

# In[ ]:





# ## 按单键连接
# 
# 根据 `key` 连接 `left` 和 `right`
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key.png)

# In[1]:


import pandas as pd
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


# In[2]:


pd.merge(left, right, on='key')


# ## 按多键连接
# 
# 根据 `key1` 和 `key2` 连接 `left` 和 `right`
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key_multiple.png)

# In[3]:


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


# In[4]:


pd.merge(left, right, on=['key1', 'key2'])


# ## 左外连接
# 
# 
# 如下图所示的结果连接 left 和 right，保留左表全部键
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key_left.png)

# In[5]:


pd.merge(left, right, how='left', on=['key1', 'key2'])


# ## 右外连接
# 
# 
# 如下图所示的结果连接 left 和 right，保留右表全部键
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key_right.png)

# In[6]:


pd.merge(left, right, how='right', on=['key1', 'key2'])


# ## 全外连接
# 
# 
# 如下图所示的结果连接 left 和 right，保留全部键
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key_outer.png)

# In[7]:


pd.merge(left, right, how='outer', on=['key1', 'key2'])


# ## 内连接
# 
# 
# 如下图所示的结果连接 left 和 right，保留交集
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_on_key_inner.png)

# In[8]:


pd.merge(left, right, how='inner', on=['key1', 'key2'])


# ## 重复索引
# 
# 
# 按下图所示进行连接
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_merge_overlapped_suffix.png)

# In[9]:


left = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'v': [1, 2, 3]})
right = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'v': [4, 5, 6]})


# In[10]:


pd.merge(left, right, on='k', suffixes=['_l', '_r'])

