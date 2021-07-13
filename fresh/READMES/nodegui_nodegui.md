# NodeGui

[![Join the NodeGUI community on Spectrum](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/nodegui)
[![All Contributors](https://img.shields.io/badge/all_contributors-16-orange.svg?style=flat-square)](#contributors)
[![JS Party #96](https://img.shields.io/badge/JS%20Party-%2396-FFCD00.svg)](https://changelog.com/jsparty/96)

[![Build and Test status](https://github.com/nodegui/nodegui/workflows/.github/workflows/test.yml/badge.svg)](https://github.com/nodegui/nodegui/actions)

Build **performant**, **native** and **cross-platform** desktop applications with **Node.js** and **CSS like styling**.🚀

NodeGUI is powered by **Qt5** 💚 which makes it CPU and memory efficient as compared to other chromium based solutions like electron.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1024px-React-icon.svg.png" alt="" width="25"> If you are looking for **React** based version, check out: **[React NodeGUI](https://github.com/nodegui/react-nodegui)**.

<img src="https://vuejs.org/images/logo.png" alt="" width="25" /> If you are looking for **Vue** based version, check out: **[Vue NodeGUI](https://github.com/nodegui/vue-nodegui)**.

<img src="https://github.com/sveltejs/branding/raw/master/svelte-logo.png" alt="" width="25" /> If you are looking for **Svelte** based version, check out: **[Svelte NodeGUI](https://github.com/nodegui/svelte-nodegui)**

Visit: https://nodegui.github.io/nodegui for docs.

<img alt="logo" src="https://github.com/nodegui/nodegui/raw/master/extras/logo/nodegui.png" height="200" />

## How does it look?

<div style="display:inline; margin: 0 auto;">
<img alt="demo_linux" src="https://github.com/nodegui/examples/raw/master/nodegui/calculator/calculator_linux.png" height="280" />
<img alt="demo_win" src="https://github.com/nodegui/examples/raw/master/nodegui/calculator/calculator_win.jpg" height="280" />
<img alt="demo_mac" src="https://github.com/nodegui/examples/raw/master/nodegui/calculator/calculator_mac.png" height="280" />
</div>

<div style="display:inline; margin: 0 auto;"><img alt="kitchen" src="https://github.com/nodegui/nodegui/raw/master/extras/assets/kitchen.png" height="280" /><img alt="demo_mac" src="https://github.com/nodegui/examples/raw/master/react-nodegui/weather-app-widget/weather_widget_mac.png" height="280" /><img alt="demo_win" src="https://github.com/nodegui/examples/raw/master/react-nodegui/image-view/image_view_win.jpg" height="280" />
</div>

**More screenshots?**

### More Examples:

https://github.com/nodegui/examples

---

## Features

-   🧬 **Cross platform.** Should work on major Linux flavours, Windows and MacOS.
-   📉 **Low CPU and memory** footprint. Current CPU stays at 0% on idle and memory usage is under 20mb for a hello world program.
-   💅 **Styling with CSS** (includes actual cascading). Also has full support for Flexbox layout (thanks to Yoga).
-   ✅ **Complete Nodejs api support** (Currently runs on Node v12.x - and is easily upgradable). Hence has access to all nodejs compatible npm modules.
-   🎪 **Native widget event listener support.** Supports all events available from Qt / NodeJs.
-   💸 **Can be used for Commercial applications.**
-   🕵️‍♂️ **Good Devtools support.**
-   📚 **Good documentation and website.**
-   🧙‍♂️ **Good documentation for contributors.**
-   🦹🏻‍♀️ **Good support for dark mode (Thanks to Qt).**
-   🏅**First class Typescript support.** (Works on regular JS projects too 😉).

## Getting Started

-   Check out [nodegui-starter](https://github.com/nodegui/nodegui-starter) to get up and running with your own React NodeGUI app!
-   Read through the [docs](https://nodegui.github.io/nodegui).
-   Checkout the examples: https://github.com/nodegui/examples .
-   [Tutorial: Build a native Meme Search Desktop app with Javascript (NodeGui) and Giphy API](https://www.sitepoint.com/build-native-desktop-gif-searcher-app-using-nodegui/)

## Installation

NodeGui requires CMake and Compilation Tools as it is a wrapper for a native C++ widget toolkit QT.
Detailed instructions here: https://www.sitepoint.com/build-native-desktop-gif-searcher-app-using-nodegui/

TL;DR:
MacOS

```
brew install cmake
brew install make
```


Windows
https://cmake.org/download/

Linux (Debian/Ubuntu)

```
sudo apt-get install pkg-config build-essential
sudo apt-get install cmake make
sudo apt-get install mesa-common-dev libglu1-mesa-dev
```

Linux (Fedora/RHEL/CentOS)

```
sudo dnf groupinstall "Development Tools" "Development Libraries"
sudo dnf groupinstall "C Development Tools and Libraries"
sudo dnf install mesa-libGL mesa-libGL-devel
```

Then install NodeGui from your command line:

#### To install latest stable release:

```
npm install @nodegui/nodegui
```

#### To install the latest version available on master branch:

```
npm install https://github.com/nodegui/nodegui/releases/download/v0.0.0-latest-master/nodegui-master.tgz
```

or a shorter version:

```
npm i http://master-release.nodegui.org
```

If the installation fails to download the Qt binaries, a mirror can be used by setting the following environment variable and running the install command again:

```sh
QT_LINK_MIRROR=<alternative domain> # eg. QT_LINK_MIRROR=https://qt-mirror.dannhauer.de

npm install @nodegui/nodegui
```

See [FAQs](https://github.com/nodegui/nodegui/tree/master/website/docs/faq.md#why-does-installation-fail-at-minimal-qt-setup) for more details.


#### Using your own custom Qt installation (Optional)

**Compiling Qt from source**

You will need to download and install Qt from source since there are no binaries from Qt for M1 yet. 

(https://www.reddit.com/r/QtFramework/comments/ll58wg/how_to_build_qt_creator_for_macos_arm64_a_guide/)

```
git clone git://code.qt.io/qt/qt5.git
cd qt5
git checkout 5.15

./init-repository --module-subset=essential -f
git submodule init qtsvg
git submodule update qtsvg

cd ..
mkdir qt5-5.15-macOS-release
cd qt5-5.15-macOS-release

../qt5/configure -release QMAKE_APPLE_DEVICE_ARCHS=arm64 -opensource -confirm-license -nomake examples -nomake tests -skip qt3d -skip webengine -skip qtactiveqt -skip qtcanvas3d  -skip qtdeclarative -skip qtdatavis3d -skip qtdoc -skip qtgamepad -skip qtcharts -skip qtgraphicaleffects -skip qtlocation  -skip qtpurchasing -skip qtquickcontrols -skip qtquickcontrols2 -skip qtremoteobjects -skip qtscxml -skip qtsensors -skip qtserialbus -skip qtserialport -skip qtspeech -skip qtvirtualkeyboard -skip qtscript

make -j15

make install
```

This should install Qt into something like this `/usr/local/Qt-5.15.3` (your directory can change. This will be displayed when running make)

**Pointing nodegui to use your custom Qt installation**

Now just set `export QT_INSTALL_DIR=<your qt path>` . In the above example it would look something like this `export QT_INSTALL_DIR=/usr/local/Qt-5.15.3`. Add this in your .zshrc or .bashrc so that you dont need to repeat this process again.

Now just `rm -rf node_modules` and do `npm install` again.

The logs should say something like `CustomQt detected at <your qt path>. Hence, skipping Mini Qt installation`.

**Community guides**

-   [Tutorial: Build a native Meme Search Desktop app with Javascript (NodeGui) and Giphy API](https://www.sitepoint.com/build-native-desktop-gif-searcher-app-using-nodegui/)
-   https://blog.logrocket.com/electron-alternatives-exploring-nodegui-and-react-nodegui/ - Electron alternatives: Exploring NodeGUI and React NodeGUI by [Siegfried Grimbeek](https://blog.logrocket.com/author/siegfriedgrimbeek/).
-   https://hibbard.eu/node-gui/ - Excellent guide from [James Hibbard](https://github.com/jameshibbard).

**Talks/Podcasts**

-   [NodeGui and React NodeGui at KarmaJS Nov 2019 meetup: https://www.youtube.com/watch?v=8jH5gaEEDv4](https://www.youtube.com/watch?v=8jH5gaEEDv4)

-   <audio data-theme="night" data-src="https://changelog.com/jsparty/96/embed" src="https://cdn.changelog.com/uploads/jsparty/96/js-party-96.mp3" preload="none" class="changelog-episode" controls></audio><p><a href="https://changelog.com/jsparty/96">JS Party 96: Performant Node desktop apps with NodeGUI</a> – Listen on <a href="https://changelog.com/">Changelog.com</a></p>

## Docs for contributing

```
It is easier than you think, try it
```

Looking to contribute? If you wish to implement a new widget/add more features and need help understanding the codebase, you can start here: [Contributing developer docs](https://github.com/nodegui/nodegui/tree/master/website/docs/development).

Please read https://github.com/nodegui/.github/blob/master/CONTRIBUTING.md

## Building

`npm run build`

Optionally set `QT_INSTALL_DIR='/path/to/qt'` environment variable to build using your own version of Qt.

## Updating docs

`npm run docs`

then followed by:

`cd website && GIT_USER=<your_git_username> yarn deploy`

## Funding

NodeGui is an open source project and requires your support. If you like this project, please consider supporting my work by clicking on the Sponsor button on this Github repository or via Ko-Fi.
Alternatively, Issues on NodeGui can be funded by anyone via Issuehunt and the amount will be distributed to respective contributors.

<p>
<a href='https://ko-fi.com/E1E510AV9' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi4.png?v=2' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a> &nbsp; &nbsp;<a href="https://issuehunt.io/r/nodegui/nodegui"><img alt="issuehunt" src="https://github.com/BoostIO/issuehunt-materials/raw/master/v1/issuehunt-button-v1.svg?sanitize=true"  height="30px" /></a>
</p>

## Special Thanks

-   [Logo: Thanks to Vishwas Shetty from the Noun Project.](https://github.com/nodegui/nodegui/blob/master/extras/legal/logo/thanks.md)

## Code of Conduct

https://github.com/nodegui/.github/blob/master/CODE_OF_CONDUCT.md

## License

MIT

## Backers 🚀

Thanks goes to these wonderful people.

<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/yazla"><img src="https://avatars1.githubusercontent.com/u/681281?s=460&v=4" width="100px;" alt="Yuriy Yazlovytskyy"/><br /><sub><b>Yuriy Yazlovytskyy</b></sub></a></td>
    <td align="center"><a href="https://github.com/johnsusek"><img src="https://avatars1.githubusercontent.com/u/611996?s=460&v=4" width="100px;" alt="John Susek"/><br /><sub><b>John Susek</b></sub></a></td>
     <td align="center"><a href="https://github.com/Spharax"><img src="https://avatars2.githubusercontent.com/u/2892381?s=460&v=4" width="100px;" alt="Marc Dijoux"/><br /><sub><b>Marc Dijoux</b></sub></a></td>
    <td align="center"><a href="https://github.com/Qard"><img src="https://avatars2.githubusercontent.com/u/205482?s=460&v=4" width="100px;" alt="Stephen Belanger"/><br /><sub><b>Stephen Belanger</b></sub></a></td>
     <td align="center"><a href="https://github.com/irustm"><img src="https://avatars3.githubusercontent.com/u/16316579?s=460&v=4" width="100px;" alt="Rustam"/><br /><sub><b>Rustam</b></sub></a></td>
  </tr>
</table>

## Maintainers ✨

People maintaining this project.

<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://blog.atulr.com"><img src="https://avatars2.githubusercontent.com/u/4029423?v=4" width="100px;" alt="Atul R"/><br /><sub><b>Atul R</b></sub></a></td>
    <td align="center"><a href="https://github.com/sedwards2009"><img src="https://avatars.githubusercontent.com/u/6926644?v=4" width="100px;" alt="Simon Edwards"/><br /><sub><b>Simon Edwards</b></sub></a></td>
  </tr>
</table>

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://lramage.gitlab.io"><img src="https://avatars1.githubusercontent.com/u/43783393?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lucas Ramage</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=oxr463" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/gamtiq"><img src="https://avatars3.githubusercontent.com/u/1177323?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Denis Sikuler</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=gamtiq" title="Documentation">📖</a></td>
    <td align="center"><a href="https://twitter.com/nahueljo"><img src="https://avatars1.githubusercontent.com/u/1612488?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nahuel José</b></sub></a><br /><a href="#question-Naahuel" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/kakulgupta"><img src="https://avatars3.githubusercontent.com/u/10727047?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Kakul Gupta</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=kakulgupta" title="Code">💻</a></td>
    <td align="center"><a href="http://rahulgaba.com"><img src="https://avatars3.githubusercontent.com/u/7898942?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rahul Gaba</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=rgabs" title="Code">💻</a></td>
    <td align="center"><a href="http://uriziel.pl"><img src="https://avatars1.githubusercontent.com/u/568207?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Paweł Borecki</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=Uriziel01" title="Code">💻</a></td>
    <td align="center"><a href="http://marcus-sa.me"><img src="https://avatars0.githubusercontent.com/u/8391194?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Marcus S. Abildskov</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=marcus-sa" title="Tests">⚠️</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://www.mad3linux.org"><img src="https://avatars3.githubusercontent.com/u/508624?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Átila Camurça Alves</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=atilacamurca" title="Documentation">📖</a></td>
    <td align="center"><a href="http://hibbard.eu"><img src="https://avatars2.githubusercontent.com/u/1940994?v=4?s=100" width="100px;" alt=""/><br /><sub><b>James Hibbard</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=jameshibbard" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/soonoo"><img src="https://avatars2.githubusercontent.com/u/5436405?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Soonwoo Hong</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=soonoo" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/illBeRoy"><img src="https://avatars2.githubusercontent.com/u/6681893?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Roy Sommer</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=illBeRoy" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/paulocoghi"><img src="https://avatars1.githubusercontent.com/u/378397?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Paulo Coghi</b></sub></a><br /><a href="#ideas-paulocoghi" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://balthild.com"><img src="https://avatars2.githubusercontent.com/u/2662758?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Balthild Ires</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=balthild" title="Code">💻</a></td>
    <td align="center"><a href="https://dimitarnestorov.com"><img src="https://avatars0.githubusercontent.com/u/8790386?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dimitar Nestorov</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=dimitarnestorov" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.greatapes.fi"><img src="https://avatars3.githubusercontent.com/u/3404389?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mikko Sairio</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=msairio" title="Code">💻</a></td>
    <td align="center"><a href="http://blog.pepf.nl"><img src="https://avatars1.githubusercontent.com/u/1265435?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Pepijn</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=pepf" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/slidinghotdog"><img src="https://avatars3.githubusercontent.com/u/33790211?v=4?s=100" width="100px;" alt=""/><br /><sub><b>slidinghotdog</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=slidinghotdog" title="Code">💻</a></td>
    <td align="center"><a href="http://www.bundyo.org"><img src="https://avatars1.githubusercontent.com/u/98318?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Bundyo (Kamen Bundev)</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=bundyo" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/feng8848"><img src="https://avatars2.githubusercontent.com/u/40539968?v=4?s=100" width="100px;" alt=""/><br /><sub><b>feng8848</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=feng8848" title="Code">💻</a></td>
    <td align="center"><a href="https://karelov.info"><img src="https://avatars3.githubusercontent.com/u/2384454?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maksim Karelov</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=Ty3uK" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mspencer92"><img src="https://avatars2.githubusercontent.com/u/1910455?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mspencer92</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=mspencer92" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/blncd2020"><img src="https://avatars1.githubusercontent.com/u/59541979?v=4?s=100" width="100px;" alt=""/><br /><sub><b>blncd2020</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=blncd2020" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/gluaxspeed"><img src="https://avatars2.githubusercontent.com/u/16431709?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gluaxspeed</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=gluaxspeed" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Solant"><img src="https://avatars2.githubusercontent.com/u/5971578?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Solant</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=Solant" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/shubhamzanwar"><img src="https://avatars0.githubusercontent.com/u/15626155?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Shubham Zanwar</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=shubhamzanwar" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Singha360"><img src="https://avatars1.githubusercontent.com/u/35334787?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Singha360</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=Singha360" title="Code">💻</a></td>
    <td align="center"><a href="http://wellenline.com"><img src="https://avatars3.githubusercontent.com/u/3790782?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mihkel</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=MihkelBaranov" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/stevo2588"><img src="https://avatars1.githubusercontent.com/u/3278045?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Stephen A</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=stevo2588" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://liujunjiang.com"><img src="https://avatars1.githubusercontent.com/u/15191056?v=4?s=100" width="100px;" alt=""/><br /><sub><b>流君酱</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=jardenliu" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/agg23"><img src="https://avatars1.githubusercontent.com/u/238679?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adam Gastineau</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=agg23" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/swittk"><img src="https://avatars2.githubusercontent.com/u/5000572?v=4?s=100" width="100px;" alt=""/><br /><sub><b>swittk</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=swittk" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/craftingmod"><img src="https://avatars2.githubusercontent.com/u/9389278?v=4?s=100" width="100px;" alt=""/><br /><sub><b>craftingmod</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=craftingmod" title="Code">💻</a></td>
    <td align="center"><a href="http://www.m2osw.com"><img src="https://avatars1.githubusercontent.com/u/643129?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Doug Barbieri</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=dooglio" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/NeryHenrique"><img src="https://avatars0.githubusercontent.com/u/6879141?v=4?s=100" width="100px;" alt=""/><br /><sub><b>HENRIQUE DE SOUZA NERY</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=NeryHenrique" title="Code">💻</a></td>
    <td align="center"><a href="https://ruslang.xyz"><img src="https://avatars0.githubusercontent.com/u/25264730?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ruslan Garifullin</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=ruslang02" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/ran-j"><img src="https://avatars0.githubusercontent.com/u/17410205?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ranieri</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=ran-j" title="Code">💻</a> <a href="https://github.com/nodegui/nodegui/commits?author=ran-j" title="Documentation">📖</a></td>
    <td align="center"><a href="https://master-technology.com"><img src="https://avatars3.githubusercontent.com/u/850871?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nathanael Anderson</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=NathanaelA" title="Code">💻</a></td>
    <td align="center"><a href="https://ubiq.co.za"><img src="https://avatars0.githubusercontent.com/u/4415071?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ross</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=rocbear" title="Code">💻</a> <a href="https://github.com/nodegui/nodegui/commits?author=rocbear" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/4h7l"><img src="https://avatars.githubusercontent.com/u/69183283?v=4?s=100" width="100px;" alt=""/><br /><sub><b>4h7l</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=4h7l" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Maks-s"><img src="https://avatars.githubusercontent.com/u/26678512?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Maks</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=Maks-s" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/zhb124404"><img src="https://avatars.githubusercontent.com/u/16805041?v=4?s=100" width="100px;" alt=""/><br /><sub><b>zhb124404</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=zhb124404" title="Documentation">📖</a></td>
    <td align="center"><a href="http://www.apsis.io"><img src="https://avatars.githubusercontent.com/u/579688?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Wyatt Kirby</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=wkirby" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://stvkoch.github.io."><img src="https://avatars.githubusercontent.com/u/14454?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Steven Koch</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=stvkoch" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sedwards2009"><img src="https://avatars.githubusercontent.com/u/6926644?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Simon Edwards</b></sub></a><br /><a href="https://github.com/nodegui/nodegui/commits?author=sedwards2009" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
