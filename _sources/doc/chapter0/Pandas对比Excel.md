---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(content:PandasvsExcel)=

# Pandas 对比 Excel

> 为了方便长期使用 Excel 的用户转到 Pandas，我将结合官方文档对部分操作进行对比

```{admonition} 在线刷题
:class: seealso

检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
```


##  数据结构

### 通用术语对比



| pandas | Excel  |
| :-----------: | :------: |
| `DataFrame` | 工作表 |
| `Series`   | 列     |
| `Index`     | 索引   |
| row         | 行     |
| `NaN`       | 空值   |

### DataFrame

`pandas` 中的 `dataframe` 类似于`Excel` 工作表。虽然一个 `Excel` 工作簿可以包含多个工作表，但通常情况下 `pandas.DataFrame`是独立存在的。

### Series

`Series`是表示 `DataFrame`一列的数据结构。使用 `Series` 类似于引用电子表格中的一列。

### Index

每个 `DataFrame` 和 `Series` 都有一个 `Index`，它是数据行的标签。在`pandas`中，如果没有指定索引，则默认使用RangeIndex(第一行= 0，第二行= 1，等等)，类似于电子表格中的行标题/数字。



在 `pandas` 中，索引可以设置为一个(或多个)惟一值，这就像在工作表中有一列用作行标识符一样。与大多数电子表格不同，这些Index值实际上可以用来引用行。(注意，这可以在Excel的结构化引用中完成。)例如，在电子表格中，您可以引用第一行为 `A1:Z1`，而在 pandas 中，您可以使用`population .loc['Chicago']`。



## 常见操作对比

为了更方便介绍 Pandas 相关功能，方便长期使用 Excel 进行数据分析的用户学习，下面是常见操作的 Excel 与 Pandas 实现对比。

### 1 - 数据读取

#### `Excel`

Excel读取本地数据需要打开目标文件夹选中该文件并打开

```{figure} gif/读取数据.gif
:width: 600px
:align: center
```

 #### `Pandas`



Pandas支持读取本地Excel、txt文件，也支持从网页直接读取表格数据，只用一行代码即可，例如读取上述本地Excel数据可以使用`pd.read_excel("示例数据.xlsx")`

```{code-cell} ipython3
:tags: [output_scroll]

import pandas as pd
pd.read_excel("示例数据.xlsx") #将示例数据.xlsx放在该Notebook同一文件夹下
```

### 2 - 数据生成


#### `Excel`


以生成**10\*2的0—1均匀分布随机数矩阵**为例，在Excel中需要使用`rand()`函数生成随机数，并手动拉取指定范围

```{figure} gif/生成数据.gif
:width: 600px
:align: center
```

#### `Pandas`


在Pandas中可以结合NumPy生成由指定随机数(均匀分布、正态分布等)生成的矩阵，例如同样生成**10\*2的0—1均匀分布随机数矩阵**为，使用一行代码即可：`pd.DataFrame(np.random.rand(10,2))`

```{code-cell} ipython3
import numpy  as np
pd.DataFrame(np.random.rand(10,2))
```

### 3 - 数据存储


#### `Excel`

在Excel中需要点击保存并设置格式/文件名

```{figure} gif/保存数据.gif
:width: 600px
:align: center
```

#### `Pandas`

在Pandas中可以使用`pd.to_excel("filename.xlsx")`来将当前工作表格保存至当前目录下，当然也可以使用`to_csv`保存为csv等其他格式，也可以使用绝对路径来指定保存位置
```{code-cell} ipython3
# data.to_excel("测试数据.xlsx")
```

### 4 - 数据筛选


#### `Excel`



使用我们之前的示例数据，在Excel中筛选出`薪资大于5000`的数据步骤如下


```{figure} gif/数据筛选.gif
:width: 600px
:align: center
```

#### `Pandas`

在Pandas中，可直接对数据框进行条件筛选，例如同样进行单个条件(薪资大于5000)的筛选可以使用`df[df['薪资水平']>5000]`，如果使用多个条件的筛选只需要使用`&`(并)与`|`(或)操作符实现

```{code-cell} ipython3
df = pd.read_excel("示例数据.xlsx")
df[df['薪资水平']>5000]
```

### 5 - 数据插入

#### `Excel`



在Excel中我们可以将光标放在指定位置并右键增加一行/列，当然也可以在添加时对数据进行一些计算，比如我们就可以使用IF函数(`=IF(G2>10000,"高","低")`)，将薪资大于10000的设为高，低于10000的设为低，**添加一列**在最后

```{figure} gif/插入数据.gif
:width: 600px
:align: center
```

#### `Pandas`

在 pandas 中，如果不借助自定义函数的话，我们可以使用`cut`方法来实现同样操作
```{code-cell} ipython3
bins = [0,10000,max(df['薪资水平'])]
group_names = ['低','高']
df['new_col'] = pd.cut(df['薪资水平'], bins, labels=group_names)
```

