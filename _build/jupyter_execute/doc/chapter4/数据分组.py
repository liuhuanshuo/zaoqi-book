#!/usr/bin/env python
# coding: utf-8

# # 数据分组

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 本页数据说明
# 
# 为了更好的介绍相关操作，本页面使用 **某招聘网站数据.csv** 数据进行展开，你应该对数据**字段、数值、类型**等相关信息做一个大致了解！

# In[1]:


import pandas as pd
pd.set_option('display.max_colwidth',8)
df = pd.read_csv("某招聘网站数据.csv",parse_dates=['createTime'])
df.head()


# ## 分组统计

# ### 均值
# 
# 计算各区(`district`)的薪资(`salary`)均值

# In[2]:


df[['district','salary']].groupby(by='district').mean()

# df.groupby("district")['salary'].mean()


# ### 取消索引
# 
# 重新按照上一题要求进行分组，但不使用 `district` 做为索引

# In[3]:


df.groupby("district", as_index=False)['salary'].mean()


# ### 排序
# 
# 计算并提取平均薪资最高的区

# In[4]:


df[['district','salary']].groupby(by='district').mean().sort_values('salary',ascending=False).head(1)


# ### 频率
# 
# 计算不同行政区(`district`)，不同规模公司(`companySize`)出现的次数

# In[5]:


pd.DataFrame(df.groupby("district")['companySize'].value_counts())

# df.groupby(['district','companySize']).size()


# ### 修改索引名
# 
# 将上一题的索引名修改为
# - district -> 行政区
# - companySize -> 公司规模

# In[6]:


pd.DataFrame(df.groupby("district")['companySize'].value_counts()).rename_axis(["行政区", "公司规模"])


# ### 计数
# 
# 在上一个操作的基础上，统计每个区出现的公司数量

# In[7]:


df.groupby("district")['companySize'].count()


# ## 分组查看

# ### 查看各组信息
# 
# 将数据按照 `district`、`salary` 进行分组，并查看各分组内容

# In[8]:


df.groupby(["district",'salary']).groups


# ### 查看指定条件信息
# 
# 将数据按照 `district`、`salary` 进行分组，并查看西湖区薪资为 30000 的工作

# In[9]:


df.groupby(["district",'salary']).get_group(("西湖区",30000))


# ## 分组规则

# ### 过匿名函数1
# 
# 根据 createTime 列，计算每天不同 行政区 新增的岗位数量

# In[10]:


pd.DataFrame(df.groupby([df.createTime.apply(lambda x:x.day)])[
             'district'].value_counts()).rename_axis(["发布日", "行政区"])


# ### 通过匿名函数2
# 
# 计算各行政区的企业领域（industryField）包含电商的总数
# 
# 

# In[11]:


df.groupby("district", sort=False)["industryField"].apply(
lambda x: x.str.contains("电商").sum())


# ### 通过内置函数
# 
# 通过 positionName 的长度进行分组，并计算不同长度岗位名称的薪资均值

# In[12]:


df.set_index("positionName").groupby(len)['salary'].mean()


# ### 通过字典
# 
# 将 score 和 matchScore 的和记为总分，与 salary 列同时进行分组，并查看结果

# In[13]:


df.groupby({'salary':'薪资','score':'总分','matchScore':'总分'}, axis=1).sum()


# ### 通过多列
# 
# 计算不同 工作年限（`workYear`）和 学历（`education`）之间的薪资均值

# In[14]:


pd.DataFrame(df['salary'].groupby([df['workYear'], df['education']]).mean())


# ## 分组转换（transform）
# 
# 在原数据框 df 新增一列，数值为该区的平均薪资水平

# In[15]:


df['该区平均工资'] = df[['district','salary']].groupby(by='district').transform('mean')


# ## 分组过滤（filter）
# 

# 提取平均工资小于 30000 的行政区的全部数据

# In[16]:


df.groupby('district').filter(lambda x: x['salary'].mean() < 30000)


# 微信搜索公众号「早起Python」，关注后可以获得更多资源！

# In[ ]:





# ## 分组可视化
# 
# 对杭州市各区公司数量进行分组，并使用柱状图进行可视化

# In[17]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
plt.rcParams['font.sans-serif'] = ['Songti SC']

df.groupby("district")['positionName'].count().plot(
    kind='bar', figsize=(10, 6), color='#5172F0', fontsize=12)

plt.ylabel("公司数量",fontsize = 14)
plt.xlabel("杭州市各区",fontsize = 14)

plt.show()

