#!/usr/bin/env python
# coding: utf-8

# # option - 个性化显示设置
# 
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# ## 本页面数据说明
# 
# 为了更好的介绍相关操作，本页面使用 **某招聘数据** 数据进行展开，你应该对数据字段、数值、类型等相关信息做一个大致了解！

# In[1]:


import pandas as pd
data = pd.read_csv("data.csv")
data.head()


# ## 显示全部列
# 
# 如下图所示👇，直接查看 `data` 会发现，由于数据维度较大，部分行列会被折叠，显示为 `...` ，现在需要显示全部的列方便预览。

# In[2]:


pd.set_option('display.max_columns', None) #显示全部列
# pd.set_option('display.max_rows', None) # 显示全部行

data.head()


# ## 显示指定行/列
# 
# 指定让 `data` 在预览时显示10列，7行

# In[3]:


pd.set_option('display.max_columns', 10)  
pd.set_option('display.max_rows', 7)

data.head()


# ## 还原行/列显示数
# 
# 还原上面的显示设置

# In[4]:


pd.reset_option("max_rows")
pd.reset_option("max_columns")


# ## 修改每列最大字符宽度
# 
# 即每列最多显示的字符长度，例如【每列最多显示10个字符，多余的会变成`...`】

# In[5]:


pd.set_option('display.max_colwidth',10)
data.head()


# ```{admonition} 在线刷题
# :class: attention
# 
# 基于 option 修改显示设置并未修改数据，仅是在原有数据基础上优化显示状态，随时可以通过重置选项重置全部设置，恢复数据默认显示状态。
# ```

# ## 修改小数点精度
# 
# 修改默认显示精度为小数点后5位

# In[6]:


pd.set_option('precision', 5)


# ## 还原所有显示设置

# 还原上面的全部显示设置

# In[7]:


pd.reset_option("^display")


# ## 忽略警告
# 
# 取消`pandas`相关`warning`提示

# In[8]:


pd.set_option("mode.chained_assignment", None) 
# 全局取消warning
# import warnings
# warnings.filterwarnings('ignore')


# ## 设置数值显示条件
# 
# 例如，若数值小于 20 则显示为0

# In[9]:


pd.set_option('chop_threshold', 20) 


# ## 支持 LaTex
# 
# 让`dataframe`中内容支持 `Latex` 显示（需要使用`$$`包住）

# In[10]:


pd.set_option("display.html.use_mathjax",True)


# ## 修改默认绘图引擎
# 
# 修改`pandas`默认绘图引擎为`plotly`（需要提前安装好`plotly`）

# In[11]:


pd.set_option("plotting.backend","plotly")


# ## 还原所有 option 设置
# 
# 还原上面全部 option 设置

# In[12]:


pd.reset_option("all") 

