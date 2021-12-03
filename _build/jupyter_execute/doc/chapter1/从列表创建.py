#!/usr/bin/env python
# coding: utf-8

# # 常见数据创建
# 
# 除了学会如何从静态文件中读取数据，有时我们需要直接将接口返回的数据转换为 pandas dataframe 或生成一小段数据用于测试，这时就需要知道如何创建数据。
# 
# 下面是通过常见的几种数据结构创建数据，你可以点击右侧目录进入对应内容。

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 从列表创建 DataFrame

# ### 常规方法
# 
# 
# 将下面的 `list` 转换为 `dataframe`，并指定列名为`"早起Python"`

# In[1]:


import pandas as pd


# In[2]:


l = [1,2,3,4,5]


# In[3]:


pd.DataFrame(l,columns=['早起Python'])


# ### 嵌套列表转换
# 
# 
# 将下面的 `list` 转换为 `dataframe`，并指定行索引为`"公众号","早起Python"`

# In[4]:


l = [[1,2,3],[4,5,6]]


# In[5]:


pd.DataFrame(l,index=['公众号','早起Python'])


# ## 从字典创建 DataFrame

# ### 常规方法

# 执行下方代码，并将字典转换为`dataframe`

# In[6]:


d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]) }


# In[7]:


pd.DataFrame(d)


# ### 指定索引
# 
# 还是上一题的字典`d`，将其转换为`dataframe`并指定索引顺序为 `d、b、a`

# In[8]:


pd.DataFrame(d, index=["d", "b", "a"])


# ### 指定列名
# 
# 还是上一题的字典`d`，将其转换为`dataframe`并指定索引顺序为 `d、b、a`，列名为`"two", "three"`

# In[9]:


pd.DataFrame(d, index=["d", "b", "a"], columns=["two", "three"])


# ### 字典列表
# 
# 将下方列表型字典转换为`dataframe`

# In[10]:


d = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]


# In[11]:


pd.DataFrame(d)


# ```{admonition} 思考
# :class: hint
# 
# 如何指定行/列索引？
# ```

# ## 从集合创建 DataFrame

# ### 常规方法
# 
# 
# 将下面的元组转换为 dataframe 且行列索引均为 `1,2,3,4`

# In[12]:


t =((1,0,0,0,),(2,3,0,0,),(4,5,6,0,),(7,8,9,10,))


# In[13]:


pd.DataFrame(t, columns=[1,2,3,4], index=[1,2,3,4])

