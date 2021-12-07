#!/usr/bin/env python
# coding: utf-8

# # 读取 TXT 文件

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 常规读取
# 

# ```{admonition} 注意
# :class: Attention
#         
# 在接下来的几种格式文件读取中，对于在 [读取 Excel 文件](读取Excel文件.ipynb) 中重复的参数/功能将不再整理，仅介绍常规读取功能。
# 
# ```
# 
# 
# 读取当前目录下 `Titanic.txt` 文件。

# In[1]:


import pandas as pd

data = pd.read_table("Titanic.txt")


# ## 含中文读取
# 
# 
# 对于 `txt` 格式，更多是带有中文的文本文件，如果直接默认读取，有可能会产生报错，因此需要读取时设置编码。
# 
# 例如，读取当前目录下 `TOP250.txt` 文件。

# In[2]:


data = pd.read_table("TOP250.txt",encoding='gb18030')

# data = pd.read_csv("TOP250.txt",encoding='gb18030',sep = '\t') # 使用 read_csv 也可

