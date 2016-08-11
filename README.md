### CReply

一款基于 Chrome 扩展的常用回复工具。

#### 功能

**2016-08-10**

* 常用回复 txt 添加管理
* 关键字搜索
* 复制到剪切板

#### 安装使用

**下载并解压为目录 `CReply`，导入 Chrome 扩展 `chrome://extensions/`**

![](http://seeknowing.b0.upaiyun.com/CReply/creply_install.png)

**内容管理**

修改 `CReply/common_reply.txt` 文件，一行一条内容，如：

```
秦时明月汉时关，万里长征人未还。但使龙城飞将在，不教胡马度阴山。
春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。
君自故乡来，应知故乡事。来日绮窗前，寒梅著花未？
松下问童子，言师采药去。只在此山中，云深不知处。
朝辞白帝彩云间，千里江陵一日还。两岸猿声啼不住，轻舟已过万重山。
独在异乡为异客，每逢佳节倍思亲。
白日依山尽，黄河入海流。欲穷千里目，更上一层楼。
```

HTML 格式化

Linux/Mac 执行 `CReply/generate_content.py` 程序：

```
$ python generate_content.py
```

Windows 双击 `GenerateContent.exe`

**演示**

![](http://seeknowing.b0.upaiyun.com/CReply/creply_use.gif)
