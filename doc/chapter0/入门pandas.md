---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(content:code-outputs)=

# Pandas 入门

> 在本页面，我将对 `Pandas` 数据分析做一个快速、不全面的概述，以帮助您快速入门，

```{admonition} 在线刷题
:class: seealso

检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
```


## Pandas是什么

[Pandas](https://pandas.pydata.org/)是一种基于 Python 的快速、强大、灵活且易于使用的开源数据分析和操作工具。

以下是 Pandas 擅长的一些事情：

- 轻松处理浮点和非浮点数据中的缺失数据
- 强大、灵活的分组功能，可对数据集执行拆分-应用-组合操作，用于聚合和转换数据
- 简单的将其他Python和NumPy的数据结构不同索引的数据转换成pandas对象
- 直观的合并和连接数据集
- 灵活地重塑和旋转数据集
- 强大的 IO 工具，用于从平面文件（CSV 和分隔符）、Excel 文件、数据库加载数据，以及从超快HDF5 格式保存/加载数据
- 时间序列特定功能：日期范围生成和频率转换、移动窗口统计、日期偏移和滞后。

这里的许多原则是为了解决使用其他语言/科学研究环境时经常遇到的缺陷。对于数据科学家来说，处理数据通常分为多个阶段:对数据进行筛选和清理，**对数据进行分析/建模，然后将分析结果组织成适合绘图或表格显示**。而 Pandas 是完成所有这些任务的理想工具。

## 安装与使用

安装 pandas 需要基础环境是 Python，如果你还没有 Python 可以[点击查看如何安装与配置](Python安装.md)

现在假定你已经安装完毕，便可以使用如下命令通过 pip 安装 pandas
```
pip install pandas
```
安装成功后，我们就可以导入 pandas 包使用：

```{code-cell} ipython3
import pandas as pd
```

另外需要注意的是，本网站的教程都将基于 `pandas == 1.1.3` 进行展开，你可以使用下方代码检查你的 pandas 版本，在出现和教程不一致的问题时，优先考虑检索版本差异！
```{code-cell} ipython3
pd.__version__
```


## Pandas的数据结构

在使用 `pandas` 之前我们需要对其数据结构进行初步的了解，至少要知道我们在处理什么样的数据。 
### DataFrame
通常情况下我们都是对 `pd.DataFrame` 进行操作，其基本结构如下图所示

```{figure} https://pic.liuzaoqi.com/picgo/202112111201158.png
:width: 600px
:align: center
```

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame)是一种二维数据结构，我们可以在每一个 `cell` 中存储不同类型的数据（包括字符串、整数、浮点值、分类数据等），你可以将它想象成 Excel 表格、SQL表或者 R中的 `data.frame`。

例如可以用下面的代码创建一个 DataFrame 用于存储泰坦尼克号的乘客数据。
```{code-cell} ipython3
df = pd.DataFrame( {"Name": [
              "Braund, Mr. Owen Harris",
              "Allen, Mr. William Henry",
              "Bonnell, Miss. Elizabeth",],
              "Age": [22, 35, 58],
              "Sex": ["male", "male", "female"],})
df
```
这和我们在如下的 Excel 表中输入是相似的，只不过用代码的形式可以更方便的进行后续的分析，更多有关导入、创建 `DataFrame` 的方法，可以查阅[数据加载与存储](../chapter1/chapt1.md)

```{figure} https://pic.liuzaoqi.com/picgo/202112111138179.png
:width: 500px
:align: center
```
### Series

此外，另一个需要关注的数据结构是 `pd.Series` ，`pandas`的每一列都是一个 Series 

```{figure} https://pic.liuzaoqi.com/picgo/202112111125570.png
:align: center
```

例如我们只对 age 列感兴趣，可以使用 `[]` 将其筛选出来，结果是便是一个`pd.Series`
```{code-cell} ipython3
df["Age"]
```


```{admonition} 注意
:class: attention

Series 没有列标签，只有行标签因为它只是 DataFrame 的一个列，您可以查看[官方文档](https://pandas.pydata.org/docs/user_guide/dsintro.html#series)以获得更多相关资料。
```

如果你想了解更多的筛选数据方法，可以阅读[数据筛选](../chapter3/数据筛选.ipynb)


## 利用 DataFrame 或 Series 进行分析

在上面了解了 Pandas 的基本数据结构之后，现在，我将介绍一些简单的分析代码，例如想知道乘客的最大年龄，我们可以通过 DataFrame 选择 Age 列并应用 `max()` 来实现
```{code-cell} ipython3
df["Age"].max()
```
正如 `max()` 方法所示，我们可以使用DataFrame进行操作。pandas提供了很多功能，每个功能都是可以应用于DataFrame或Series的方法。因为方法是函数，所以不要忘记使用括号()。

除了返回数值，大部分 pandas 操作都会返回一个DataFrame或一个Series。例如若果对数据表的数值数据的一些基本统计感兴趣，可以使用 `describe()` 来得到一个新的 dataframe
```{code-cell} ipython3
df.describe()
```

就像上面介绍的简单案例，利用 Pandas 进行数据分析通常包括三个流程
1. 导入包（`import pandas as pd`）
2. 读取或创建 DataFrame
3. 使用不同的 pandas 函数进行分析

更多的分析方法我已经按照操作场景进行分类整理，你可以点击左边的目录进行相关内容的查看。

## 十分钟入门Pandas