### 6 - 数据删除


#### `Excel`



在Excel删除数据十分简单，找到需要删除的数据**右键删除**即可，比如删除刚刚生成的最后一列

```{figure} gif/数据删除.gif
:width: 600px
:align: center
```



#### `Pandas`
在pandas中删除数据也很简单，比如删除最后一列使用`del df['new_col']`即可

### 7 - 数据排序
  
#### `Excel`



在Excel中可以点击排序按钮进行排序，例如将示例数据按照薪资从高到低进行排序可以按照下面的步骤进行

```{figure} gif/数据排序.gif
:width: 600px
:align: center
```

#### `Pandas`

在pandas中可以使用`sort_values`进行排序，使用`ascending`来控制升降序，例如将示例数据按照薪资从高到低进行排序可以使用`df.sort_values("薪资水平",ascending=False,inplace=True)`
```{code-cell} ipython3
:tags: [output_scroll]

df1 = df
df1.sort_values("薪资水平",ascending=False)
df1
```

### 8 - 缺失值处理

#### `Excel`



在Excel中可以按照**查找—>定位条件—>空值**来快速定位数据中的空值，接着可以自己定义缺失值的填充方式，比如将缺失值用上一个数据进行填充

```{figure} gif/缺失值处理.gif
:width: 600px
:align: center
```

#### `Pandas`

在pandas中可以使用 `data.isnull().sum()` 来检查缺失值，之后可以使用多种方法来填充或者删除缺失值，比如我们可以使用`df = df.fillna(axis=0,method='ffill')` 来横向/纵向用缺失值前面的值替换缺失值

```{code-cell} ipython3
df.isnull().sum()
```

### 9 - 数据去重

#### `Excel`

在Excel中可以通过点击**数据—>删除重复值**按钮并选择需要去重的列即可，例如对示例数据按照创建时间列进行去重，可以发现去掉了196 个重复值，保留了 629 个唯一值。

```{figure} gif/数据去重.gif
:width: 600px
:align: center
```
#### `Pandas`



在pandas中可以使用`drop_duplicates`来对数据进行去重，并且可以指定列以及保留顺序，例如对示例数据按照创建时间列进行去重`df.drop_duplicates(['创建时间'],inplace=True)`，可以发现和Excel处理的结果一致，保留了 629 个唯一值。
```{code-cell} ipython3
:tags: [output_scroll]

df.drop_duplicates(['创建时间'],inplace=True)
df
```

### 10 - 格式修改


#### `Excel`

在Excel中可以选中需要转换格式的数据之后**右键—>修改单元格格式**来选择我们需要的格式

```{figure} gif/格式转换.gif
:width: 600px
:align: center
```

#### `Pandas`

在Pandas中没有一个固定修改格式的方法，不同的数据格式有着不同的修改方法，比如类似Excel中将创建时间修改为年-月-日可以使用`df['创建时间'] = df['创建时间'].dt.strftime('%Y-%m-%d')`

```{code-cell} ipython3
df1 = df
df1['创建时间'] = df1['创建时间'].dt.strftime('%Y-%m-%d')
```


### 11 - 数据交换


#### `Excel`



在Excel中交换数据是很常用的操作，以交换示例数据中地址与岗位两列为例，可以选中地址列，按住shift键并拖动边缘至下一列松开即可

```{figure} gif/数据交换.gif
:width: 600px
:align: center
```

#### `Pandas`

在 pandas 中交换两列也有很多方法，以交换示例数据中地址与岗位两列为例，可以通过修改列号来实现
```{code-cell} ipython3
cols = df.columns[[0,2,1,3,4,5,6]]
df1 = df[cols]
```


### 12 - 数据合并


#### Excel

在Excel中可以使用公式也可以使用Ctrl+E快捷键完成多列合并，以公式为例，合并示例数据中的地址+岗位列步骤如下

```{figure} gif/数据合并.gif
:width: 600px
:align: center
```
#### `Pandas`

在Pandas中合并多列比较简单，类似于之前的数据插入操作，例如合并示例数据中的地址+岗位列使用`df['合并列'] = df['地址'] + df['岗位']`
```{code-cell} ipython3
df['合并列'] = df['地址'] + df['岗位']
```

### 13 - 数据拆分


#### `Excel`

在Excel中可以通过点击**数据—>分列**并按照提示的选项设置相关参数完成分列，但是由于该列含有[]等特殊字符，所以需要先使用查找替换去掉


```{figure} gif/数据拆分.gif
:width: 600px
:align: center
```

#### `Pandas`



