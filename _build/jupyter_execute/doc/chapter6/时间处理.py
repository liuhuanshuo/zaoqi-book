#!/usr/bin/env python
# coding: utf-8

# # pandas中的时间操作

# ## 时间生成

# ### 生成当前时间
# 
# 使用 `pandas` 获取当前时间
# 

# In[1]:


import pandas as pd

pd.Timestamp('now')


# ### 生成指定时间范围
# 
# 使用 `pandas` 按天生成 `2021年1月1日` 至 `2021年9月1日` 的全部日期

# In[2]:


pd.date_range('1/1/2021','9/11/2021')


# ### 生成指定间隔时间
# 
# 使用 `pandas` 从 `2021年1月1日` 开始，按天生成 10 天日期

# In[3]:


pd.date_range("2021-01-01", periods=10)


# ### 生成指定频率时间
# 
# 使用 pandas 从 2021年1月1日开始，按周生成 7 周日期

# In[4]:


pd.date_range("2021-01-01", periods=7, freq="W")


# ### 生成工作日时间
# 
# 使用 pandas 按天生成 2021年1月1日 至 2021年9月1日的全部**工作日**日期

# In[5]:


pd.bdate_range(start='1/1/2021', end='9/1/2021')


# ## 时间计算

# ### 计算时间差（天）
# 
# 使用 pandas 计算 2021年2月14日 距离今天相差多少天

# In[6]:


(pd.Timestamp('now') - pd.to_datetime('2021-02-14')).days


# ### 计算时间差（小时）
# 
# 使用 pandas 计算 2021年9月1日13点14分 距离今天相差多少小时

# In[8]:


import numpy as np
(pd.Timestamp('now') - pd.to_datetime('2021-09-01 13:14:00'))/np.timedelta64(1, 'h')


# ### 时间加减
# 
# 将现在的时间减去一天，并格式化为 xx年xx月xx日 xx时xx分xx秒

# In[7]:


(pd.Timestamp('now') - pd.to_timedelta('1 day'))


# ## 时间格式化
# 
# 将上一题的结果式化为 xx年xx月xx日-xx时xx分xx秒

# In[9]:


(pd.Timestamp('now') - pd.to_timedelta('1 day')).strftime("%Y年%m月%d日-%H时%M分%S秒")

