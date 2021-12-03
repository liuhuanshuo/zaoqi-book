#!/usr/bin/env python
# coding: utf-8

# # 缺失值检查与处理

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


# ## 缺失值检查

# ### 检查全部缺失值

# In[2]:


df.isna().sum().sum()


# ### 检查每列缺失值
# 
# 再看看具体每列有多少缺失值

# In[3]:


df.isnull().sum()


# ### 定位缺失值
# 
# 
# 为了后面更方便的处理缺失值，现在先看看全部缺失值所在的行

# In[4]:


df[df.isnull().T.any() == True]


# ### 高亮缺失值

# 很明显，虽然上一题找到了全部缺失值所在的行，但是看的很头疼
# 
# 我们可以将缺失值进行高亮进一步查看

# In[5]:


(df[df.isnull().T.any() == True]
.style
.highlight_null(null_color='skyblue')
.set_table_attributes('style="font-size: 10px"'))


# ## 缺失值处理

# In[6]:


import pandas as pd
df = pd.read_excel("TOP250.xlsx")


# ### 删除缺失值
# 
# 
# 处理缺失值最简单的方式，当然是将缺失值出现的行全部删掉～
# 
# -> 现在，将缺失值出现的行全部删掉

# In[7]:


df = df.dropna()


# ### 整体填充补全
# 
# 
# 除了删除缺失值最省事之外，将全部缺失值替换为一个 **固定的值/文本** 也是一个较为省事的方法'
# 
# -> 现在，将全部缺失值替换为 `*`

# In[8]:


df = df.fillna('*') 


# ### 向上填充补全
# 
# 
# 从上一小节的查看数据中，不难发现整理数据是按照评分进行降序排列的
# 
# 因此对于评分列的缺失值处理，我们可以用上一个电影的评分进行填充
# 
# -> 现在将评分列的缺失值，替换为上一个电影的评分

# In[9]:


df['评分'] = df['评分'].fillna(axis=0,method='ffill')


# ###  整体均值填充补全
# 
# 
# 对于评价人数列的缺失值处理，我们可以使用整列的均值进行填充
# 
# -> 现在，将评价人数列的缺失值，用整列的均值进行填充

# In[10]:


df['评价人数'] = df['评价人数'].fillna(df['评价人数'].mean())


# ### 上下均值填充补全
# 
# 
# 除了可以使用整列的均值进行填充，也可以使用缺失值位置的上下均值进行填充、
# 
# -> 现在，将评价人数列的缺失值，用上下数字的均值进行填充

# In[11]:


df['评价人数'] = df['评价人数'].fillna(df['评价人数'].interpolate())


# ### 匹配填充补全
# 
# 
# 除了利用均值填充，有时还需要根据另一列的值进行匹配填充
# 
# -> 现在填充 “语言” 列的缺失值，要求根据 “国家/地区” 列的值进行填充
# 
# > 例如 《海上钢琴师》国家/地区为 意大利，根据其他意大利国家对应的语言来看，应填充为 意大利语

# In[12]:


df['语言']=df.groupby('国家/地区').语言.bfill()


# ```{admonition} 思考
# :class: hint
# 
# 还有其他方法可以实现吗？
# ```
