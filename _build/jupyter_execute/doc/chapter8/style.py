#!/usr/bin/env python
# coding: utf-8

# # style - 自定义样式输出
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

# 上面基于 `option` 的 `pandas` 相关设置是<font color=#E36C07>全局配置</font>，一次设置会在关闭notebook前一直有效
# 
# 但相关常用的设置并不多，不能满足更多的个性化需求。
# 
# 幸运的是在 `pandas` 中提供 `Styler` 对象让我们进一步个性化展示数据。
# 
# 注意：基于 `style` 个性化设置<font color=#E36C07>**同样不会修改数据**</font>，所有 `data.style.xxxx` 输出的数据均是<font color=#E36C07>一次性的（可以复用、导出）</font>，因此你应该在合适的时间选择使用该方法。
# 
# 下面仅列举常用的方法，若想了解更多可以查阅[**pandas官方文档对应文章👉**](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)

# ## 本页面数据说明
# 
# 为了更好的介绍相关操作，本页面使用 **某招聘数据** 数据进行展开，你应该对数据字段、数值、类型等相关信息做一个大致了解！

# In[1]:


import pandas as pd
data = pd.read_csv("data.csv", usecols=[
                   'positionName', 'createTime', 'salary', 'subwayline', 'matchScore'], nrows=20, parse_dates=['createTime'])

data.head()


# ## 隐藏索引
# 
# 
# 隐藏索引列

# In[2]:


data.style.hide_index().set_table_attributes('style="font-size: 10px"')


# ## 调整精度
# 
# 将带有小数点的列精度调整为小数点后2位

# In[3]:


data.style.set_precision(2).set_table_attributes('style="font-size: 10px"')


# ## 标记缺失值
# 
# 将缺失值标记为`数据缺失`

# In[4]:


(data
.style
.set_na_rep("数据缺失")
.set_table_attributes('style="font-size: 10px"'))


# ## 高亮缺失值
# 
# 将缺失值高亮，颜色名`skyblue`

# In[5]:


(data
.style
.set_na_rep("数据缺失")
.highlight_null(null_color='skyblue')
.set_table_attributes('style="font-size: 10px"'))


# ## 高亮数值列最大值
# 
# 将 数值格式列的最大值进行高亮

# In[6]:


data.style.highlight_max().set_table_attributes('style="font-size: 10px"')


# ## 高亮数值列最小值
# 
# 将 数值格式列的最小值进行高亮

# In[7]:


data.style.highlight_min().set_table_attributes('style="font-size: 10px"')


# ## 同时高亮最大最小值
# 
# 
# 同时高亮最大值（颜色代码为`#F77802`）与最小值（颜色代码为`#26BE49`）

# In[8]:


(data
.style
.highlight_max(color='#F77802')
.highlight_min(color='#26BE49')
.set_table_attributes('style="font-size: 10px"'))


# ## 指定区间高亮
# 
# 
# 高亮 salary 列范围在 3000 - 10000 的数值

# In[9]:


# 需要 pandas 版本大于 1.3.0 才可以执行
# (data
# .style
# .highlight_between(left=3000, right=10000, subset=['salary'])
# .set_table_attributes('style="font-size: 10px"'))


# ## 渐变显示数值列
# 
# 
# 将数值格式的列使用渐变色（绿色）进行显示，以突出趋势

# In[10]:


import seaborn as sns

cm = sns.light_palette("green", as_cmap=True)

(data
.style
.background_gradient(cmap=cm)
.set_table_attributes('style="font-size: 10px"'))


# ##  修改字体颜色
# 
# 将 `salary` 列修改为红色字体

# In[11]:


(data
.style
.set_properties(
    subset=['salary'], **{'color': 'red'})
.set_table_attributes('style="font-size: 10px"'))


# ## 修改背景颜色、对齐方式、字体大小
# 
# 将整个 `dataframe` 进行如下设置：
# - 居中
# - 背景色修改为 `#F8F8FF`
# - 字体:13px

# In[12]:


(data
.style
.set_properties(**{'background-color': '#F8F8FF','text-align':'center', 'font-size': '13px'})
.set_table_attributes('style="font-size: 10px"'))


# ## 综合(链式)设置
# 
# 
# 除了上面的单个设置，还可以将多个设置进行结合，下面对整个 `dataframe` 进行如下设置：
# - 居中
# - 背景色修改为 `#F8F8FF`
# - 字体:13px
# 
# 并将 `salary` 列字体修改为红色

# In[13]:


(data
.style
.set_properties(**{'background-color': '#F8F8FF','text-align':'center', 'font-size': '13px'})
.set_properties(
    subset=['salary'], **{'color': 'red'})
.set_table_attributes('style="font-size: 10px"'))


# ## 导出样式
# 
# 
# 将上一题带有样式的 pandas 数据框导出为本地 Excel(.xlsx格式)

# In[14]:


(data
.style
.set_properties(**{'background-color': '#F8F8FF','text-align':'center', 'font-size': '13px'})
.set_properties(
    subset=['salary'], **{'color': 'red'})).to_excel('带有样式导出.xlsx')


# ## 制作指定列条形图
# 
# 在 `pandas` 中对 `salary` 列使用条形图进行可视化，指定颜色`skyblue`

# In[15]:


(data
.style
.bar(subset=['salary'],color='skyblue')
.set_table_attributes('style="font-size: 10px"'))


# ## 自定义样式
# 
# 将 `salary` 列数值大于 30000 的单元格字体修改为红色

# In[16]:


def my_style(val):

    color = 'red' if val > 30000 else 'black'
    return 'color: %s' % color


data.style.applymap(my_style, subset="salary").set_table_attributes('style="font-size: 10px"')


# ## 格式化输出日期类型
# 
# 
# 将 `createTime` 列格式化输出为 `xx年xx月xx日` 

# In[17]:


data.style.format({"createTime": lambda t: t.strftime("%Y年%m月%d日")}).set_table_attributes('style="font-size: 10px"')


# ## 自定义格式化数据
# 
# 
# - 在 `salary` 列后增加"元"
# - 对 `matchScore` 列保留两位小数并增加"分"
# 

# In[18]:


(data
.style
.format("{0:,.2f}分", subset="matchScore")
.format("{""}元", subset="salary")
.set_table_attributes('style="font-size: 10px"'))

