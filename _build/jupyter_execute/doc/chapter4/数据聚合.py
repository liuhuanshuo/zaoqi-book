#!/usr/bin/env python
# coding: utf-8

# # 数据聚合

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
# 为了更好的介绍相关操作，本页面使用 **某招聘网站数据.csv** 数据进行展开，你应该对数据**字段、数值、类型**等相关信息做一个大致了解！

# In[1]:


import pandas as pd
pd.set_option('display.max_colwidth',8)
df = pd.read_csv("某招聘网站数据.csv",parse_dates=['createTime'])
df.head()


# ## 聚合统计

# ### 计算指标
# 
# 分组计算不同行政区，薪水的最小值、最大值和平均值

# In[2]:


import numpy as np
df.groupby('district')['salary'].agg([min, max, np.mean])


# ### 修改列名
# 
# 将上一题的列名（包括索引名）修改为中文

# In[3]:


df.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=(
    'salary', 'max'), 平均工资=('salary', 'mean')).rename_axis(["行政区"])


# ### 组合计算
# 
# 对不同岗位(`positionName`)进行分组，并统计其薪水(`salary`)中位数和得分(`score`)均值

# In[4]:


df.groupby('positionName').agg({'salary': np.median, 'score': np.mean})


# ### 多层统计
# 
# 对不同行政区进行分组，并统计薪水的均值、中位数、方差，以及得分的均值

# In[5]:


df.groupby('district').agg(
    {'salary': [np.mean, np.median, np.std], 'score': np.mean})


# ### 自定义函数
# 
# 在 18 题基础上，在聚合计算时新增一列计算最大值与平均值的差值

# In[6]:


def myfunc(x):

    return x.max()-x.mean()

df.groupby('district').agg(最低工资=('salary', 'min'), 最高工资=(
    'salary', 'max'), 平均工资=('salary', 'mean'), 最大值与均值差值=('salary', myfunc)).rename_axis(["行政区"])

