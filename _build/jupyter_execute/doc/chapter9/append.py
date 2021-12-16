#!/usr/bin/env python
# coding: utf-8

# # append - 数据添加
# 
# 在很多教程，包括 [pandas 官方文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#appending-rows-to-a-dataframe)中，都将 `append` 结合 `merge、concat、join` 一起讲解
# 
# 但是对我来说，虽然append得到的结果也类似合并，可它常常出现的地方就是它的字面意思 -> 添加（追加），下面是几个 append 的常用操作。
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 末尾追加
# 
# 将 s2 添加至 df8 的末尾
# 
# ![](https://pandas.pydata.org/pandas-docs/stable/_images/merging_append_series_as_row.png)

# In[1]:


import pandas as pd
df8 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

s2 = pd.Series(["X0", "X1", "X2", "X3"], index=["A", "B", "C", "D"])
s3 = pd.DataFrame({"A": ['s1'],"B": ['s2'],"C": ['s3'],"D": ['s4']})
dicts = [{"A": 1, "B": 2, "C": 3, "X": 4}, {"A": 5, "B": 6, "C": 7, "Y": 8}]


# In[2]:


result = df8.append(s2, ignore_index=True)
result


# ## 指定位置追加
# 
# 将 s3 添加至 df8 的第三行

# In[3]:


df9 = df8.iloc[:2, :]
df10 = df8.iloc[2:, :]

pd.concat([df9, s3, df10])


# ## 添加字典
# 
# 将下面的字典 dicts 插入添加至 df8，并保留索引，如下图所示
# 
# ![](https://pandas.pydata.org/pandas-docs/stable/_images/merging_append_dits.png)

# In[4]:


result = df8.append(dicts, ignore_index=True, sort=False)
result

