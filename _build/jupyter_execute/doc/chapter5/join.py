#!/usr/bin/env python
# coding: utf-8

# # join - 数据组合
# 
# `DataFrame.join`是一种将两个可能具有不同索引的 `DataFrame` 的列组合成单个 `DataFrame` 的便捷方法。
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

# ## 默认方法
# 
# 组合 left 和 right，并按照 left 的索引进行对齐

# In[1]:


import pandas as pd
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])


right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])


# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_join.png)

# In[2]:


left.join(right)


# ## 取并集
# 
# 按下图所示进行组合
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_join_outer.png)

# In[3]:


left.join(right, how='outer')


# ## 取交集
# 
# 按下图所示进行组合
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_join_inner.png)

# In[4]:


left.join(right, how='inner')


# ```{admonition} 思考
# :class: hint
# 
# 用 `merge` 如何实现？
# ```

# In[5]:


pd.merge(left, right, left_index=True, right_index=True, how='inner')


# ## 按索引组合
# 
# 重新产生数据并按下图所示进行连接（根据 `key`）
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_join_key_columns.png)
# 

# In[6]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key': ['K0', 'K1', 'K0', 'K1']})


right = pd.DataFrame({'C': ['C0', 'C1'],
                      'D': ['D0', 'D1']},
                      index=['K0', 'K1'])


# In[7]:


left.join(right, on='key')


# ## 多索引组合
# 
# 按下图所示进行连接（根据 `key1` 和 `key2`）
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_join_multikeys.png)
# 

# In[8]:


left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1']})


index = pd.MultiIndex.from_tuples([('K0', 'K0'), ('K1', 'K0'),
                                  ('K2', 'K0'), ('K2', 'K1')])


right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                   'D': ['D0', 'D1', 'D2', 'D3']},
                  index=index)


# In[9]:


left.join(right, on=['key1', 'key2'])


# In[ ]:




