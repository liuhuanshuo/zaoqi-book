#!/usr/bin/env python
# coding: utf-8

# # 官方教程 - 10分钟入门pandas
# 
# > 教程译自[10 Minutes to pandas](https://pandas.pydata.org/pandas-docs/version/0.18.0/10min.html)，有删改，[点击直达最新文档地址](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
# 
# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```
# 
# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！

# 首先导入 Python 数据处理中常用的三个库，如果没有需要提前使用 `pip` 安装

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 注：本教程基于Pandas0.18.0版本，因版本不同可能有些代码无法成功执行，请自行查阅解决办法

# ## 创建数据

# 使用pd.Series创建Series对象

# In[2]:


s = pd.Series([1,3,5,np.nan,6,8])


# In[3]:


s


# 通过numpy的array数据来创建DataFrame对象

# In[4]:


dates = pd.date_range('20130101', periods=6)


# In[5]:


dates


# In[6]:


df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))


# In[7]:


df


# 通过字典创建DataFrame对象

# In[8]:


df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })


# In[9]:


df2


# In[10]:


df2.dtypes


# In[11]:


dir(df2)


# ## 数据查看

# 基本方法，务必掌握，更多相关查看数据的方法可以参与[官方文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#basics)

# 下面分别是查看数据的顶部和尾部的方法

# In[12]:


df.head()


# In[13]:


df.tail(3)


# 查看DataFrame对象的索引，列名，数据信息

# In[14]:


df.index


# In[15]:


df.columns


# In[16]:


df.values


# 描述性统计

# In[17]:


df.describe()


# 数据转置

# In[18]:


df.T


# 根据列名排序

# In[19]:


df.sort_index(axis=1, ascending=False)


# 根据B列数值排序

# In[20]:


df.sort_values(by='B')


# ## 数据选取

# 官方建议使用优化的熊猫数据访问方法`.at，.iat，.loc`和`.iloc`，部分较早的pandas版本可以使用`.ix`
# 
# 这些选取函数的使用需要熟练掌握，我也曾写过相关文章帮助理解
# 
# - [5分钟学会Pandas中iloc/loc/ix区别](https://mp.weixin.qq.com/s/5xJ-VLaHCV9qX2AMNOLRtw)

# ### 使用\[\]选取数据

# 选取单列数据，等效于`df.A`:

# In[21]:


df['A']


# 按行选取数据，使用[]

# In[22]:


df[0:3]


# In[23]:


df['20130102':'20130104']


# ### 通过标签选取数据

# In[24]:


df.loc[dates[0]]


# In[25]:


df.loc[:,['A','B']]


# In[26]:


df.loc['20130102':'20130104',['A','B']]


# In[27]:


df.loc['20130102',['A','B']]


# In[28]:


df.loc[dates[0],'A']


# In[29]:


df.at[dates[0],'A']


# ### 通过位置选取数据

# In[30]:


df.iloc[3]


# In[31]:


df.iloc[3:5, 0:2]


# In[32]:


df.iloc[[1,2,4],[0,2]]


# In[33]:


df.iloc[1:3]


# In[34]:


df.iloc[:, 1:3]


# In[35]:


df.iloc[1, 1]


# In[36]:


df.iat[1, 1]


# ### 使用布尔索引 

# In[37]:


df[df.A>0]


# In[38]:


df[df>0]


# In[39]:


df2 = df.copy()


# In[40]:


df2['E'] = ['one', 'one','two','three','four','three']


# In[41]:


df2


# In[42]:


df2[df2['E'].isin(['two','four'])]


# ## 缺失值处理

# **reindex**
# 
# Pandas中使用`np.nan`来表示缺失值，可以使用`reindex`更改/添加/删除指定轴上的索引

# In[43]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])


# In[44]:


df1.loc[dates[0]:dates[1],'E'] = 1


# In[45]:


df1


# ### 删除缺失值
# 舍弃含有NaN的行

# In[46]:


df1.dropna(how='any')


# ### 填充缺失值
# 填充缺失数据

# In[47]:


df1.fillna(value=5)


# In[48]:


pd.isnull(df1)


# ## 常用操作

# 在我的[Pandas120题](https://mp.weixin.qq.com/s/xgqmjTt4nxHJJZCE7acDhw)系列中有很多关于Pandas常用操作介绍！
# 
# 欢迎微信搜索公众号【早起Python】关注
# 
# 后台回复pandas获取相关习题！

# ### 统计

# 在进行统计操作时需要排除缺失值！
# 
# **描述性统计👇**

# 纵向求均值

# In[49]:


df.mean()


# 横向求均值

# In[50]:


df.mean(1)


# In[51]:


s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)


# In[52]:


s


# In[53]:


df.sub(s, axis='index')


# ### Apply函数

# In[54]:


df.apply(np.cumsum)


# In[55]:


df.apply(lambda x: x.max() - x.min())


# ### value_counts()

# 文档中为`Histogramming`，但示例就是`.value_counts()`的使用

# In[56]:


s = pd.Series(np.random.randint(0, 7, size=10))


# In[57]:


s


# In[58]:


s.value_counts()


# ### 字符串方法

# In[59]:


s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])


# In[60]:


s.str.lower()


# ## 数据合并

# ### Concat

# 在连接/合并类型操作的情况下，pandas提供了各种功能，可以轻松地将Series和DataFrame对象与各种用于索引和关系代数功能的集合逻辑组合在一起。

# In[61]:


df = pd.DataFrame(np.random.randn(10, 4))


# In[62]:


df


# In[63]:


pieces = [df[:3], df[3:6], df[7:]]


# In[64]:


