#!/usr/bin/env python
# coding: utf-8

# # 读取网页

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
# 有时候我们需要网页上的表格数据，但又不想下载数据再读取，可以试试使用 `pd.read_html` 直接读取！
# 
# 
# 例如直接从<a href="https://baike.baidu.com/item/2020%E5%B9%B4%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A/10188878?fromtitle=%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A&fromid=3250130&fr=aladdin#5_1" target="_blank">百度百科 - 东京奥运会</a>读取奖牌榜数据并查看前 5 名。
# 
# 
# <a href="https://baike.baidu.com/item/2020%E5%B9%B4%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A/10188878?fromtitle=%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A&fromid=3250130&fr=aladdin#5_1" target="_blank">![image.png](http://tva1.sinaimg.cn/large/c23ef7c0ly1gwnx3k6qzpj21a80gmmz7.jpg)</a>

# In[1]:


import pandas as pd

pd.read_html("https://baike.baidu.com/item/2020%E5%B9%B4%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A/10188878?fromtitle=%E4%B8%9C%E4%BA%AC%E5%A5%A5%E8%BF%90%E4%BC%9A&fromid=3250130&fr=aladdin")[6].head(5)


# :::{admonition} 什么类型的表格可以直接读取？
# :class: tip, dropdown
# 
# 
# 
# 目标网站使用 `table` 渲染的表格可以直接读取
# 
# ![image.png](http://tva1.sinaimg.cn/large/c23ef7c0ly1gwnxjfks6vj220g0zuk8t.jpg)
# :::

# In[ ]:




