#!/usr/bin/env python
# coding: utf-8

# (content:jupyter)=
# 
# # Jupyter Notebook 进阶技巧
# 
# 无论你之前是使用何种 IDE 来进行 Python 数据分析，我都建议你转到 `Jupyter Notebook`，它是基于网页的用于交互计算的应用程序，支持在网页页面中直接编写代码和运行代码，代码的运行结果也会直接在代码块下显示。
# 
# 有关 `Jupyter Notebook` 安装与使用，可以参考 [anaconda](../chapter0/Python安装.md) 安装与配置，本页面将分享一些常见的快捷键、魔法命令、插件，来帮助你更高效的进行数据分析。
# 
# ## 快捷键
# 
# 在使用 `Jupyter Notebook` 时，有很多快捷键可以帮助我们更快的进行相关操作，下面是 macos 下的部分快捷键（Windows可以类比）
# 
# ### 命令模式
# 
# 在任意位置按下 `ESC` 以进入命令模式
# 
# | 快捷键 | 功能                         | 快捷键 | 功能                                     |
# | ------ | ---------------------------- | ------ | ---------------------------------------- |
# | F      | 查找并且替换                 | A      | 在上面插入代码块                         |
# | ↩      | 进入编辑模式                 | B      | 在下面插入代码块                         |
# | ⌘⇧F    | 打开命令配置                 | X      | 剪切选择的代码块                         |
# | ⌘⇧P    | 打开命令配置                 | C      | 复制选择的代码块                         |
# | P      | 打开命令配置                 | ⇧V     | 粘贴到上面                               |
# | ⇧↩     | 运行代码块, 选择下面的代码块 | V      | 粘贴到下面                               |
# | ⌘↩     | 运行选中的代码块             | Z      | 撤销删除                                 |
# | ⌥↩     | 运行代码块并且插入下面       | D,D    | 删除选中单元格                           |
# | Y      | 把代码块变成代码             | ⇧M     | 合并选中单元格 |
# | M      | 把代码块变成标签             | ⌘S     | 保存并检查                               |
# | R      | 清除代码块格式               | S      | 保存并检查                               |
# | K      | 选择上面的代码块             | ⌃L     | autopep8 selected  cell(s)               |
# | ↑      | 选择上面的代码块             | ⌃⇧L    | autopep8 the whole  notebook             |
# | ↓      | 选择下面的代码块             | Esc    | 关闭页面                                 |
# | J      | 选择下面的代码块             | Q      | 关闭页面                                 |
# 
# 
# ### 编辑模式
# 
# 编辑任意单元格以进入编辑模式
# 
# | 快捷键  | 功能                         | 快捷键 | 功能                         |
# | ------- | ---------------------------- | ------ | ---------------------------- |
# | ⇥       | 代码完成或缩进               | ⌘↑     | 跳到单元格起始处             |
# | ⇧⇥      | 工具提示                     | ⌘↓     | 跳到单元格最后               |
# | ⌘]      | 缩进                         | ⌥←     | 跳到单词左边                 |
# | ⌘[      | 取消缩进                     | ⌥→     | 跳到单词右边                 |
# | ⌘A      | 全选                         | ⌥⌫     | 删除前面的单词               |
# | ⌘Z      | 撤销                         | ⌥⌦     | 删除后面的单词               |
# | ⌘/      | 评论                         | ⌘⇧Z    | 重做                         |
# | ⌘D      | 删除整行                     | ⌘⇧U    | 重新选择                     |
# | ⌘S      | 保存并检查                   | ⌃M     | 进入命令行模式               |
# | ⌃L      | autopep8 selected  cell(s)   | Esc    | 进入命令行模式               |
# | ⌃⇧L     | autopep8 the whole  notebook | ⌘⇧F    | 打开命令配置                 |
# | ↓       | 光标下移                     | ⌘⇧P    | 打开命令配置                 |
# | ↑       | 光标上移                     | ⇧↩     | 运行代码块, 选择下面的代码块 |
# | ⌥↩      | 运行代码块并且插入下面       | ⌘↩     | 运行选中的代码块             |
# 
# ## 魔法命令
# 
# 在 Jupyter Notebook 中，使用 `%lsmagic` 可以列出全部魔法命令
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011217267.png
# :width: 80%
# :align: center
# ```
# 
# 下面，我将分享一些好用的 `Jupyter Notebook` 魔法命令
# 
# ```{admonition} 注意
# :class: attention
# 
# 以下内容仅限在 `Jupyter Notebook` 中使用，将代码打包至命令行或者其他 IDE 则不会生效 
# ```
# 
# 
# 
# ### 输出全部变量
# 
# 在单元格内执行 `%whos` 可以输出当前工作环境下的全部
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011517224.png
# :width: 80%
# :align: center
# ```
# 
# ### 计算程序执行时间
# 
# 在单元格开头添加 `%%time` 可以自动计算该单元格内代码执行所需时间
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011525607.png
# :width: 80%
# :align: center
# ```
# 
# ### 输出历史命令
# 
# 如果你删除并忘记了之前执行过的某条代码，可以使用 `%history` 来查看该notebook启动后执行过的全部命令
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011528725.png
# :width: 80%
# :align: center
# ```
# ### 执行本地脚本
# 
# 使用 `%run` 加上脚本路径可以在单元格内执行本地的 Python 脚本。
# 
# ### 写入本地文件
# 
# 使用 `%%writefile` 加上文件名可以将当前单元格内容保存至本地文件。
# 
# ### 查询当前工作目录
# 
# 使用 `%pwd` 可以输出当前 `ipynb` 文件所在的绝对路径
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011538607.png
# :width: 80%
# :align: center
# ```
# 
# ### 输出 latex
# 
# 使用 `%%latex` 可以输出 Latex 编译的内容
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011541784.png
# :width: 80%
# :align: center
# ```
# 
# 
# 上面就是一些我常用的魔法命令，此外如果你对任何命令想进一步了解，都可以在对应命令后添加 `?` 来查看更多使用方法
# ```{figure} https://pic.liuzaoqi.com/picgo/202201011535417.png
# :width: 80%
# :align: center
# ```
# 
# ## 插件
# 
# 除了上面介绍的一些快捷键可以极大的提高工作效率，在 `Jupyter Notebook` 中还可以安装第三方插件来提升使用体验。
# 
# 若要想使用这些插件，首先需要安装相关依赖，从命令行/终端切换到当前工作环境，并执行下方代码进行安装
# ```
# pip install jupyter_contrib_nbextensions && jupyter contrib nbextension install
# ```
# 
# 之后重新启动 `Jupyter Notebook` 并点击 `nbextensions` 即可进入插件配置页面
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311043443.png
# :width: 80%
# :align: center
# ```
# 
# 下面，我讲分享一些好用的 `Jupyter Notebook` 插件。
# 
# ###  Table of Contents
# 
# 如果你在一个 Jupyter Notebook 中同时开启了十几个单元格，那你想跟踪所有单元格就会有些困难。Table of Contents 通过添加 TOC 链接解决了这个问题，通过 TOC 链接你可以定位到页面中的任何位置。
# 
# 并且在使用 [Pandas进阶修炼300题](https://mp.weixin.qq.com/s/GW6OxfwIp2X8p2X9fcQZOg)时开启目录插件，可以得到最完美的体验！
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311046107.png
# :width: 80%
# :align: center
# ```
# 
# 
# ### Autopep8
# 
# 大多数利用 Jupyter Notebook 进行数据分析的用户并不是专业的 Python 开发，在代码编辑规范上并没有太注意，并且有时代码越写越长并不易于分享别人阅读。
# 
# 这时可以使用 `Autopep8` 来快速格式化自己的代码，只需要点击插件按钮即可将代码整理成规范、易于阅读的形式
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311302647.gif
# :width: 80%
# :align: center
# ```
# 
# 
# ### ExecuteTime
# 
# 在 Python 中有很多方法计算某段代码的执行时间，在 Jupyter Notebook 中也支持直接输出某个单元格的执行耗时，不用写代码也能评估代码效率
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311258263.png
# :width: 80%
# :align: center
# ```
# 
# 
# 只需要激活 `ExecuteTime` 插件即可
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311257531.png
# :width: 80%
# :align: center
# ```
# 
# ### nbdime
# 
# 使用 nbdime 可以快速对比你的 `Jupyter Notebook` 不同版本之间的差异
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311300451.png
# :width: 80%
# :align: center
# ```
# 
# ### Variable Inspector
# 
# 使用 Variable Inspector 可以让你快速看到当前 Notebook 页面定义了哪些变量以及变量的基本信息
# 
# ```{figure} https://pic.liuzaoqi.com/picgo/202112311314291.png
# :width: 80%
# :align: center
# ```
