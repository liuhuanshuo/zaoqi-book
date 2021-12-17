# Pandas 对比 R/R libraries

> 为了方便长期使用 R 的用户转到 Pandas，我将结合官方文档对部分操作进行对比

```{admonition} 在线刷题
:class: seealso

检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
```

本页面将对数据分析中的常见操作，给出 Pandas 和 R 的实现函数对比，以期望读者能够明白

- 功能/灵活性:每个工具可以/不能做什么
- 性能:操作有多快
- 易用性:是否有一个工具更容易使用/更难使用(您可能必须自己判断，通过并排代码比较)

## 数据查询、过滤、抽样

| R                                  | pandas                                                       |
| ---------------------------------- | ------------------------------------------------------------ |
| `dim(df)`                          | `df.shape`                                                   |
| `head(df)`                         | `df.head()`                                                  |
| `slice(df, 1:10)`                  | `df.iloc[:9]`                                                |
| `filter(df, col1 == 1, col2 == 1)` | `df.query('col1 == 1 & col2 == 1')`                          |
| `df[df$col1 == 1 & df$col2 == 1,]` | `df[(df.col1 == 1) & (df.col2 == 1)]`                        |
| `select(df, col1, col2)`           | `df[['col1', 'col2']]`                                       |
| `select(df, col1:col3)`            | `df.loc[:, 'col1':'col3']`                                   |
| `select(df, -(col1:col3))`         | `df.drop(cols_to_drop, axis=1)` 
| `distinct(select(df, col1))`       | `df[['col1']].drop_duplicates()`                             |
| `distinct(select(df, col1, col2))` | `df[['col1', 'col2']].drop_duplicates()`                     |
| `sample_n(df, 10)`                 | `df.sample(n=10)`                                            |
| `sample_frac(df, 0.01)`            | `df.sample(frac=0.01)`                                       |


## 数据排序

| R                         | pandas                                    |
| ------------------------- | ----------------------------------------- |
| `arrange(df, col1, col2)` | `df.sort_values(['col1', 'col2'])`        |
| `arrange(df, desc(col1))` | `df.sort_values('col1', ascending=False)` |



## 数据修改

| R                            | pandas                                              |
| ---------------------------- | --------------------------------------------------- |
| `select(df, col_one = col1)` | `df.rename(columns={'col1': 'col_one'})['col_one']` |
| `rename(df, col_one = col1)` | `df.rename(columns={'col1': 'col_one'})`            |
| `mutate(df, c=a-b)`          | `df.assign(c=df['a']-df['b'])`                      |

## 数据分组

| R                                            | pandas                                     |
| -------------------------------------------- | ------------------------------------------ |
| `summary(df)`                                | `df.describe()`                            |
| `gdf <- group_by(df, col1)`                  | `gdf = df.groupby('col1')`                 |
| `summarise(gdf, avg=mean(col1, na.rm=TRUE))` | `df.groupby('col1').agg({'col1': 'mean'})` |
| `summarise(gdf, total=sum(col1))`            | `df.groupby('col1').sum()`                 |


## 常见操作对比


### 数据切片

````{tabbed} R
在 R 中使用 data.frame按名称访问列
```r
df <- data.frame(a=rnorm(5), b=rnorm(5), c=rnorm(5), d=rnorm(5), e=rnorm(5))
df[, c("a", "c", "e")]
```
或者使用列号来选择
```r
df <- data.frame(matrix(rnorm(1000), ncol=100))
df[, c(1:10, 25:30, 40, 50:100)]
```
````

`````{tabbed} pandas
在 pandas 中同样可以使用列名来访问对应列
```python
df = pd.DataFrame(np.random.randn(10, 3), columns=list("abc"))
df[["a", "c"]]
```
或者使用 loc 访问
```python
df.loc[:, ["a", "c"]]
```
通过结合使用iloc，可以按整数位置选择多个不连续的列。
```python
named = list("abcdefg")
n = 30
columns = named + np.arange(len(named), n).tolist()
df = pd.DataFrame(np.random.randn(n, n), columns=columns)
df.iloc[:, np.r_[:10, 24:30]]
```
`````

### 数据聚合


````{tabbed} R
在R中，可以按如下形式将 dataframe 分成两组并计算均值
```r
df <- data.frame(
  v1 = c(1,3,5,7,8,3,5,NA,4,5,7,9),
  v2 = c(11,33,55,77,88,33,55,NA,44,55,77,99),
  by1 = c("red", "blue", 1, 2, NA, "big", 1, 2, "red", 1, NA, 12),
  by2 = c("wet", "dry", 99, 95, NA, "damp", 95, 99, "red", 99, NA, NA))
aggregate(x=df[, c("v1", "v2")], by=list(mydf2$by1, mydf2$by2), FUN = mean)
```
````

