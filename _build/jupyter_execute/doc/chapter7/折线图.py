#!/usr/bin/env python
# coding: utf-8

# # 折线图
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 导入与预设
# 
# 虽然在 `pandas` 中可以直接调用 `matplotliab` 进行可视化，但是依旧需要进行相关设置，例如字体、精度等。

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus']=False


# In[2]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()


# ## 指定列绘制
# 
# 绘制 df 第一列的折线图

# In[3]:


df['A'].plot()
plt.show()


# ## 子图
# 
# 将 df 的四列分别放在四个子图上

# In[4]:


df.plot(subplots=True)
plt.show()


# ## 全部列
# 
# 绘制 df 全部列的折线图

# In[5]:


df.plot()
plt.show()


# ## 调整大小
# 
# 绘制 df 全部列的折线图，将大小调整为 1000*600 来让图片更美观

# In[6]:


df.plot(figsize=(10,6))
plt.show()


# ## 修改标题
# 
# 在上一题的基础上，添加标题 `早起Python`

# In[7]:


df.plot(figsize=(10,6),title='早起Python')
plt.show()


# ## 添加网格
# 
# 在上一题的基础上，给折线图添加网格

# In[8]:


df.plot(figsize=(10,6),title='早起Python',grid = True)
plt.show()


# ## 添加轴标签
# 
# 在上一题的基础上，给X轴添加标签（时间），Y轴添加标签（数量）

# In[9]:


df.plot(figsize=(10, 6), title='早起Python', grid=True, xlabel='时间', ylabel='数量')
plt.show()


# ## 调整刻度大小
# 
# 在上一题的基础上，将刻度调大一点

# In[10]:


df.plot(figsize=(10, 6), title='早起Python', grid=True, xlabel='时间', ylabel='数量',fontsize = 13)
plt.show()


# ## 调整文字大小
# 
# 在上一题的基础上，将标题、坐标轴文字适当调大

# In[11]:


df.plot(figsize=(10, 6), grid=True, fontsize = 13)
plt.title("早起Python",size = 17)
plt.xlabel('时间',size = 15)
plt.ylabel('数量',size =15)
plt.show()


# ## 图例位置
# 
# 在上一题的基础上，将图例位置调整到左下角

# In[12]:


df.plot(figsize=(10, 6), grid=True, fontsize = 13)
plt.title("早起Python",size = 17)
plt.xlabel('时间',size = 15)
plt.ylabel('数量',size =15)
plt.legend(loc=3)
plt.show()


# ## 双y轴
# 
# A、B使用一个y轴，CD使用一个y轴

# In[13]:


ax = df.plot(secondary_y=['A', 'B'], figsize=(10, 6), fontsize = 13)
ax.set_ylabel('CD')  
ax.right_ax.set_ylabel('AB')  
ax.legend(loc=2)
plt.title("早起Python",size = 17)
plt.xlabel('时间',size = 15)
plt.ylabel('数量',size =15)
plt.legend(loc=1) 
plt.show()

