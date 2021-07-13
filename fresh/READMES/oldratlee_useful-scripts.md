🐌 useful-scripts
====================================

<img src="docs/script-logo.png" alt="repo-icon" width="20%" align="right" />

[![Build Status](https://img.shields.io/travis/com/oldratlee/useful-scripts/dev-2.x?logo=travis-ci&logoColor=white)](https://travis-ci.com/github/oldratlee/useful-scripts)
[![GitHub release](https://img.shields.io/github/release/oldratlee/useful-scripts.svg)](https://github.com/oldratlee/useful-scripts/releases)
[![License](https://img.shields.io/github/license/oldratlee/useful-scripts?color=4D7A97)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Chat at gitter.im](https://img.shields.io/gitter/room/oldratlee/useful-scripts?color=46BC99&logo=gitter&logoColor=white)](https://gitter.im/oldratlee/useful-scripts?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)  
[![GitHub Stars](https://img.shields.io/github/stars/oldratlee/useful-scripts)](https://github.com/oldratlee/useful-scripts/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/oldratlee/useful-scripts)](https://github.com/oldratlee/useful-scripts/fork)
[![GitHub issues](https://img.shields.io/github/issues/oldratlee/useful-scripts)](https://github.com/oldratlee/useful-scripts/issues)
[![GitHub Contributors](https://img.shields.io/github/contributors/oldratlee/useful-scripts)](https://github.com/oldratlee/useful-scripts/graphs/contributors)

👉 把平时有用的手动操作做成脚本，这样可以便捷的使用。 ✨


欢迎 👏💖

- 建议和提问，[提交 Issue](https://github.com/oldratlee/useful-scripts/issues/new)
- 贡献和改进，[Fork 后提通过 Pull Request 贡献代码](https://github.com/oldratlee/useful-scripts/fork)
- 分享 平时常用但没有写成脚本的功能（即需求、想法），[提交Issue](https://github.com/oldratlee/useful-scripts/issues/new)
- 提供 自己的好用脚本，[Fork 后提通过 Pull Request 提供](https://github.com/oldratlee/useful-scripts/fork)

本仓库的脚本（如`Java`相关脚本）在阿里等公司（如随身云，见[`awesome-scripts`仓库](https://github.com/Suishenyun/awesome-scripts)说明）的线上生产环境部署使用。

如果你的公司有部署使用，欢迎使用通过 [Issue：who's using | 用户反馈收集](https://github.com/oldratlee/useful-scripts/issues/96) 告知，方便互相交流反馈～ 💘

🔰 快速下载&使用
----------------------

```bash
source <(curl -fsSL https://raw.githubusercontent.com/oldratlee/useful-scripts/release-2.x/test-cases/self-installer.sh)
```

更多下载&使用方式，参见[下载使用](docs/install.md)。

📚 使用文档
----------------------

### ☕ [`Java`相关脚本](docs/java.md)

1. [show-busy-java-threads](docs/java.md#-show-busy-java-threads)  
    用于快速排查`Java`的`CPU`性能问题(`top us`值过高)，自动查出运行的`Java`进程中消耗`CPU`多的线程，并打印出其线程栈，从而确定导致性能问题的方法调用。
1. [show-duplicate-java-classes](docs/java.md#-show-duplicate-java-classes)  
    找出`jar`文件和`class`目录中的重复类。用于排查`Java`类冲突问题。
1. [find-in-jars](docs/java.md#-find-in-jars)  
    在目录下所有`jar`文件里，查找类或资源文件。

### 🐚 [`Shell`相关脚本](docs/shell.md)

`Shell`使用加强：

1. [c](docs/shell.md#-c)  
    原样命令行输出，并拷贝标准输出到系统剪贴板，省去`CTRL+C`操作，优化命令行与其它应用之间的操作流。
1. [coat](docs/shell.md#-coat)  
    彩色`cat`出文件行，方便人眼区分不同的行。
1. [a2l](docs/shell.md#-a2l)  
    按行彩色输出参数，方便人眼查看。
1. [uq](docs/shell.md#-uq)  
    不重排序输入完成整个输入行的去重。相比系统的`uniq`命令加强的是可以跨行去重，不需要排序输入。
1. [ap and rp](docs/shell.md#-ap-and-rp)  
    批量转换文件路径为绝对路径/相对路径，会自动跟踪链接并规范化路径。
1. [cp-into-docker-run](docs/shell.md#-cp-into-docker-run)  
    一个`Docker`使用的便利脚本。拷贝本机的执行文件到指定的`docker container`中并在`docker container`中执行。
1. [tcp-connection-state-counter](docs/shell.md#-tcp-connection-state-counter)  
    统计各个`TCP`连接状态的个数。用于方便排查系统连接负荷问题。
1. [xpl and xpf](docs/shell.md#-xpl-and-xpf)  
    在命令行中快速完成 在文件浏览器中 打开/选中 指定的文件或文件夹的操作，优化命令行与其它应用之间的操作流。

`Shell`开发/测试加强：

1. [echo-args](docs/shell.md#-echo-args)  
    输出脚本收到的参数，在控制台运行时，把参数值括起的括号显示成 **红色**，方便人眼查看。用于调试脚本参数输入。
1. [console-text-color-themes.sh](docs/shell.md#-console-text-color-themessh)  
    显示`Terminator`的全部文字彩色组合的效果及其打印方式，用于开发`Shell`的彩色输出。
1. [parseOpts.sh](docs/shell.md#-parseoptssh)  
    命令行选项解析库，加强支持选项有多个值（即数组）。

### ⌚ [`VCS`相关脚本](docs/vcs.md)

目前`VCS`的脚本都是`svn`分支相关的操作。使用更现代的`Git`吧！ 💥

因为不推荐使用`svn`，这里不再列出有哪些脚本了，如果你有兴趣可以点上面链接去看。
