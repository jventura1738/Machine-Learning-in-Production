# qmui-ios-codesnippets 
*qmui-ios-codesnippets* 是一个 QMUI 团队日常工作中整理出来的用于 Xcode 的 iOS 通用代码片段集，其中也包含若干专用于 QMUI for iOS 框架的代码片段。

整理这个代码片段集的初衷有以下几点：

1. 我们发现由于 Xcode 本身的功能不足，导致我们经常在重写一些系统父类方法时容易忘了调用 `super`，从而出现一些很难排查的诡异bug。
2. Xcode 虽然有模糊匹配的代码提醒，但代码提醒只能帮你写方法名，而code snippets 还可以帮你填充一些默认的方法实现，或者直接移动光标到方法体内，省去几次光标操作。
3. 一些常用的写法本身语法可能比较复杂，难以记忆，例如实现一个类的单例、使用 `swizzle` 来重写系统控件的方法、block 在不同地方的语法不同等。
4. 一些代码本身看似简单，但由于特别常用，所以使用 code snippets 可以大大节省时间。


## 使用方式
Xcode 的 Code Snippets 文件存放于 `~/Library/Developer/Xcode/UserData/CodeSnippets` 目录，只要直接把 `*.codesnippets` 文件放到这个目录下（若没有则自己创建），重启 Xcode 即可生效。

为了方便更新，建议直接将 QMUI iOS CodeSnippets clone 到这个目录内（注意，不是在 CodeSnippets 里创建一个 QMUI 的目录，这里不支持子目录）：
```bash
cd ~/Library/Developer/Xcode/UserData/CodeSnippets
```
CodeSnippets 目录为空:
```bash
git clone https://github.com/QMUI/QMUI_iOS_CodeSnippets.git ./
```
CodeSnippets 目录不为空:
```bash
git init .
git remote add origin https://github.com/QMUI/QMUI_iOS_CodeSnippets.git
git pull origin master 
```

其中以 `QM_` 前缀开头的文件是通用的 Code Snippets，以 `QMUI_` 前缀开头的文件是专用于 `QMUI for iOS` 框架的代码片段。在下方的快捷键汇总里，QMUI 的代码片段将会以QMUI的形式标记出来。

注意，Xcode 对每一段 Code Snippet 都有规定适用的语言（Objective-C、Objective-C++、Swift、...）和作用域（如 Class 的 Interface 定义内、Class 的 Implementation 内、方法体内、...），所以测试某段 Code Snippet 不生效时请注意你当前是否处于不匹配的位置。

## 快捷键汇总
*NSObject*
- `pa` - 定义一个 `assign` 的 property
- `par` - 定义一个 `assign, readonly` 的 property
- `pc` - 定义一个 `copy` 的 property
- `pcr` - 定义一个 `copy, readonly` 的 property
- `ps` - 定义一个 `strong` 的property
- `psr` - 定义一个 `strong, readonly` 的property
- `pw` - 定义一个 `weak` 的property
- `pwr` - 定义一个 `weak, readonly` 的property
- `load_once` - 创建一个带 `dispatch_once` 的 `+load` 方法
- `propertySwizzleAssign` - 用 `swizzle` 的方式定义一个 `assign` 的property
- `propertySwizzleCopy` - 用 `swizzle` 的方式定义一个 `copy` 的property
- `propertySwizzleStrong` - 用 `swizzle` 的方式定义一个 `strong` 的property
- `propertySwizzleWeak` - 用 `swizzle` 的方式定义一个 `weak` 的property
- `sharedInstance` - 为当前类创建一个实现单例功能的 `sharedInstance` 方法
- `exchangeImplementation` - 重写当前类的 `load` 方法并在其中用 `swizzle` 替换方法实现
- `exchangeImplementation_QMUI` - 用 QMUI 重写当前类的 `load` 方法并用 `ExchangeImplementations()` 函数替换方法的实现
- `exchangeMultipleImplementations_QMUI` - 用 QMUI 重写当前类的 `load` 方法并用 `ExchangeImplementations()` 函数批量替换多个方法的实现
- `override_void_non_argv` - 用 QMUI 的 `OverrideImplementation()` 重写指定 class 的某个无返回值、无参数的方法实现
- `override_void_single_argv` - 用 QMUI 的 `OverrideImplementation()` 修改指定 class 的某个无返回值、带一个参数的方法实现
- `override_void_two_argvs` - 用 QMUI 的 `OverrideImplementation()` 修改指定 class 的某个无返回值、带两个参数的方法实现
- `override_return_non_argv` - 用 QMUI 的 `OverrideImplementation()` 修改指定 class 的某个带返回值、无参数的方法实现
- `override_return_single_argv` - 用 QMUI 的 `OverrideImplementation()` 修改指定 class 的某个带返回值、带一个参数的方法实现
- `override_return_two_argvs` - 用 QMUI 的 `OverrideImplementation()` 修改指定 class 的某个带返回值、带两个参数的方法实现
- `extend_void_non_argv` - 用 QMUI 的 `ExtendImplementationOfVoidMethodWithoutArguments()` 修改指定 class 的某个无返回值、无参数的方法实现
- `extend_void_single_argv` - 用 QMUI 的 `ExtendImplementationOfVoidMethodWithSingleArgument()` 修改指定 class 的某个无返回值、带一个参数的方法实现
- `extend_void_two_argvs` - 用 QMUI 的 `ExtendImplementationOfVoidMethodWithTwoArguments()` 修改指定 class 的某个无返回值、带两个参数的方法实现
- `extend_return_non_argv` - 用 QMUI 的 `ExtendImplementationOfNonVoidMethodWithoutArguments()` 修改指定 class 的某个带返回值、无参数的方法实现
- `extend_return_single_argv` - 用 QMUI 的 `ExtendImplementationOfNonVoidMethodWithSingleArgument()` 修改指定 class 的某个带返回值、带一个参数的方法实现
- `extend_return_two_argvs` - 用 QMUI 的 `ExtendImplementationOfNonVoidMethodWithTwoArguments()` 修改指定 class 的某个带返回值、带两个参数的方法实现


