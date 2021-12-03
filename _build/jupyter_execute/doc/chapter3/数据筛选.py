#!/usr/bin/env python
# coding: utf-8

# # 数据筛选

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

df = pd.read_csv("东京奥运会奖牌数据.csv")

df.rename(columns={'Unnamed: 2':'金牌数',
                  'Unnamed: 3':'银牌数',
                  'Unnamed: 4':'铜牌数'},inplace=True)


# ## 筛选列

# 
# ### 通过列号
# 
# 提取第 1、2、3、4 列

# In[2]:


df.iloc[:,[0,1,2,3]]


# ### 通过列名
# 
# 提取 `金牌数、银牌数、铜牌数` 三列

# In[3]:


df[['金牌数','银牌数','铜牌数']]


# ### 条件（列号）
# 
# 筛选全部 **奇数列**

# In[4]:


df.iloc[:,[i%2==1 for i in range(len(df.columns))]]


# ### 条件（列名）
# 
# 提取全部列名中包含 数 的列

# In[5]:


df.loc[:, df.columns.str.endswith('数')]


# ### 组合（行号+列名）
# 
# 提取倒数后三列的10-20行

# In[6]:


df.loc[10:20, '总分':] 


# ## 筛选行

# ### 通过行号
# 
# 提取第 10 行

# In[7]:


df.loc[9:9]


# ### 通过行号（多行）
# 
# 提取第 10 行之后的全部行

# In[8]:


df.loc[9:]


# ### 固定间隔
# 
# 提取 0-50 行，间隔为 3

# In[9]:


df[:50:3]


# ### 判断（大于）
# 
# 提取 金牌数 大于 30 的行

# In[10]:


df[df['金牌数'] > 30]


# ### 判断（等于）
# 
# 提取 `金牌数` 等于 10 的行

# In[11]:


df.loc[df['金牌数'] == 10]


# ### 判断（不等于）
# 
# 提取 `金牌数` 不等于 `10` 的行

# In[12]:


df.loc[~(df['金牌数'] == 10)]


# ### 条件（指定行号）
# 
# 提取全部 **奇数行**
# 

# In[13]:


df[[i%2==1 for i in range(len(df.index))]]


# ### 条件（指定值）
# 
# 
# 提取 中国、美国、英国、日本、巴西五行数据

# In[14]:


df.loc[df['国家奥委会'].isin(['中国','美国','英国','日本','巴西'])]


# ### 多条件
# 
# 在上一题的条件下，新增一个条件：**金牌数小于30**

# In[15]:


df.loc[(df['金牌数'] < 30) & (df['国家奥委会'].isin(['中国','美国','英国','日本','巴西']))]


# ### 条件（包含指定值）
# 
# 提取 国家奥委会 列中，所有包含 `国`的行

# In[16]:


df[df.国家奥委会.str.contains('国')]


# ## 组合筛选

# ### 筛选某行某列
# 
# 提取 `第 0 行第 2 列`

# In[17]:


df.iloc[0:1,[1]]


# ### 筛选多行多列
# 
# 
# 提取 第 0-2 行第 0-2 列
# 

# In[18]:


df.iloc[0:2,[0,1]]


# ### 组合（行号+列号）
# 
# 提取第 4 行，第 4 列的值

# In[19]:


df.iloc[3,3]


# ### 组合（行号+列名）
# 
# 提取行索引为 4 ，列名为 金牌数 的值
# 

# In[20]:


df.at[4,'金牌数']


# ### 条件
# 
# 提取 国家奥委会 为 中国 的金牌数

# In[21]:


df.loc[df['国家奥委会'] == '中国'].loc[1].at['金牌数']


# ### query
# 
# 使用 query 提取 金牌数 + 银牌数 大于 15 的国家

# In[22]:


df.query('金牌数+银牌数 > 15')


# ###  query（引用变量）
# 
# 使用 query 提取 金牌数 大于 金牌均值的国家

# In[23]:


gold_mean = df['金牌数'].mean()
df.query(f'金牌数 > {gold_mean}')

