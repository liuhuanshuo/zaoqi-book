#!/usr/bin/env python
# coding: utf-8

# # 更多图形
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


# ## 箱线图

# In[2]:


df5 = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
df5.plot.box(figsize=(8, 6))
plt.show()


# ## 箱线图｜修改颜色

# In[3]:


color = {
    "boxes": "DarkGreen",
    "whiskers": "DarkOrange",
    "medians": "DarkBlue",
    "caps": "Gray",
}


df5.plot.box(color=color, sym="r+", figsize=(8, 6))
plt.show()


# ## 箱线图｜水平
# 
# 将上一题的图改为水平格式

# In[4]:


df5.plot.box(vert=False,color=color, figsize=(8, 6))
plt.show()


# ## 面积图
# 
# 重新生成数据，并使用面积图对 df6 进行可视化

# In[185]:





# In[5]:


df6 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])
df6.plot.area(alpha = 0.7, figsize=(8, 6))
plt.show()


# ## 六边形箱图
# 
# 如果数据太密集而无法单独绘制每个点，则 Hexbin 图可能是散点图的有用替代方案。
# 
# 重新生成数据 df7，并使用 hexbin 图进行可视化

# In[189]:





# In[6]:


df7 = pd.DataFrame(np.random.randn(1000, 2), columns=["a", "b"])
df7["b"] = df7["b"] + np.arange(1000)
df7.plot.hexbin(x="a", y="b", gridsize=25, figsize=(8, 6));


# ## 密度曲线图
# 
# 重新生成数据 df8 并绘制密度曲线图

# In[200]:





# In[7]:


df8 = pd.Series(np.random.randn(1000))
df8.plot(kind='kde', figsize=(8, 6))
plt.show()