*Block*
- `blockParameterInMethod` - 声明一个用于 OC 方法参数的 block
- `blockParameterInFunction` - 声明一个用于 C 函数参数的 block
- `blockproperty` - 声明一个用于 property 的 block
- `blocktypedef` - 用 `typedef` 定义一个 block
- `blockvar` - 定义一个作为局部变量的 block


*Method & Function*
- `fnv` - 定义一个返回值为 `void` 的方法
- `fnv:` - 定义一个返回值为 `void` 且带参数的方法
- `fnblock` - 定义一个返回值类型为 block 的方法
- `fnv_handleEvent` - 定义一个用于 `UIControl` 事件回调的方法
- `fnv_longPress` - 定义一个用于 `UILongPressGestureRecognizer` 的回调方法（你就不用每次都去拼写那个很长的手势名字了）
- `fnv_pan` - 定义一个用于 `UIPanGestureRecognizer` 的回调方法
- `fnv_tap` - 定义一个用于 `UITapGestureRecognizer` 的回调方法


*UIView*
- `setFrame` - 为 `UIView` 设置 `frame`
- `setFrame_QMUI` - QMUI 使用像素对齐的 `CGRectFlatMake()` 为 `UIView` 设置 `frame`
- `setFrameX` - QMUI 使用 `CGRectSetX()` 修改 `UIView` 的 `frame.origin.x`
- `setFrameY` - QMUI 使用 `CGRectSetY()` 修改 `UIView` 的 `frame.origin.y`
- `setFrameXY` - QMUI 使用 `CGRectSetXY()` 修改 `UIView` 的 `frame.origin`
- `sizeThatFits` - 为当前 view 创建 `sizeThatFits:` 方法
- `layoutSubviews` - 展开 `layoutSubviews` 方法
- `updateConstraints` - 展开 `updateConstraints` 方法
- `getWidth` - 展开 `CGRectGetWidth()`
- `getHeight` - 展开 `CGRectGetHeight()`
- `getMinX` - 展开 `CGRectGetMinX()`
- `getMinY` - 展开 `CGRectGetMinY()`
- `addtarget` - 调用 `UIControl addTarget:action:forEvents:` 方法
- `setImageForButton` - 为 `UIButton` 设置图片
- `setTitleColorForButton` - 为 `UIButton` 设置文字颜色
- `setTitleForButton` - 为 `UIButton` 设置文字

