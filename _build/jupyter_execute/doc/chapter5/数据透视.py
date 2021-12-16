#!/usr/bin/env python
# coding: utf-8

# # 数据透视
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
# ```

# ## 本页数据说明
# 
# 为了更好的介绍相关操作，本页面使用 **某超市销售数据** 进行展开，你应该对数据字段、数值、类型等相关信息做一个大致了解！

# In[1]:


import pandas as pd
df = pd.read_csv("某超市销售数据.csv",thousands=',')
df.head()


# ## 默认方法
# 
# 制作各省「平均销售额」的数据透视表

# In[2]:


pd.pivot_table(df,values = ['销售额'],index = '省/自治区')


# ```{admonition} 思考
# :class: hint
# 
# 用分组如何实现？
# ```

# In[3]:


df.groupby("省/自治区")['销售额'].mean() 


# ## 指定维度
# 
# 制作各省「销售总额」的数据透视表

# In[4]:


pd.pivot_table(df,values = ['销售额'],index = '省/自治区',aggfunc = sum)


# ## 组合计算
# 
# 制作各省「销售总额」与「平均销售额」的数据透视表

# In[5]:


pd.pivot_table(df,values = ['销售额'],index = '省/自治区',aggfunc = ['mean',sum])


# ## 组合多列
# 
# 制作各省市「销售总额」与「利润总额」的数据透视表

# In[6]:


pd.pivot_table(df,values = ['销售额','利润','数量'],index = '类别',aggfunc = sum)


# ## 组合索引
# 
# 制作「各省市」与「不同类别」产品「销售总额」的数据透视表

# In[7]:


pd.pivot_table(df,values = ['销售额'],index = ['省/自治区','类别'],aggfunc = sum)


# ## 多层透视
# 
# 制作各省市「不同类别」产品的「销售总额」透视表

# In[8]:


pd.pivot_table(df,values = ['销售额'],index = ['省/自治区'], columns='类别',aggfunc = sum)


# ## 综合使用
# 
# 制作「各省市」、「不同类别」产品「销售量与销售额」的「均值与总和」的数据透视表，并在最后追加一行『合计』

# In[9]:


pd.pivot_table(df,values = ['销售额','数量'],index = ['省/自治区','类别'],aggfunc = ['mean',sum],margins=True)


# ## 透视筛选
# 
# 在上一题的基础上，查询 **「类别」** 等于 **「办公用品」** 的详情

# In[10]:


table = pd.pivot_table(df,values = ['销售额','数量'],index = ['省/自治区','类别'],aggfunc = ['mean',sum],margins=True)
table.query('类别 == ["办公用品"]')


# ## 逆透视
# 
# 逆透视就是将宽的表转换为长的表，例如将第 5 题的透视表进行逆透视，其中不需要转换的列为『数量』列

# In[11]:


table = pd.pivot_table(df,values = ['销售额','利润','数量'],index = '类别',aggfunc = sum)
table.melt(id_vars=['数量'],var_name='分类',value_name='金额')