`````{tabbed} pandas
在 pandas 中同样可以使用 groupby 来实现
```python
df = pd.DataFrame(
    {
        "v1": [1, 3, 5, 7, 8, 3, 5, np.nan, 4, 5, 7, 9],
        "v2": [11, 33, 55, 77, 88, 33, 55, np.nan, 44, 55, 77, 99],
        "by1": ["red", "blue", 1, 2, np.nan, "big", 1, 2, "red", 1, np.nan, 12],
        "by2": [
            "wet",
            "dry",
            99,
            95,
            np.nan,
            "damp",
            95,
            99,
            "red",
            99,
            np.nan,
            np.nan,
        ],
    }
)

g = df.groupby(["by1", "by2"])
g[["v1", "v2"]].mean()
```
`````


### match / %in%


````{tabbed} R
在R中选择数据的一种常见方法是使用%in%，它是使用函数match来定义的。%in%用于返回一个逻辑向量，表示是否存在匹配
```r
s <- 0:4
s %in% c(2,4)
```
````

````{tabbed} pandas
在 pandas 中可以通过 isin 实现
```python
s = pd.Series(np.arange(5), dtype=np.float32)
s.isin([2, 4])
```
````

### tapply



````{tabbed} R

Tapply类似于聚合，但数据可能是不规则的，例如使用一个名为 `baseball` 的 `data.frame`，并获得相关统计信息

```r
baseball <-
  data.frame(team = gl(5, 5,
             labels = paste("Team", LETTERS[1:5])),
             player = sample(letters, 25),
             batting.average = runif(25, .200, .400))

tapply(baseball$batting.average, baseball.example$team,
       max)
```
````

````{tabbed} pandas
在 pandas 中可以通过 pivot_table 实现
```python
import random
import string
baseball = pd.DataFrame(
    {
        "team": ["team %d" % (x + 1) for x in range(5)] * 5,
        "player": random.sample(list(string.ascii_lowercase), 25),
        "batting avg": np.random.uniform(0.200, 0.400, 25),
    }
)
baseball.pivot_table(values="batting avg", columns="team", aggfunc=np.max)
```
````

### subset

````{tabbed} R
`query()`方法类似于基R子集函数。在R中，你可能想要得到 `data.frame` 的某行，其中一列的值小于另一列的值:
```r
df <- data.frame(a=rnorm(10), b=rnorm(10))
subset(df, a <= b)
df[df$a <= df$b,]  # note the comma
```
````

````{tabbed} pandas
在 pandas 中可以通过 `query` 来实现
```r
df = pd.DataFrame({"a": np.random.randn(10), "b": np.random.randn(10)})
df.query("a <= b")
```
````

### plyr 

plyr是一个R库，用于数据分析的分离-应用-组合策略。这些函数围绕着三种数据结构R, a代表数组，l代表列表，d代表data.frame。下表显示了如何在Python中映射这些数据结构。

| R          | Python                        |
| ---------- | ----------------------------- |
| array      | list                          |
| lists      | dictionary or list of objects |
| data.frame | dataframe                     |

### ddply

````{tabbed} R
在 R 中还可以使用 ddply 来实现类似聚合的功能
```r
require(plyr)
df <- data.frame(
  x = runif(120, 1, 168),
  y = runif(120, 7, 334),
  z = runif(120, 1.7, 20.7),
  month = rep(c(5,6,7,8),30),
  week = sample(1:4, 120, TRUE)
)

ddply(df, .(month, week), summarize,
      mean = round(mean(x), 2),
      sd = round(sd(x), 2))
```
````

````{tabbed} pandas
在 pandas 同样可以使用 groupby 来实现
```r
df = pd.DataFrame(
    {
        "x": np.random.uniform(1.0, 168.0, 120),
        "y": np.random.uniform(7.0, 334.0, 120),
        "z": np.random.uniform(1.7, 20.7, 120),
        "month": [5, 6, 7, 8] * 30,
        "week": np.random.randint(1, 4, 120),
    }
)
grouped = df.groupby(["month", "week"])
grouped["x"].agg([np.mean, np.std])
```
````

现在，你应该可以看出，使用 pandas 和 使用 R 在数据分析上的异同，并可以快速的从 R 转换到 pandas，尽情的享受 Python 生态。