*UITableView*
- `initWithStyle` - 展开 `initWithStyle:` 方法
- `initWithStyleForCell` - 展开 `UITableViewCell initWithStyle:reuseIdentifier:` 方法
- `tableViewDelegate` - 展开常用的几个 `UITableViewDelegate` 方法
- `numberOfSectionsInTableView` - 展开 `numberOfSectionsInTableView:`方法
- `numberOfRowsInSection` - 展开 `tableView:numberOfRowsInSection:` 方法
- `cellForRowAtIndexPath` - 展开 `tableView:cellForRowAtIndexPath:` 方法
- `heightForRowAtIndexPath` - 展开 `tableView:heightForRowAtIndexPath:` 方法
- `didSelectRowAtIndexPath` - 展开 `tableView:didSelectRowAtIndexPath:` 方法


*UICollectionView*
- `collectionViewDelegate` - 展开常用的几个`UICollectionViewDelegate` 方法
- `numberOfSectionsInCollectionView` - 展开 `numberOfSectionsInCollectionView:`
- `numberOfItemsInSection` - 展开 `collectionView:numberOfItemsInSection:`
- `cellForItemAtIndexPath` - 展开 `collectionView:cellForItemAtIndexPath:`
- `sizeForItemAtIndexPath` - 展开 `collectionView:layout:sizeForItemAtIndexPath:` 方法
- `didSelectItemAtIndexPath` - 展开 `collectionView:didSelectItemAtIndexPath:` 方法
- `didDeselectItemAtIndexPath` - 展开 `collectionView:didDeselectItemAtIndexPath:` 方法


*UIViewController*
- `initWithNib` - 展开 `initWithNibName:bundle:` 方法
- `didInitialize` - 展开某些 QMUI 控件提供的 `didInitialize` 方法
- `didInitializeWithStyle` - 展开 QMUICommonTableViewController 的 `didInitializeWithStyle:` 方法
- `loadView` - 展开 `loadView` 方法
- `viewDidLoad` - 展开 `viewDidLoad` 方法
- `viewWillAppear` - 展开 `viewWillAppear:` 方法
- `viewDidAppear` - 展开 `viewDidAppear:` 方法
- `viewWillDisappear` - 展开 `viewWillDisappear:` 方法
- `viewDidDisappear` - 展开 `viewDidDisappear:` 方法
- `viewDidLayoutSubviews` - 展开 `viewDidLayoutSubviews:` 方法
- `updateViewConstraints` - 展开 `updateViewConstraints:` 方法
- `addChildViewController` - 在当前 `UIViewController` 里添加 `childViewController`
- `removeFromParentViewController` - 将 `childViewController` 从当前的 `UIViewController` 里移除
- `initSubviews` - QMUI 展开 `initSubviews` 方法
- `setupNavigationItems` - QMUI 重写 `QMUICommonViewController` 里的 `setupNavigationItems` 方法
- `setupToolbarItems` - QMUI 重写 `QMUICommonViewController` 里的 `setupToolbarItems` 方法

*UIBarButtonItem*
- `backItem` - 用 QMUI 方法生成一个返回按钮
- `boldTitleItem` - 用 QMUI 方法生成一个文字加粗的导航栏按钮
- `closeItem` - 用 QMUI 方法生成一个导航栏上的关闭图标按钮
- `imageItem` - 用 QMUI 方法生成一个导航栏上的图片按钮
- `titleItem` - 用 QMUI 方法生成一个导航栏上的文字按钮


*Other*
- `pragma` - 展开一个用于 Xcode 导航的 `#pragma mark -` 宏
- `log` - 展开 `NSLog(@"xxx")`
- `osif` - 展开一个 @available(iOS xxx, \*) 的 if 判断
- `externRefInH` - 在 `*.h` 文件里声明一个 `extern const` 的指针
- `externRefInM` - 在 `*.m` 文件里为一个 `extern const` 的指针赋值
- `externValueInH` - 在 `*.h` 文件里声明一个 `extern const` 的值变量
- `externValueInM` - 在 `*.m` 文件里为一个 `extern const` 的变量赋值
- `static reference` - 定义一个 `static` 的指针
- `static` - 定义一个 `static` 的值变量
- `__weakSelf` - 定义一个 `weak` 的 `self` 指针
- `__strongSelf` - 将 `weakSelf` 指针改为 `strong` 的 `self` 指针
- `logCallStackSymbols` - 用 `NSLog` 打出当前的方法调用栈信息
- `timeConsuming` - 展开一段用 `CACurrentMediaTime()` 来计算方法耗时的代码
