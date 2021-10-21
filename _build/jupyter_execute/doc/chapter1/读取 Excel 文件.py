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
# :class: warning
# 
# 使用 `pandas` 读取 `CSV` 与读取 `xlsx` 格式的 `Excel` 文件方法大致相同
# 
# 因此下面与 `Excel` 相关的读取操作均以 `CSV` 格式进行介绍
# 
# ```

# ## 指定行读取（顺序）
# <br>
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件的 <font color = '#5F5FFC'>前20行</font>

# In[2]:


data = pd.read_csv("某招聘网站数据.csv",nrows = 20)


# ## 指定行读取（跳过）
# <br>
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件并<font color = '#5F5FFC'>跳过前20行</font>

# In[3]:


data = pd.read_csv("某招聘网站数据.csv",skiprows = [i for i in range(1,21)])


# ## 指定行读取（条件）
# <br>
# 
# 读取当前目录下 `某招聘网站数据.csv` 文件中全部<font color = '#5F5FFC'>偶数行</font>
# 
# 思考：如果是读取全部奇数行，或者更多满足指定条件的行呢？

# In[4]:


data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: (x != 0) and not x % 2)

# data = pd.read_csv('某招聘网站数据.csv', skiprows=lambda x: x % 2) 奇数行

