# Pandas 对比 R/R libraries

> 为了方便长期使用 Excel 的用户转到 Pandas，我将结合官方文档对部分操作进行对比

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



## Transforming

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
