## 功能描述：

参考 [GitHub push 过程中的 time out 问题](https://blog.csdn.net/CynthiaLLL/article/details/106611164) 一文中介绍的解决办法，写了个快速完成操作的脚本。


## 使用前设置：

找到  `C:\Windows\System32\drivers\etc` 目录下的hosts文件，右键-属性，选择安全，为本机上用户增加修改与写入的权限。


## 编写与测试环境

* python 3.6.13

* 通过 conda 配置了 requests、lxml、bs4 库

* Windows 11 64位
