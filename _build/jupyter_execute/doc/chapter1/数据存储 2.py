#!/usr/bin/env python
# coding: utf-8

# # 数据存储

# ```{admonition} 在线刷题
# :class: seealso
# 
# 检查 or 强化 `Pandas` 数据分析操作？<a href="https://www.heywhale.com/mw/project/6146c0318447b8001769ff20" target="_blank">👉在线体验「Pandas进阶修炼300题」</a>
# ```

# ```{note} 
# 本页面代码可以[在线编辑、执行](../指引/在线执行.md)！
# ```

# ## 保存为 CSV
# 
# 
# 将数据保存为 `csv` 格式至当前目录下（文件名任意）

# In[ ]:


data.to_csv("out.csv",encoding = 'utf_8_sig')


# ## 指定列保存
# 
# 
# 
# 将 [读取 Excel 文件](读取Excel文件.ipynb) 中读取到的数据保存为 `csv` 格式至当前目录下（文件名任意），且只保留`positionName、salary`两列

# In[ ]:


data.to_csv("out.csv",encoding = 'utf_8_sig',columns=['positionName','salary'])


# ## 取消索引
# 
# 
# 将 [读取 Excel 文件](读取Excel文件.ipynb) 中读取到的数据保存为 `csv` 格式至当前目录下（文件名任意），且取消每一行的索引

# In[ ]:


data.to_csv("out.csv",encoding = 'utf_8_sig',index = False)


# ## 标记缺失值
# 
# 
# 在上面的基础上，在保存的同时，将缺失值标记为`'数据缺失'`

# In[ ]:


data.to_csv("out.csv",encoding = 'utf_8_sig',index = False,na_rep = '数据缺失')


# ## 保存为 ZIP
# 
# 
# 将上面的数据保存至 `zip` 文件，解压后出现 `out.csv`

# In[ ]:


compression_opts = dict(method='zip',
                        archive_name='out.csv')  
data.to_csv('out.zip', index=False,
          compression=compression_opts)  


# ## 保存为 Excel 
# 
# 
# 
# 将数据保存为 `xlsx` 格式至当前目录下（文件名任意）

# In[ ]:


data.to_excel("test.xlsx")


# ## 保存为 JSON
# 
# 将数据保存为 `json` 格式至当前目录下（文件名任意）

# In[ ]:


data.to_json("out.json")


# ## 保存为 Markdown

# 将数据转换为 `markdown` 形式表格，这样可以直接复制进 `.md` 文件中使用

# In[ ]:


data.head().to_markdown(index = None)


# ## 保存为 Html
# 
# 将数据保存为 `html` 格式至当前目录下（文件名任意），并进行如下设置
# - 取消行索引
# - 标题居中对齐
# - 列宽100

# In[ ]:


data.to_html("out.html", col_space=100,index = None,justify = 'center',border = 1)

