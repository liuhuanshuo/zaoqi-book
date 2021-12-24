#!/usr/bin/env python
# coding: utf-8

# # join - 横向连接
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
# 
# 
# `join` 本质上和 [merge](merge.ipynb) 类似，或者说是 `merge` 的特殊情况，所以也是一种 `SQL` 风格的合并方法。
# 
# 但和 `merge` 不一样的地方在于，`join` **只能按照行索引去合并数据，因此我翻译成 「横向连接」**。
# 
# 有关 `join` 的基本用法可以通过下图大致了解，至于 `how` 参数中的 `inner、outer` 可以参考 [merge](merge.ipynb) 中的图解。
# 
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112242051282.png
# :width: 100%
# :align: center
# ```
# 
# 需要注意的是 `df2` 与 `df3` 的连接，如果有重复的列名，需要指定合并后左右的列名后缀，否则会报错。
# 
# 下面是官方文档中的案例，你可以修改相关代码来验证自己的想法！

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




