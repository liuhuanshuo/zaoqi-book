#!/usr/bin/env python
# coding: utf-8

# # 从字典创建 DataFrame

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 常规方法

# 执行下方代码，并将字典转换为`dataframe`

# In[1]:


import pandas as pd


# In[2]:


d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]) }


# In[3]:


pd.DataFrame(d)


# ## 指定索引
# 
# <br>
# 
# 还是上一题的字典`d`，将其转换为`dataframe`并指定索引顺序为 `d、b、a`

# In[4]:


pd.DataFrame(d, index=["d", "b", "a"])


# ## 指定列名
# 
# <br>
# 
# 还是上一题的字典`d`，将其转换为`dataframe`并指定索引顺序为 `d、b、a`，列名为`"two", "three"`

# In[5]:


pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])


# ## 字典列表
# <br>
# 
# 将下方列表型字典转换为`dataframe`

# In[6]:


d = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]


# In[7]:


pd.DataFrame(d)


# ```{admonition} 思考
# :class: hint
# 
# 如何指定行/列索引？
# ```

# In[ ]:




