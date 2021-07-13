# ZXingLite

![Image](app/src/main/ic_launcher-web.png)

[![Download](https://img.shields.io/badge/download-App-blue.svg)](https://raw.githubusercontent.com/jenly1314/ZXingLite/master/app/release/app-release.apk)
[![MavenCentral](https://img.shields.io/maven-central/v/com.github.jenly1314/zxing-lite)](https://repo1.maven.org/maven2/com/github/jenly1314/zxing-lite)
[![JCenter](https://img.shields.io/badge/JCenter-2.0.3-46C018.svg)](https://bintray.com/beta/#/jenly/maven/zxing-lite)
[![JitPack](https://jitpack.io/v/jenly1314/ZXingLite.svg)](https://jitpack.io/#jenly1314/ZXingLite)
[![CI](https://travis-ci.org/jenly1314/ZXingLite.svg?branch=master)](https://travis-ci.org/jenly1314/ZXingLite)
[![CircleCI](https://circleci.com/gh/jenly1314/ZXingLite.svg?style=svg)](https://circleci.com/gh/jenly1314/ZXingLite)
[![API](https://img.shields.io/badge/API-21%2B-blue.svg?style=flat)](https://android-arsenal.com/api?level=21)
[![License](https://img.shields.io/badge/license-Apche%202.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)
[![Blog](https://img.shields.io/badge/blog-Jenly-9933CC.svg)](https://jenly1314.github.io/)
[![QQGroup](https://img.shields.io/badge/QQGroup-20867961-blue.svg)](http://shang.qq.com/wpa/qunwpa?idkey=8fcc6a2f88552ea44b1.1.982c94fd124f7bb3ec227e2a400dbbfaad3dc2f5ad)

ZXingLite for Android 是ZXing的精简版，基于ZXing库优化扫码和生成二维码/条形码功能，扫码界面完全支持自定义，也可一行代码使用默认实现的扫码功能。总之你想要的都在这里。
>简单如斯，你不试试？ Come on~


## Gif 展示
![Image](GIF.gif)


## ViewfinderView属性说明
| 属性 | 值类型 | 默认值 | 说明 |
| :------| :------ | :------ | :------ |
| maskColor | color |<font color=#000000>#60000000</font>| 扫描区外遮罩的颜色 |
| frameColor | color |<font color=#1FB3E2>#7F1FB3E2</font>| 扫描区边框的颜色 |
| cornerColor | color |<font color=#1FB3E2>#FF1FB3E2</font>| 扫描区边角的颜色 |
| laserColor | color |<font color=#1FB3E2>#FF1FB3E2</font>| 扫描区激光线的颜色 |
| labelText | string |  | 扫描提示文本信息 |
| labelTextColor | color |<font color=#C0C0C0>#FFC0C0C0</font>| 提示文本字体颜色 |
| labelTextSize | dimension |14sp| 提示文本字体大小 |
| labelTextPadding | dimension |24dp| 提示文本距离扫描区的间距 |
| labelTextWidth | dimension | | 提示文本的宽度，默认为View的宽度 |
| labelTextLocation | enum |bottom| 提示文本显示位置 |
| frameWidth | dimension |  | 扫码框宽度 |
| frameHeight | dimension |  | 扫码框高度 |
| laserStyle | enum | line | 扫描激光的样式 |
| gridColumn | integer | 20 | 网格扫描激光列数 |
| gridHeight | integer | 40dp | 网格扫描激光高度，为0dp时，表示动态铺满 |
| cornerRectWidth | dimension | 4dp | 扫描区边角的宽 |
| cornerRectHeight | dimension | 16dp | 扫描区边角的高 |
| scannerLineMoveDistance | dimension | 2dp | 扫描线每次移动距离 |
| scannerLineHeight | dimension | 5dp | 扫描线高度 |
| frameLineWidth | dimension | 1dp | 边框线宽度 |
| scannerAnimationDelay | integer | 20 | 扫描动画延迟间隔时间，单位：毫秒 |
| frameRatio | float | 0.625f | 扫码框与屏幕占比 |
| framePaddingLeft | dimension | 0 | 扫码框左边的内间距 |
| framePaddingTop | dimension | 0 | 扫码框上边的内间距 |
| framePaddingRight | dimension | 0 | 扫码框右边的内间距 |
| framePaddingBottom | dimension | 0 | 扫码框下边的内间距 |
| frameGravity | enum | center | 扫码框对齐方式 |


## 引入

> 由于2021年2月3日 **JFrog宣布将关闭Bintray和JCenter，计划在2022年2月完全关闭。** 所以后续版本不再发布至 **JCenter**

### Gradle:

1. 在Project的 **build.gradle** 里面添加远程仓库  
          
```gradle
allprojects {
    repositories {
        //...
        mavenCentral()
    }
}
```

2. 在Module的 **build.gradle** 里面添加引入依赖项

```gradle
//AndroidX 版本
implementation 'com.github.jenly1314:zxing-lite:2.1.0'

```


以前发布至JCenter的版本
```gradle
//AndroidX 版本
implementation 'com.king.zxing:zxing-lite:2.0.3'

```

**v1.x** 旧版本
```gradle
//AndroidX 版本
implementation 'com.king.zxing:zxing-lite:1.1.9-androidx'

//Android Support 版本
implementation 'com.king.zxing:zxing-lite:1.1.9'
```

## 版本说明

### v2.x 基于CameraX重构震撼发布

#### v2.x 相对于 v1.x 的优势

* v2.x基于CameraX，抽象整体流程，可扩展性更高。
* v2.x基于CameraX通过预览裁剪的方式确保预览界面不变形，无需铺满屏幕，就能适配（v1.x通过遍历Camera支持预览的尺寸，找到与屏幕最接近的比例，减少变形的可能性（需铺满屏幕，才能适配）)

#### v2.x 特别说明

* v2.x如果您是通过继承CaptureActivity或CaptureFragment实现扫码功能，那么动态权限申请相关都已经在CaptureActivity或CaptureFragment处理好了。
* v2.x如果您是通过继承CaptureActivity或CaptureFragment实现扫码功能，如果有想要修改默认配置，可重写**initCameraScan**方法，修改CameraScan的配置即可，如果无需修改配置，直接在跳转原界面的**onActivityResult** 接收扫码结果即可（更多具体详情可参见[app](app)中的使用示例）。

##### 关于CameraX

* CameraX暂时还是Beta版，可能会存在一定的稳定性，如果您有这个考量，可以继续使用 **ZXingLite** 以前的 **v1.x** 版本。相信不久之后CameraX就会发布稳定版。

#### v1.x 说明

[【v1.1.9】](https://github.com/jenly1314/ZXingLite/tree/androidx) 如果您正在使用 **1.x** 版本请点击下面的链接查看分支版本，当前 **2.x** 版本已经基于 **Camerx** 进行重构，不支持升级，请在新项目中使用。

查看AndroidX版 **1.x** 分支 [请戳此处](https://github.com/jenly1314/ZXingLite/tree/androidx)

查看Android Support版 **1.x** 分支 [请戳此处](https://github.com/jenly1314/ZXingLite/tree/android)

查看 [ **1.x** API帮助文档](https://jenly1314.github.io/projects/ZXingLite/doc/)

使用 **v1.x** 版本的无需往下看了，下面的示例和相关说明都是针对于当前最新版本。

## 示例

布局示例
>  可自定义布局（覆写getLayoutId方法），布局内至少要保证有PreviewView。

> PreviewView 用来预览，布局内至少要保证有PreviewView，如果是继承CaptureActivity或CaptureFragment，控件id可覆写getPreviewViewId方法自定义

> ViewfinderView 用来渲染扫码视图，给用户起到一个视觉效果，本身扫码识别本身没有关系，如果是继承CaptureActivity或CaptureFragment，控件id可复写getViewfinderViewId方法自定义，默认为previewView，返回0表示无需ViewfinderView

> ivFlashlight 用来内置手电筒，如果是继承CaptureActivity或CaptureFragment，控件id可复写getFlashlightId方法自定义，默认为ivFlashlight。返回0表示无需内置手电筒。您也可以自己去定义


```Xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <androidx.camera.view.PreviewView
        android:id="@+id/previewView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
    <com.king.zxing.ViewfinderView
        android:id="@+id/viewfinderView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
    <ImageView
        android:id="@+id/ivFlashlight"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:src="@drawable/zxl_flashlight_selector"
        android:layout_marginTop="@dimen/zxl_flashlight_margin_top" />
</FrameLayout>
```

或在你的布局中添加

```Xml
    <include layout="@layout/zxl_capture"/>
```

代码示例 （二维码/条形码）
```Java
    //跳转的默认扫码界面
    startActivityForResult(new Intent(context,CaptureActivity.class),requestCode);

    //生成二维码
    CodeUtils.createQRCode(content,600,logo);
    //生成条形码
    CodeUtils.createBarCode(content, BarcodeFormat.CODE_128,800,200);
    //解析条形码/二维码
    CodeUtils.parseCode(bitmapPath);
    //解析二维码
    CodeUtils.parseQRCode(bitmapPath);
```

CameraScan配置示例
```java
    //获取CameraScan，扫码相关的配置设置。CameraScan里面包含部分支持链式调用的方法，即调用返回是CameraScan本身的一些配置建议在startCamera之前调用。
    getCameraScan().setPlayBeep(true)//设置是否播放音效，默认为false
            .setVibrate(true)//设置是否震动，默认为false
            .setCameraConfig(new CameraConfig())//设置相机配置信息，CameraConfig可覆写options方法自定义配置
            .setNeedAutoZoom(false)//二维码太小时可自动缩放，默认为false
            .setNeedTouchZoom(true)//支持多指触摸捏合缩放，默认为true
            .setDarkLightLux(45f)//设置光线足够暗的阈值（单位：lux），需要通过{@link #bindFlashlightView(View)}绑定手电筒才有效
            .setBrightLightLux(100f)//设置光线足够明亮的阈值（单位：lux），需要通过{@link #bindFlashlightView(View)}绑定手电筒才有效
            .bindFlashlightView(ivFlashlight)//绑定手电筒，绑定后可根据光线传感器，动态显示或隐藏手电筒按钮
            .setOnScanResultCallback(this)//设置扫码结果回调，需要自己处理或者需要连扫时，可设置回调，自己去处理相关逻辑
            .setAnalyzer(new MultiFormatAnalyzer(new DecodeConfig()))//设置分析器,DecodeConfig可以配置一些解码时的配置信息，如果内置的不满足您的需求，你也可以自定义实现，
            .setAnalyzeImage(true)//设置是否分析图片，默认为true。如果设置为false，相当于关闭了扫码识别功能
            .startCamera();//启动预览


    //设置闪光灯（手电筒）是否开启,需在startCamera之后调用才有效
    getCameraScan().enableTorch(torch);

```

CameraScan配置示例（只需识别二维码的配置示例）
```java
        //初始化解码配置
        DecodeConfig decodeConfig = new DecodeConfig();
        decodeConfig.setHints(DecodeFormatManager.QR_CODE_HINTS)//如果只有识别二维码的需求，这样设置效率会更高，不设置默认为DecodeFormatManager.DEFAULT_HINTS
            .setFullAreaScan(false)//设置是否全区域识别，默认false
            .setAreaRectRatio(0.8f)//设置识别区域比例，默认0.8，设置的比例最终会在预览区域裁剪基于此比例的一个矩形进行扫码识别
            .setAreaRectVerticalOffset(0)//设置识别区域垂直方向偏移量，默认为0，为0表示居中，可以为负数
            .setAreaRectHorizontalOffset(0);//设置识别区域水平方向偏移量，默认为0，为0表示居中，可以为负数

        //在启动预览之前，设置分析器，只识别二维码
        getCameraScan()
                .setVibrate(true)//设置是否震动，默认为false
                .setAnalyzer(new MultiFormatAnalyzer(decodeConfig));//设置分析器,如果内置实现的一些分析器不满足您的需求，你也可以自定义去实现
```

如果直接使用CaptureActivity需在您项目的AndroidManifest中添加如下配置
```Xml
    <activity
        android:name="com.king.zxing.CaptureActivity"
        android:screenOrientation="portrait"
        android:theme="@style/CaptureTheme"/>
```

### 快速实现扫码有以下几种方式：

> 1、直接使用CaptureActivity或者CaptureFragment。(纯洁的扫码，无任何添加剂)

> 2、通过继承CaptureActivity或者CaptureFragment并自定义布局。（适用于大多场景，并无需关心扫码相关逻辑，自定义布局时需覆写getLayoutId方法）

> 3、在你项目的Activity或者Fragment中实例化一个CameraScan即可。（适用于想在扫码界面写交互逻辑，又因为项目架构或其它原因，无法直接或间接继承CaptureActivity或CaptureFragment时使用）

> 4、继承CameraScan自己实现一个，可参照默认实现类DefaultCameraScan，其它步骤同方式3。（扩展高级用法，谨慎使用）

### 其他

需使用JDK8+编译，在你项目中的build.gradle的android{}中添加配置：

```gradle
compileOptions {
    targetCompatibility JavaVersion.VERSION_1_8
    sourceCompatibility JavaVersion.VERSION_1_8
}

```

更多使用详情，请查看[app](app)中的源码使用示例或直接查看[API帮助文档](https://jenly1314.github.io/projects/ZXingLite/doc/)

## 相关推荐

[MLKit](https://github.com/jenly1314/MLKit) 一个强大易用的工具包。通过ML Kit您可以很轻松的实现文字识别、条码识别、图像标记、人脸检测、对象检测等功能。

## 版本记录

#### v2.1.0：2021-6-30 (从v2.1.0开始不再发布至JCenter)
* 更新CameraX至v1.0.0
* 优化细节

#### v2.0.3：2021-3-26
* 更新CameraX至v1.0.0-rc03
* 优化一些默认配置

#### v2.0.2：2021-1-14
* **ViewfinderView** 新增 **labelTextWidth** 属性

#### v2.0.1：2020-12-30
* 更新CameraX至v1.0.0-rc01
* 新增支持点击预览区域对焦目标
* 修改一些默认配置
* 优化细节

#### v2.0.0：2020-12-24
* 基于CameraX进行重构
* 抽象整体流程，可扩展性更高
* 从2.x开始只支持AndroidX
* minSdk要求从 **16+** 改为 **21+**

#### [查看更多版本记录](update_log.md)

## 赞赏
如果您喜欢ZXingLite，或感觉ZXingLite帮助到了您，可以点右上角“Star”支持一下，您的支持就是我的动力，谢谢 :smiley:<p>
您也可以扫描下面的二维码，请作者喝杯咖啡 :coffee:
    <div>
        <img src="https://jenly1314.github.io/image/pay/wxpay.png" width="280" heght="350">
        <img src="https://jenly1314.github.io/image/pay/alipay.png" width="280" heght="350">
        <img src="https://jenly1314.github.io/image/pay/qqpay.png" width="280" heght="350">
        <img src="https://jenly1314.github.io/image/alipay_red_envelopes.jpg" width="233" heght="350">
    </div>

## 关于我
   Name: <a title="关于作者" href="https://about.me/jenly1314" target="_blank">Jenly</a>

   Email: <a title="欢迎邮件与我交流" href="mailto:jenly1314@gmail.com" target="_blank">jenly1314#gmail.com</a> / <a title="给我发邮件" href="mailto:jenly1314@vip.qq.com" target="_blank">jenly1314#vip.qq.com</a>

   CSDN: <a title="CSDN博客" href="http://blog.csdn.net/jenly121" target="_blank">jenly121</a>

   CNBlogs: <a title="博客园" href="https://www.cnblogs.com/jenly" target="_blank">jenly</a>

   GitHub: <a title="GitHub开源项目" href="https://github.com/jenly1314" target="_blank">jenly1314</a>

   Gitee: <a title="Gitee开源项目" href="https://gitee.com/jenly1314" target="_blank">jenly1314</a>

   加入QQ群: <a title="点击加入QQ群" href="http://shang.qq.com/wpa/qunwpa?idkey=8fcc6a2f88552ea44b1411582c94fd124f7bb3ec227e2a400dbbfaad3dc2f5ad" target="_blank">20867961</a>
   <div>
       <img src="https://jenly1314.github.io/image/jenly666.png">
       <img src="https://jenly1314.github.io/image/qqgourp.png">
   </div>



