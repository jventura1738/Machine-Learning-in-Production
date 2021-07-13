# HelloFlask

这里是《Flask Web 开发实战》（Python Web Development with Flask）的 Meta 仓库，包含第 1-6 章、13 章的示例程序源码和勘误等信息。访问[本书主页](http://helloflask.com/book)查看本书的资源索引、目录、购买链接等详细信息。

P.S. 如果你阅读这本书感到有一点吃力，那么可以先翻一翻《[Flask 入门教程](https://github.com/greyli/flask-tutorial)》。

## 相关资源

* [勘误](http://helloflask.com/book/errata)
* [FAQ](https://github.com/greyli/helloflask/blob/master/faq/faq.md)（常见问题）
* [可改进实现](https://github.com/greyli/helloflask/blob/master/improvement/improvement.md)（可改进的内容描述或代码实现）
* [版本更新记录](https://github.com/greyli/helloflask/blob/master/CHANGES.md)（电子书与实体书版本更新与改进记录）

## 反馈、提问和讨论

* [勘误反馈和改进建议](https://github.com/greyli/helloflask/issues/new/)
* [提问和讨论（HelloFlask 论坛）](https://discuss.helloflask.com) 
* [提问和讨论（GitHub Discussion）](https://github.com/greyli/helloflask/discussions/new)（提问请选择 Q&A 分类，并提供尽可能详细的信息）

欢迎在本书的[豆瓣图书页面](https://book.douban.com/subject/30310340/)、[知乎问题](https://www.zhihu.com/question/296048455)撰写评价，欢迎在你的博客和社交网站分享这本书。

## 示例程序

这个仓库的 demos 文件夹包含本书第一部分的示例程序，每一章对应一个文件夹。为了方便操作，我们把虚拟环境创建在 helloflask 目录，激活以后切换进 helloflask/demos 目录对应的程序子目录再执行 flask run 命令来启动程序。注意不要在 helloflask 目录下创建 .env 文件。 

### 克隆仓库

```
$ git clone https://github.com/greyli/helloflask.git
$ cd helloflask
```
### 创建 & 激活虚拟环境 & 安装依赖包

（下面两种方式二选一）：

Option 1：使用 venv/virtualenv + pip：
```
$ python -m venv env  # Python 2 使用 virtualenv env 命令
$ source env/bin/activate  # Windows 使用 env\Scripts\activate 命令
$ pip install -r requirements.txt
```

对于上面的第一条命令，如果你在 Linux 或 macOS 上使用 Python 3，则使用 `python3 -m venv env`。

Option 2：使用 Pipenv：
```
$ pipenv install --dev
$ pipenv shell
```
如果你还没有安装 Pipenv，那么可以在运行 `pipenv` 命令前通过 pip 安装（`pip install pipenv`）。

### 运行示例程序

每一章的示例程序放在不同的子文件内，以第一章示例程序为例，你需要把工作目录切换到 demos/hello 目录内，然后执行 `flask run` 启动程序：

```
$ cd demos/hello
$ flask run
```
现在使用浏览器打开 http://localhost:5000

通过切换到不同的示例程序目录来运行不同章节的示例程序。比如，下面的命令将会运行第 4 章的示例程序：
```
$ cd demos/form
$ flask run
```

*在书中，每一章的开头都会包含运行实例程序的提示。*

## HelloFlask Projects

以下为本书第二部分各章节对应的示例程序源码：

* [SayHello](https://github.com/greyli/sayhello)： 本书第 7 章示例程序，一个简单的留言板程序。
* [Bluelog](https://github.com/greyli/bluelog)：本书第 8 章示例程序，一个个人博客。
* [Albumy](https://github.com/greyli/albumy)：本书第 9 章示例程序，多人图片社交网站。
* [Todoism](https://github.com/greyli/todoism)：本书第 10 章示例程序，实现了 Web API 和 i18n 支持的 Todo 程序。
* [CatChat](https://github.com/greyli/catchat)：本书第 11 章示例程序，基于 WebSocket 实现，并提供了社交账户登录功能的聊天室。
* [Flask-Share](https://github.com/greyli/flask-share)：本书第 15 章的 Flask 扩展示例。

## License

该项目基于 MIT 协议授权，具体可以参考 `LICENSE` 文件。