在Pandas中可以使用`.split`来完成分列，但是在分列完毕后需要使用 `merge` 来将分列完的数据添加至原DataFrame，对于分列完的数据含有`[]`字符，我们可以使用正则或者字符串`lstrip`方法进行处理，但因不是pandas特性，此处不再展开。

```{code-cell} ipython3
:tags: [output_scroll]

df['技能要求'].str.split(',',expand=True)
```

### 14 - 数据分组

#### `Excel`



在Excel中对数据进行分组计算需要先对需要分组的字段进行排序，之后可以通过点击分类汇总并设置相关参数完成，比如对示例数据的学历进行分组并求不同学历的平均薪资

```{figure} gif/数据分组.gif
:width: 600px
:align: center
```
#### `Pandas`


在Pandas中对数据进行分组计算可以使用groupby轻松搞定，比如使用`df.groupby("学历").mean()`一行代码即可对示例数据的学历进行分组并求不同学历的平均薪资，结果与Excel一致


### 15 - 数据计算


#### `Excel`



在Excel中有很多计算相关的公式，比如可以使用`COUNTIFS`来统计薪资大于10000的岗位数量有518个

```{figure} gif/生成数据.gif
:width: 600px
:align: center
```
#### `Pandas`

在Pandas中可以直接使用类似数据筛选的方法来统计薪资大于10000的岗位数量`len(df[df["薪资水平"]>10000])`
```{code-cell} ipython3
len(df[df["薪资水平"]>10000])
```

### 16 - 数据统计


#### `Excel`



在Excel中有很多统计相关的公式，也有现成的分析工具，比如对薪资水平列进行描述性统计分析，可以通过添加工具库之后点击数据分析按钮并设置相关参数

```{figure} gif/数据统计.gif
:width: 600px
:align: center
```

#### `Pandas`

在pandas中也有现成的函数describe快速完成对数据的描述性统计，比如使用`df["薪资水平"].describe()`即可得到薪资列的描述性统计结果

```{code-cell} ipython3
df["薪资水平"].describe()
```

### 17 - 数据可视化


#### `Excel`



在Excel中可以通过点击插入并选择图表来快速完成对数据的可视化，比如制作薪资的直方图，并且有很多样式可以直接使用

```{figure} gif/数据可视化.gif
:width: 600px
:align: center
```
#### `Pandas`


在Pandas中也支持直接对数据绘制不同可视化图表，例如直方图，可以使用plot或者直接使用hist来制作df["薪资水平"].hist()
```{code-cell} ipython3
df["薪资水平"].hist()
```

### 18 - 数据抽样


#### `Excel`

在Excel中抽样可以使用公式也可以使用分析工具库中的抽样，但是仅支持对**数值型**的列抽样，比如随机抽20个示例数据中薪资的样本

```{figure} gif/数据抽样.gif
:width: 600px
:align: center
```

#### `Pandas`

在pandas中有抽样函数sample可以直接抽样，并且支持任意格式的数据抽样，可以按照数量/比例抽样，比如随机抽20个示例数据中的样本
```{code-cell} ipython3
:tags: [output_scroll]
df.sample(20)
```

### 19 - 数据透视表


#### `Excel`



数据透视表是一个非常强大的工具，在Excel中有现成的工具，只需要**选中数据—>点击插入—>数据透视表**即可生成，并且支持**字段的拖取**实现不同的透视表，非常方便，比如制作地址、学历、薪资的透视表

```{figure} gif/数据透视表.gif
:width: 600px
:align: center
```

#### `Pandas`

在Pandas中制作数据透视表可以使用pivot_table函数，例如制作地址、学历、薪资的透视表`pd.pivot_table(df,index=["地址","学历"],values=["薪资水平"])`，虽然结果一样，但是并没有Excel一样方便调整与多样
```{code-cell} ipython3
:tags: [output_scroll]

pd.pivot_table(df,index=["地址","学历"],values=["薪资水平"])
```

### 20 - vlookup


#### `Excel`



VLOOKUP算是EXCEL中最核心的功能之一了，我们用一个简单的数据来进行示例

```{figure} gif/vlookup.gif
:width: 600px
:align: center
```

#### `Pandas`


在Pandas中没有现成的vlookup函数，所以实现匹配查找需要一些步骤，首先我们读取该表格
```{code-cell} ipython3
df1 = pd.read_excel("vlookup.xlsx")
df1
```

接着将该dataframe切分为两个
```{code-cell} ipython3
df2 = df1[["序号","科目","成绩","排名"]]
df2
```

```{code-cell} ipython3
df3 = df1[["序号.1","科目.1","成绩.1","排名.1"]]
df3.columns = ["序号","科目","成绩","排名"]
df3 = df3.loc[0:0]
df3
```

最后修改索引并使用update进行两表的匹配
```{code-cell} ipython3
df2 = df2.set_index("序号")
df3 = df3.set_index("序号")
df3.update(df2)
df3
```