pd.concat(pieces)


# **注意**
# 
# 将列添加到DataFrame相对较快。 
# 
# 但是，添加一行需要一个副本，并且可能浪费时间
# 
# 我们建议将预构建的记录列表传递给DataFrame构造函数，而不是通过迭代地将记录追加到其来构建DataFrame

# ### Join

# In[65]:


left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})


# In[66]:


right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})


# In[67]:


left


# In[68]:


right


# In[69]:


pd.merge(left, right, on='key')


# ### Append

# In[70]:


df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])


# In[71]:


df


# In[72]:


s = df.iloc[3]


# In[73]:


df.append(s, ignore_index=True)


# ## 数据分组

# **数据分组**是指涉及以下一个或多个步骤的过程：
# 
# - 根据某些条件将数据分成几组
# 
# - 对每个组进行独立的操作
# 
# - 对结果进行合并
# 
# 更多操作可以查阅[官方文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#groupby)

# In[74]:


df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                           'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
df


# In[75]:


df.groupby('A').sum()


# In[76]:


df.groupby(['A', 'B']).sum()


# ## 数据重塑

# ### 数据堆叠
# 可以进行数据压缩

# In[77]:


tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                   ['one', 'two', 'one', 'two',
                    'one', 'two', 'one', 'two']]))


# In[78]:


index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])


# In[79]:


df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])


# In[80]:


df2 = df[:4]


# In[81]:


df2


# In[82]:


stacked = df2.stack()


# In[83]:


stacked


# stack()的反向操作是unstack()，默认情况下，它会将最后一层数据进行unstack():

# In[84]:


stacked.unstack()


# In[85]:


stacked.unstack(1)


# In[86]:


stacked.unstack(0)


# ### 数据透视表

# In[87]:


df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                   'B' : ['A', 'B', 'C'] * 4,
                   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D' : np.random.randn(12),
                   'E' : np.random.randn(12)})


# In[88]:


df


# In[89]:


df.pivot_table(values='D', index=['A', 'B'], columns='C')


# ## 时间序列

# 对于在频率转换期间执行重采样操作(例如，将秒数据转换为5分钟数据)，pandas具有简单、强大和高效的功能。这在金融应用中非常常见，但不仅限于此。 参见[时间序列](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries)部分。

# 时区表示

# In[90]:


rng = pd.date_range('1/1/2012', periods=100, freq='S')


# In[91]:


ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)


# In[92]:


ts.resample('5Min').sum()


# In[93]:


rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')


# In[94]:


ts = pd.Series(np.random.randn(len(rng)), rng)


# In[95]:


ts


# In[96]:


ts_utc = ts.tz_localize('UTC')


# In[97]:


ts_utc


# 时区转换

# In[98]:


ts_utc.tz_convert('US/Eastern')


# 在时间跨度表示之间进行转换

# In[99]:


rng = pd.date_range('1/1/2012', periods=5, freq='M')


# In[100]:


ts = pd.Series(np.random.randn(len(rng)), index=rng)


# In[101]:


ts


# In[102]:


ps = ts.to_period()


# In[103]:


ps


# In[104]:


ps.to_timestamp()


# 在周期和时间戳之间转换可以使用一些方便的算术函数。 
# 
# 在以下示例中，我们将以11月结束的年度的季度频率转换为季度结束后的月末的上午9点：

# In[105]:


prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')


# In[106]:


ts = pd.Series(np.random.randn(len(prng)), prng)


# In[107]:


ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9


# In[108]:


ts.head()


# 事实上，常用有关时间序列的操作远超过上方的官方示例，简单来说与日期有关的操作从创建到转换pandas都能很好的完成！

# ## 灵活的使用分类数据

# Pandas可以在一个DataFrame中包含分类数据。有关完整文档，请参阅分类介绍和API文档。

# In[109]:


df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})


# In[110]:


df['grade'] = df['raw_grade'].astype("category")


# In[111]:


df['grade']


# 将类别重命名为更有意义的名称(`Series.cat.categories()`)

# In[112]:


df["grade"].cat.categories = ["very good", "good", "very bad"]


# 重新排序类别，并同时添加缺少的类别(在有缺失的情况下，string .cat()下的方法返回一个新的系列)。

# In[113]:


df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])


# In[114]:


df["grade"]


# In[115]:


df.sort_values(by='grade')


# In[116]:


df.groupby("grade").size()


# ## 数据可视化

# In[117]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))


# In[118]:


ts.head()


# In[119]:


ts = ts.cumsum() #累加


# 在Pandas中可以使用`.plot()`直接绘图，支持多种图形和自定义选项点击可以查阅[官方文档](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#plotting)

# In[120]:


ts.plot()


# In[121]:


df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D']) 


# In[122]:


df = df.cumsum()


# 使用`plt`绘图，具体参数设置可以查阅matplotlib官方文档

# In[123]:


plt.figure(); df.plot(); plt.legend(loc='best')


# ## 导入导出数据

# **将数据写入`csv`，如果有中文需要注意编码**

# In[124]:


# df.to_csv('foo.csv')


# 从`csv`中读取数据

# In[125]:


# pd.read_csv('foo.csv').head()


# 将数据导出为`hdf`格式

# In[126]:


# df.to_hdf('foo.h5','df')


# 从`hdf`文件中读取数据前五行

# In[127]:


# pd.read_hdf('foo.h5','df').head()


# 将数据保存为`xlsx`格式

# In[128]:


# df.to_excel('foo.xlsx', sheet_name='Sheet1')


# 从`xlsx`格式中按照指定要求读取sheet1中数据

# In[129]:


# pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']).head()

