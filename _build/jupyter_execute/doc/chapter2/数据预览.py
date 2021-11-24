#!/usr/bin/env python
# coding: utf-8

# # 数据预览

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# In[1]:


import pandas as pd
df = pd.read_excel("TOP250.xlsx")


# ## 数据维度
# 
# 先看看数据多少行，多少列，对接下来的处理量心里有个数

# In[2]:


df.shape


# ## 数据抽样
# 
# 也就是随机查看一个样本，大致了解下数据

# In[3]:


df.sample()

# df.sample(n) #抽n个样本


# ## 查看数据前 3 行
# 
# 检查头尾数据，更详细的看一下数据

# In[4]:


df.head(3)
# df.tail() # 查看后5行


# ## 查看数据基本信息
# 
# 看看数据类型，有无缺失值什么的

# In[5]:


df.info()


# ## 查看数值数据统计信息
# 
# 查看 **数值型** 列的统计信息，计数、均值什么的

# In[6]:


df.describe().round(2).T


# ## 查看离散数据统计信息
# 
# 查看 **离散型** 列的统计信息，计数、频率什么

# In[7]:


df.describe(include=['O'])

