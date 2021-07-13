# 超星学习通全自动刷课程序
  
**发布日期: 2020-3-22**  
  
![count](https://img.shields.io/endpoint?url=https://quesbank.math.cat:6062/bank/getCountInfo)

---
2020-5-21 更新内容:  
添加了一个登录接口使得无验证码登录变得可能但是当新接口失效时会回退至上版本接口以保证程序可用性  

增加了config.json文件，通过config文件可以实现无交互登录以及筛选需要刷的课程, 该文件不存在时程序会以默认方式运行  
使用方法:  
在程序根目录下增加config.json文件, 并按照以下形式进行编写
```
{
	"uname": string, //手机号
	"password": string, //密码
	// 如果上面两个字段任何一个不存在程序都会让你输入一次完整的账号密码, 只有这两个是必要字段
	
	"speed": number, // 刷课速度 默认为 2  
	"test": boolean, // 是否过测试 默认为true  
	"pick": boolean, // 是否通过配置文件进行课程配置 默认为false  
	// 以上默认值都之会在config.json读取成功且没有该字段时生效, 如果config.json不存在则全部由键盘输入  
	// 当pick为true时且pickinfos字段不存在, 程序只会记录所有课程并写入pickinfos然后结束, pickinfos字段存在时程序会读取pickinfos并跳过所有picked为false的课程  
	
	"pickinfos": {

	}
	// 该字段由程序生成请勿手动编写, 只需要调整该字段内picked值即可
	// 重新获取课程请删除该字段而不仅是值

}
```
2020-3-31 更新内容:
  
修复一个任务点识别的问题  
假如你提前把上锁的课程的视频都刷好了  
由于学习通的识别逻辑比较简单，它会在你刷视频完成  
发生的那一刻（只有这一刻），检测一次任务点是否存在  
然后给任务点打上完成的标记。  
  
但是假如老师并没有开放这个章节，自然也不存在这个任务点。  
但是由于协议可以把老师没有开放的章节里的视频也刷掉。  
就会出现一种情况：视频刷完了，后台也记录了，但是任务点并没有过。  
  
本版本换了一种判别任务点的方法，从原本的判断视频有没有刷完，  
改为判断视频对应的任务点有没有过。  
  
建议所有用户都更新到最新版。  
  
有关解决该问题的commit：https://github.com/ZhyMC/chaoxing-xuexitong-autoflush/commit/a1f7af

2020-3-27 更新内容:  
<strong> ①新增自动过测验功能,新增共享题库.</strong>  
  
题库是一个人人为我,我为人人的机制.运行本程序后,  
会自动分享你的正确答案到题库,然后你可以任意使用题库里的  
正确答案自动过测验.  

该功能测试中,欢迎参与测试  
  
  
2020-3-24 更新内容：  
①修复一章节多卡片，只支持自动过第一张卡片中的视频的问题  
有关该问题的issue:  
https://github.com/ZhyMC/chaoxing-xuexitong-autoflush/issues/3  

②增加自定义选择课程功能  
有关该特性建议的issue:  
https://github.com/ZhyMC/chaoxing-xuexitong-autoflush/issues/4  
  
  
2020-3-23 更新内容：  
  
①彻底修复有时刷完视频，无法成功完成任务点的BUG  
有关该问题的issue:  
https://github.com/ZhyMC/chaoxing-xuexitong-autoflush/issues/2  
  
②新增任意调倍速功能，以超快的速度刷完所有章节  

---

声明: 本程序仅供学习研究程序工程原理

![desc1](https://raw.githubusercontent.com/ZhyMc/chaoxing-xuexitong-autoflush/master/imgs/chaoxing1.png)
![desc2](https://raw.githubusercontent.com/ZhyMc/chaoxing-xuexitong-autoflush/master/imgs/chaoxing3.png)
![desc3](https://raw.githubusercontent.com/ZhyMc/chaoxing-xuexitong-autoflush/master/imgs/chaoxing2.png)

---
```
若该程序对你有帮助，请给作者一颗star以表示鼓励，谢谢！
```

---

用法:

---

① 
```
git clone https://github.com/ZhyMc/chaoxing-xuexitong-autoflush
```
② 
```
cd chaoxing-xuexitong-autoflush   (到程序目录底下)
```
③
```
npm install
```

之后你就可以通过执行 

```
npm start 
```

启动本程序

---
如果看不懂上面的步骤（上面步骤需要一点编程知识），你可以参照详细使用步骤：  
  
Windows (x64)系统:  
  
①进入 http://nodejs.cn/download/ 下载 nodejs 的 "windows安装包"  
②打开安装包并安装，以保证你的机器拥有 Node.js 运行环境  
③进入 http://npm.taobao.org/mirrors/git-for-windows/v2.26.0-rc2.windows.1/ 下载 git 安装包  
你可以选择此版本：Git-2.26.0-rc2-64-bit.exe  
④打开安装包并安装，以保证你的机器拥有 Git 环境。  
  
⑤打开命令行，你可以按Win键+R，然后输入cmd打开  
⑥依次敲入命令并执行  
  
```
git clone https://github.com/ZhyMc/chaoxing-xuexitong-autoflush
```
```
cd chaoxing-xuexitong-autoflush
```
```
npm install
```
每次执行请等待命令的执行完毕再运行下一个命令  
然后通过运行命令  
```
npm start
```
启动本程序

⑦之后你都可以通过打开cmd (Win+R) 再运行  
```
cd chaoxing-xuexitong-autoflush
```
```
npm start
```
的方式启动本程序  
  
---
说明：
```
本程序会自动遍历你的所有课程，课程的所有章节，甚至包括上锁的章节内的视频都会被自动刷完。
所以你可以挂机本程序至后台。因为由 Node.js 平台编写，你可以在Linux下运行本程序.
```
