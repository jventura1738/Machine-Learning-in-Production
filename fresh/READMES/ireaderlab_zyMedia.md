# zyMedia —— 一个轻量级媒体播放器

zyMedia是一款基于HTML5原生multimedia、自定义UI的多媒体播放器。

已用于公司的各非本地化产品线。

* 支持Android、iOS移动端平台
* 支持主流移动设备及国内TOP10移动端浏览器
（机型和浏览器版本更新较快，欢迎提issue，方便请标注下机型和环境，比如客户端版本（客户端内打开），浏览器默认的navigator.userAgent（浏览器打开））
* 支持多种视频、音频格式，如mp4、mp3、oga、webm等
* 轻量，UglifyJS压缩15KB，gzip约5k


## 视频界面展示

![video ui](docs/images/video_ui_v1.1.jpg)


## 使用说明

1. 引入样式文件zy.media.css和js文件zy.media.js
2. 输入html结构，例如视频，其中video标签的data-config属性用于设置参数，
```html

<div class="zy_media">
    <video poster="test.jpg" data-config='{"mediaTitle": "《疯狂动物城》--腾讯视频"}'>
        <source src="test.mp4" type="video/mp4">
        您的浏览器不支持HTML5视频
    </video>
</div>

```
3. 绑定媒体节点，zymedia是一个全局对象，可重复调用，不返回视频实例，需要的话建议直接获取视频和监听相应事件，第二个参数是用于批量设置视频参数，示例
```javascript

    zymedia('video');
    // zymedia('video', {...参数});

```

    zymedia是做批量处理用的，单独设置用每个音视频上的data-config，
    每个音视频的src可随时替换（比如document.querySelector('video').src = 'test.mp4'），容器尺寸会保持不变


## 参数说明
* type: ''<br>
指定媒体类型，默认空

* mediaTitle: ''<br>
设置媒体标题，默认空，不展示

* nativeControls: false<br>
强制用原生的播放控制器，默认不使用，true为使用

* autoplay: false<br>
是否自动播放，默认否，true为自动播放

* preload: 'none'<br>
是否预加载，默认关闭，和原生preload对应，其他值为metadata|auto|''

* videoWidth: '100%'<br>
指定视频宽，默认100%

* videoHeight: 'auto'<br>
指定视频高，默认auto

* aspectRation: (16 / 9)<br>
指定视频宽高比，默认16:9

* audioWidth: '100%'<br>
指定音频宽，默认100%

* audioHeight: 44<br>
指定音频高，默认44px

* autoLoop: false<br>
是否循环播放，默认否，true为无限循环

* timeFormatType: 1<br>
时间格式类型，默认mm:ss，2为m:s

* alwaysShowHours: false<br>
是否强制显示小时位，默认否，true为显示

* alwaysShowControls: false<br>
是否始终显示控制栏，默认否，自动隐藏，true为始终显示

* hideVideoControlsOnLoad: false<br>
加载时是否隐藏视频控制栏，默认否，true为隐藏

* enableFullscreen: true<br>
是否显示全屏按钮，默认显示，false为不显示

* pauseOtherPlayers: true<br>
是否播放唯一，默认唯一，播放时将暂停其他播放实例，false为不唯一

* enableVisibilityState: true,<br>
是否页面不可见时暂停当前所有播放，默认暂停

* duration: 0<br>
指定媒体时长，默认0

* success: null<br>
实例化成功时的回调，默认无

* error: null<br>
实例化错误时的回调，默认无

* beforePlay: null<br>
点击播放前的交互，默认无，如果函数返回true，将不播放视频


## 已测试移动设备列表

* 小米1、小米2s、小米 MI3、红米、小米 Mi-4C、小米平板 MI PAD

* vivo X5Max L、vivo Y33、vivo s7i(t)、vivo X6

* 联想sisley2OFPL、联想A3860、联想 s720、联想 A820T

* 魅蓝m1、魅蓝m2 note、魅族MX4、魅族 MX5、魅族 MX M031、魅蓝 note 2 M571C

* NX(yunOS)、NX青橙(yunOS)

* HTC T328d、HTC onex、HTC S710d、HTC X920e、HTC Desire

* coolpad 8190、Coolpad5950

* OPPO A31、OPPO R821T

* 三星i9100、三星 GT-I9000、三星 GT-I9220、三星 GT-S5360、三星 GT-i9300、三星平板 Galaxy Tab S SM-T805C

* 华为 C8650、华为 C8812、华为 MT1-U06、华为 PE-TL20(荣耀6plus)、华为荣耀5X、华为 A199、Honor U8860、荣耀6 H60-L01、华为 GRA-UL10、华为荣耀平板

* 金立v182、GioNEE GN9000L、GioNEE GN9001L

* iPhone4S、iPhone5C、iPhone5S、iPhone 6、iPhone 6 Plus、iPhone 7 Plus, iPad mini、iPad

* nexus 5x、SONY S39h、AMOI N828、TCL S720T、Newman、中兴V960、小辣椒LA2-L、摩托罗拉ME863、读者 i800、昂达平板 V819mini


## 常见问题

* autoplay自动播放受限（preload类似）

	据说Android4+和iOS6 - 9开始，禁用了非用户行为触发autoplay，chrome可以在flags里启用“停用媒体播放的手势要求”

	[2016.11.17 苹果开发者官网](https://developer.apple.com/library/content/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/AudioandVideoTagBasics/AudioandVideoTagBasics.html#//apple_ref/doc/uid/TP40009523-CH2-SW8)的解释是：

	> Warning: To prevent unsolicited downloads over cellular networks at the user’s expense, embedded media cannot be played automatically in Safari on iOS—the user always initiates playback.

    iOS10+，策略已发生改变，允许静音下自动播放[webkit官方博客](https://webkit.org/blog/6784/new-video-policies-for-ios)

* 全屏播放受限

	插件的全屏按钮只是触发浏览器（或客户端浏览器内核）全屏事件，是否能全屏要看浏览器或客户端自身实现。

* 黑边

	通常是poster图的尺寸比例和视频尺寸比例不一致，如果不能自己裁剪图的话，可以把poster图单拿出来，盖在视频上。

* 音视频格式支持
    
    插件使用的浏览器自身的解码，具体解码要看浏览器自身对格式支持情况和播放时环境，通常浏览器支持情况见[维基百科](https://en.wikipedia.org/wiki/HTML5_video)，[MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Supported_media_formats)。




## 开源交流
* QQ群：329474804
