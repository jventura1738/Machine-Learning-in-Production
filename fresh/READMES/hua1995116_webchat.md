# webchat

<img src="https://s3.qiufengh.com/webchat/webchat-logo-160.png" />

[![Build Status](https://www.travis-ci.org/hua1995116/webchat.svg?branch=master)](https://www.travis-ci.org/hua1995116/webchat)

[中文版](./README.md) [English](./zh_en.md)

> 说明: master 分支还不太稳定，可以查看 https://github.com/hua1995116/webchat/tree/v2.2.0 稳定分支， 3.0 版本持续重构中。

## 功能

- [x] 注册登录功能
- [x] 聊天功能
- [x] 查看历史记录
- [x] 多个聊天室
- [x] 与机器人对接
- [x] 图片发送
- [x] 发送链接
- [x] 发送表情
- [x] 图片预览
- [x] 消息未读
- [x] 断线重连
- [x] 好友资料查看
- [x] 添加好友
- [x] 单聊
- [x] 搜索好友
- [x] 热门好友推荐


## 启动项目

Dev环境: MongoDB、Node 8.5.0+、Npm 5.3.0+

Prod环境: Redis、MongoDB、Node 8.5.0+、Npm 5.3.0+

启动客户端
```
$webchat cd client

$client npm install -----安装依赖

$client npm run serve -----运行

```
启动服务端
```
$client cd ..

$webchat npm install

$webchat npm run dev
```

## 打包

打包客户端
```
cd client

npm run build
```

服务端运行
```
cd ..

npm run prod
```

在线观看

[https://www.qiufengh.com/](https://www.qiufengh.com/)

<img src="http://s3.qiufengh.com/images/1536588077.png" width="400" />

## 技术交流


qq群: 437938625

微信群: 加微信拉你进微信群。

<img src="https://s3.qiufengh.com/webchat/webcaht-my.jpeg?imageView2/2/w/360" width="300" />


## 技术栈

 - 前端 vue，vue-router ,vuex
 - 后端 nodejs，express
 - 数据库 mongodb
 - 通讯 websocket
 - 脚手架工具 vue-cli

## 效果

<img src="http://s3.qiufengh.com/screenshot/1.png"/>

<img src="http://s3.qiufengh.com/screenshot/2.png"/>

<img src="http://s3.qiufengh.com/screenshot/3.png"/>

<img src="http://s3.qiufengh.com/screenshot/4.png"/>

## 版本更新

**v3新增功能**

1. 网络异常判断、重连提示
2. 多端信息同步
3. 好友资料查看
4. 添加好友
5. 单聊
6. 搜索好友
7. 热门好友推荐
8. 性别、手机号修改
9. 搜索加好友

## 版本预览

**v2 稳定版本**

https://github.com/hua1995116/webchat/tree/v2.2.0

**其他版本**

<a href="./RELEASE.md">RELEASE</a>

## 项目wiki

https://qiufeng.blue/node/#websocket-%E7%B3%BB%E5%88%97

## API

<a href="./API.md">API</a>

## License

[MIT](http://opensource.org/licenses/MIT)

MIT License

Copyright (c) 2018 蓝色的秋风
