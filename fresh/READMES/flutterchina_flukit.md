[English](README-EN.md)|中文简体

# Flukit [![Pub](https://img.shields.io/pub/v/flukit.svg?style=flat-square)](https://pub.dartlang.org/packages/flukit)


*flukit* （Flutter UI Kit）是一个Flutter Widget库。

## 注意

本项目正在持续迭代中，欢迎大家贡献代码。  

## 贡献代码须知

### 工程目录

```
flukit
	--lib           //示例目录
	--package_src
	  --lib
	   --src  //widget库目录
	--docs //文档目录，文档必须是markdown格式
      --images //文档用到的图片都放在这里，如截图
      --chs //中文文档目录
      --en //英文文档目录
```

### 运行Demo

```
flutter run
```

### **提交代码须知**

如果你添加了一个，请遵循如下规则：

1. 尽可能多的添加注释，文档注释为三斜线"///"
2. 添加一个新的Widget后，请在Demo目录添加使用示例，示例应该纯净无干扰，如果一个widget需要多个示例，可以创建一个二级页面，可以参照Pull Refresh、QuickSelectListView。
3. 如果可以，请尽可能在doc目录下为widget添加使用文档，文档必须是markdown格式，文档名应与widget文件名同名

### Widgets

| Widget名称                        | 介绍                                       |
| --------------------------------- | ------------------------------------------ |
| QuickScrollbar                    | 可拖动的滚动条                             |
| TurnBox                           | 可按任意角度旋转子组件                     |
| AnimatedRotationBox               | 可对子组件执行旋转动画                     |
| ScaleView                         | 可以对子组件进行缩放（双指伸缩）           |
| Swiper                            | 一个轮播组件                               |
| GradientButton                    | 背景色渐变按钮                             |
| RaisedGradientButton              | 背景色渐变按钮(Raised)                     |
| GradientCircularProgressIndicator | 一个支持颜色渐变的圆形进度指示器           |
| InfiniteListView                  | 支持下拉刷新的无限加载列表组件             |
| PullRefreshBox（betal）           | 下拉刷新（该组件并未成熟，将来可能会删掉） |
| NineGridView                      | 类似微信/微博展示图片九宫格，钉钉群组，微信群组，QQ讨论组头像   |
| DragSortView                      | 类似微博/微信发布动态选图九宫格，拖拽换位 |



### Demo部分截图

|![](docs/images/quick_scroll_bar.gif)|![](docs/images/animated_rotation_box.gif)|![](docs/images/gradient_circular_progress_indicator.gif)|
|:---:|:---:|:---:|
|![](docs/images/swiper.gif)|![](docs/images/photoview.gif)|![](docs/images/city_select.gif)|
|![](docs/images/pull_refresh.gif)|![](docs/images/pull_refresh_with_custom_header.gif)|![](docs/images/city_select.gif)|
|![](docs/images/quick_list.gif)|![](docs/images/raised_button.png)|![](docs/images/infinite_listview.png)|
|![](https://s1.ax1x.com/2020/09/09/w3DOZq.png)|![](https://s1.ax1x.com/2020/09/09/w3rZFK.png)|![](https://s1.ax1x.com/2020/09/09/w3rJFf.png)|
|![](docs/images/nine_grid_view1.jpg)|![](docs/images/nine_grid_view2.jpg)|![](docs/images/nine_grid_view3.jpg)|
|![](docs/images/nine_grid_view4.jpg)|![](docs/images/nine_grid_view5.jpg)|![](docs/images/nine_grid_view6.jpg)|
|![](docs/images/nine_grid_view7.jpg)|![](docs/images/nine_grid_view8.jpg)|![](docs/images/nine_grid_view9.gif)|


### Others

另外一个[NineGridView](https://github.com/flutterchina/nine_grid_view)，使用的Stack + Positioned实现，本项目通过封装GridView实现。

[AzListView](https://github.com/flutterchina/azlistview) A Flutter sticky headers & index ListView. Flutter 城市列表，联系人列表，索引&悬停。