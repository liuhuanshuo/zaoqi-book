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

# Python 安装与环境配置

本页面将引导各位读者如何在 Windows 下安装配置 Python 环境

- 如何下载安装 Python 
- 如何下载安装 Anaconda
- 如何下载安装sublime 并执行你的第一个 Python 程序

注意，由于每个人的机器不同，每个人的初始环境也不同，以下的安装教程不一定能够让所有人都复现，我已经尽量的详细讲解每一个步骤，如果你有遇到问题可以先进行百度，善用搜索是一个程序员的基本素养。



## 安装 Python

Python可以从官网下载，也可以通过`anaconda`一键安装，下面是**从官网下载安装的步骤**。

首先进入 Python 官网 `https://www.python.org/`，在 `Downloads` 下拉菜单中的右半部分直接点击 `python3.x.x` 版本即可下载，**它会自动下载32位的版本**
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151806966847.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

如果想下载64位的，或者其他版本的，可以直接点击列表中的 Windows 跳转到如下列表图，可以选择自己心仪的版本（文末也有下载好的百度云链接）
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151810723887.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151811616906.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


下载完成后，是一个 `.exe` 后缀的文件，双击安装即可。先点击图中的 1 勾选上，再点击 2 安装：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151812086917.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

安装完毕后直接在搜索中输入 **cmd** 调出命令行，或者快捷键**win+R**

**然后输入 python3 即可进入 Python 环境**
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151812324634.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


如果是快速安装，需要再确认下 Python 的安装位置，在电脑中搜索 "Python"
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151812714831.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


右键，选择“打开文件位置”，选择 Python 程序的快捷方式后点击右键 -> 属性：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151819050287.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


在“起始位置”即可获取安装位置，我的显示：`C:\Users\chenx\AppData\Local\Programs\Python\Python38-32\` 

建议复制或记住这个步骤，下文配置环境时会需要这一路径。



## 配置环境变量

现在进入“我的电脑”或“此电脑”，空白处右击选择“属性”

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/10/img8.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


选择“高级系统设置” -> 选“环境变量” -> 在“系统变量”中选中“Path”，再点“编辑” -> 再点“编辑文本”，具体可以参考如下图示

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151823202345.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151823314187.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```



```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151823400190.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151823470963.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




接着在变量值中加上 `;Python路径`，即 `;C:\Users\chenx\AppData\Local\Programs\Python\Python38-32\` （这里要替换成刚刚让大家复制的路径）点击确定：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151824090104.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

至此，Python 的环境变量配置就完成了！



## Anaconda 下载、配置及使用

Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。

如果你觉得上面从官网下载安装比较复杂，使用anaconda可以一键安装，并且后续的**代码的逐行运行将在Anaconda下的Jupyter notebook中演示**。

首先进入官网 `https://www.anaconda.com/products/individual`，并按照如下步骤下载安装包（文末也有下载好的百度云链接）
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151825289761.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151825403522.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

下载后点击安装，过程也很简单，直接依照默认即可，需要注意的依然是勾选环境变量：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151825601962.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

安装完，打开cmd，输入conda，若不提示无效命令，则表明配置成功，如果提示无效命令，则需要按照以下命令进行配置。


首先，用之前类似的方法获取 Anaconda 的安装路径，我的是 `C:\Users\chenx\Anaconda3` ，在这个路径后加上 `\Scripts`  变为 `C:\Users\chenx\Anaconda3\Scripts` 这个路径为需要添加进系统变量的路径，位置如前所述，为 **控制面板\系统和安全\系统\高级系统设置\环境变量\用户变量\PATH**

进入“我的电脑”或“此电脑”，空白处右击选择“属性”
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151827602789.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


选择“高级系统设置” -> 选“环境变量” -> 在“系统变量”中选中“Path”，再点“编辑” -> 再点“编辑文本”

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151827660554.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151827717779.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151827795367.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```



```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151827838768.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


在变量值中加上 `;Anaconda脚本路径`，即 `;C:\Users\chenx\Anaconda3\Scripts` (此处应替换成你的路径)点击确定即完成配置！

## 如何使用Jupyter notebook

接下来我们尝试如何打开 `Jupyter Notebook`，这是我们主要编写程序的IDE，可以方便逐行运行观察结果利于理解！

在搜索框中输入 Anaconda，打开 **Anaconda Prompt (Anaconda3)** 或者 **Anaconda Powershell Prompt (Anaconda3)** 都可以

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151828413927.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


输入 **jupyter notebook** 如下图：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151828465525.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




回车后就可以打开 `Jupyter Notebook` 了！注意这个命令行要保持不能关闭：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830504412.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


Jupyter Notebook 进入后的界面如下图：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830667436.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


接下来创建一个新文件夹，以后我们写代码都在这个文件夹里存放，命名为 `Anaconda Practice`
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830746693.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


往下拉，找到 `Untitled Folder` 将其选中：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830806772.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


重新往上拉，点击 **Rename**
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830873878.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830931667.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151830980169.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


即创建成功，点击进入，然后创建 Python3 文件：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831026860.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831069329.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


在 **In** 中输入内容，点击运行后，就可以显示该步的结果，非常方便！



## Sublime Text 下载、配置及使用

Sublime Text 是一款跨平台代码编辑器，**非常方便运行整个 Python 代码脚本**

首先进入官网 `https://www.sublimetext.com/`（文末也有下载好的百度云链接）

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831291087.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


下载后双击应用程序打开，一路直接点选下一步进行安装，注意在安装时勾选 Add to explorer context menu，这样在右键单击文件时就可以直接使用 Sublime Text 打开

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831404078.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




Windows 搜索栏中输入 Sublime Text 并点击打开：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831461482.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


对 Sublime Text 进行配置，依次如下点选：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831517131.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


产生了如下文件：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831559539.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


要将上述内容换成如下内容：

```shell
{
    "cmd": [电脑中python.exe的路径,"-u","$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "encoding": "cp936" 
}
```

之前我们已经确认过 Python 的安装路径。在电脑中搜索 "Python"

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831699804.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


右键，选择“打开文件位置”，选择 Python 程序的快捷方式后点击右键 -> 属性：

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831741706.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```




这次我们不是在“起始位置”获取安装位置，而是在目标中获取 `python.exe` 所在的位置：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831792379.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


我的显示 `C:\Users\chenx\AppData\Local\Programs\Python\Python38-32\python.exe` ，那么就可以在Sublime修改配置了！

```shell
{
    "cmd": ["C:\\Users\\chenx\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe","-u","$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "encoding": "cp936" 
}
```

注意区分正反斜杠，路径中的斜杠都改为 `\\` 或者 `/` 

然后按 `Ctrl+S`，将文件保存在默认路径，文件名命名为“Python3”

打开 Tools > Build System，选择新建好的 Python3 即可：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831873282.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


点页面上的 X 关闭改文件，重新创建新文件：
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831930552.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


简单输入代码后，`Ctrl+S` 保存，命名为 `test.py`
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151831973621.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```


可以观察到代码变色了，此时按 `Ctrl+B` 运行，如果能成功运行说明已经配置完成！
```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/08/16151832021191.jpg?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```

## 下载

最后如果你需要 `Python 3.9`，`Anaconda 3`，`Sublime Text 3` 安装包，可以在关注公众号「早起Python」，关注后回复安装包，一键获取与下载

```{figure} http://liuzaoqi.oss-cn-beijing.aliyuncs.com/2021/03/10/img45.png?域名/sample.jpg?x-oss-process=style/stylename
:width: 700px
:align: center
```
