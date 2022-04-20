#!/usr/bin/env python
# coding: utf-8

# # 数据编码的十种方式
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
# ```
# 
# 在使用`Python`进行机器学习时，很多算法都需要我们对分类特征进行转换（编码），即根据某一列的值，新增（修改）一列。
# 
# 这个操作在`pandas`中也有多种解决方案，本文就将介绍十种方法，代码拿走就用，希望你在遇到不同类型的数据时，可以灵活使用。
#   
# 下面先创建用于示例的数据👇
# 

# In[1]:


import sklearn
sklearn.__version__


# In[152]:


import pandas as pd
df = pd.DataFrame({
    "Sex": pd.Series(['Male','Female','Male','Male','Male','Female','Male','Male','Female','Female']),
    "Course Name": pd.Series(['Python','Java','C','Sql','Linux','Python','Python','Java','C','Php']),
    "Score":[95,85,75,65,55,95,75,65,55,85]})

df


# ## 数值型数据编码

# ### 1 - 使用自定义函数 + 循环遍历
# 
# 首先然是最简单，最笨的方法，自己写一个函数来转换数据，并用循环遍历，肯定就是一个`def`加一个`for`

# In[153]:


df1 = df.copy()

def myfun(x):
    if x>90:
        return 'A'
    elif x>=80 and x<90:
        return 'B'
    elif x>=70 and x<80:
        return 'C'
    elif x>=60 and x<70:
        return 'D'
    else:
        return 'E'
    
df1['Score_Label'] = None
for i in range(len(df1)):
    df1.iloc[i,3] = myfun(df1.iloc[i,2])
    
df1


# 这段代码，相信所有人都能看懂，简单好想但比较麻烦
# 
# 有没有更简单的办法呢？`pandas`当然提供了很多高效的操作的函数，继续往下看。

# ### 2 - 使用 map + 自定义函数
# 
# 现在，可以使用`map`来干掉循环（虽然本质上也是循环）

# In[154]:


df2 = df.copy()

def mapfun(x):
    if x>90:
        return 'A'
    elif x>=80 and x<90:
        return 'B'
    elif x>=70 and x<80:
        return 'C'
    elif x>=60 and x<70:
        return 'D'
    else:
        return 'E'

df2['Score_Label'] = df2['Score'].map(mapfun)
df2


# ### 3 - 使用 apply + 匿名函数
# 
# 如果还想简洁代码，可以使用`自定义函数 + apply`来干掉自定义函数(结果和上面是一致的，只不过这么写容易被打。)

# In[184]:


df3 = df.copy()
df3['Score_Label'] = df3['Score'].apply(lambda x: 'A' if x > 90 else (
    'B' if 90 > x >= 80 else ('C' if 80 > x >= 70 else ('D' if 70 > x >= 60 else 'E'))))
df3


# ### 4 - 使用cut
# 
# 现在，让我们继续了解更高级的`pandas`函数，依旧是对 `Score` 进行编码，使用`pd.cut`，并指定划分的区间后，可以直接帮你分好组

# In[156]:


df4 = df.copy()
bins = [0, 59, 70, 80, 100]
df4['Score_Label'] = pd.cut(df4['Score'], bins)
df4


# 也可以直接使用`labels`参数来修改对应组的名称，是不是方便多了

# In[157]:


df4['Score_Label_new'] = pd.cut(df4['Score'], bins, labels=[
                                'low', 'middle', 'good', 'perfect'])
df4


# ### 5 - 使用 sklearn 二值化
# 
# 既然是和机器学习相关，`sklearn`肯定跑不掉，如果需要新增一列并判定成绩是否及格，就可以使用`Binarizer`函数，代码也是简洁好懂

# In[158]:


from sklearn.preprocessing import Binarizer

df5 = df.copy()
binerize = Binarizer(threshold = 60)
trans = binerize.fit_transform(np.array(df1['Score']).reshape(-1,1))
df5['Score_Label'] = trans

df5


# ## 文本型数据编码
# 
# 下面介绍更常见的，对文本数据进行转换打标签。例如新增一列，将性别男、女分别标记为0、1

# ### 6 - 使用 replace
# 
# 首先介绍`replace`，但要注意的是，上面说过的自定义函数相关方法依旧是可行的

# In[160]:


df6 = df.copy()
df6['Sex_Label'] = df6['Sex'].replace(['Male','Female'],[0,1])
df6


# 上面是对性别操作，因为只有男女，所以可以手动指定0、1，但要是类别很多，也可以使用`pd.value_counts()`来自动指定标签，例如对`Course Name`列分组

# In[161]:


df6 = df.copy()
value = df6['Course Name'].value_counts()
value_map = dict((v, i) for i,v in enumerate(value.index))
df6['Course Name_Label'] = df6.replace({'Course Name':value_map})['Course Name']
df6


# ### 7 - 使用map
# 
# 额外强调的是，新增一列，一定要能够想到`map`

# In[162]:


df7 = df.copy()
Map = {elem:index for index,elem in enumerate(set(df["Course Name"]))}
df7['Course Name_Label'] = df7['Course Name'].map(Map)
df7


# ### 8 - 使用astype
# 
# 这个方法应该很多人不知道，这就属于上面提到的知乎问题，能实现的方法太多了

# In[163]:


df8 = df.copy()
value = df8['Course Name'].astype('category')
df8['Course Name_Label'] = value.cat.codes
df8


# ### 9 - 使用 sklearn
# 
# 同数值型一样，这种机器学习中的经典操作，`sklearn`一定有办法，使用`LabelEncoder`可以对分类数据进行编码

# In[164]:


from sklearn.preprocessing import LabelEncoder
df9 = df.copy()
le = LabelEncoder()
le.fit(df9['Sex'])
df9['Sex_Label'] = le.transform(df9['Sex'])
le.fit(df9['Course Name'])
df9['Course Name_Label'] = le.transform(df9['Course Name'])
df9


# 一次性转换两列也是可以的

# In[165]:


from sklearn.preprocessing import LabelEncoder
df9 = df.copy()
le = OrdinalEncoder()
le.fit(df9[['Sex','Course Name']])
df9[['Sex_Label','Course Name_Label']] = le.transform(df9[['Sex','Course Name']])

df9


# ### 10 - 使用factorize
# 
# 最后，再介绍一个小众但好用的`pandas`方法，我们需要注意到，在上面的方法中，自动生成的`Course Name_Label`列，虽然一个数据对应一个语言，因为避免写自定义函数或者字典，这样可以自动生成，所以大多是无序的。
# 
# 如果我们希望它是有序的，也就是 `Python` 对应 `0`，`Java`对应`1`，除了自己指定，还有什么优雅的办法？这时可以使用`factorize`，它会根据出现顺序进行编码

# In[166]:


df10 = df.copy()
df10['Course Name_Label'] = pd.factorize(df10['Course Name'])[0]
df10


# 结合匿名函数，我们可以做到对多列进行有序编码转换

# In[168]:


df10 = df.copy()
cat_columns = df10.select_dtypes(['object']).columns

df10[['Sex_Label', 'Course Name_Label']] = df10[cat_columns].apply(
    lambda x: pd.factorize(x)[0])
df10


# ```{admonition} 注意
# :class: attention
# 
# 你无需完全记住所有方法与细节，**只需知道有这么个函数能完成这样操作，需要用时能想到，想到再来查就行**。
# ```
