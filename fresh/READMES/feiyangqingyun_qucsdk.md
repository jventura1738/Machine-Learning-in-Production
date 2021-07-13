#### 项目介绍
Qt编写的自定义控件插件的sdk集合，包括了各个操作系统的动态库文件以及控件的头文件和sdk使用demo。

#### 体验地址
- 体验地址：[https://pan.baidu.com/s/1A5Gd77kExm8Co5ckT51vvQ](https://pan.baidu.com/s/1A5Gd77kExm8Co5ckT51vvQ) 
- 提取密码：877p 
- 文件名称：bin_quc.zip
- 尊贵提示：可付费购买控件完整源码，每个控件都有独立的使用demo

#### 版本说明
1. sdk分带日期的目录，建议用新版本。
2. 其他文件夹为对应日期的版本，而且同时提供了debug和release的动态库。
3. 头文件请使用对应文件夹下的头文件，因为控件一直在升级完善。
4. 强烈推荐使用最新版，目前共163个控件。
5. 理论上小版本向上向下兼容的，比如5.12.3的dll可以放到5.12.0中使用。

#### 目录说明
1. sdk目录下的include文件为控件对应的头文件。
2. sdk目录为各个Qt版本对应的动态库文件。
3. sdkdemo目录为演示如何调用动态库文件。
4. snap目录为各个控件的运行效果图，一直更新。

#### 使用说明
1. 第一步：前提是qt版本、编译器类型、编译器版本、编译器位数必须完全一致。
2. 第二步：找到qt安装目录的库所在的bin目录，同级有个plugins文件夹，plugins文件夹下有个designer目录，将对应插件文件例如 quc_5_7_0_msvc2013_32.dll 放到此目录即可。
3. 第三步：双击bin目录下的designer.exe，打开提供的demo.ui，即可看到效果。或者新建个空白UI然后从左边的控件栏里面拖动过去。
4. 如果想集成到qtcreator中，则必须保证你下载的库版本必须和你的qtcreator所用的qt版本+编译器+位数完全一致才行，很可能集成安装包中的qtcreator版本是上一个qt版本编译的，这样是无法集成进去的，推荐用qt5.12.3这个集成安装包，如果你是msvc编译器那是可以顺利集成进去的。
5. windows系统上Qt Designer设计师动态库存放的地址一般是 C:\Qt\Qt5.15.2\5.15.2\mingw81_64\plugins\designer，Qt Creator动态库存放的地址一般是 C:\Qt\Qt5.15.2\Tools\QtCreator\bin\plugins\designer。
6. linux系统上Qt Designer设计师动态库存放的地址一般是 /home/liu/Qt/Qt5.14.0/5.14.0/gcc_64/plugins/designer，Qt Creator动态库存放的地址一般是 /home/liu/Qt/Qt5.14.0/Tools/QtCreator/lib/Qt/plugins/designer。
7. mac系统上Qt Designer设计师动态库存放的地址一般是 /Users/liu/Qt/5.15.2/clang_64/plugins/designer，Qt Creator动态库存放的地址一般是 /Users/liu/Qt/Qt Creator.app/Contents/PlugIns/designer。
8. 非官方使用图文教程 [https://blog.csdn.net/u014779536/article/details/106923566](https://blog.csdn.net/u014779536/article/details/106923566)

#### 特别说明
1. **动态库和对应的头文件会一直更新完善修复BUG，由于作者精力有限，不保证所有的插件都是最新的，只保证qt_5_7_0_mingw530_32这个版本永远是最新的正确的，为什么选择这个版本，因为5.7.0是最后一个支持XP的版本。谢谢信任和理解。**
2. **务必记得要集成到QtCreator就必须和QtCreator的版本保持一致，要编译项目成功就必须和你使用的构建套件的版本保持一致，比如安装的5.12.3的qt集成开发环境，你需要拷贝qt_5_12_3_msvc2017_32.zip这个下面的dll到对应的目录，而如果你使用的是5.12.3+mingw32编译器的话，在编译sdkdemo的时候需要拷贝qt_5_12_3_mingw730_32.zip这个下面的dll到sdkdemo目录下同文件替换dll，切记qt和qtcreator是两个东西，不一样，一个creator可以加载多个不同的qt构建套件。千万别把QtCreator的dll拷贝到sdkdemo目录。**

#### 功能特点
 1. 超过160个精美控件，涵盖了各种仪表盘、进度条、进度球、指南针、曲线图、标尺、温度计、导航条、导航栏，flatui、高亮按钮、滑动选择器、农历等。远超qwt集成的控件数量。
 2. 每个类都可以独立成一个单独的控件，零耦合，每个控件一个头文件和一个实现文件，不依赖其他文件，方便单个控件以源码形式集成到项目中，较少代码量。qwt的控件类环环相扣，高度耦合，想要使用其中一个控件，必须包含所有的代码。
 3. 全部纯Qt编写，QWidget+QPainter绘制，支持Qt4.6到Qt5.13的任何Qt版本，支持mingw、msvc、gcc等编译器，支持任意操作系统比如windows+linux+mac+嵌入式linux等，不乱码，可直接集成到Qt  Creator中，和自带的控件一样使用，大部分效果只要设置几个属性即可，极为方便。
 4. 每个控件都有一个对应的单独的包含该控件源码的DEMO，方便参考使用。同时还提供一个所有控件使用的集成的DEMO。
 5. 每个控件的源代码都有详细中文注释，都按照统一设计规范编写，方便学习自定义控件的编写。
 6. 每个控件默认配色和demo对应的配色都非常精美。
 7. 超过130个可见控件，6个不可见控件。
 8. 部分控件提供多种样式风格选择，多种指示器样式选择。
 9. 所有控件自适应窗体拉伸变化。
 10. 集成自定义控件属性设计器，支持拖曳设计，所见即所得，支持导入导出xml格式。
 11. 集成fontawesome图形字体+阿里巴巴iconfont收藏的几百个图形字体，享受图形字体带来的乐趣。
 12. 所有控件最后生成一个dll动态库文件，可以直接集成到qtcreator中拖曳设计使用。

![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/000.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/00.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/0.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/0.png)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/1_qtcreator_msvc2017.png)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/customring.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugecar.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugecolor.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugemini.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugepanel.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugepercent.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugespeed.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/progresspercent.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/telwidget.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/wavebar.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/switchbutton.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/progresstip.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugeedit.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/timeaxis.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/shadowclock.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/shadowcalendar.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/progressshadow.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/wavewater.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/progressarc.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/scantantan.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/imageanimation.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugecompasspan.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/progressbutton.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/lunarcalendarwidget.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/colorpanel.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/navlistview.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/navbutton.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugecloud.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugedial.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/rulerprogress.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/gaugeprogress.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/rulerslider.gif)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/1_property1.png)
![avatar](https://github.com/feiyangqingyun/qucsdk/raw/master/snap/1_property2.png)