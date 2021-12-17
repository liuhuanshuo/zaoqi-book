#!/usr/bin/env python
# coding: utf-8

# # 读取 JSON 文件

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
# 
# `JSON`(JavaScript Object Notation) 是一种轻量级的数据交换格式，在我们写爬虫或者 `web` 与网页交互时，常常会用到。
# 
# 读取 `json` 一般使用`pd.read_json()`，例如读取当前目录下 `某基金数据.json` 文件。

# In[1]:


import pandas as pd

data = pd.read_json("某基金数据.json")

