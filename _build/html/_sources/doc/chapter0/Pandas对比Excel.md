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

```{table}
:width: 200px

| pandas &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      | Excel  |
| ----------- | ------ |
| DataFrame | 工作表 |
| Series   | 列     |
| Index     | 索引   |
| row         | 行     |
| NaN       | 空值   |

```

### DataFrame

`pandas` 中的 `dataframe` 类似于`Excel` 工作表。虽然一个 `Excel` 工作簿可以包含多个工作表，但通常情况下 `pandas.DataFrame`是独立存在的。

### Series

`Series`是表示 `DataFrame`一列的数据结构。使用 `Series` 类似于引用电子表格中的一列。

### Index

每个 `DataFrame` 和 `Series` 都有一个 `Index`，它是数据行的标签。在`pandas`中，如果没有指定索引，则默认使用RangeIndex(第一行= 0，第二行= 1，等等)，类似于电子表格中的行标题/数字。



在 `pandas` 中，索引可以设置为一个(或多个)惟一值，这就像在工作表中有一列用作行标识符一样。与大多数电子表格不同，这些Index值实际上可以用来引用行。(注意，这可以在Excel的结构化引用中完成。)例如，在电子表格中，您可以引用第一行为 `A1:Z1`，而在 pandas 中，您可以使用`population .loc['Chicago']`。



## 常见操作对比

### 数据读取

#### Excel

Excel读取本地数据需要打开目标文件夹选中该文件并打开

![](https://mmbiz.qpic.cn/mmbiz_gif/2GcSFhuAFlBtFJ5icGS87d9XrWRWhshFmgiammrwwf1KPMuyon5JESMPqvJ7dOqvawgjNAJ4lkZTNnUO993nHBEA/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

 #### Pandas



Pandas支持读取本地Excel、txt文件，也支持从网页直接读取表格数据，只用一行代码即可，例如读取上述本地Excel数据可以使用`pd.read_excel("示例数据.xlsx")`

```{code-cell} ipython3
:tags: [output_scroll]

import pandas as pd
pd.read_excel("示例数据.xlsx") #将示例数据.xlsx放在该Notebook同一文件夹下
```

### 数据生成


#### Excel


以生成**10\*2的0—1均匀分布随机数矩阵**为例，在Excel中需要使用`rand()`函数生成随机数，并手动拉取指定范围

![](https://mmbiz.qpic.cn/mmbiz_gif/2GcSFhuAFlBtFJ5icGS87d9XrWRWhshFmH7v9mibQIU7Cm7JdAhQLIcPzLnBeG5aBlhZ6U8LOWCibfh5ocCOK1vmQ/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

#### Pandas


在Pandas中可以结合NumPy生成由指定随机数(均匀分布、正态分布等)生成的矩阵，例如同样生成**10\*2的0—1均匀分布随机数矩阵**为，使用一行代码即可：`pd.DataFrame(np.random.rand(10,2))`

```{code-cell} ipython3
import numpy  as np
pd.DataFrame(np.random.rand(10,2))
```

