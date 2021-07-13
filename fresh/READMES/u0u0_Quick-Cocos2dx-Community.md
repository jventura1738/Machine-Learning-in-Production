# Quick-Cocos2dx-Community

Cocos2d-x Lua 社区版是在Cocos2d-x的基础上，关注于Lua进行游戏开发的引擎框架变种，意在减少重复造轮子，节省开发人员的时间。

## 官方网站

[http://www.cocos2d-lua.org/](http://www.cocos2d-lua.org/)

**社区版 千人群(1群)号：361920466**

**社区版 2群：138934064**

## 相关开源仓库地址

* 引擎代码仓库: [Quick-Cocos2dx-Community](https://github.com/u0u0/Quick-Cocos2dx-Community)
* 第三方库编译框架: [Quick-3rd-party-libs](https://github.com/u0u0/Quick-3rd-party-libs)
* vim开发插件: [vim-quick-community](https://github.com/u0u0/vim-quick-community)
* sublime开发插件: [quick-comminuty-dev](https://github.com/u0u0/quick-comminuty-dev)
* protoc-gen-lua: [protoc-gen-lua-bin](https://github.com/u0u0/protoc-gen-lua-bin)

## 快速安装指南

1. 下载 Quick-Cocos2dx-Community 最新版，并解压到一个路径。
	> 解压的路径以及文件夹名称**不要有中文或空格**.
2. Mac系统：在终端中执行：setup_mac.sh
	> 命令前*不需要*加入sudo。当提示输入密码的时候，请输入当前用户的登陆密码。 如果遇到新建的工程mac_ios项目不能编译通过，多是Xcode环境变量设置失败，建议在终端手动输入下面的命令。

	```
    defaults write com.apple.dt.Xcode IDEApplicationwideBuildSettings -dict
	# 路径替换为自己的Quick root
	defaults write com.apple.dt.Xcode IDEApplicationwideBuildSettings -dict-add QUICK_V3_ROOT "/User/u0u0/Quick_cocos2dx_Community"
	defaults write com.apple.dt.Xcode IDESourceTreeDisplayNames -dict
	defaults write com.apple.dt.Xcode IDESourceTreeDisplayNames -dict-add QUICK_V3_ROOT QUICK_V3_ROOT
    ```

   Windows系统：双击setup_win.bat即可。
3. 启动 player
	> 运行步骤2以后，脚本会自动创建player的快捷方式。

	 Mac 系统在 Applications 文件夹(或系统应用列表)中 player.app 。
	 Windows 系统在桌面上的 player.exe 快捷方式。
	 
## 创建新工程	 

目前支持两种方式：

1. player 中新建按纽

2. python 脚本 quick/bin/CreateProject.py:

	```shell
    CreateProject [-h]

    -h 显示帮助
    -p 包ID
    -o 输出目录
    -l 设置为横屏，默认不设置为竖屏
    --deep-copy 拷贝cocos2d源码至新工程中，默认不设置为使用全局的 QUICK_V3_ROOT 下的代码
	
	如:
	
	quick/bin/CreateProject.py  -p com.yygame.helloworld -o /tmp --deep-copy
	```
