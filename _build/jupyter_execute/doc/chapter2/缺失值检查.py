#!/usr/bin/env python
# coding: utf-8

# # 缺失值检查

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
pd.set_option('display.max_colwidth',10)


# ## 检查全部缺失值

# In[2]:


df.isna().sum().sum()


# ## 检查每列缺失值
# 
# 再看看具体每列有多少缺失值

# In[3]:


df.isnull().sum()


# ## 定位缺失值
# 
# 
# 为了后面更方便的处理缺失值，现在先看看全部缺失值所在的行

# In[4]:


df[df.isnull().T.any() == True]


# ## 高亮缺失值

# 很明显，虽然上一题找到了全部缺失值所在的行，但是看的很头疼
# 
# 我们可以将缺失值进行高亮进一步查看

# In[5]:


(df[df.isnull().T.any() == True]
.style
.highlight_null(null_color='skyblue')
.set_table_attributes('style="font-size: 10px"'))


# In[ ]:




