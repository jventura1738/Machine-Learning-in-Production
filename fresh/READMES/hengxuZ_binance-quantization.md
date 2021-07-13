# 数字货币量化交易-网格策略

推荐使用 -> 
v2版 [现货做多网格](https://github.com/hengxuZ/spot-trend-grid)

v3版 [双向多空合约网格](https://gitee.com/XingFuCunDeMaNong/bothway-grid)

v4版 [趋势做空网格](https://github.com/hengxuZ/future-short-grid)


---

### 介绍
这是一款**单方向(多)现货网格交易策略**的量化项目。
并且支持防踏空,行情上涨。网格价也自动提升。

### 优势：🎉
1. 简单易上手
2. 安全(不用将api_secret告诉他人)

### 为什么选择币安交易所
最开始我使用的是火币网的api接口来做量化交易，久而久之，我发现交易的手续费看起来很少，但是一个月下来也是一笔不小的数目。所以我得赶忙找一个手续费低的大平台交易所，所以我选择了币安
> 火币手续费 Maker 0.2% Taker 0.2%

> 币安手续费 Maker 0.1% Taker 0.1% （加上BNB家持手续费低至0.075%）



### 如何启动

1. 修改app目录下的authorization文件

```
api_key='你的key'
api_secret='你的secret'

dingding_token = '申请钉钉群助手的token'   # 强烈建议您使用 （若不会申请，请加我个人微信）
```
申请api_key地址: [币安API管理页面](https://www.binance.com/cn/usercenter/settings/api-management)

如果你还没有币安账号： [注册页面](https://www.binancezh.io/zh-CN/register?ref=OW7U53AB)[免翻墙地址](https://www.binancezh.cc/zh-CN/register?ref=OW7U53AB)交易返佣20% 注册立刻返现10元，充值交易再返现10元。

或者可以注册火币账号：[注册页面](https://www.huobi.ms/zh-cn/topic/double-reward/?invite_code=w2732223)交易返佣15% 注册立刻返现5元，充值并且交易再返现10元

交易返佣计算公式：交易金额1W元 * 手续费比率0.1% * 0.02 = 2元（交易1w节约2元）


2. 修改data/data.json配置文件  （参数详细解读->[一定要看](https://github.com/hengxuZ/binance-quantization/blob/master/dev-ReadMe.md)）
```
{
    "runBet": {
        "next_buy_price": 350,      <- 下次开仓价   （你下一仓位买入价）
      
        "grid_sell_price": 375      <- 当前止盈价  （你的当前仓位卖出价）
        "step":0                    <- 当前仓位  （0:仓位为空）
    },
    "config": {
        "profit_ratio": 5,         <- 止盈比率      （卖出价调整比率。如：设置为5，当前买入价为100，那么下次卖出价为105）
        "double_throw_ratio": 5,   <- 补仓比率      （买入价调整比率。如：设置为5，当前买入价为100，那么下次买入价为95）
        "cointype": "ETHUSDT",     <- 交易对        （你要进行交易的交易对，请参考币安现货。如：BTC 填入 BTC/USDT）
        "quantity": [1,2,3]        <- 交易数量       (第一手买入1,第二手买入2...超过第三手以后的仓位均按照最后一位数量(3)买入)
        
    }
}

```
3. 安装依赖包
'''
pip install requests
'''
4. 运行主文件
```
# python eth-run.py 这是带有钉钉通知的主文件(推荐使用钉钉模式启动👍)
```


### 注意事项（一定要看）
- 由于交易所的api在大陆无法访问,请使用海外服务器才能够稳定运行

- 如果您使用的交易所为币安，那么**请保证账户里有足够的bnb**
    - 手续费足够低
    - 确保购买的币种完整(如果没有bnb,比如购买1个eth,其中你只会得到0.999。其中0.001作为手续费支付了)
- 第一版本现货账户保证有足够的U（一般交易对最少10u购买一次）
- 第三版本现货、合约账户保证有足够的U
- 默认运行环境是国外的服务器,默认环境是python3(linux自带的是python2)
### 钉钉预警

如果您想使用钉钉通知，那么你需要创建一个钉钉群，然后加入自定义机器人。最后将机器人的token粘贴到authorization文件中的dingding_token
关键词输入：报警

#### 钉钉通知交易截图

![钉钉交易信息](https://s3.ax1x.com/2021/02/01/yZSi1x.jpg)
#### 1月到5月实战收益
![收益图](https://z3.ax1x.com/2021/05/15/gyLTB9.jpg)

如果您不想那么麻烦，又是python、linux 服务器。可以使用下面链接注册派网。体验网格交易
![派网注册](https://www.pionex.cc/zh-CN/sign/ref/gP7byIO9)（通过该链接注册的用户，加我立马返现5元）



![币圈快讯爬取群](https://s3.ax1x.com/2021/02/01/yZSU4s.jpg)
![钉钉群二维码](https://i0.hdslb.com/bfs/album/4f50bfd7f1fddaa7c340bc06d7ce078404670fb2.jpg)

![拉vx群助手](https://z3.ax1x.com/2021/07/09/RxkHW4.jpg) 
### 私人微信：欢迎志同道合的朋友一同探讨，一起进步。
#### qq群号：1143200770
![qq群](https://z3.ax1x.com/2021/07/09/RxAllj.jpg)
麻烦备注来自github
### 钉钉设置教程
![钉钉设置教程](https://s3.ax1x.com/2021/01/08/suMVIK.png)


### 钉钉设置教程
![钉钉设置教程](https://s3.ax1x.com/2021/01/08/suMVIK.png)

重大喜讯第三版本它来了！！真正的网格多空！！

### 🎉第三版本🎉 （双向网格、多空、趋势开单）
点击➡ 查看[项目地址](https://gitee.com/XingFuCunDeMaNong/bothway-grid)


### 免责申明
本项目不构成投资建议，投资者应独立决策并自行承担风险
币圈有风险，入圈须谨慎。

> 🚫风险提示：防范以“虚拟货币”“区块链”名义进行非法集资的风险。
