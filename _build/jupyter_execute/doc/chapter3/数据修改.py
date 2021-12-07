#!/usr/bin/env python
# coding: utf-8

# # 数据修改

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 本页数据说明
# 
# 为了更好的介绍相关操作，本页面使用 **东京奥运会奖牌数据** 数据进行展开，你应该对数据**字段、数值、类型**等相关信息做一个大致了解！

# In[1]:


import pandas as pd

df = pd.read_csv("东京奥运会奖牌数据.csv")

df.head()


# ## 数据修改
# 
# 

# ### 修改列名
# 
# 
# 将原 `df` 列名 `Unnamed: 2`、`Unnamed: 3`、`Unnamed: 4` 修改为 `金牌数`、`银牌数`、`铜牌数`

# In[2]:


df.rename(columns={'Unnamed: 2':'金牌数',
                  'Unnamed: 3':'银牌数',
                  'Unnamed: 4':'铜牌数'},inplace=True) 


# ### 修改行索引
# 
# 
# 将第一列（排名）设置为索引

# In[3]:


df.set_index("排名",inplace=True)


# ### 修改索引名
# 
# 修改索引名为 金牌排名

# In[4]:


df.rename_axis("金牌排名",inplace=True)


# ### 修改值
# 
# 将 ROC（第一列第五行）修改为 俄奥委会

# In[5]:


df.iloc[4,0] = '俄奥委会'


# ### 替换值（单值）
# 
# 将金牌数列的数字 `0` 替换为 `无`

# In[6]:


df['金牌数'].replace(0,'无',inplace=True)


# ### 替换值（多值）
# 
# 

# 同时替换
# 
# - 将 `无` 替换为 缺失值
# - 将 0 替换为 `None`
# 
# 注意：缺失值的 Nan 该怎么生成？

# In[7]:


import numpy as np
df.replace(['无',0],[np.nan,'None'],inplace = True)


# ### 修改类型
# 
# 将 `金牌数` 列类型修改为 `int`

# In[8]:


df['金牌数'] = df['金牌数'].fillna('0').astype(int)


# ## 数据增加

# ### 新增列（固定值）
# 
# **新增一列** 比赛地点，值为 `东京`
# 

# In[9]:


df['比赛地点'] = '东京'


# ### 新增列（计算值）
# 
# 
# **新增一列** 金银牌总数列，值为该国家金银牌总数

# In[10]:


df = df.replace('None',0)
df['金银牌总数']  = df['金牌数']  + df['银牌数']


# ### 新增列（比较值）
# 
# 新增一列 最多奖牌数量 列，值为该过金银牌数量种最多的一个奖牌数量
# 
# 例如美国银牌最多，则为41，中国为38

# In[11]:


df['最多奖牌数量'] = df.bfill(1)[["金牌数", "银牌数",'铜牌数']].max(1)


# ### 新增列（判断值）
# 
# 新增一列 金牌大于30
# 
# 如果一个国家的金牌数大于 30 则值为 是，反之为 否

# In[12]:


df['金牌大于30']  = np.where(df['金牌数'] > 30, '是', '否')


# ### 增加多列
# 
# 新增两列，分别是
# 
# - 金铜牌总数（金牌数+铜牌数）
# - 银铜牌总数（银牌数+铜牌数）

# In[13]:


df = df.assign(金铜牌总数=df.金牌数 + df.铜牌数,
         银铜牌总数=df.银牌数+df.铜牌数) 


# ### 新增列（引用变量）
# 
# 新增一列金牌占比，为各国金牌数除以总金牌数（gold_sum）

# In[14]:


gold_sum = df['金牌数'].sum()
df.eval(f'金牌占比 = 金牌数 / {gold_sum}',inplace=True)


# ### 新增行（末尾追加）
# 
# 
# 在 df 末尾追加一行，内容为 0,1,2,3... 一直到 `df` 的列长度

# In[15]:


df1 = pd.DataFrame([[i for i in range(len(df.columns))]], columns=df.columns)
df_new = df.append(df1)


# ### 新增行（指定位置）
# 
# 在第 2 行新增一行数据，即美国和中国之间。
# 
# 数据内容同上一题

# In[16]:


df1 = df.iloc[:1, :]
df2 = df.iloc[1:, :]
df3 = pd.DataFrame([[i for i in range(len(df.columns))]], columns=df.columns)
df_new = pd.concat([df1, df3, df2], ignore_index=True)


# ## 数据删除

# ### 删除指定行
# 
# 删除 `df` 第一行

# In[17]:


df.drop(1)


# ### 删除条件行

# In[18]:


df.drop(df[df.金牌数<20].index)


# ### 删除列
# 
# 
# 删除刚刚新增的 比赛地点 列

# In[19]:


df.drop(columns=['比赛地点'],inplace=True)


# ### 删除列（按列号）
# 
# 删除 `df` 的 `7、8、9、10` 列

# In[20]:


df.drop(df.columns[[7,8,9,10]], axis=1,inplace=True)

