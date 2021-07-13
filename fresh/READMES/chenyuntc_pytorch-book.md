## [English Version](README_EN.md)


这是书籍《深度学习框架PyTorch：入门与实践》的对应代码，但是也可以作为一个独立的PyTorch入门指南和教程。

## 更新说明
Working on migration to Pytorch 1.0, stay tuned!

当前版本的代码是基于pytorch 1.0.1， 如果想使用旧版的 请 `git checkout v0.4` 或者 `git checkout v0.3`。旧版代码有更好的python2/python3 兼容，CPU/GPU兼容测试。 新版的代码未经过完整测试，已在GPU和python3 下测试通过。但是理论上在python2和CPU上不应该有太多的问题。

## 内容

该书（教程/仓库）的内容如图所示：
![思维导图](imgs/mindmap.png)

可以看出本教程可以分为两部分：

**基础部分**（前五章）讲解PyTorch内容，这部份介绍了PyTorch中主要的的模块，和深度学习中常用的一些工具。对于这部分内容，这里利用Jupyter Notebook作为教学工具，读者可以结合notebook修改运行，反复实验。

- 第二章介绍如何安装PyTorch和配置学习环境。同时提供了一个快速入门教程，基于官方的教程简化并更新内容，读者可以花费大约1到2小时的时间快速完成入门任务，而后根据需求再选择深入阅读后续相关章节的内容。
- 第三章介绍了PyTorch中多维数组Tensor和动态图autograd/Variable的使用，并配以例子，让读者分别使用Tensor和autograd实现线性回归，比较二者的不同点。除了介绍这二者的基础使用之外，本章还对Tensor的底层设计，以及autograd的计算图原理进行比较深入分析，希望能使得读者能对这些底层知识有更全面的掌握。
- 第四章介绍了PyTorch中神经网络模块nn的基础用法，同时讲解了神经网络中“层”，“损失函数”，“优化器”等，最后带领读者用不到50行的代码搭建出曾夺得ImageNet冠军的ResNet。
- 第五章介绍了PyTorch中数据加载，GPU加速，持久化和可视化等相关工具。

**实战部分**（第六到十章）利用PyTorch实现了几个酷炫有趣的应用，对于这部分的内容，本仓库给出完整的实现代码，并提供预训练好的模型作为demo，供读者测试。

- 第六章是承上启下的一章，这一章的目标不是教会读者新函数，新知识，而是结合Kaggle中一个经典的比赛，实现一个深度学习中比较简单的图像二分类问题。在实现过程中，带领读者复习前五章的知识，并提出代码规范以合理的组织程序，代码，使得程序更加可读，可维护。第六章还介绍了在PyTorch中如何进行debug。
- 第七章为读者讲解了当前最火爆的生成对抗网络（GAN），带领读者从头实现一个动漫头像生成器，能够利用GAN生成风格多变的动漫头像。
- 第八章为读者讲解了风格迁移的相关知识，并带领读者实现风格迁移网络，将自己的照片变成高大上的名画。
- 第九章为读者讲解了一些自然语言处理的基础知识，并讲解了CharRNN的原理。而后利用收集了几万首唐诗，训练出了一个可以自动写诗歌的小程序。这个小程序可以控制生成诗歌的**格式**，**意境**，还能生成**藏头诗**。
- 第十章为读者介绍了图像描述任务，并以最新的AI Challenger比赛的数据为例，带领读者实现了一个可以进行简单图像描述的的小程序。
- 第十一章（**新增，实验性**） 由[Diamondfan](https://github.com/Diamondfan) 编写的语音识别。完善了本项目（本项目已囊括图像，文本，语音三大领域的例子）。


 **Notebook中的文字描述内容属于本书的初稿，有描述不通顺，错别字之处还请谅解**。本打算删除notebook中描述的内容，只留下代码，但为了方便读者阅读学习，最终还是决定留下。 我会抽空根据书中内容逐字校对这部分内容，但并不对此并不提供具体时间点。

## 是否需要买书

书**不是必要的**，这个仓库包含书中50%以上的文字内容，90%以上的代码，尤其是前几章入门内容，几乎是完全保留了书中的讲解内容。读者即使不买书也能正常使用本教程。

~~如果你觉得纸质书的优势吸引你，不妨小破费一笔，支持一下作者这大半年来的工作。同时为了尽可能的方便读者，笔者还专门开通腾讯云的服务，用以保存教程中用到的部分模型，预处理的数据和部分大文件。~~
书中的部分内容已经过时，以此仓库内容为准。

## 代码说明

- 代码主要在python3下测试得到最终结果，python2暂未测试。v0.2和v0.3 分支的代码同时经过严格测试支持python2/python3
- 实战部分代码同时在GPU和CPU环境下测试通过
- 代码已更新兼容到PyTorch `0.4.1`, 后续会考虑兼容 `v1.0`，但暂无确切时间点。

如果你想在PyTorch 0.2.0或0.3下运行,请 
```
git checkout v0.2 # v0.3
```

如果有任何不当，或者有待改进的地方，欢迎读者开issue讨论，或者提交pull request。

## 环境配置

1. 安装[PyTorch](http://pytorch.org)，请从官网选择指定的版本安装即可，一键安装（即使你使用anaconda，也建议使用pip）。更多的安装方式请参阅书中说明。

2. 克隆仓库

   ```python
   git clone https://github.com/chenyuntc/PyTorch-book.git
   ```

3. 安装第三方依赖包

   ```python
   cd pytorch-book && pip install -r requirements.txt
   ```

## Visdom打不开及其解决方案
**新版的visdom已经解决了这个问题,只需要升级即可**
```
pip install --upgrade visdom
```
之前的[解决方案](https://github.com/chenyuntc/pytorch-book/blob/2c8366137b691aaa8fbeeea478cc1611c09e15f5/README.md#visdom%E6%89%93%E4%B8%8D%E5%BC%80%E5%8F%8A%E5%85%B6%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88) 不再需要，已删除。

## ^_^

有任何bug，解释不清楚的地方或者是困惑，欢迎开issue

欢迎pull requests

Happy Coding!

![](http://img14.360buyimg.com/n1/jfs/t13339/32/2463730198/217483/e8148c6b/5a41277dNbd1470c1.jpg)

- [京东购买链接](https://search.jd.com/Search?keyword=pytorch%20入门与实践&enc=utf-8&wq=pytorch%20入门与实践&pvid=8b0d91d7108845ad8cbaf596326f3eb3)
- [当当购买链接](http://search.dangdang.com/?key=pytorch%20%C8%EB%C3%C5%D3%EB%CA%B5%BC%F9&act=input)
