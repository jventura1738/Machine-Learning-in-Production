

# 科学上网

作者：左耳朵 [http://coolshell.cn](http://coolshell.cn)
更新时间：2020-08-01

这篇文章可以写的更好，欢迎到 [https://github.com/haoel/haoel.github.io](https://github.com/haoel/haoel.github.io) 更新

![](./images/cover.jpg)

- [科学上网](#科学上网)
  - [0. 序](#0-序)
  - [1. 英文能力](#1-英文能力)
  - [2. 购买VPS](#2-购买vps)
    - [2.1 常规VPS](#21-常规vps)
    - [2.2 CN2 线路](#22-cn2-线路)
    - [2.3 NCP 线路](#23-ncp-线路)
  - [3. 搭建相关代理服务](#3-搭建相关代理服务)
    - [3.1 设置Docker服务](#31-设置docker服务)
    - [3.2 开启 TCP BBR 拥塞控制算法](#32-开启-tcp-bbr-拥塞控制算法)
    - [3.3 用 Gost 设置 HTTPS 服务](#33-用-gost-设置-https-服务)
    - [3.4 设置Shadowsocks服务](#34-设置shadowsocks服务)
    - [3.5 设置L2TP/IPSec服务](#35-设置l2tpipsec服务)
    - [3.6 设置PPTP服务](#36-设置pptp服务)
  - [4. 客户端设置](#4-客户端设置)
    - [4.1 gost 客户端](#41-gost-客户端)
    - [4.2 Shadowsocks 客户端](#42-shadowsocks-客户端)
    - [4.3 VPN 客户端](#43-vpn-客户端)
  - [5. 流量伪装和其它方式](#5-流量伪装和其它方式)
    - [5.1 V2Ray](#51-v2ray)
    - [5.2 Brook](#52-brook)
  - [6. 针对 IP 被封的解决方案](#6-针对-ip-被封的解决方案)
    - [6.1 Cloudflare](#61-cloudflare)
    - [6.2 V2Ray](#62-v2ray)
    - [6.3 补充](#63-补充)
  - [7. 透明网关](#7-透明网关)
    - [7.1 OpenWRT 路由器](#71-openwrt-路由器)
    - [7.2 通过树莓派做旁路网关](#72-通过树莓派做旁路网关)
    - [7.3 安装 Clash](#73-安装-clash)
    - [7.4 设置 iptables 转发](#74-设置-iptables-转发)
  - [8. 其它](#8-其它)
    - [8.1 其它方式](#81-其它方式)
    - [8.2 搭建脚本](#82-搭建脚本)

## 0. 序

首先，我们先明确一下，我科学上网的目的主要是为了学习、工作、交友、查资料、和丰富自己的眼界，不是为了看黄片，或是干一些非法、政治或是见不得人的事。

对我来说，科学上网很重要，下面罗列一下需要科学上网，我才能真正学习工作和生活的网站：

- Youtube 和 Vimeo 上的各种大会和教学视频，除了我自己要学，我的孩子也要学。
- Wikipedia 维基百科是我目前唯一信得过的百科全书，我在上面可以比较系统地翻阅各种词条。
- Slideshare 上有很多的技术文档和资料的PPT，是我的知识学习的地方。
- Quora 问答网站，在上面有很多有趣的问答。
- 博客和论文，很多博客和论文站点都被墙了，比如：Blogspot 和 Medium。
- Google 的各种服务，比如：Gmail, Map, Docs，Driver，照片，图片搜索，Voices，论文搜索……包括Google官方的各种技术文档……
- 一些云服务，比如：Dropbox，IFTTT，Imgur，archive.org……
- Twitter 上 Follow 一些牛人和一些官方账号，比如：AWS、Docker……
- 社交 Facebook, Telegram, Whatsapp，Slack…… 有一些我在国外的亲戚和朋友……
- Reddit 是一个聚合网站，一个新闻和文章的集散地，你可以认为是各种频道的今日头条……
- Pinterest 和 Instagram  上面有很多不错的图片和视频新闻，是我减压力的地方……
- 新闻，如BBC。 BBC是全球比较出众的媒体，有太多的有价值资源和内容了，比如纪录片、学英文……
- 编程，有很多编程的场景需要翻墙，比如，Go语言编程时的 go get 中的很多库是放在 Google的服务器上， 然而Google是全部被墙，包括 Android 和其它一些文档和资源也是一样。包括 SourceForge 的某些项目也需要科学上网，Docker Registry也有部分被墙，还有偶尔抽疯的Github，以及不能访问的gist……
- ……等等

是的，我的互联网不是——全是骗子的百度、充满广告的微信朋友圈、质量低下的公众号、娱乐至死的新浪微博、只有抖机灵和“怎么看XX”的知乎、毫无营养的今日头条…… 在这样的网络空间里，我真的无法生存…… 这根本不是互联网，不是为我服务的互联网，而是在消费我的互联网，是让我变傻变笨的互联网…… 我不能忍，因为它影响到了我的生存……


## 1. 英文能力

**首先，你应该对英文读写没什么问题!**

为什么这么说？**这主要是针对计算机相关的知识，逻辑是这样的，如果你上了Google还是在用中文关键词，那么你好不容易出来了，结果又回去了，所以没什么意义。** 换言之，科学上网的目的是为了进入广阔的世界范围与全世界的人交流，所以，英文是必备的，如果你英文有问题，VPN过去的用处也不大。

所以，我把这个前提条件放在第一的位置，就是说—— **真正的墙不是GFW，而是人的大脑！** 意思是，屏蔽你获得信息能力的不是墙，而很大一部分则是我们自己的语言能力！


## 2. 购买VPS

然后，你需要一个VPS。 在这里，强烈建议通过自建的方式，可能成本会略高一点，但是，整体来说比共享的好很多了。

（注：*当然，你也可以直接购买一些科学上网的服务，但我这里不推荐了，一方面是广告，另一方面通常这样的服务非常的不稳定，而且也容易被代理方做中间人攻击*）

**现在你买一台VPS也不贵了，也就是一个月10美金左右（70元），我个人觉得一个月花70元钱不算奢侈的事，而且会让你的生活质量得得改善。当然，线路好的得需要多花一些钱。**。

（注：*我现在每个投入在科学上网上的成本大概在不到1000元人民币左右，常备3-5个不同国家的VPS，因为国内的网络路由经常性的变化，所以，为了确保总是有一条快的，所以，得多备几个*）。

### 2.1 常规VPS

对于VPS，下面是一些常规选项。

- [AWS LightSail](https://lightsail.aws.amazon.com/) 是一个非常便宜好用的服务，最低配置一个月 $3.5 美金，目前的Zone不多，推荐使用日本或新加坡（支持银联卡）
- [AWS EC2](https://aws.amazon.com/cn/)香港、日本或韩国申请个免费试用一年的EC2 VPS （支持银联卡）
- [Google Cloud Platform](https://cloud.google.com/)提供免费试用，赠送300刀赠金（需要国际信用卡）
- [Linode](https://www.linode.com)买个一月USD5刀的VPS
- [Conoha](https://www.conoha.jp/zh/)上买一个日本的VPS，一个月900日元 （可以支付宝）
- [Vultr](https://www.vultr.com)上买一个日本的VPS，一个月5刀 （可以支付宝）(注：据说被墙的IP太多）
- [Oracle Cloud](https://www.oracle.com/cloud/free/)两台VPS无限期使用，可选美日韩等地（需要国际信用卡）


> **注意**
> - 在中国，因为有太多的网络提供商，所以，国内的网络也是很奇葩的，可以看到的是，不同的地方，不同的网络，到不同的国家完全不一样，而且还经常性地调整路由，所以，经常性地有时候快有时候慢，简直就是随机的。所以，像我这样要求比较高的人，一般会备3-5个不同国家地区的VPS，以保障上网的速度。
> 
> - 香港网速应该是比较好的，但是香港的成本也是比较高的。台湾的网速也是不错的，日本的网速其次，新加坡再次之，然后是美国的东海岸（这里是基于北京和上海的情况）
>
> - 日本区的网络质量并不一定很好，有时候快的飞快，但有时候会有很大的丢包率（不同的网络不一样），有时候会很慢。上述的这几个VPS服务商中，AWS韩国和日本会好点，然后是Linode，最后是Conoha和Vultr（如果你有更好的，请推荐）
>
> - Google Cloud Platform - GCP 的香港和台湾结点也是很快的。但是你要能买GCP的主机，你还得先翻墙，所以，感觉有点死锁了。所以，你可能先用Vultr（按时付费）翻墙，然后再到GCP上购买。

### 2.2 CN2 线路

如果你需要更好更高速的网络服务（比如你要看Youtube的1080P），那么，你需要下面的这些服务器资源了（价格也会高一些）

`CN2` 和 `GIA` 是两个关键词。**CN2 GIA** 全称 China telecom Next Carrier Network- Global Internet Access 电信国际精品网络，特征是路由线路上骨干节点均为59.43开头的IP。如果想要寻找接入CN2线路的国外VPS提供商，建议使用 `Next Carrier Network` 或者 `CN2` 这个关键词搜索即可。

多说一句， CN2本身又分为两种类型：

- **CN2 GT**: CN2 里属于Global Transit的产品(又名GIS-Global Internet Service)，在CN2里等级低，省级/出国节点为 `202.97` 开头，国际骨干节点有2～4个 `59.43` 开头的CN2节点。在出国线路上拥堵程度一般，相对于163骨干网的稍强，相比CN2 GIA，性价比也较高。

- **CN2 GIA**: CN2 里属于Global Internet Access的产品，等级最高，省级/出国/国际骨干节点都以`59.43`开头，全程没有`202.97`开头的节点。在出国线路上表现最好，很少拥堵，理论上速度最快最稳定，当然，价格也相对 CN2 GT 偏高。
 
关于 `CN2` 线路的主机提供商，下面罗列几个

- [搬瓦工](https://bwh8.net/aff.php?aff=39384)  这应该是美区最好的一个用来科学上网的VPS提供商了，实测飞快。购买时你需要注意VPS规格上的 `CN2` 和 `GIA` 的描述。（注：点击主页右上角的 `regisiter` 以后，你可以看到页面上方有两个导航条，在下面的导航条上点 `Services` -> `Order New Services` 就可以看到所有的列表了。买完后，你可能需要重装一下操作系统，装成64位带BBR的 ）
- [Gigsgigscloud](https://clientarea.gigsgigscloud.com/index.php?/cart/cloudlet-v-hk/&step=0) CN2 GIA 在香港的结点是很不错的，当然，价格也很不错（建议几个人一起平摊费用）
- [Hostdare](https://manage.hostdare.com/index.php) 的CN2 GIA产品也是三网直连，KVM和OpenVZ两种架构，KVM产品长期缺货

更多的可以参考这篇文章《[CN2 GIA VPS主机收集整理汇总-电信,联通,移动三网CN2 GIA线路VPS主机](https://wzfou.com/cn2-gia-vps/)》（注：随时间推移，这篇文章的内容可能会失效）

重点说一下，**CN2 GIA + 香港机房**，你会得到巨快无比的上网速度（无论你在中国的哪个位置，无论使用哪家运营商，CN2 GIA都是最优的），然而，香港地区的VPS的确是有点贵了。在Youtube.com上看 4K 的视频毫无压力。虽然阿里云和腾讯的也有，但是被查到的风险基本上是100%，不建议使用，被抓了别怪我没警告过你。

### 2.3 NCP 线路
**NCP** 全称 New Cross Pacific（新跨太平洋海底光缆系统）。
2018年11月底，中国到美国之间的海底光缆新开通了NCP线路，并且容量更大（系统设计容量超过80Tbps），路由更少（中国上海到美国中间路由节点只有11个，ping值110ms）。

NCP线路全长13,000公里，连接美国俄勒冈州希尔斯伯勒，连接崇明（中国大陆），南汇（中国大陆），临港（中国大陆），釜山（韩国），头城（台湾），和丸山（日本）。

相对于第二条中美直达海底光缆系统（跨太平洋快线，TPE），现阶段NCP线路的网络流量更少更稳定。特征是华东/中地区流量会经过NCP直达路由节点，IP地址为202.97.95.201/202。

关于 `NCP` 线路的主机提供商，下面罗列两个（欢迎补充）

- [50KVM VPS](https://www.50kvm.com) 截止2018年12月2日KVM 产品最低价格￥81.60/月。
- [OLVPS](https://t667.com/) 截止2018年12月2日KVM 产品最低价格¥22/月。（**特别注意** ： 在 OLVPS 上的《[服务条款](https://olvps.com/index.php?rp=/knowledgebase/1/TOS.html)》 中有一条说明：“**禁止OpenV*P*N/Socks5/PPTP/L2TP等软件、公共代理**”，所以，可能OLPVS并不太适合）

## 3. 搭建相关代理服务

> 注：如下的搭建和安装脚本可参看本库的 scripts 目录下的脚本，如： [Ubuntu 18.04 Installation Script](https://github.com/haoel/haoel.github.io/blob/master/scripts/install.ubuntu.18.04.sh) （感谢网友 [@gongzili456](https://github.com/gongzili456) 开发）

### 3.1 设置Docker服务

首先，你要安装一个Docker CE 服务，这里你要去看一下docker官方的安装文档：

- [CentOS 上的 Docker CE 安装](https://docs.docker.com/install/linux/docker-ce/centos/)
- [Ubuntu 上的 Docker CE 安装](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

然后开始设置你的VPN/SS服务

### 3.2 开启 TCP BBR 拥塞控制算法

TCP BBR（Bottleneck Bandwidth and Round-trip propagation time）是由Google设计，于2016年发布的拥塞算法。以往大部分拥塞算法是基于丢包来作为降低传输速率的信号，而BBR则基于模型主动探测。该算法使用网络最近出站数据分组当时的最大带宽和往返时间来创建网络的显式模型。数据包传输的每个累积或选择性确认用于生成记录在数据包传输过程和确认返回期间的时间内所传送数据量的采样率。该算法认为随着网络接口控制器逐渐进入千兆速度时，分组丢失不应该被认为是识别拥塞的主要决定因素，所以基于模型的拥塞控制算法能有更高的吞吐量和更低的延迟，可以用BBR来替代其他流行的拥塞算法，例如CUBIC。Google在YouTube上应用该算法，将全球平均的YouTube网络吞吐量提高了4%，在一些国家超过了14%。

BBR之后移植入Linux内核4.9版本，并且对于QUIC可用。

如果开启，请参看 《[开启TCP BBR拥塞控制算法](https://github.com/iMeiji/shadowsocks_install/wiki/开启-TCP-BBR-拥塞控制算法) 》

### 3.3 用 Gost 设置 HTTPS 服务

[gost](https://github.com/ginuerzh/gost) 是一个非常强的代理服务，它可以设置成 HTTPS 代理，然后把你的服务伪装成一个Web服务器，**我感觉这比其它的流量伪装更好，也更隐蔽。这也是这里强烈推荐的一个方式**。

为了更为的隐蔽，你需要一个域名（可以上 Godaddy，但一定要使用美国版），然后使用 [Let's Encrypt](https://letsencrypt.org) 来签 一个证书。使用 Let's Encrypt 证书你需要在服务器上安装一个 [certbot](https://certbot.eff.org/instructions)，点击 [certbot](https://certbot.eff.org/instructions) 这个链接，你可以选择你的服务器，操作系统，然后就跟着指令走吧。

接下来，你需要申请一个证书（我们使用standalone的方式，然后，你需要输入你的电子邮件和你的域名）：

```
$ sudo certbot certonly --standalone
```

证书默认生成在 `/etc/letsencrypt/live/<YOUR.DOMAIN.COM/>` 目录下，这个证书90天后就过期了，所以，需要使用一个 cron job 来定期更新（稍后给出）

接下来就是启动 gost 服务了，我们这里还是使用 Docker 的方式建立 gost 服务器。
```
#!/bin/bash

## 下面的四个参数需要改成你的
DOMAIN="YOU.DOMAIN.NAME"
USER="username"
PASS="password"
PORT=443

BIND_IP=0.0.0.0
CERT_DIR=/etc/letsencrypt
CERT=${CERT_DIR}/live/${DOMAIN}/fullchain.pem
KEY=${CERT_DIR}/live/${DOMAIN}/privkey.pem
sudo docker run -d --name gost \
    -v ${CERT_DIR}:${CERT_DIR}:ro \
    --net=host ginuerzh/gost \
    -L "http2://${USER}:${PASS}@${BIND_IP}:${PORT}?cert=${CERT}&key=${KEY}&probe_resist=code:404&knock=www.google.com"
```

上面这个脚本，你需要配置：域名(`DOMAIN`), 用户名 (`USER`), 密码 (`PASS`) 和 端口号(`PORT`) 这几个变量。

关于 gost 的参数， 你可以参看其文档：[Gost Wiki](https://docs.ginuerzh.xyz/gost/)，上面我设置一个参数 `probe_resist=code:404` 意思是，如果服务器被探测，或是用浏览器来访问，返回404错误，也可以返回一个网页（如：`probe_resist=file:/path/to/file.txt` 或其它网站 `probe_resist=web:example.com/page.html`）

**注意**：开启了探测防御功能后，当认证失败时服务器默认不会响应 `407 Proxy Authentication Required`，但某些情况下客户端需要服务器告知代理是否需要认证(例如Chrome中的 SwitchyOmega 插件)。通过knock参数设置服务器才会发送407响应。对于上面的例子，我们的`knock`参数配置的是`www.google.com`，所以，你需要先访问一下 `https://www.google.com` 让服务端返回一个 `407` 后，SwitchyOmega 才能正常工作。

如无意外，你的服务就启起来了。你可以使用下面的命令验证你的 gost 服务是否正常。

```
curl -v "https://www.google.com" --proxy "https://DOMAIN" --proxy-user 'USER:PASS'
```


接下来就是证书的自动化更新。

可以使用命令  `crontab -e`  来编辑定时任务：

```
0 0 1 * * /usr/bin/certbot renew --force-renewal
5 0 1 * * /usr/bin/docker restart gost
```

这样，服务器就配置完成了。客户端请移动后面的客户端章节。

### 3.4 设置Shadowsocks服务

**（注：Shadowsocks被查的机率非常大，不推荐使用）**

Shadowsocks 的 Docker 启动脚本 （其中的 `SS_PORT` 和 `SS_PASSWD` 需要重新定义一下）


```
#!/bin/bash

SS_PORT=1984
SS_PASSWD=MyPasswd

sudo docker run -dt --name ss \
   -p ${SS_PORT}:${SS_PORT} mritd/shadowsocks \
   -s "-s 0.0.0.0 -p ${SS_PORT} -m aes-256-cfb -k ${SS_PASSWD} --fast-open"
```


### 3.5 设置L2TP/IPSec服务

**（注：VPN方式被查的机率非常大，不推荐使用）**

L2TP/IPSec 的启动脚本，其中的三个环境变量 `USER`， `PASS` 和 `PSK` 需要替换一下。

```
#!/bin/bash

USER=someone
PASS=password
PSK=psk_key

sudo docker run -d  --privileged \
    -e PSK=${PSK} \
    -e USERNAME=${USER} -e PASSWORD=${PASS} \
    -p 500:500/udp \
    -p 4500:4500/udp \
    -p 1701:1701/tcp \
    -p 1194:1194/udp  \
    siomiz/softethervpn
```

### 3.6 设置PPTP服务

**（注：PPTP不安全，请不要使用）**

```
sudo docker run -d --privileged --net=host 
                -v {/path_to_file/chap-secrets}:/etc/ppp/chap-secrets \
                mobtitude/vpn-pptp
```
PPTP 使用 `/etc/ppp/chap-secrets` 文件设置用户名和密码，所以你需要给docker容器提供这个文件，下面是这个文件的示例：

```
# Secrets for authentication using PAP
# client    server      secret           acceptable local IP addresses
  fuckgfw   *           whosyourdaddy    *
```


## 4. 客户端设置

### 4.1 gost 客户端

大多数的代理服务都支持 https 的代理，但是我们需要智能代理（也就是该翻的时候翻，不用翻的时候不翻），那么我们可以重用 Shadowsocks 的客户端。

对于电脑来说，你同样可以 [下载 gost 程序](https://github.com/ginuerzh/gost/releases)，然后使用下面的命令行：

```
gost -L ss://aes-128-cfb:passcode@:1984 -F 'https://USER:PASS@DOMAIN:443'
```
这样用 gost 在你的本机启动了一个 `Shadowsocks` 的服务，然后，把请求转到你在上面配置的 HTTPS服务器上，这样就完成转接。

```
  +-------------------+       +-------------+       +-------------+
  | ShadowSocks Client|------>| Gost Client |------>| Gost Server |
  +-------------------+       +-------------+       +-------------+
```

这样，你的ShadowSocks客户端只需要简单的配置一个本机的 SS 配置就好了。

对于手机端

 - iPhone，可以考虑使用 `ShadowRocket` （需要付费），其中使用 HTTPS 的代理，配置上就好了。
 - Android，可以考虑使用这个Plugin - [ShadowsocksGostPlugin](https://github.com/xausky/ShadowsocksGostPlugin) 

**注明**：如果你之前使用了Chrome插件 SwitchyOmega，如果无法直接配置HTTPS代理，具体原因可能是因为你设置了`probe_resist`以开启探测防御功能。这里，你需要在服务器端设置 `knock` 参数（参看 [用 Gost 设置 HTTPS 服务](#33-用-gost-设置-https-服务) 中的“注意”一节 ）

或是，干脆使用gost客户端在本机启动一个 SOCKS5的代理服务用来代替（`gost -L socks5://:1080 -F 'https://USER:PASS@DOMAIN:443'`），然后在SwitchyOmega配置代理为'127.0.0.1:1080'即可。比如:


### 4.2 Shadowsocks 客户端

对于 Shadowsocks 客户端，可以到这里查看 [Shadowsocks Clients](https://shadowsocks.org/en/download/clients.html)

- MacOS 上你可以下载 [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases)
- Windows上你可以下载 [Shadowsocks-Windows](https://github.com/shadowsocks/shadowsocks-windows/releases)，需要先安装 [.NET Framework](https://dotnet.microsoft.com/download/dotnet-framework-runtime)
- Android的客户端，你可以用手机访问并下载 [Shadowsocks-Android](https://github.com/shadowsocks/shadowsocks-android/releases)
- iPhone 端就比较麻烦了。因为国内全都被下架了。
	1. 你需要注册一个美国的苹果ID.
	2. 然后 iTunes/App Store 用这个美区的ID登录（不是退出iCloud ，而是退出App Store）
	3. 然后搜索 `Potatso Lite` ，`ShadowRocket`, `Wingy`, `Quantumult` 等。（我使用前两个）

> **注意**
>
> - 关于如何注册美区Apple ID账号，你可以参看如下的这几篇文章（我不保证这些文章可不可用，但是你可以自行Google）。
>    - [5分钟注册美国区Apple ID（18年亲测有效）](https://zhuanlan.zhihu.com/p/36574047)
>    - [2018年6月亲测：注册美国地区苹果apple ID帐号终极教程](https://www.jianshu.com/p/b32da641e849)
>    - [iOS开发之注册美国Apple Id不需要绑定信用卡，亲测可用](https://blog.csdn.net/ziyuzhiye/article/details/82769129)


### 4.3 VPN 客户端

对于L2TP/IPSec，几乎所有的客户端操作系统（无论是Windows/Mac/Linux的电脑，还是iPhone/Android）都支持，你可以自行Google。

- [Mac OS X PPTP/L2TP设置教程](https://www.jianshu.com/p/24e48cfb574f)
- [Windows 7操作系统配置L2TP VPN方法](http://nic.upc.edu.cn/2016/0928/c7809a132077/page.htm)

## 5. 流量伪装和其它方式

无论你用VPN，SS，SSR，都有可能被识别，**只有使用 HTTP over TLS 的样子，才会跟正常的流量混在一起，很难被识别**，所以，目前来说，V2Ray客户端 + Nginx + V2Ray服务端的方式，或是gost的HTTPS的方式，基本上来说，在网络四层上看到的都是TLS的包，很难被识别。这种代理服务我觉得只能做探测，或是得到更多的算力来做统计学分析。所以，V2Ray 和 gost 的服务器端用 nginx 再挡一道，那么就很难被发现了。

> **注：** 说句老实话，我其时并不想害怕别人知道自己的上什么样的网站，因为我觉得我访问的都是合法的网站，但是就今天这个局势我也没办法——为什么要让像我这样的光明正大的良民搞得跟偷鸡摸狗之徒一样……

### 5.1 V2Ray

V2Ray 可以配置成一个非常隐蔽的代理软件。

 - V2Ray 用户手册：[https://www.v2ray.com](https://www.v2ray.com)
 - V2Ray 项目地址：[https://github.com/v2ray/v2ray-core](https://github.com/v2ray/v2ray-core)
 - V2Ray Telegram 使用群链接：[https://t.me/projectv2ray](https://t.me/projectv2ray)


一般来说，祼用 V2Ray 不是一个很好的方式，现在比较流行的是使用nginx来代理，也就是 V2Ray + Websocket + TLS + Nginx，可以参看这篇文章《[V2Ray+WebSocket+TLS+Nginx配置与使用教程](https://doubibackup.com/v2ray-ws-tls-nginx.html)》（需要翻墙）。

我个人觉得，配置起来比较复杂，而且环节太多，不如直接用 `gost` 的 https/http2 的方式配置起来简单，所以，没有放在前面。


### 5.2 Brook

Brook是一个由 Go语言编写的跨平台代理软件，支持 Linux/MacOS/Windows/Android/iOS 各个平台。

- Brook Github项目：[https://github.com/txthinking/brook](https://github.com/txthinking/brook)
- Github Wiki教程：[https://github.com/txthinking/brook/wiki/使用说明(中文)](https://github.com/txthinking/brook/wiki/使用说明(中文))

服务器一行命令安装：

```
wget -N --no-check-certificate https://raw.githubusercontent.com/ToyoDAdoubi/doubi/master/brook.sh && chmod +x brook.sh && bash brook.sh
```

运行 `brook.sh` 会出菜单项，你可以按菜单项来，主要就是设置端口号，密码。很简单的，我这里就不截图了，因为这个脚本运行起来中文菜单式的。

然后你可以在 Brook 项目的 Github 首页上下载不同平台的客户端。设置起来也很简单！

> 注意: 如果运行出现下载错误，可能是因为brook的下载文件名问题，你需要自己修改一下脚本：
>
> ```
> Download_brook(){
>  	[[ ! -e ${file} ]] && mkdir ${file}
>  	cd ${file}
>  	if [[ ${bit} == "x86_64" ]]; then
> -		wget --no-check-certificate -N "https://github.com/txthinking/brook/releases/download/${brook_new_ver}/brook"
> +		wget --no-check-certificate -N "https://github.com/txthinking/brook/releases/download/${brook_new_ver}/brook_linux_amd64"
> +		mv brook_linux_amd64 brook
>  	else
>  		wget --no-check-certificate -N "https://github.com/txthinking/brook/releases/download/${brook_new_ver}/brook_linux_386"
>  		mv brook_linux_386 brook
>  	fi
> ```

## 6. 针对 IP 被封的解决方案

花钱购买的 VPS 即便做了流量伪装依然有很大的几率 IP 被封锁，大多 VPS 服务商并不提供更换 IP 的服务，使用 CDN 可以让被封锁的 VPS 继续发挥翻墙功能。

### 6.1 Cloudflare

Cloudflare 是一个 CDN 服务商，目前国内依然能正常的访问，可以作为跳板来实现翻墙。

注册 Cloudflare 帐号，并有一个空闲域名（三级域名即可），交给 Cloudflare 托管并将域名指向被封的 VPS IP，注意开启 Proxied 并且 SSL-TLS 使用 Flexible 选项。

Cloudflare 只需免费方案足以，不必花钱。

### 6.2 V2Ray

VPS 上正常安装并配置好 V2Ray，注意两点:

1. 传输协议必须要使用 ws
2. 要使用 80 或者 8080 端口

如果端口有其他用途，那么用 Nginx/Caddy 之类软件，做一个 WebSocket proxy 到 V2Ray 即可。

### 6.3 补充

客户端注意使用网址来连接。

目前支持 WebSocket 的免费 CDN 似乎只有 Cloudflare 一家，国内 CDN 服务商既不支持也不安全，不要考虑了。如果有更好的服务商欢迎补充。

网络延迟比直连增加不少，如果是频繁操作会很痛苦。网络带宽如果运气好可能比直连还优化了，用来看 Youtube 搞不好更流畅。

## 7. 透明网关

### 7.1 OpenWRT 路由器

所谓透明网关的意思是，一切都交给网关来做。最好的方式是你需要一个 OpenWRT 的路由器，推荐使用华硕的路由器，贵是贵一些，但是这几年用下来，非常不错。我用的是  **华硕（ASUS） RT-AC68U 1900M AC 双频智能无线路由路** 。

路由器买来后，要刷一下固件。首先Asuswrt是华硕公司为他的路由器所开发的固件。Asuswrt-merlin是一个对Asuswrt固件二次开发进行各种改进和修正的项目。源代码在这里：[https://github.com/RMerl/asuswrt-merlin](https://github.com/RMerl/asuswrt-merlin)

不必担心把路由器刷废了，华硕的路由器可以让你一键重置回来

**1）下载固件**。先到 [https://asuswrt.lostrealm.ca/download](https://asuswrt.lostrealm.ca/download) 下载相应的固件，并解压。（我下载的是 `RT-AC68U_380.61_0.zip` ）

**2）升级固件**。登录到你的路由器后台 `http://192.168.1.1/` ，在 `系统管理` -> `固件升级` 中上传固件文件（我上传的是：`RT-AC68U_380.61_0.trx`）

**3）打开 JFFS 分区**。`系统管理` -> `系统设置` -> `Persistent JFFS2 partition`

- `Format JFFS partition at next boot` - `否`
- `Enable JFFS custom scripts and configs` - `是`


**4）打开 ssh 登录**。 `系统管理` -> `系统设置` -> `SSH Daemon` 

- `Allow SSH password login` - `是`

### 7.2 通过树莓派做旁路网关

如果你的路由器不能刷OpenWRT，也就是没发通过SSH登录上去装软件，你就用一个别的设备。比如用一个树莓派。我正好有一个很老旧的树莓派，刷了一个老旧的Debain 7.5的操作系统。

把它连上你的路由器上，然后，
- 你需要把你设备上的IP地址、网关和DNS服务器都要手动设置到这个树莓派上。
- 于是，所有的路由就会通过路由器转到树莓派上，再由树莓派决定是否要走代理。

大概的示意图如下所示。

- 1 --> 2 是设备把所有的请求都发给树莓派。
- 3 --> 3.1 或 3.2 是由树莓派来决走是否翻墙。

```
              Phone/PC/Pad
                    +
                    |  1
                    |
            +-------v-------+      2      +--------+
            |               |------------->        |
            |  WiFi 路由器   |             |  树莓派 |
            |               <-------------|        |
            +------+--+-----+      3      +--------+
                   |  |
                3.1|  | 3.2
                   |  +---------->  China LAN
                   v
               +---+---+
               | Proxy |
               +---+---+
                   |
                   |
                   v
             Internet WAN

```

### 7.3 安装 Clash

Clash 的 Github项目是：[Dreamacro/clash](https://github.com/Dreamacro/clash) ，在它的 Release 页面上，你可以找到相关的下载。（注：在本文更新的时候，如果你需要支持 Tun，你需要下载 Clash 的 [Premium 版本](https://github.com/Dreamacro/clash/releases/tag/premium)

Clash支持很多翻墙协议：ShadowSocks(R), Vmess, Socks5, HTTP(s)，Snell，Trojan。

在你的 OpenWRT 或 树莓派 下用 `uname -m` 查看一下你的硬件架构是什么的，比如，我的是华硕和树莓派都是 `armv7l` 的，所以，需要下载 `clash-linux-armv7-....`的版本。 下载完解压后，加个可执行权限 `chmod +x clash` 就可以运行了，不过，还差一个界面和两个配置文件，它们的目录关系如下：

```
├── clash                <- 建一个 clash 的目录
│   ├── clash            <- 运行文件 
│   ├── config.yaml      <- 配置文件 
│   ├── Country.mmdb     <- IP地址库
│   └── ui               <- Clash 的 UI
│       ├── index.html
│       ├── ...
```

- UI界面可以到 [haishah/yacd](https://github.com/haishanh/yacd) 下载。放到clash的配置目录下 `ui` 目录下

- 一个是 `Country.mmdb` 这是IP地址的在哪个国家的数据库。你需要到这里下载 - [Country.mmdb](https://github.com/Dreamacro/maxmind-geoip/releases/latest/download/Country.mmdb) （当然，clash启动时，会自动下载，我这里给你一个手动下载的链接）

- 另一个是 `config.yaml` 文件，这个文件详细解释可参看 - [官方Wiki](https://github.com/Dreamacro/clash/wiki/configuration)


下面是个示例：

```
port: 7890
socks-port: 7891
redir-port: 7892
mixed-port: 7893
ipv6: false
allow-lan: true
mode: Rule
log-level: info
external-controller: '0.0.0.0:9090'
external-ui: ui
secret: ''
tun:
  enable: true
  stack: system
  dns-hijack:
    - tcp://8.8.8.8:53
    - udp://8.8.8.8:53
dns:
  enable: true
  ipv6: false
  listen: 0.0.0.0:53
  default-nameserver:
    - 114.114.114.114
  #enhanced-mode: redir-host
  enhanced-mode: fake-ip #如果要玩netflix，需要使用fake-ip
  fake-ip-range: 198.18.0.1/16
  nameserver:
    - 114.114.114.114
    - 223.5.5.5
    - tls://8.8.8.8:853
  fallback:
    - tls://8.8.8.8:853

# 两个代理服务器
proxies:
  # http
  - name: "https01"
    type: http
    server: https.server.domain
    port: 443
    username: user
    password: "password"
    tls: true # https
    skip-cert-verify: true
  - name: "https01"
    type: http
    server: https.server.domain
    port: 443
    username: user
    password: "passowrd"
    tls: true # https
    skip-cert-verify: true

# 配置 Group
proxy-groups:
  # 自动切换
  - name: "auto"
    type: url-test
    proxies:
      - us01_https
      #- us02_https
      #- hk_https
    # tolerance: 150
    url: 'https://www.google.com/'
    interval: 300
  # 按需选择 - 可以在UI上选择
  - name: "netflix"
    type: select
    proxies:
      - us01_https
      - us02_https
      - hk_https

rules:
# LAN
  - DOMAIN-SUFFIX,local,DIRECT
  - IP-CIDR,127.0.0.0/8,DIRECT
  - IP-CIDR,172.16.0.0/12,DIRECT
  - IP-CIDR,192.168.0.0/16,DIRECT
  - IP-CIDR,10.0.0.0/8,DIRECT

# Netflix
  - DOMAIN-SUFFIX,fast.com,netflix
  - DOMAIN-SUFFIX,api-global.netflix.com,netflix
  - DOMAIN-SUFFIX,netflix.com,netflix
  - DOMAIN-SUFFIX,netflix.net,netflix
  - DOMAIN-SUFFIX,nflxext.com,netflix
  - DOMAIN-SUFFIX,nflximg.com,netflix
  - DOMAIN-SUFFIX,nflximg.net,netflix
  - DOMAIN-SUFFIX,nflxso.net,netflix
  - DOMAIN-SUFFIX,nflxvideo.net,netflix

# 最终规则（除了中国区的IP之外的，全部翻墙）
  - GEOIP,CN,DIRECT 
  - MATCH,auto

```
更多的规则网上可以找到很多，也可以参看这里：[SS-Rule-Snippet/LAZY_RULES/clash.yaml](https://github.com/Hackl0us/SS-Rule-Snippet/blob/master/LAZY_RULES/clash.yaml)

这个时候你就可以启动 clash 了：

```
/path/to/clash/cash -d /path/to/clash &
```

然后，你就可以把你的上网设备上的 路由网关 和 DNS 服务器都手动地配置成这个网关就好了（OpenWRT应该不用配置了，树莓派的方式需要手动配置一下）

### 7.4 设置 iptables 转发

```
iptables -t nat -N CLASH
iptables -t nat -A CLASH -d 10.0.0.0/8 -j RETURN
iptables -t nat -A CLASH -d 127.0.0.0/8 -j RETURN
iptables -t nat -A CLASH -d 169.254.0.0/16 -j RETURN
iptables -t nat -A CLASH -d 172.16.0.0/12 -j RETURN
iptables -t nat -A CLASH -d 192.168.0.0/16 -j RETURN
iptables -t nat -A CLASH -d 224.0.0.0/4 -j RETURN
iptables -t nat -A CLASH -d 240.0.0.0/4 -j RETURN
iptables -t nat -A CLASH -p tcp -j REDIRECT --to-ports 7892
```
然后，你可以保存一下这些iptables的规则

```
 iptables-save > /etc/iptables.up.rules
```
编辑  `//etc/network/if-pre-up.d/iptables`，在网卡启动的时候加载这些规则

```
#!/bin/sh
/sbin/iptables-restore < /etc/iptables.up.rules
```
然后，再 `chmod +x /etc/network/if-pre-up.d/iptables` 加上可执行权限就好了。

## 8. 其它 

### 8.1 其它方式

如下还有一些其它的方式（注：均由网友提供，我没有验证过）

[Outline](https://getoutline.org/en/home) 是由 Google 旗下 [Jigsaw](https://jigsaw.google.com/) 团队开发的整套翻墙解决方案。Server 端使用 Shadowsocks，MacOS, Windows, iOS, Android 均有官方客户端。使用 Outline Manager 可以一键配置 DigitalOcean。其他平台例如 AWS, Google Cloud 也提供相应脚本。主要优点就是使用简单并且整个软件栈全部[开源](https://github.com/Jigsaw-Code/?q=outline)，有专业团队长期维护。

### 8.2 搭建脚本

上述的搭建和安装脚本可参看本库的 scripts 目录下的脚本（感谢网友 [@gongzili456](https://github.com/gongzili456) 开发）

-  [Ubuntu 18.04 Installation Script](https://github.com/haoel/haoel.github.io/blob/master/scripts/install.ubuntu.18.04.sh) 

欢迎补充和改善！

（全文完）

