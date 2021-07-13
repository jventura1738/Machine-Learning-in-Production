[![tag](https://img.shields.io/badge/tag-0.4.7-blue.svg)](https://github.com/jpush/imui/releases)
[![support](https://img.shields.io/badge/support-iOS%20%26%20Android-brightgreen.svg)]()
[![QQ Group](https://img.shields.io/badge/QQ%20Group-604798367-red.svg)]()

# Aurora IMUI
[中文文档](./README_zh.md)

Aurora IMUI is a general IM UI components library, which does not depend on any specific IM SDK.

This library provides common UI components such as MessageList, InputView. It supports common message type, such as text, image, audio, video, etc. By default it has several UI style for choice, and also supports style customization.

We already have Android/iOS/React Native platforms support.

Already supports three main platforms: Android, iOS, React Native.

Please refer to [aurora-imui-examples](https://github.com/jpush/aurora-imui-examples) for more examples.

<p align="center">
    <a target="_blank">
        <img src="https://github.com/huangminlinux/resource/blob/master/IMUIPick%402x.png" alt="IMUI" width=960/>
    </a>
</p>

## Features

With Aurora IMUI, you can implement these features easily:

- Displaying message list:
  - supports different message types;
  - supports click & long click events for each type of message;
  - supports user avatar.
- Message input:
  - supports multiple message types;
  - voice input component;
  - photo album selection component;
  - record video or take picture using camera.

Currently support for display and input message types:
- Text
- Image
- Voice
- Video
- Custom


## Usage

Ready components:

### Android
- [MessageList](./docs/Android/message_list_usage.md)
- [ChatInputView](./Android/chatinput/README_EN.md)

### iOS (Swift)
- [IMUIMessageCollectionView](./docs/iOS/IMUIMessageCollectionView_usage.md)
- [IMUIInputView](./docs/iOS/IMUIInputView_usage.md)

### React Native
- [AuroraIMUI_Pure_JS  Beta](./ReactNative_JS/README.md)
- [AuroraIMUI_Native_Bridge](./ReactNative/README.md)

## Contribute

Welcome contribution! [Look at the issues](https://github.com/jpush/imui/issues).

## License

MIT © [JiGuang](/LICENSE)

