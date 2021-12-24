#!/usr/bin/env python
# coding: utf-8

# # concat - 数据拼接
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
# `concat` 我翻译成数据拼接，需要和 [merge](merge.ipynb) 进行区分，在进行 concat 时一个重要的参数就是 axis ，下图是一个简单的例子
# ```{figure} https://pic.liuzaoqi.com/picgo/202112232236228.png
# :width: 100%
# :align: center
# ```
# 
# 下面是官方文档中的案例，你可以修改相关代码来验证自己的想法！

# ## 本页数据说明
# 
# 在学习本页面操作时，应先了解大致数据结构如下
# 
# ![](https://liuzaoqi.oss-cn-beijing.aliyuncs.com/picgo/202112052026569.png)

# In[1]:


import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])


df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                    'D': ['D2', 'D3', 'D6', 'D7'],
                    'F': ['F2', 'F3', 'F6', 'F7']},
                   index=[2, 3, 6, 7])


# ## 默认拼接
# 
# 垂直拼接 `df1、df2、df3`，效果如下图所示
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_basic.png)

# In[2]:


pd.concat([df1, df2, df3])


# ## 重置索引
# 
# 垂直拼接 df1 和 df4，并按顺序重新生成索引，
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_ignore_index.png)

# In[3]:


pd.concat([df1, df4], ignore_index=True)


# ## 横向拼接
# 
# 横向拼接 `df1、df4`，效果如下图所示
# 
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_axis1.png)

# In[4]:


pd.concat([df1,df4],axis=1)


# ## 横向拼接（取交集）
# 
# 在上一题的基础上，只取结果的交集
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_axis1_inner.png)

# In[5]:


pd.concat([df1,df4],axis=1,join='inner')


# ## 横向拼接（取指定）
# 
# 在 14 题基础上，只取包含 df1 索引的部分
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_axis1_join_axes.png)

# In[6]:


pd.concat([df1, df4], axis=1).reindex(df1.index)


# ## 新增索引
# 
# 拼接 `df1、df2、df3`，同时新增一个索引（`x、y、z`）来区分不同的表数据来源
# 
# ![](https://pandas.pydata.org/pandas-docs/version/0.20/_images/merging_concat_keys.png)

# In[7]:


pd.concat([df1, df2, df3], keys=['x', 'y', 'z'])


# In[ ]:




