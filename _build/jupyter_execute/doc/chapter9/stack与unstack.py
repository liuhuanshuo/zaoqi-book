#!/usr/bin/env python
# coding: utf-8

# # stack 与 unstack
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
# ````

# ## 数据堆叠
# 
# 
# stack字面意思是数据堆叠，但是理解起来就是将数据由宽变长
# 
# 怎样做到？
# 
# 通过**将部分列名拿下来当作索引**来实现，例如下图所示
# 
# 本来应是`2列4行`，但通过 `stack` 可以将列A拿下来当作索引，从而变成`1列8行`
# 
# ![](https://pandas.pydata.org/docs/_images/reshaping_stack.png)
# 
# 
# 现在，按上图所示，对 df2 进行堆叠

# In[2]:


import pandas as pd
import numpy as np
tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)
index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])
df = pd.DataFrame(np.arange(1,17).reshape([8,2]), index=index, columns=["A", "B"])
df2 = df[:4]

df2


# In[5]:


stacked = df2.stack()
stacked


# ## 逆堆叠
# 
# 对上一题的结果进行还原，即逆堆叠，过程如下图所示
# 
# ![](https://pandas.pydata.org/docs/_images/reshaping_unstack.png)

# In[6]:


stacked.unstack()


# ## 分层逆堆叠
# 
# 在使用 unstack 进行逆堆叠时，可以指定层级，例如指定按照 second 进行，也就是如下图所示
# 
# ![](https://pandas.pydata.org/docs/_images/reshaping_unstack_1.png)

# In[7]:


stacked.unstack('second')

