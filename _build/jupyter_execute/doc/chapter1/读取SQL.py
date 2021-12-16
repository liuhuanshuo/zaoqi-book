#!/usr/bin/env python
# coding: utf-8

# # 读取 SQL

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 常规读取
# 
# 虽然我们使用 `pandas` 就是看中其相对于 `SQL` 简单一点的操作，但毕竟存数据还需要使用 `SQL`，如果先将数据导出再`pandas`读取并不是一个合适的选择，幸运的是在 `pandas` 中支持直接从 `sql` 中查询并读取。
# 
# 为了方便统一操作，我们先执行下面的代码创建数据。

# In[1]:


from sqlite3 import connect
import pandas as pd
conn = connect(':memory:')
df = pd.DataFrame(data=[[0, '10/11/12'], [1, '12/11/10']],
                  columns=['int_column', 'date_column'])
df.to_sql('test_data', conn)


# 下面示例代码即是在 `pandas` 中直接使用 `SQL` 语句操作数据库，并将结果返回为 `dataframe`

# In[2]:


pd.read_sql('SELECT int_column, date_column FROM test_data', conn)

