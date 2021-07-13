[![](https://img.shields.io/badge/Author-有来技术团队-orange.svg)](https://gitee.com/wangjiabin-x/uh5)
![](https://img.shields.io/badge/youlai--mall-v2.0.0-blue)
[![](https://img.shields.io/github/stars/hxrui/youlai-mall.svg?style=social&label=Stars)](https://github.com/hxrui/youlai-mall/stargazers)
[![](https://img.shields.io/badge/license-Apache%20License%202.0-blue.svg)](https://github.com/hxrui/youlai-mall/blob/master/LICENSE)
![](https://img.shields.io/badge/SpringBoot-2.5.2-brightgreen.svg)
![](https://img.shields.io/badge/SpringCloud-2020-green.svg)
![](https://img.shields.io/badge/vue--element--admin-v4.4.0-orange)


## 项目信息

#### 项目简介

[youlai-mall](https://gitee.com/youlaitech/youlai-mall) 是基于Spring Boot 2.5.0、Spring Cloud 2020 & Alibaba 2021、vue、element-ui、uni-app快速构建的一套全栈开源商城项目。

项目采用微服务、前后端分离开发模式；汇集全栈主流的技术栈； 涉及 [后端微服务](https://gitee.com/youlaitech/youlai-mall) 、 [前端管理](https://gitee.com/youlaitech/youlai-mall-admin) 、 [微信小程序](https://gitee.com/youlaitech/youlai-mall-weapp) 和 [APP应用](https://gitee.com/youlaitech/youlai-mall-weapp) 等多端的开发。

#### 项目特色
- Spring Cloud + Vue + Docker全栈开发
- 项目使用的都是当前主流的技术栈，无过度自定义封装，易学习理解和方便二次扩展
- 基于Spring Boot 2.5.0、Spring Cloud 2020 & Alibaba 2021一站式微服务解决方案实现快速开发
- 完整的Spring Security OAuth2 认证中心统一认证授权，网关统一鉴权逻辑
- 特有一套微服务+前后端分离的RBAC权限设计，实现Spring Cloud Gateway网关下的RESTful接口细粒度的统一鉴权和vue页面按钮级别权限控制
- 基于vue-element-admin的后台前端解决方案，实现动态路由
- 移动端采用uni-app、实现跨多端移动应用开发，包括微信小程序、Android和IOS等
- Docker快速构建项目环境和一键打包部署微服务项目

#### 项目预览

- **系统管理**

| ![image-20210621004954228](https://gitee.com/haoxr/image/raw/master/image-20210621004954228.png) | ![image-20210621005011310](https://gitee.com/haoxr/image/raw/master/image-20210621005011310.png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
|![](https://gitee.com/haoxr/image/raw/master/30719657a4b183428a2472231fee55a6_image-20210621005037964.png) | ![image-20210621005123432](https://gitee.com/haoxr/image/raw/master/image-20210621005123432.png) |



- **微信小程序**

| ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005253.jpg) | ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005338.jpg) | ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005331.jpg) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005349.jpg) | ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005356.jpg) | ![](https://gitee.com/haoxr/image/raw/master/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20210621005344.jpg) |


#### 项目架构流程图

![](https://gitee.com/haoxr/image/raw/master/youlai-architecture.jpg)

#### 技术栈

- **后端技术栈：** Spring Boot、Spring Cloud、Spring Cloud Alibaba、Spring Security OAuth2、JWT、Mybatis-Plus、Seata、Sentinel、ELK、Redis

- **前端技术栈：** vue、element-ui、uni-app、vue-element-admin

#### 项目地址

**线上预览地址：** http://www.youlai.tech

| 项目名称   | 源码地址                                                        |项目名称   | 源码地址                                                   |
| ---------- | ------------------------------------------------------------ |---------- | ------------------------------------------------------------ |
| 微服务后台 | [youlai-mall](https://gitee.com/youlaitech/youlai-mall)      | 微信小程序 | [youlai-mall-weapp](https://gitee.com/youlaitech/youlai-mall-weapp) |
| 管理前端   | [youlai-mall-admin](https://gitee.com/youlaitech/youlai-mall-admin) |APP应用    | [youlai-mall-app](https://gitee.com/youlaitech/youlai-mall-app) |

#### 项目结构

``` lua
youlai-mall
├── docs
    ├── nacos -- Nacos配置文件
    ├── sql   -- mysql数据库脚本
├── mall-oms
    ├── oms-api -- 订单中心Feign接口客户端
    ├── oms-boot -- 订单中心
├── mall-pms
    ├── pms-api -- 商品中心Feign接口客户端
    ├── pms-boot -- 商品中心
├── mall-sms
    ├── sms-api -- 营销中心Feign接口客户端
    ├── sms-boot -- 营销中心
├── mall-ums
    ├── ums-api -- 会员中心Feign接口客户端
    ├── ums-boot -- 会员中心
├── middleware -- 中间件（Nacos、Sentinel）
├── youlai-admin 
    ├── admin-api -- 系统管理服务Feign接口客户端
    ├── admin-boot -- 系统管理服务
├── youlai-auth     -- 认证中心【OAuth2认证服务器】
├── youlai-common   -- 公共模块
└── youlai-gateway  -- Gateway网关【OAuth2资源服务器】
```

## 项目启动

#### 后台微服务启动

1. **安装环境**

   安装`MySQL8`、`Redis`

2. **创建数据库**
    - 新建平台数据库，执行项目`docs/sql`下的SQL脚本完成数据库创建，基础sql脚本为`youlai.sql`，商城业务的脚本为`mall-*`，商城数据库按需创建
    - 创建`Nacos`数据库，执行脚本`middleware/nacos/conf/nacos-mysql.sql`完成`Nacos`数据库的初始化
3. **Nacos配置和启动（非常重要）**

    - 修改`Nacos`数据源，进入配置`middleware/nacos/conf/application.properties`将数据源修改为自己的环境连接

    - 启动`Nacos`,  IDEA下方工具栏点击Terminal终端命令行，执行`cd middleware/nacos/bin`命令切换到`Nacos`的启动脚本文件夹下，然后执行`startup -m standalone`命令启动`Nacos`服务；

    - 启动`Nacos`成功之后，访问`Nacos`控制台，在浏览器输入 http://localhost:8848/nacos ,输入用户名/密码:nacos/nacos进入管理页面；

      ![](https://gitee.com/haoxr/image/raw/master/20210623012937.png)

    - 导入`Nacos`配置，在启动`Nacos`服务进入控制台导入`docs/nacos/DEFAULT_GROUP.zip`配置，然后分别进入各个项目配置文件中修改MySQL、Redis连接信息即可。

      ![image-20210623013306256](https://gitee.com/haoxr/image/raw/master/image-20210623013306256.png)

4. `Nacos`启动完成和MySQL、Redis连接信息修改完成后，分别启动`youlai-gateway`、`youlai-auth`、 `youlai-admin`模块，
   启动类分别对应的是GatewayApplication、AuthApplication以及`youlai-admin`的子模块`admin-boot`的AdminApplication类，至此完成整个项目基础服务的启动；

#### 管理前端启动

1. 本机安装Node环境
2. npm install
3. npm run dev
4. 访问 http://localhost:9527

#### 微信小程序启动

1. 下载`HBuilder X`和`微信开发者工具`
2. 微信公众平台申请小程序，获得小程序的AppID
3. `微信开发者工具`微信扫码登录，开启服务端口，点击工具栏`设置`->`安全设置`->`安全`->`服务端口`选择打开
4. `Hbuilder X`替换项目AppID成自己的，点击`manifest.json`文件->微信小程序配置
5. Nacos控制台修改`youlai-auth`配置中的微信小程序AppID和AppSecret为自己申请的小程序
6. `Hbuilder X`工具栏点击 `运行`->`运行到小程序模拟器`->`微信开发者工具`

## 接口测试

#### Spring Security OAuth2认证授权接口

- **Postman**

    1.  请求参数类型为Query Param或者form-data，出现很多错误的情况是将参数是JSON格式放在请求Body中
    2.  Spring Security OAuth2新版本不再支持将客户端信息client_id和client_secret放在请求路径的这种方式，否者会出现401的错误（已验证）
    3.  OAuth2客户端信息在Authorization标签选择Basic Auth然后填写client_id和client_secret

  | Query Params参数                                             | Authorization                                                |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | ![](https://gitee.com/haoxr/image/raw/master/image-20210621075338100.png) | ![image-20210621075517108](https://gitee.com/haoxr/image/raw/master/image-20210621075517108.png) |

- **Knife4j接口文档（推荐）**

    1.  接口文档地址，启动网关访问 http://localhost:9999/doc.html (默认)
    2.  请求接口之前，先执行对应模块下的第一个接口Authorize完成认证，通过后再打开其他接口请求头会**自动**填充token
    3.  client/123456 是**有来项目**预留用于测试的客户端信息，因为Knife4j完成自动填充不能包装返回值，和大多数实际项目需包装返回值添加状态码不符

| 认证授权                                                     | 认证成功自动填充Header                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![image-20210622000304570](https://gitee.com/haoxr/image/raw/master/image-20210622000304570.png) | ![image-20210622000046029](https://gitee.com/haoxr/image/raw/master/image-20210622000046029.png) |

## 项目文档

[项目文档地址](https://www.cnblogs.com/haoxianrui/)

## Star趋势
- Github
[![Github](https://starchart.cc/hxrui/youlai-mall.svg)](https://starchart.cc/hxrui/youlai-mall)
- Gitee
[![Gitee](https://whnb.wang/stars/youlaitech/youlai-mall)](https://whnb.wang/stars/youlaitech/youlai-mall)

## contributors
[![contributors](https://whnb.wang/contributors/youlaitech/youlai-mall)](https://whnb.wang/contributors/youlaitech/youlai-mall)


## 联系信息
因为微信交流群满200人只能通过邀请进入，如果想进入交流群学习可添加以下开发人员，备注“**有来**“由其拉进群。

| ![](https://gitee.com/haoxr/image/raw/master/default/113__6c5ed5b1b73ea9cd4cf32848ed350c07_b9b214638a2a406e52dbf51e9bf9a2ef.png) | ![](https://gitee.com/haoxr/image/raw/master/hxr.jpg)        | ![](https://gitee.com/haoxr/image/raw/master/huawei.jpg)     | ![](https://gitee.com/haoxr/image/raw/master/default/1625149769(1).png) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://gitee.com/haoxr/image/raw/master/default/7488479b1e2c193b04b56d1e0ff640c.jpg) | ![image-20210701232803265](https://gitee.com/haoxr/image/raw/master/default/image-20210701232803265.png) | ![](https://gitee.com/haoxr/image/raw/master/default/20210701234946.png) | ![](https://gitee.com/haoxr/image/raw/master/default/image-20210702002909113.png) |