#!/usr/bin/env python
# coding: utf-8

# # 更多样式
# 
# 
# 
# 如果对默认生成的图形不满意，我们可以通过 seaborn 来修改绘图主题活着修改绘图后端

# ## 修改主题

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']
plt.rcParams['axes.unicode_minus']=False


df6 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])


# ### 主题1

# In[2]:


import seaborn as sns
sns.set_palette("pastel", 8)

df6.plot.area(alpha = 0.7, figsize=(8, 6))


# ### 主题2

# In[3]:


import seaborn as sns
sns.set_palette("Blues_r", 8)
df6.plot.area(figsize=(8, 6))


# ### 主题3

# In[4]:


import seaborn as sns
sns.set_palette("magma", 8)
df6.plot.area(figsize=(8, 6))


# ## 修改后端

# 修改`pandas`默认绘图引擎为`plotly`（需要提前安装好`plotly`）

# In[5]:


pd.set_option("plotting.backend","plotly")
df6.plot.area()

