# Weex Ui
[中文](README_cn.md) | [English](README.md)

[![Build Status](https://img.shields.io/travis/apache/incubator-weex-ui.svg?style=flat-square)](https://travis-ci.org/apache/incubator-weex-ui)
[![npm](https://img.shields.io/npm/v/weex-ui.svg?maxAge=3600&style=flat-square)](https://www.npmjs.com/package/weex-ui?_blank)
[![NPM downloads](https://img.shields.io/npm/dm/weex-ui.svg?style=flat-square)](https://npmjs.org/package/weex-ui)
[![NPM all downloads](https://img.shields.io/npm/dt/weex-ui.svg?style=flat-square)](https://npmjs.org/package/weex-ui)
[![CNPM all downloads](http://npm.taobao.org/badge/d/weex-ui.svg?style=flat-square)](https://npm.taobao.org/package/weex-ui)
[![GitHub last commit](https://img.shields.io/github/last-commit/apache/incubator-weex-ui.svg?style=flat-square)](https://github.com/apache/incubator-weex-ui/commits/dev)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/apache/incubator-weex-ui.svg?style=flat-square)](https://github.com/apache/incubator-weex-ui/issues?utf8=%E2%9C%93&q=)
[![Package Quality](http://npm.packagequality.com/shield/weex-ui.svg?style=flat-square)](http://packagequality.com/#?package=weex-ui)
[![Join the chat at https://gitter.im/alibaba-weex-ui/chat](https://img.shields.io/gitter/room/apache/incubator-weex-ui.svg?style=flat-square)](https://gitter.im/alibaba-weex-ui/chat?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

> A rich interactive, lightweight, high performance UI library based on [Weex](https://github.com/apache/incubator-weex).

## Docs

* [**Home Page**](https://apache.github.io/incubator-weex-ui/)
* [中文文档](https://apache.github.io/incubator-weex-ui/#/cn/)
* [Use Weex Ui with weex-toolkit](https://apache.github.io/incubator-weex-ui/#/docs/with-weex-toolkit)

## Demo

<img src="https://img.alicdn.com/tfs/TB1O2ulhgoQMeJjy0FoXXcShVXa-1282-986.jpg" width=540/>

Try [**it**](https://h5.m.taobao.com/trip/weex-ui/index.html?_wx_tpl=https%3A%2F%2Fh5.m.taobao.com%2Ftrip%2Fweex-ui%2Fdemo%2Findex.native-min.js) with Fliggy, Taobao, Tmall, Weex Playground or any browsers now!

## Installation

```shell
npm i weex-ui -S
```

## Usage

```html
<template>
  <div>
    <wxc-button text="Open Popup"
                @wxcButtonClicked="buttonClicked">
    </wxc-button>
    <wxc-popup width="500"
               pos="left"
               :show="isShow"
               @wxcPopupOverlayClicked="overlayClicked">
    </wxc-popup>
  </div>
</template>

<script>
  import { WxcButton, WxcPopup } from 'weex-ui';
  // or
  // import WxcButton from 'weex-ui/packages/wxc-button';
  // import WxcPopup from 'weex-ui/packages/wxc-popup';
  module.exports = {
    components: { WxcButton, WxcPopup },
    data: () => ({
      isShow: false
    }),
    methods: {
      buttonClicked () {
        this.isShow = true;
      },
      overlayClicked () {
        this.isShow = false;
      }
    }
  };
</script>
```

### Before use

In order to not pack all the components, you need to use [`babel-plugin-component`](https://www.npmjs.com/package/babel-plugin-component) to import the specified component.
At the same time, if you haven't installed `babel-preset-stage-0`, it's necessary to install it.

```shell
npm i babel-preset-stage-0 babel-plugin-component -D
```

```json
{
    "presets": ["es2015", "stage-0"],
    "plugins": [
        [
            "component",
            {
                "libraryName": "weex-ui",
                "libDir": "packages",
                "style": false
            }
        ]
    ]
}
```

### More

* If babel-loader in `webpack.config.js` has a exclude for node_modules, please turn on for weex-ui as `exclude: /node_modules(?!(\/|\\).*(weex).*)/`.
* In order to get the latest features, please focus on the [ChangeLog](https://github.com/apache/incubator-weex-ui/releases) and often update `weex-ui` to the latest.
* Many questions can be found in the [faq](https://apache.github.io/incubator-weex-ui/#/docs/faq) and [issue list](https://github.com/apache/incubator-weex-ui/issues?utf8=%E2%9C%93&q=), if you find a new bug, just file an [issue](https://github.com/apache/incubator-weex-ui/issues/new).
* More experience in Weex construction can be learned from [Weex + Ui - Weex Conf 2018](https://apache.github.io/incubator-weex-ui/#/docs/weex-ui-weex-conf-2018), welcome to translate it.

## Development

```shell
npm i
npm run start
```

Once it has been compiled, a browser window will be opened automatically. You can switch to developer mode to see the demo. And there will be a QR code that you can use to try the demo on your phone in the console.

## Support

* Use Weex Ui in your daily work.
* **Star it** if you like.
* Join the chat at DingTalk to help solve weex problems.

 <table><tr><td><img src="https://img.alicdn.com/tfs/TB1AEsZf7T2gK0jSZPcXXcKkpXa-750-990.jpg" width="190"></td><td><img  src="https://img.alicdn.com/tfs/TB1tpS2LxnaK1RjSZFtXXbC2VXa-606-799.png" width="190"></td><td><img src="https://img.alicdn.com/tfs/TB1lf1CLCzqK1RjSZFpXXakSXXa-1125-1485.png" width="190"></td></tr></table>

## Contribution

Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our [Contributing Guide](https://github.com/apache/incubator-weex-ui/blob/master/CONTRIBUTING.md) before making a pull request.

Thank you to all the people who already contributed to Weex Ui!

<a href="https://github.com/apache/incubator-weex-ui/graphs/contributors"><img src="https://opencollective.com/weex-ui/contributors.svg?width=890&button=false"/></a>

## License

* The [Apache License](https://apache.org/)
* Please feel free to use and contribute to the development.
