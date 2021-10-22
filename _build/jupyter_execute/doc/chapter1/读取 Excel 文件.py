#!/usr/bin/env python
# coding: utf-8

# # 读取 Excel 文件

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 默认读取
# 
# 
# 默认读取是最简单的方式，使用 `pd.read_csv('xxxx.csv')` 即可读取对应文件
# 
# 现在尝试使用 `pandas` 读取当前目录下 `某招聘网站数据.csv`
# 

# In[1]:


import pandas as pd
data = pd.read_csv("某招聘网站数据.csv")


# ```{admonition} 注意
# :class: Attention
# 
# 使用 `pandas` 读取 `CSV` 与读取 `xlsx` 格式的 `Excel` 文件方法大致相同
# 
# 因此下面与 `Excel` 相关的读取操作均以 `CSV` 格式进行介绍
# 
# ```

# ## 指定行读取（顺序）
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 **前20行**

# In[2]:


data = pd.read_csv("某招聘网站数据.csv",nrows = 20)


# ## 指定行读取（跳过）
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件并 **跳过前20行**

# In[3]:


data = pd.read_csv("某招聘网站数据.csv",skiprows = [i for i in range(1,21)])


# ## 指定行读取（条件）
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件中全部**偶数行**

# In[4]:


data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: (x != 0) and not x % 2)


# ```{admonition} 思考
# :class: hint
# 
# 如果是读取全部奇数行，或者更多满足指定条件的行呢？
# ```

# In[5]:


data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: x % 2) #读取奇数行


# ## 指定列号读取
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的第 `1、3、5` 列

# In[6]:


data = pd.read_csv("某招聘网站数据.csv",usecols = [0,2,4])


# ##  指定列名读取
# 
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 `positionId、positionName、salary` 列

# In[7]:


data = pd.read_csv("某招聘网站数据.csv",usecols = ['positionId','positionName','salary'])


# ## 指定列匹配读取
# 
# 
# 让我们来个更难一点的，还是读取 `某招聘网站数据.csv` 文件，但现在有一个 list 中包含多个字段👇
# 
# `usecols = ['positionId','test','positionName', 'test1','salary']`
# 
# 如果 `usecols` 中的列名存在于 `某招聘网站数据.csv` 中，则读取。

# In[8]:


usecols = ['positionId', 'test', 'positionName', 'test1', 'salary']

data = pd.read_csv('某招聘网站数据.csv', usecols=lambda c: c in set(usecols))

