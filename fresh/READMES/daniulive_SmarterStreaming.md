**视沃科技-大牛直播SDK <a href="https://daniusdk.com" target="_blank">daniusdk.com</a>**

业内为数不多致力于极致体验的**超强全自研跨平台**(windows/android/iOS)**流媒体内核**，通过模块化自由组合，支持实时RTMP推流、RTSP推流、RTMP/RTSP直播播放(**支持RTSP/RTMP H.265**)、实时**录像**、多路流媒体**转发**(RTSP转RTMP，RTMP转RTMP)、音视频导播、动态视频合成、音频混音、**一对一互动**直播、内置轻量级RTSP服务、RTSP网关服务等，**比快更快**，业界**真正靠谱**的超低延迟直播SDK(1秒内，低延迟模式下200~400ms)。

适用于**在线教育、[智慧教室|无纸化推屏|会议](https://daniusdk.com/index.php/2020/01/09/%e5%9f%ba%e4%ba%8e%e6%99%ba%e6%85%a7%e6%95%99%e5%ae%a4%e6%97%a0%e7%ba%b8%e5%8c%96%e4%bc%9a%e8%ae%ae%e7%9a%84%e6%96%b0%e9%80%89%e6%8b%a9%ef%bc%9artmp%e8%a7%a3%e5%86%b3%e6%96%b9%e6%a1%88/)、运营商视频云平台、远程医疗、金融双录、智能可视门禁对讲、智慧安防、智能家居、物联网、智能车载、传统硬件领域、媒体移动直播、应急指挥调度(针对保险、城管、交警、消防、公安等职能管理部门的单兵应急执法系统)、远程专家诊断、可视化巡检、(如电信/电力线路/铁路沿线/水利设施/油田/消防设施巡检)、移动视频安防监控，企业内训、监控对接、活动现场直播**等场景。

**[视沃科技(大牛直播SDK)官方测试版获取流程](https://daniusdk.com/index.php/2020/09/10/%e8%a7%86%e6%b2%83%e7%a7%91%e6%8a%80%e5%a4%a7%e7%89%9b%e7%9b%b4%e6%92%adsdk%e5%ae%98%e6%96%b9%e6%b5%8b%e8%af%95%e7%89%88%e8%8e%b7%e5%8f%96%e6%b5%81%e7%a8%8b/)**

**[latest release note](https://daniusdk.com/index.php/tag/release-note/)**

## 平台扩展 ## 

除了Windows/Android/iOS Native SDK，大牛直播SDK发布了Unity环境下的RTMP推流（Windows平台+Android平台）和RTMP|RTSP拉流（Windows平台+Android平台+iOS平台）低延迟的解决方案。

目前，大牛直播SDK的Unity3D环境下，已覆盖以下SDK：

- [x] Windows平台RTMP直播推送SDK（采集Unity窗体、摄像头或屏幕）;
- [x] Windows平台RTMP|RTSP直播播放SDK；
- [x] Android平台RTMP直播推送SDK（采集Unity窗体）；
- [x] Android平台RTMP|RTSP直播播放SDK；
- [x] iOS平台RTMP|RTSP直播播放SDK。

**[大牛直播SDK Unity3D接口调用SDK说明](http://daniusdk.com/wp-content/uploads/2021/06/%E8%A7%86%E6%B2%83%E7%A7%91%E6%8A%80-%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADSDKV2Unity3D%E8%B0%83%E7%94%A8%E8%AF%B4%E6%98%8E1.5.pdf)**

**[Unity3d RTSP/RTMP直播播放端SDK视频演示](http://web1712221406366.gz01.bdysite.com/wp-content/uploads/2018/05/unity3d-android-iOS.mp4)**

相关博客：

- [x] [Windows平台实现Unity下窗体|摄像头|屏幕采集推送](https://blog.csdn.net/renhui1112/article/details/117785180)
- [x] [Android平台实现Unity3D下RTMP推送](https://blog.csdn.net/renhui1112/article/details/117669587)
- [x] [Windows平台Unity3d下如何同时播放多路RTSP或RTMP流](https://blog.csdn.net/renhui1112/article/details/114674572)
- [x] [如何在Unity3d平台下低延迟播放RTMP或RTSP流](https://blog.csdn.net/renhui1112/article/details/104154788)

## 模块概览 ## 

**RTSP/RTMP推拉流SDK概览图**

<img src="https://img-blog.csdnimg.cn/2020020612174317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Jlbmh1aTExMTI=,size_16,color_FFFFFF,t_70" alt="RTSP/RTMP推拉流SDK概览图" />

**多路RTSP/RTMP转RTMP推送SDK概览图**

<img src="http://daniusdk.com/wp-content/uploads/2020/01/daniulive_relaysdk_20200130.png" alt="多路RTSP/RTMP转RTMP推送SDK概览图" />

## 支持平台架构 ##
|支持平台|支持架构|
| ----|-----|
|Windows平台|x86 debug/release, x64 debug/release |
|Android平台|armeabi-v7a, arm64-v8a, x86, x86_64|
|iOS平台|armv7, arm64|

**Windows端**

- [x] [**RTMP直播推流SDK**](https://daniusdk.com/index.php/2018/04/02/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) RTMP推送SDK(支持同时推多路url，支持**RTMP扩展H.265推送**(64位库)))；

- [x] [**RTSP直播推流SDK**](https://daniusdk.com/index.php/2018/12/14/rtsp%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) 支持RTSP H.264/H.265推送，音频支持AAC格式，支持TCP/UDP模式推送，支持RTSP鉴权，支持重连和异常网络处理，超低延迟；

- [x] [**RTMP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtmp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内首屈一指的RTMP超低延迟直播播放器SDK(**支持RTMP H.265扩展播放**)；

- [x] [**RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtsp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 支持RTSP H.265播放及扩展录像、业内为数不多真正好用的RTSP播放器SDK，支持IE浏览器**OCX控件**接口调用；

- [x] [**Unity3D RTMP/RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/06/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsdk-unity3d%E7%9B%B4%E6%92%AD%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内为数不多的Windows支持Unity3D的超低延迟RTMP/RTSP直播播放器SDK，支持快照、录像、实时静音、view旋转、快速切换URL等特性；

- [x] [**RTMP/RTSP多路流媒体转RTMP推送SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%9A%E8%B7%AF%E6%B5%81%E5%AA%92%E4%BD%93%E8%BD%AC%E5%8F%91sdk/) 支持同时**多路拉取rtmp/rtsp流/本地flv文件，并分别转发到服务器**，业内为数不多**支持RTSP/RTMP H.265拉流转发**的SDK；

- [x] [**轻量级RTSP服务SDK**](https://daniusdk.com/index.php/2018/06/22/%E8%BD%BB%E9%87%8F%E7%BA%A7rtsp%E6%9C%8D%E5%8A%A1sdk/) 为满足内网无纸化/电子教室等内网超低延迟需求，避免让用户配置单独的服务器，大牛直播SDK在推送端支持轻量级RTSP服务SDK，推送端SDK支持的功能，内置轻量级RTSP服务SDK后，功能继续支持，windows端特定机型支持**RTSP H.265**视频输出，支持**单播**和**组播**模式；

- [x] [**内网RTSP网关SDK**](https://daniusdk.com/index.php/2018/11/10/%E5%86%85%E7%BD%91rtsp%E7%BD%91%E5%85%B3sdk/) 内网RTSP网关SDK，系内置轻量级RTSP服务SDK扩展，完成**外部RTSP/RTMP数据拉取并注入到轻量级RTSP服务SDK工作**，多个内网客户端直接访问内网轻量级RTSP服务获取公网数据，无需部署单独的服务器，支持RTSP/RTMP H.265数据接入，支持**单播**和**组播**模式；

- [x] [**导播SDK**](https://daniusdk.com/index.php/2018/06/23/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E5%AF%BC%E6%92%ADsdk/) 数据源：1. rtmp/rtsp音视频流；2. 本地屏幕/摄像头/音频数据；3.本地flv文件；**多路流合成一路**实时导播推送；

- [x] [**录像SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E5%BD%95%E5%83%8Fsdk/) 支持拉取rtmp/rtsp流实时**录像**模块/实时**快照**功能，支持纯音频、纯视频、音视频录制模式，支持音频(PCMU/PCMA,Speex等)**转AAC**后再录像，业内为数不多的支持**RTSP/RTMP H.265录制到MP4文件**的录像SDK；

- [x] [**RTMP/RTSP一对一互动SDK**](https://daniusdk.com/index.php/2018/12/01/%E4%B8%80%E5%AF%B9%E4%B8%80%E4%BA%92%E5%8A%A8sdk/) 基于标准协议(RTMP或RTSP)的跨平台(Windows/Andriod/iOS)一对一互动SDK，支持回音消除，完美支持一对一互动场景；

- [x] [**连麦SDK**](https://daniusdk.com/index.php/2018/06/23/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E8%BF%9E%E9%BA%A6sdk/) 以标准协议为基础，完美支持Windows连麦；

- [x] [**SEI扩展数据发送/接收SDK**](https://daniusdk.com/index.php/2018/07/10/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsei%E6%89%A9%E5%B1%95%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81-%E6%8E%A5%E6%94%B6sdk/) 支持推送端通过H.264 SEI信息扩展，实时传输文本/二进制数据信息(如实时字幕/时间戳/题目分发/公告广播等)，播放端做相应解析和回显；

- [x] [**视频处理SDK**](https://daniusdk.com/index.php/2018/09/21/%E9%9F%B3%E9%A2%91%E9%87%87%E9%9B%86%E5%A4%84%E7%90%86sdk/) 屏幕/多摄像头/水印/遮挡区域多层自由合成模块；

- [x] [**音频处理SDK**](https://daniusdk.com/index.php/2018/09/21/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86%E5%A4%84%E7%90%86sdk/) 多路混音、回音消除、噪音抑制、自动增益、VAD检测模块；

**Android端**

- [x] [**RTMP直播推流端SDK**](https://daniusdk.com/index.php/2018/04/02/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) Android屏幕、摄像头RTMP推流SDK，支持**RTMP扩展H.265推送**(H.265硬编码)；

- [x] [**RTSP直播推流SDK**](https://daniusdk.com/index.php/2018/12/14/rtsp%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) 支持RTSP H.264/H.265推送，音频支持AAC格式，支持TCP/UDP模式推送，支持RTSP鉴权，支持重连和异常网络处理，超低延迟；

- [x] [**RTMP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtmp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内首屈一指的RTMP超低延迟直播播放器SDK(**支持RTMP H.265扩展播放**)；

- [x] [**RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtsp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 支持RTSP H.265播放及扩展录像、业内为数不多真正好用的RTSP播放器SDK;

- [x] [**Unity3D RTMP/RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/06/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsdk-unity3d%E7%9B%B4%E6%92%AD%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内为数不多的Android支持Unity3D的超低延迟RTMP/RTSP直播播放器SDK，支持快照、录像、实时静音、view旋转、快速切换URL等特性;

- [x] [**录像SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E5%BD%95%E5%83%8Fsdk/) 支持拉取rtmp/rtsp流实时**录像**模块/实时**快照**功能，支持纯音频、纯视频、音视频录制模式，支持音频(PCMU/PCMA,Speex等)**转AAC**后再录像，业内为数不多的支持**RTSP/RTMP H.265录制到MP4文件**的录像SDK；

- [x] [**RTMP/RTSP多路流媒体转RTMP推送SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%9A%E8%B7%AF%E6%B5%81%E5%AA%92%E4%BD%93%E8%BD%AC%E5%8F%91sdk/) 支持实时拉取的rtmp/rtsp流转发到指定rtmp url;

- [x] [**轻量级RTSP服务SDK**](https://daniusdk.com/index.php/2018/06/22/%E8%BD%BB%E9%87%8F%E7%BA%A7rtsp%E6%9C%8D%E5%8A%A1sdk/) 为满足内网无纸化/电子教室等内网超低延迟需求，避免让用户配置单独的服务器，大牛直播SDK在推送端支持轻量级RTSP服务SDK，推送端SDK支持的功能，内置轻量级RTSP服务SDK后，功能继续支持(支持H.265)；

- [x] [**RTMP/RTSP一对一互动SDK**](https://daniusdk.com/index.php/2018/12/01/%E4%B8%80%E5%AF%B9%E4%B8%80%E4%BA%92%E5%8A%A8sdk/) 基于标准协议(RTMP或RTSP)的跨平台(Windows/Andriod/iOS)一对一互动SDK，支持回音消除，完美支持一对一互动场景；

- [x] [**SEI扩展数据发送/接收SDK**](https://daniusdk.com/index.php/2018/07/10/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsei%E6%89%A9%E5%B1%95%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81-%E6%8E%A5%E6%94%B6sdk/) 支持推送端通过H.264 SEI信息扩展，实时传输文本/二进制数据信息(如实时字幕/时间戳/题目分发/公告广播等)，播放端做相应解析和回显；

- [x] [**视频处理SDK**](https://daniusdk.com/index.php/2018/09/21/%E9%9F%B3%E9%A2%91%E9%87%87%E9%9B%86%E5%A4%84%E7%90%86sdk/)Android文字水印、png图片水印；

- [x] [**音频处理SDK**](https://daniusdk.com/index.php/2018/09/21/%E8%A7%86%E9%A2%91%E9%87%87%E9%9B%86%E5%A4%84%E7%90%86sdk/)Android回音消除、噪音抑制、自动增益、VAD检测模块；


**iOS端**

- [x] [**RTMP直播推流端SDK**](https://daniusdk.com/index.php/2018/04/02/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) iOS屏幕(基于[ReplayKit](https://daniusdk.com/index.php/2018/04/02/%E5%A6%82%E4%BD%95%E5%9F%BA%E4%BA%8Ereplaykit%E5%AE%9E%E7%8E%B0%E4%BD%8E%E5%BB%B6%E8%BF%9Frtmp%E6%8E%A8%E5%B1%8F/))、摄像头RTMP推流SDK;

- [x] [**RTSP直播推流SDK**](https://daniusdk.com/index.php/2018/12/14/rtsp%E7%9B%B4%E6%92%AD%E6%8E%A8%E6%B5%81sdk/) 支持RTSP H.264/H.265推送，音频支持AAC格式，支持TCP/UDP模式推送，支持RTSP鉴权，支持重连和异常网络处理，超低延迟；

- [x] [**RTMP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtmp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内首屈一指的RTMP超低延迟直播播放器SDK(**支持RTMP H.265扩展播放**);

- [x] [**RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/12/12/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADrtsp%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 支持RTSP H.265播放及扩展录像、业内为数不多真正好用的RTSP播放器SDK;

- [x] [**Unity3D RTMP/RTSP直播播放器SDK**](https://daniusdk.com/index.php/2018/06/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsdk-unity3d%E7%9B%B4%E6%92%AD%E6%92%AD%E6%94%BE%E5%99%A8sdk/) 业内为数不多的iOS支持Unity3D的超低延迟RTMP/RTSP直播播放器SDK，支持快照、录像、实时静音、view旋转、快速切换URL等特性;

- [x] [**录像SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%AD%E5%BD%95%E5%83%8Fsdk/) 支持拉取rtmp/rtsp流实时**录像**模块/实时**快照**功能，支持纯音频、纯视频、音视频录制模式，支持音频(PCMU/PCMA,Speex等)**转AAC**后再录像，业内为数不多的支持**RTSP/RTMP H.265录制到MP4文件**的录像SDK；

- [x] [**RTMP/RTSP多路流媒体转RTMP推送SDK**](https://daniusdk.com/index.php/2018/04/04/%E5%A4%9A%E8%B7%AF%E6%B5%81%E5%AA%92%E4%BD%93%E8%BD%AC%E5%8F%91sdk/) 支持实时拉取的rtmp/rtsp流转发到指定rtmp url;

- [x] [**轻量级RTSP服务SDK**](https://daniusdk.com/index.php/2018/06/22/%E8%BD%BB%E9%87%8F%E7%BA%A7rtsp%E6%9C%8D%E5%8A%A1sdk/) 为满足内网无纸化/电子教室等内网超低延迟需求，避免让用户配置单独的服务器，大牛直播SDK在推送端支持轻量级RTSP服务SDK，推送端SDK支持的功能，内置轻量级RTSP服务SDK后，功能继续支持；

- [x] [**内网RTSP网关SDK**](https://daniusdk.com/index.php/2018/11/10/%E5%86%85%E7%BD%91rtsp%E7%BD%91%E5%85%B3sdk/) 内网RTSP网关SDK，系内置轻量级RTSP服务SDK扩展，完成**外部RTSP/RTMP数据拉取并注入到轻量级RTSP服务SDK工作**，多个内网客户端直接访问内网轻量级RTSP服务获取公网数据，无需部署单独的服务器，支持RTSP/RTMP H.265数据接入；

- [x] [**RTMP/RTSP一对一互动SDK**](https://daniusdk.com/index.php/2018/12/01/%E4%B8%80%E5%AF%B9%E4%B8%80%E4%BA%92%E5%8A%A8sdk/) 基于标准协议(RTMP或RTSP)的跨平台(Windows/Andriod/iOS)一对一互动SDK，支持回音消除，完美支持一对一互动场景；

- [x] [**SEI扩展数据发送/接收SDK**](https://daniusdk.com/index.php/2018/07/10/%E5%A4%A7%E7%89%9B%E7%9B%B4%E6%92%ADsei%E6%89%A9%E5%B1%95%E6%95%B0%E6%8D%AE%E5%8F%91%E9%80%81-%E6%8E%A5%E6%94%B6sdk/) 支持推送端通过H.264 SEI信息扩展，实时传输文本/二进制数据信息(如实时字幕/时间戳/题目分发/公告广播等)，播放端做相应解析和回显；

## QQ技术对接交流 ##

**加群请简要描述使用场景/需求，否则不予通过**：

- [x] 大牛直播技术交流群3(推荐加入): [182979815](http://shang.qq.com/wpa/qunwpa?idkey=69308e344e276f43ecf27b4bd59dc61eb475a9b8b59134d036079b92154e0962)	

- [x] 大牛直播技术交流群2(已满): [294891451](http://shang.qq.com/wpa/qunwpa?idkey=476a9cc05db0b2924530ccbbf4fae78fa485d39418ef79c8ab71b24a8fee8a48)	

- [x] 大牛直播技术交流群1(已满): [499687479](http:////shang.qq.com/wpa/qunwpa?idkey=e7686f68a39bf1b95dc2ac3b775867efc7d3cbaf3596daf6e12bc1df21e1dc59)	

或者直接从私有服务器下载(Windows提供C#/C++ demo, android提供android studio demo，iOS提供xcode demo)：	

## 大牛直播SDK相关demo本地下载 ##	

**1. Windows平台测试EXE：**	

- [x] [**SmartPublisherDemo.exe**] RTMP|RTSP推送、轻量级RTSP服务、扩展SEI发送、采集录像演示程序；	

- [x] [**SmartPlayer.exe**] RTMP|RTSP播放SDK、扩展SEI接收、拉流录像演示程序；	

- [x] [**SmartStreamRelayDemo.exe**] 多路RTSP|RTMP转RTMP推送演示程序；	

- [x] [**SmartMixStreamDemo.exe**] RTMP|RTSP拉流然后和本地摄像头或屏幕**合流**演示程序（demo源码以C++为例）；	

- [x] [**SmartEchoCancellation.exe**] 基于标准RTMP服务的一对一互动演示程序（demo源码以C#为例）；	

- [x] [**Windows平台RTMP|RTSP 4路播放演示程序**] Windows 4路RTSP/RTMP播放Demo；

- [x] [**Windows平台IE浏览器OCX控件RTMP|RTSP播放测试程序**] Windows平台RTMP|RTSP播放SDK OCX控件。

**2. Windows平台集成对接DEMO：**	

- [x] [**Windows平台C++ SDK demo工程代码**] Windows平台RTMP|RTSP推送SDK、内置RTSP服务SDK、录像SDK(C++) Demo

- [x] [**Windows平台C++ SDK demo工程代码**] Windows平台RTMP|RTSP播放SDK(C++) Demo

- [x] [**Windows平台C++ SDK demo工程代码**] Windows平台多路RTSP|RTMP转RTMP推送模块SDK(C++) Demo

- [x] [**Windows平台C++ SDK demo工程代码**] Windows平台混流SDK(C++) Demo

- [x] [**Windows平台C# SDK demo工程代码**] Windows平台RTMP|RTSP推送SDK、内置RTSP服务SDK、录像SDK(C#) Demo

- [x] [**Windows平台C# SDK demo工程代码**] Windows平台RTMP|RTSP播放SDK(C#) Demo

- [x] [**Windows平台C# SDK demo工程代码**] Windows平台多路RTSP|RTMP转RTMP推送模块SDK(C#) Demo

- [x] [**Windows平台一对一互动SDK demo工程代码(以C#为例)**] 基于标准RTMP服务的一对一互动demo，可扩展RTSP一对一互动

**3.Android平台集成对接DEMO：**	

- [x] [**SmartPlayerV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartPlayerV2): RTMP|RTSP直播播放SDK demo，涵盖实时录像、快照、扩展SEI数据接收等功能；	

- [x] [**SmartPublisherV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartPublisherV2): RTMP直播推送SDK、RTSP直播推送SDK、轻量级RTSP服务SDK、扩展SEI发送SDK、实时录像SDK多合一demo；	

- [x] [**SmartEchoCancellationV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartEchoCancellationV2): 基于RTMP的一对一互动demo(可扩展RTSP一对一互动)；	

- [x] [**SmartServiceCameraPublisherV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartServiceCameraPublisherV2): 后台摄像头RTMP直播推送SDK；	

- [x] [**SmartServicePublisherV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartServicePublisherV2): 智慧教室|无纸化会议等屏幕采集(推屏) 、RTMP直播推送demo；	

- [x] [**SmartRelayDemoV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartRelayDemoV2): RTMP|RTSP直播播放SDK、RTMP|RTSP转RTMP推送SDK、RTMP|RTSP实时录像、轻量级RTSP服务四合一demo。	

**4.iOS平台集成对接DEMO：**	

- [x] [**SmartiOSPlayerV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSPlayerV2): RTMP|RTSP直播播放SDK demo，涵盖实时录像、快照、扩展SEI数据接收等功能；

- [x] [**SmartiOSPublisherV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSPublisherV2): RTMP直播推送SDK、RTSP直播推送SDK、轻量级RTSP服务SDK、扩展SEI发送SDK、实时录像SDK多合一demo；	

- [x] [**SmartiOSEchoCancellation**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSEchoCancellation): 基于RTMP的一对一互动demo(可扩展RTSP一对一互动)；	

- [x] [**SmartiOSScreenPublisherV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSScreenPublisherV2): 基于ReplayKit采集的智慧教室|无纸化会议等屏幕采集(推屏) 、RTMP直播推送demo；	

- [x] [**SmartiOSRelayDemoV2**](https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSRelayDemoV2): RTMP|RTSP直播播放SDK、RTMP|RTSP转RTMP推送SDK、RTMP|RTSP实时录像、轻量级RTSP服务四合一demo。	

**NOTE:** Windows平台，以C++ SDK Demo为最新，C# Demo更新速度稍滞于C++ Demo。	

## 大牛直播SDK集成和调用说明 ##	

右键“链接另存为(K)...”下载文档即可。	

- [x] [**Android、iOS平台RTMP/RTSP直播推送、RTMP/RTSP播放、内置RTSP服务、转发SDK(V2)调用说明**](http://daniusdk.com/wp-content/uploads/2021/04/视沃科技-大牛直播移动端SDKV2调用说明2.17.pdf)	

- [x] [**Windows平台RTMP/RTSP直播推送、RTMP/RTSP播放、内置RTSP服务、转发SDK调用说明(以C#为例)**](http://daniusdk.com/wp-content/uploads/2021/04/视沃科技-Windows平台-SDK集成说明2.16.pdf)	

## 上层源码目录 ##	

1. android推流 SmartPublisherV2	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartPublisherV2	

2. android推流 SmartServicePublisherV2(后台service推送屏幕)	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartServicePublisherV2	

3. android推流 SmartServiceCameraPublisherV2(后台service推送摄像头)	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartServiceCameraPublisherV2	

4. android一对一互动demo SmartEchoCancellationV2	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartEchoCancellationV2	

5. android播放器 SmartPlayerV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartPlayerV2	

6. android转发-录像-播放三合一 SmartRelayDemoV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/AndroidStudio/SmartRelayDemoV2	

7. iOS推流 SmartiOSPublisherV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSPublisherV2	

8. iOS后台推屏 SmartiOSScreenPublisherV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSScreenPublisherV2	

9. iOS播放器 SmartiOSPlayerV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSPlayerV2	

10. iOS转发-录像-播放三合一 SmartiOSRelayDemoV2:	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSRelayDemoV2	

11. iOS RTSP/RTMP一对一互动Demo SmartiOSEchoCancellation：	
https://github.com/daniulive/SmarterStreaming/tree/master/SourceCode/IOS/SmartiOSEchoCancellation	


## 功能支持 ##	
---	
**1. Windows视频采集处理SDK**	

1. 支持视频源	
- [x] 支持Windows屏幕采集、**屏幕裁剪**、**屏幕缩放**、**特定窗口采集**、摄像头采集、扩展外部H.264数据对接；	
2. 摄像头和屏幕合成	
- [x] [摄像头和屏幕实时切换]支持推送过程中，摄像头和屏幕互相切换，单画面显示摄像头或屏幕；	
- [x] [摄像头叠加到屏幕] 支持摄像头按照设置坐标，叠加到屏幕指定位置，并支持实时关闭叠加层；	
- [x] [屏幕叠加到摄像头] 支持屏幕按照设定坐标，叠加到摄像头指定位置，并支持实时关闭叠加层；	
3. 水印和透明度遮挡	
- [x] [实时水印]支持**动态水印**设置，完美支持`文字水印、实时时间水印和图片水印`；	
- [x] [透明度]可以设置透明度处理（设置遮盖）；	
4. 对应Demo：	
- [x] 测试程序：SmartPublisherDemo.exe；	
- [x] C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] C#工程：WIN-PublisherSDK-CSharp-Demo。	
---	

**2. Windows音频采集处理SDK**	

1. 支持音频源	
- [x] 支持Windows采集**麦克风**、**扬声器**和外部AAC, Speex WB, PCMA, PCMU数据接口输入；	
2. 音频合成	
- [x] [音频]支持扬声器和麦克风音频**混音输出**(同时选择“采集扬声器”和“采集麦克风”)；	
3. 音频处理	
- [x] 支持音频“端点检测（VAD）”，自适应码流，音频码流更节省；	
- [x] 支持回音消除功能；	
- [x] 支持噪音抑制功能；	
- [x] 支持自动增益控制。	
4. 对应Demo：	
- [x] 测试程序：SmartPublisherDemo.exe；	
- [x] C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] C#工程：WIN-PublisherSDK-CSharp-Demo。	
---	

**3. Windows/Android/iOS RTMP直播推流SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] [**视频采集处理**]Windows平台涵盖“Windows视频采集处理SDK”功能；	
- [x] [**音频采集处理**]Windows平台涵盖“Windows音频采集处理SDK”功能；	
- [x] [**本地预览**]Windows平台支持摄像头/屏幕/合成数据**实时预览**功能，Android/iOS平台支持本地前后置摄像头预览；	
- [x] [**摄像头反转/旋转**]Windows平台支持摄像头水平反转、垂直反转、0°/90°/180°/270°旋转；	
- [x] [**摄像头采集**]除常规YUV格式外，Windows平台还支持**MJPEG**格式的摄像头采集；	
- [x] [**RTMP推流**]超低延时的RTMP协议直播推流SDK（Windows/Android/iOS支持RTMP扩展H.265推送）；		
- [x] [**视频格式**]Windows/Android平台支持H.264/H.265编码；	
- [x] [**音频格式**]Windows/Android/iOS平台支持AAC编码，Windows/Android平台支持Speex编码；	
- [x] [**音频编码**]Windows/Android平台支持Speex推送、Speex编码质量设置；
- [x] [**音量调节**]Windows/Android平台采集端支持实时音量调节(其中，Windows平台混音模式下支持单独控制麦克风、扬声器音量)；
- [x] [**H.264硬编码**]Android/iOS平台支持H.264特定机型硬编码；	
- [x] [**H.265硬编码**]Android/iOS平台支持H.265特定机型硬编码；	
- [x] [**硬编码自适应**]Android/iOS平台支持硬编码自适应，如检测到硬编码不支持，可切换到软编（iOS如H.265硬编，先切换到H.264硬编码，如不支持再尝试H.264软编）；	
- [x] [**软硬编码参数配置**]支持gop间隔、帧率(Windows最高限定120帧)、bit-rate设置；	
- [x] [**软编码参数配置**]支持软编码profile、软编码速度、可变码率设置；	
- [x] [**多实例推送**]支持多实例推送(如同时推送屏幕/摄像头和外部数据)；	
- [x] [**RTMP扩展H.265**]Windows/Android/iOS推送SDK支持**RTMP扩展H.265推送**；
- [x] [**横竖屏推流**]Android/iOS平台支持支持横屏、竖屏推流；	
- [x] [**多分辨率支持**]支持摄像头或屏幕多种分辨率设置；	
- [x] [**Windows推屏**]Windows平台支持**屏幕裁剪、窗口采集、屏幕/摄像头数据合成**等多种模式推送；	
- [x] [**移动端推屏**]Android平台支持后台service推送摄像头或屏幕(推送屏幕需要5.0+版本)；	
- [x] [**移动端推屏**]iOS平台支持后台推送屏幕(基于ReplayKit，需要iOS 10.0+版本)；	
- [x] [**事件回调**]支持各种状态实时回调；	
- [x] [**水印**]Windows平台支持文字水印、png水印、实时遮挡，Android平台支持文字水印、png水印；	
- [x] [**RTMP推送模式**]支持RTMP推送 live|record模式设置（需服务器支持）；	
- [x] [**镜像**]Android/iOS平台支持前置摄像头实时镜像功能；	
- [x] [**前后摄像头实时切换**]Android/iOS平台支持采集过程中，前后摄像头切换；	
- [x] [**复杂网络处理**]支持断网重连等各种网络环境自动适配；	
- [x] [**动态码率**]支持根据网络情况自动调整推流码率；	
- [x] [**实时静音**]支持推送过程中，实时静音/取消静音；	
- [x] [**实时快照**]支持推流过程中，实时快照；	
- [x] [**纯音频推流**]支持仅采集音频流并发起推流功能；	
- [x] [**纯视频推流**]支持特殊场景下的纯视频推流功能；	
- [x] [**降噪**]Windows/Android平台支持环境音、手机干扰等引起的噪音降噪处理、自动增益、VAD检测；	
- [x] [**回音消除**]Android平台支持实时传递远端PCM数据，方便回音消除处理；	
- [x] [**外部编码前视频数据对接**]支持YUV数据对接；	
- [x] [**外部编码前音频数据对接**]支持PCM对接；	
- [x] [**外部编码后视频数据对接**]支持外部H.264数据对接；	
- [x] [**外部编码后音频数据对接**]外部AAC/PCMA/PCMU/SPEEX数据对接；	
- [x] [**推送端休眠设置**]Windows平台支持休眠接口(设置成休眠模式后CPU会适当降低)；	
- [x] [**编码后数据输出**]Android平台支持输出编码后的H264/AAC数据到上层，方便对接第三方平台(如GB28181)对接；	
- [x] [**扩展录像功能**]完美支持和录像SDK组合使用，录像相关功能，可参见"**8. Windows/Android/iOS录像SDK**"；	
- [x] [**裁剪模式**]Android/iOS平台支持特定分辨率摄像头裁剪模式设置；	
- [x] [**服务器兼容**]支持自建标准RTMP服务器(如Nginx、SRS)或CDN。	

对应Demo：	
- [x] Windows测试程序：SmartPublisherDemo.exe；	
- [x] Windows C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] Windows C#工程：WIN-PublisherSDK-CSharp-Demo；	
- [x] Android工程：SmartPublisherV2；	
- [x] iOS工程：SmartiOSPublisherV2。	
---	

**4. Windows/Android/iOS RTSP直播推流SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] [**视频采集处理**]Windows平台涵盖“Windows视频采集处理SDK”功能；	
- [x] [**音频采集处理**]Windows平台涵盖“Windows音频采集处理SDK”功能；	
- [x] [**本地预览**]Windows平台支持摄像头/屏幕/合成数据**实时预览**功能，Android/iOS平台支持本地前后置摄像头预览；	
- [x] [**摄像头反转/旋转**]Windows平台支持摄像头水平反转、垂直反转、0°/90°/180°/270°旋转；	
- [x] [**摄像头采集**]除常规YUV格式外，Windows平台还支持**MJPEG**格式的摄像头采集；	
- [x] [**RTSP推流**]超低延时的RTSP协议直播推流SDK；	
- [x] [**视频格式**]Windows/Android平台支持H.264/H.265编码；	
- [x] [**音频格式**]Windows/Android/iOS平台支持AAC编码；
- [x] [**音量调节**]Windows平台采集端支持实时音量调节(混音模式下支持单独控制麦克风、扬声器音量)；
- [x] [**H.264硬编码**]Android/iOS平台支持H.264特定机型硬编码；	
- [x] [**H.265硬编码**]Android/iOS平台支持H.265特定机型硬编码；	
- [x] [**硬编码自适应**]Android/iOS平台支持硬编码自适应，如检测到硬编码不支持，可切换到软编（iOS如H.265硬编，先切换到H.264硬编码，如不支持再尝试H.264软编）；	
- [x] [**RTSP鉴权**]支持RTSP鉴权推送；	
- [x] [**TCP/UDP模式**]支持rtp over udp和rtp over tcp两种传输方式；	
- [x] [**401事件处理**]RTSP推送支持401事件上报；	
- [x] [**视频格式**]支持H.264/**H.265**(64位库)编码；	
- [x] [**音频格式**]支持AAC编码；	
- [x] [**软硬编码参数配置**]支持gop间隔、帧率、bit-rate设置；	
- [x] [**软编码参数配置**]支持软编码profile、软编码速度、可变码率设置；	
- [x] [**多实例推送**]支持多实例推送(如同时推送屏幕/摄像头和外部数据)；	
- [x] [**多分辨率支持**]支持摄像头或屏幕多种分辨率设置；	
- [x] [**Windows推屏**]Windows平台支持**屏幕裁剪、窗口采集、屏幕/摄像头数据合成**等多种模式推送；		
- [x] [**事件回调**]支持各种状态实时回调；	
- [x] [**水印**]Windows平台支持文字水印、png水印、实时遮挡，Android平台支持文字水印、png水印；	
- [x] [**复杂网络处理**]支持断网重连等各种网络环境自动适配；	
- [x] [**动态码率**]支持根据网络情况自动调整推流码率；	
- [x] [**实时静音**]支持推送过程中，实时静音/取消静音；	
- [x] [**实时快照**]支持推流过程中，实时快照；	
- [x] [**纯音频推流**]支持仅采集音频流并发起推流功能；	
- [x] [**纯视频推流**]支持特殊场景下的纯视频推流功能；	
- [x] [**降噪**]Windows/Android平台支持降噪处理、自动增益、VAD检测；	
- [x] [**回音消除**]Android平台支持实时传递远端PCM数据，方便回音消除处理；	
- [x] [**外部编码前视频数据对接**]支持YUV数据对接；	
- [x] [**外部编码前音频数据对接**]支持PCM对接；	
- [x] [**外部编码后视频数据对接**]支持外部H.264数据对接；	
- [x] [**外部编码后音频数据对接**]外部AAC/PCMA/PCMU数据对接；	
- [x] [**推送端休眠设置**]Windows平台支持休眠接口(设置成休眠模式后CPU会适当降低)；	
- [x] [**扩展录像功能**]完美支持和录像SDK组合使用，录像相关功能，可参见"**8. Windows/Android/iOS录像SDK**"；	
- [x] [**服务器兼容**]支持支持自建服务器(如Darwin Stream Server)。	

对应Demo：	
- [x] Windows测试程序：SmartPublisherDemo.exe；	
- [x] Windows C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] Android工程：SmartPublisherV2；	
- [x] iOS工程：SmartiOSPublisherV2。	
---	

**5. Windows/Android/iOS RTMP、RTSP直播播放器SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] [**支持播放协议**]高稳定、超低延迟（一秒内，行业内几无效果接近的播放端）、业内首屈一指的RTMP/RTSP直播播放器SDK；	
- [x] [**多实例播放**]支持多实例播放（如同时播放多路RTMP/RTSP流）；	
- [x] [**事件回调**]支持网络状态、buffer状态等回调；	
- [x] [**视频格式**]支持RTSP H.265、RTMP扩展H.265，RTSP/RTMP H.264，此外，还支持**RTSP MJPEG**播放；	
- [x] [**音频格式**]RTMP/RTSP支持AAC/PCMA/PCMU，此外RTMP还支持Speex；	
- [x] [**H.264/H.265软解码**]支持H.264/H.265软解；	
- [x] [**H.264硬解码**]**Windows**/Android/iOS支持H.264特定机型硬解码，[Windows平台硬解码播放效果展示(超低CPU占用)](http://www.iqiyi.com/w_19s8qz0f2x.html)；	
- [x] [**H.265硬解**]**Windows**/Android/iOS支持H.265特定机型硬解码；	
- [x] [**H.264/H.265硬解码**]Android支持设置Surface模式硬解和普通模式硬解码；	
- [x] [**RTSP模式设置**]支持RTSP TCP/UDP模式设置；	
- [x] [**RTSP TCP/UDP自动切换**]支持RTSP TCP、UDP模式自动切换；	
- [x] [**RTSP超时设置**]支持RTSP超时时间设置，单位：秒；	
- [x] [**RTSP 401认证处理**]支持上报RTSP 401事件，如URL携带鉴权信息，会自动处理；	
- [x] [**缓冲时间设置**]支持buffer time设置；	
- [x] [**首屏秒开**]支持首屏秒开模式；	
- [x] [**低延迟模式**]支持超低延迟模式设置；	
- [x] [**复杂网络处理**]支持断网重连等各种网络环境自动适配；	
- [x] [**快速切换URL**]支持播放过程中，快速切换其他URL，内容切换更快；	
- [x] [**音视频多种render机制**]Windows平台支持D3D和GDI绘制模式(如不支持D3D，可用GDI模式)；	
- [x] [**音视频多种render机制**]Android平台，视频：surfaceview/OpenGL ES，音频：AudioTrack/OpenSL ES（一般建议AudioTrack）；	
- [x] [**实时静音**]支持播放过程中，实时静音/取消静音；	
- [x] [**实时音量调节**]支持播放过程中，实时调节播放音量，范围[0,100]；	
- [x] [**实时快照**]支持播放过程中截取当前播放画面；	
- [x] [**只播关键帧**]Windows平台支持实时设置是否只播放关键帧；	
- [x] [**渲染角度**]支持0°，90°，180°和270°四个视频画面渲染角度设置；	
- [x] [**渲染镜像**]支持水平反转、垂直反转模式设置；	
- [x] [**等比例缩放**]支持图像等比例缩放绘制（Android硬解码设置surface模式下不支持）；	
- [x] [**实时下载速度更新**]支持当前下载速度实时回调(支持设置回调时间间隔)；	
- [x] [**ARGB叠加**]Windows平台支持ARGB图像叠加到显示视频（参看C++的DEMO）；	
- [x] [**解码前视频数据回调**]支持H.264/H.265数据回调；	
- [x] [**解码后视频数据回调**]支持解码后YUV/RGB数据回调；	
- [x] [**解码后视频数据缩放回调**]Windows平台支持指定回调图像大小的接口(可以对原视图像缩放后再回调到上层)；	
- [x] [**解码前音频数据回调**]支持AAC/PCMA/PCMU/SPEEX数据回调；	
- [x] [**音视频自适应**]支持播放过程中，音视频信息改变后自适应；	
- [x] [**扩展录像功能**]完美支持和录像SDK组合使用，录像相关功能(支持RTSP H.265流录制，支持PCMA/PCMU转AAC后录制，支持设置只录制音频或视频)，可参见"**8. Windows/Android/iOS录像SDK**"；	

对应Demo：	
- [x] Windows测试程序：SmartPlayer.exe；	
- [x] Windows C++工程：WIN-PlayerSDK-CPP-Demo；	
- [x] Windows C#工程：WIN-PlayerSDK-CSharp-Demo；	
- [x] Android工程：SmartPlayerV2；	
- [x] iOS工程：SmartiOSPlayerV2。	
---	

**6. Windows/Android/iOS内置轻量级RTSP服务SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] [**基础功能**]支持Windows/Android/iOS平台RTMP直播SDK除推送RTMP外的所有常规功能；	
- [x] [**音频格式**]AAC；	
- [x] [**视频格式**]H.264、H.265；	
- [x] [**协议类型**]RTSP；	
- [x] [**传输模式**]支持**单播**和**组播**模式；	
- [x] [**端口设置**]支持RTSP端口设置；	
- [x] [**鉴权设置**]支持RTSP鉴权用户名、密码设置；	
- [x] [**获取session连接数**]支持获取当前RTSP服务会话连接数；	
- [x] [**多服务支持**]支持同时创建多个内置RTSP服务；	
- [x] [**H.265支持**]支持发布H.265视频；	
- [x] [**RTSP url回调**]支持设置后的rtsp url通过event回调到上层。	

对应Demo：	
- [x] Windows测试程序：SmartPublisherDemo.exe；	
- [x] Windows C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] Windows C#工程：WIN-PublisherSDK-CSharp-Demo；	
- [x] Android工程：SmartPublisherV2；	
- [x] iOS工程：SmartiOSPublisherV2。	
---	

**7. 内网RTSP网关SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

内网RTSP网关SDK，系内置轻量级RTSP服务SDK扩展，完成**外部RTSP/RTMP数据拉取并注入到轻量级RTSP服务SDK工作**，多个内网客户端直接访问内网轻量级RTSP服务获取公网数据，无需部署单独的服务器，支持RTSP/RTMP H.265数据接入。	
简单来说：内置轻量级RTSP服务SDK和内置RTSP网关SDK的区别在于**数据来源不同**，内置轻量级RTSP服务SDK数据来源于**终端设备自带摄像头数据/屏幕数据/外部编码前后数据**，内置RTSP网关SDK的数据源是**RTSP/RTMP流**数据。	

- [x] [**音频格式**]AAC；	
- [x] [**视频格式**]H.264、H.265；	
- [x] [**接入协议**]支持内外网RTMP/RTSP流接入；	
- [x] [**输出协议**]RTSP，拉取的RTSP/RTMP流，注入轻量级RTSP服务SDK；	
- [x] [**传输模式**]Windows支持**单播**和**组播**模式，Android/iOS平台支持单播模式；	
- [x] [**音频转码**]支持音频(PCMU/PCMA,Speex等)转AAC后注入；	
- [x] [**端口设置**]支持RTSP端口设置；	
- [x] [**鉴权设置**]支持RTSP鉴权用户名、密码设置；	
- [x] [**获取session连接数**]支持获取当前RTSP服务会话连接数；	
- [x] [**多服务支持**]支持同时创建多个内置RTSP服务；	
- [x] [**H.265支持**]Windows内置rtsp server支持发布H.265视频；	
- [x] [**RTSP url回调**]支持设置后的rtsp url通过event回调到上层；	

对应Demo：	
- [x] Windows测试程序：SmartStreamRelayDemo.exe；	
- [x] Windows C++工程：WIN-RelaySDK-CPP-Demo；	
- [x] Windows C#工程：WIN-RelaySDK-CSharp-Demo。	
---	

**8. Windows/Android/iOS RTMP/RTSP多路流媒体转RTMP推送SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] [**拉流**]支持拉取RTSP流；	
- [x] [**拉流**]支持拉取RTMP流；	
- [x] [**预览**]支持拉取到的RTMP/RTSP随时本地预览、关闭预览；	
- [x] [**拉流音频调节**]支持拉取的RTMP/RTSP流静音；	
- [x] [**音频转码**]支持拉取的RTMP/RTSP的PCMA/PCMU/SPEEX音频格式**转AAC**后再转发到RTMP服务器；	
- [x] [**url切换**]**支持转发过程中，拉取的RTMP/RTSP实时内容切换**；	
- [x] [**转发**]超低延迟转发拉取的rtsp/rtmp流到rtmp server；	
- [x] [**H.265支持**]**业内为数不多支持RTSP/RTMP H.265转RTMP推送**的SDK(提供配套RTMP扩展H.265服务器)；	

对应Demo：	
- [x] Windows测试程序：SmartStreamRelayDemo.exe；	
- [x] Windows C++工程：WIN-RelaySDK-CPP-Demo；	
- [x] Windows C#工程：WIN-RelaySDK-CSharp-Demo；	
- [x] Android工程：SmartRelayDemoV2；	
- [x] iOS工程：SmartiOSRelayDemoV2。	

---	

**9. Windows/Android/iOS RTMP/RTSP一对一互动SDK**	

如不单独说明，系Windows、Android、iOS全平台支持。	

- [x] 基于官方现有RTMP、RTSP推送、或内置RTSP服务、播放SDK，产品稳定度高，行业内首屈一指的超低延迟特性；	
- [x] 加入噪音抑制、回音消除、自动增益控制等特性，确保通话效果；	
- [x] 采用通用的RTMP和RTSP服务器，如nginx、SRS或 Darwin Stream Server（原生版本），更有利于私有部署；	
- [x] 支持H.264的扩展SEI消息发送机制；	
- [x] 支持H.265编码（Windows 64位库，Android/iOS硬编码）和H.264可变码率设定，换句话说，之前大牛直播SDK推送端支持的功能，都可以同步支持；	
- [x] 支持H.265解码，直播播放器支持的功能，一对一互动模块都可以有选择的支持；	
- [x] Windows平台支持双流合成大小屏录制；	
- [x] Windows支持摄像头、屏幕合成、水印等各种组合模式，扩展度高；	
- [x] 适用于应急指挥、教育培训等领域。	

对应Demo：	
- [x] 以C#为例，对应SmartEchoCancellation.exe(WIN-EchoCancellation-CSharp-Demo)；	
- [x] Android工程：SmartEchoCancellationV2；	
- [x] iOS工程：SmartiOSEchoCancellation。	

---	

**10. Windows导播SDK**	

- [x] [**拉流**]支持拉取RTSP流；	
- [x] [**拉流**]支持拉取RTMP流；	
- [x] [**混音合成**]支持本地采集到屏幕或摄像头数据，和远程拉取得RTSP或RTMP流做合成、混音输出；	
- [x] [**导播**]支持导播过程中，随时切断某一路音视频或音频；	
- [x] [**混音**]支持音频混音（同时选择“采集麦克风”+“采集扬声器”）；	
- [x] [**合成**]多路流合成一路流后，推送到RTMP服务器；	
- [x] [**扩展录像快照**]多路合成后的流，支持本地录像、快照。	

对应Demo：	
- [x] 测试程序：SmartMixStreamDemo.exe；	
- [x] C++工程：WIN-MixStreamSDK-CPP-Demo；	
---	

**11. Windows/Android/iOS录像SDK**	

- [x] [**拉流**]支持拉取RTSP流录像；	
- [x] [**拉流**]支持拉取RTMP流录像；	
- [x] [**推流端录像**]支持RTMP|RTSP推送端同步录像；	
- [x] [**轻量级RTSP服务录像**]支持轻量级RTSP服务SDK同步录像；	
- [x] [**推流端录像实时暂停/恢复**]支持推送端录像过程中**实时暂停录像、恢复录像**；	
- [x] [**逻辑分离**]大牛直播录像SDK不同于普通录像接口，更智能，和推送、播放、转发、内置轻量级RTSP服务SDK功能完全分离，支持随时录像；	
- [x] [**url切换**]在录像过程中，支持切换不同URL，如两个URL配置一致，则可以录制到同一个MP4文件，如不一致，可自动分割到下一个文件；	
- [x] [**参数设置**]支持设置单个录像文件大小、录像路径等，并支持**纯音频、纯视频、音视频**录制模式；	
- [x] [**音频转码**]支持音频(PCMU/PCMA,Speex等)转AAC后再录像；	
- [x] [**265支持**]支持**RTSP/RTMP H.265**录制到MP4文件；	
- [x] [**推送端265录像**]推送端SDK支持H265录像；	
- [x] [**推送端外部编码数据对接录像**]支持推送端外部编码后数据(H.264/AAC)对接录像；	
- [x] [**事件回调**]从开始录像，到录像结束均有event callback上来，网络堵塞、音视频同步均做了非常友好的处理。	

对应Demo：	
- [x] Windows测试程序：SmartPlayer.exe；	
- [x] Windows C++工程：WIN-PlayerSDK-CPP-Demo；	
- [x] Windows C#工程：WIN-PlayerSDK-CSharp-Demo；	
- [x] 测试程序：SmartPublisherDemo.exe；	
- [x] C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] C#工程：WIN-PublisherSDK-CSharp-Demo。	
- [x] Android工程：SmartPlayerV2；	
- [x] iOS工程：SmartiOSPlayerV2；	
- [x] Android工程：SmartPublisherV2；	
- [x] iOS工程：SmartiOSPublisherV2。	
---	

**12. Windows/Android/iOS SEI扩展数据发送/接收SDK**	

- [x] [**RTSP SEI**]支持内置RTSP服务SDK携带SEI扩展信息(H.264)；	
- [x] [**RTMP SEI**]支持RTMP推送SDK携带SEI扩展信息(H.264)；	
- [x] [**自定义数据**]持发送自定义用户数据(如自定义utf8字符串)；	
- [x] [**二进制数据**]支持发送二进制数据；	
- [x] [**播放端解析**]RTSP/RTMP直播播放端SDK支持utf8文本、二进制、和原SEI数据解析。	

对应Demo：	
- [x] Windows测试程序：SmartPlayer.exe；	
- [x] Windows C++工程：WIN-PlayerSDK-CPP-Demo；	
- [x] Windows C#工程：WIN-PlayerSDK-CSharp-Demo；	
- [x] 测试程序：SmartPublisherDemo.exe；	
- [x] C++工程：WIN-PublisherSDK-CPP-Demo；	
- [x] C#工程：WIN-PublisherSDK-CSharp-Demo。	
- [x] Android工程：SmartPlayerV2；	
- [x] iOS工程：SmartiOSPlayerV2；	
- [x] Android工程：SmartPublisherV2；	
- [x] iOS工程：SmartiOSPublisherV2。	
---	

## 编译注意事项 ##	

* iOS平台支持真机和模拟器编译运行.	
* iOS播放端编译时找不到 libSmartPlayerSDK.a 时，请先到 SmartiOSPlayer/SmartiOSPlayer/libs 目录, 解压libSmartPlayerSDK.zip.	
* iOS推送端编译时找不到 libSmartPublisherSDK.a 时，请先到 SmartiOSPublisher/SmartiOSPublisher/libs 目录, 解压libSmartPublisherSDK.zip.	
* 未授权版本，限制app-name，如果需要集成到自己工程里面调试，可以用以下名字：	
 ```	
Windows推送端：SmartPublisherDemo	
Windows播放端：SmartPlayer	
Windows转发端：SmartStreamRelayDemo	
Windows合流导播端：SmartMixStreamDemo	
android推送端：SmartPublisherSDKDemo	
android后台Service推送：SmartServicePublisherSDKDemo	
android一对一互动：SmartEchoCancellation	
android播放器：SmartPlayerSDKDemo	
iOS推送端：SmartiOSPublisher	
iOS转发端：SmartiOSRelayDemo	
iOS播放器：SmartiOSPlayer	
iOS一对一互动：SmartiOSEchoCancellation	
 ```	
* 集成到自己工程，如何改名字（以推送端为例）：	

 ```	
android：strings.xml：	
<string name="app_name">SmartPublisherSDKDemo</string>	
 ```	

 ```	
 iOS：Info.plist-->右键Open As-->Source Code，添加或者编辑	
 <key>CFBundleName</key>		
 <string>SmartiOSPublisher</string>	
 ```	

## 联系我们 ##	

[点击查看联系方式](https://daniusdk.com/index.php/%E8%81%94%E7%B3%BB/)	

**QQ交流群（加群请简要描述使用场景/需求，否则不予通过）：**	


- [x] 大牛直播技术交流群3(推荐加入): [182979815](http://shang.qq.com/wpa/qunwpa?idkey=69308e344e276f43ecf27b4bd59dc61eb475a9b8b59134d036079b92154e0962)	

- [x] 大牛直播技术交流群2(已满): [294891451](http://shang.qq.com/wpa/qunwpa?idkey=476a9cc05db0b2924530ccbbf4fae78fa485d39418ef79c8ab71b24a8fee8a48)	

- [x] 大牛直播技术交流群1(已满): [499687479](http:////shang.qq.com/wpa/qunwpa?idkey=e7686f68a39bf1b95dc2ac3b775867efc7d3cbaf3596daf6e12bc1df21e1dc59)	
