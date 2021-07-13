[![Read the documentation](https://img.shields.io/badge/Read-the%20docs-green.svg)](http://qfield.org/docs/installation-guide/index.html)
[![Join the chat at https://gitter.im/opengisch/QField](https://badges.gitter.im/opengisch/QField.svg)](https://gitter.im/opengisch/QField?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Release](https://img.shields.io/github/release/opengisch/QField.svg)](https://github.com/opengisch/QField/releases)

# QField for QGIS

A simplified touch optimized interface for QGIS.

Perfect for field work on portable touch devices.

## Get it

Check the [documentation](http://qfield.org/docs)

### Android

[![Get in Google play](http://www.qfield.org/images/Get_it_on_Google_play.png)](https://play.google.com/store/apps/details?id=ch.opengis.qfield)

### Windows (Beta)

[![Download the latest windows beta version](https://qgis.org/en/_static/images/app_download_windows.png)](https://nightly.link/opengisch/QField/workflows/windows/master/QField-dev-Release.zip)

### iOS (Alpha)

An iOS version is being developed, [subscribe as iOS tester](https://forms.clickup.com/f/22wqj-2878/D6IEV7K3PKVONXPX8P) to be among the first to try

## Contribute

QField is an open source project, licensed under the terms of the GPLv2 or later. This means that it is free to use and modify and will stay like that.

We are very happy if this app helps you to get your job done or in whatever creative way you may use it.

If you found it useful, we will be even happier if you could give something back. A couple of things you can do are

 * Rate the app [★★★★★](https://play.google.com/store/apps/details?id=ch.opengis.qfield&hl=en#details-reviews)
 * [Tweet about it](https://twitter.com/share?text=Looking%20for%20a%20good%20tool%20for%20field%20work%20in%20GIS?%20Check%20out%20%23QField!)
 * Write about your experience (please [let us know](mailto:info@opengis.ch)!)
 * [Help with the documentation](https://github.com/opengisch/QField-docs#documentation-process)
 * [Translate the documentation](https://github.com/opengisch/QField-docs#translation-process) or [the app](https://www.transifex.com/opengisch/qfield-for-qgis/)
 * [Sponsor a feature](https://opengisch.github.io/QField-docs/development/index.html#make-it-grow-make-it-yours)
 * And just drop by to say thank you or have a beer with us next time you meet OPENGIS.ch at a conference

## Get master (unstable) version
We automatically publish the latest master build to a [dedicated channel on the playstore](https://play.google.com/store/apps/details?id=ch.opengis.qfield_dev). You'll need to [join the beta program](https://play.google.com/apps/testing/ch.opengis.qfield_dev) to start getting the latest version.

Please remember that this is the latest development build and is **not** tested much.


## Build

### For Android

Building QField is a multi layered process with more than a few caveats.
Luckily there is a super simple build script that does the dirty work for you.

```
./scripts/build.sh
```

This will put the apk into a subfolder `build-docker/out/build-arm64_v8a/outputs/apk`

If you want to build for a different architecture, set the ARCH enviroment variable.

```
ARCH=x86_64 ./scripts/build.sh
```

### For iOs

- [x] Build sdk in cloud
- [x] Simplify framework linking
- [ ] Dedicated Info.plist.in
- [x] Icon folder
- [x] LaunchScreen.storyboard
- [ ] Update https://www.opengis.ch/android-gis/qfield/donate-and-sponsor/ in About.qml to https://www.opengis.ch/projects/qfield-love/

### For Desktop

In general it's much easier to develop on Desktop where you get quick feedback and a step by step debugger.

To build QField for a desktop environment:

* Get QGIS development libraries. QField normally uses bleeding edge QGIS code. Ideally install nightly builds or compile it on your own and install to a custom prefix path. See more about QGIS compilation [here](https://github.com/qgis/QGIS/blob/master/INSTALL.md).
* If your system comes with a Qt version which is too low for QField, you can also install Qt manually. Download the most recent Qt 5.x version from the [Qt Website](https://www.qt.io/download) to satisfy QField dependencies. Setup a new QtCreator kit that uses the downloaded Qt libs.
* Get QField source code:

```sh
cd QField
```

 * Open `CMakeList.txt` with QtCreator.
 * Hit build

(??)If you make your own QGIS build, use the following variables: `QGIS_ANALYSIS_LIBRARY`, `QGIS_CORE_LIBRARY`, `QGIS_INCLUDE_DIR`, and `QGIS_PLUGIN_DIR`.

### On OS X

In addition to the steps above, in QtCreator's build environment (access via `Projects` > `Build`), add the following variables:

  * `QGIS_INSTALL_PATH`: the same value than in the config.pri (could be /usr/local/opt/qgis3/ or the installation folder of a local build)
  * `DYLD_FRAMEWORK_PATH` add `_QGIS_INSTALL_PATH_/QGIS.app/Contents/Frameworks` (replace `_QGIS_INSTALL_PATH_`)
  * `DYLD_LIBRARY_PATH` add `:_QGIS_INSTALL_PATH_/QGIS.app/Contents/Frameworks/qgis_core.framework/Versions/Current` (replace `_QGIS_INSTALL_PATH_`)

#### Invalid version number issue

If you get the error `invalid version number in '-mmacosx-version-min='`, you need to hardcode the minimum deployment target by setting `version_min_flag = -m$${version_identifier}-version-min=10.10` in `/usr/local/opt/qt/mkspecs/features/mac/default_post.prf`.

One line command:
```
gsed -i "s/version_min_flag = -m\$\${version_identifier}-version-min=\$\$deployment_target/version_min_flag = -m\$\${version_identifier}-version-min=10\.10/" /usr/local/opt/qt/mkspecs/features/mac/default_post.prf
```

#### In `Qt Creator` > `Projects` > `Run` >

* Check `Use debug version of frameworks`
* Add a custom deployment step: `_QField_SOURCE_DIR_/scripts/mac_deploy.sh` with `${QGIS_INSTALL_PATH}` as argument.
* In Debugger settings, check `Enable QML`

#### Other issues
If you have any issue with qmake not finding the proper SDK, in `/usr/local/opt/qt/mkspecs/features/mac/default_post.prf`, replace `$$QMAKE_MAC_SDK_PATH` (3 occurences) by `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk`
