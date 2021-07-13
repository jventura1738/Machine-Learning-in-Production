# OpenMTP | Android File Transfer for macOS

- Author: [Ganesh Rathinavel](https://www.linkedin.com/in/ganeshrvel "Ganesh Rathinavel")
- License: [MIT](https://github.com/ganeshrvel/openmtp/blob/master/LICENSE "MIT")
- System Requirements: macOS 10.11 or higher
- Website URL: [https://openmtp.ganeshrvel.com](https://openmtp.ganeshrvel.com/ "https://openmtp.ganeshrvel.com")
- Repo URL: [https://github.com/ganeshrvel/openmtp](https://github.com/ganeshrvel/openmtp/ "https://github.com/ganeshrvel/openmtp")
- Contacts: ganeshrvel@outlook.com


## Introduction

### Advanced Android File Transfer Application for macOS.

Transferring files between macOS and Android or any other MTP devices has always been a nightmare. There are a few File Transfer MTP apps which are available online but most of them are either too expensive or come with bad UI/UX. The official "Android File Transfer" app for macOS from Google comes with bugs, innumerable limitations, some of which include - not being able to transfer files larger than 4GB, frequent disconnections, unable to rename the folders or files on the android/MTP devices. Most of the other apps available online uses either WiFi or ADB protocol to transfer the files, which is an extremely time-consuming process.

Countless searches to find an app to solve these problems and failing to find one made me restless. So, I took the leap and decided to create an app for us that could help us have a smooth and hassle-free file transfer process from macOS to Android/MTP devices. Created with the objective of giving back to the community, we can all use this app for free in this lifetime.

### Features
- Safe, Transparent and Open-Source
- Plug and Play via USB. No hassles, easy and instant connection.
- Select between Internal Memory and SD Card
- Transfer multiple files which are larger than 4GB
- Dark mode
- Drag-and-drop support
- Split pane views for both Local Computer and Android device
- Choose between Grid and List view.
- Use Keyboard Shortcuts to navigate through your files.
- No collection of personally identifiable information.


### Kalam Kernel
OpenMTP 3.0 features a new MTP kernel and it was written from the scratch. It promises a file copy speed of 30 to 40 MB/s on low and mid range devices and 100 to 120 MB/s on higher end devices. The all new and powerful MTP kernel is named after [Dr. A. P. J. Abdul Kalam](https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam "Dr. A. P. J. Abdul Kalam")

Do checkout the Go package which I've written to build Kalam Kernel: [github.com/ganeshrvel/go-mtpx](https://github.com/ganeshrvel/go-mtpx "https://github.com/ganeshrvel/go-mtpx"). Feel free to raise PRs.

### Installation
* Download the [Latest Version](https://openmtp.ganeshrvel.com/?downloadApp=github&release=stable&platform=mac 'Latest Version')

* Using Homebrew Cask
```shell
  # newer versions:
  brew install openmtp --cask
  # older versions:
  brew cask install openmtp
```


* Find the latest *dmg* file from [GitHub Releases](https://github.com/ganeshrvel/openmtp/releases "GitHub Releases")

### Screengrabs

![OpenMTP File Explorer](https://github.com/ganeshrvel/openmtp/raw/master/blobs/images/file-explorer-bluebg.jpg "OpenMTP File Explorer")

![OpenMTP File Transfer](https://github.com/ganeshrvel/openmtp/raw/master/blobs/images/file-transfer-bluebg.jpg "OpenMTP File Transfer")

### Keyboard Shortcuts
| Command                                           | Keyboard Shortcut                                            |
| ------------------------------------------------- | ------------------------------------------------------------ |
| Delete                                            | <kbd>backspace</kbd>                                         |
| New Folder                                        | <kbd>command (⌘)</kbd>+<kbd>n</kbd>                          |
| Copy                                              | <kbd>command (⌘)</kbd>+<kbd>c</kbd>                          |
| Copy to Queue                                     | <kbd>command (⌘)</kbd>+<kbd>shift</kbd>+<kbd>c</kbd>         |
| Paste                                             | <kbd>command (⌘)</kbd>+<kbd>v</kbd>                          |
| Refresh                                           | <kbd>command (⌘)</kbd> +<kbd>r</kbd>                         |
| Folder Up                                         | <kbd>command (⌘)</kbd>+<kbd>b</kbd>                          |
| Select All                                        | <kbd>command (⌘)</kbd>+<kbd>a</kbd>                          |
| Rename                                            | <kbd>command (⌘)</kbd>+<kbd>d</kbd>                          |
| Switch Tab                                        | <kbd>command(⌘)</kbd>+<kbd>1</kbd>                           |
| Open                                              | <kbd>enter</kbd>                                             |
| Navigate Left                                     | <kbd>left</kbd>                                              |
| Navigate Right                                    | <kbd>right</kbd>                                             |
| Navigate Up                                       | <kbd>up</kbd>                                                |
| Navigate Down                                     | <kbd>down</kbd>                                              |
| Select Multiple Items Forward **(in Grid View)**  | <kbd>shift</kbd>+<kbd>left</kbd>                             |
| Select Multiple Items Backward **(in Grid View)** | <kbd>shift</kbd>+<kbd>right</kbd>                            |
| Select Multiple Items Forward **(in List View)**  | <kbd>shift</kbd>+<kbd>up</kbd>                               |
| Select Multiple Items Backward **(in List View)** | <kbd>shift</kbd>+<kbd>down</kbd>                             |
| Select Multiple Items **(with mouse)**            | <kbd>command (⌘)</kbd>+<kbd>click</kbd> or <kbd>shift</kbd>+<kbd>click</kbd> |

## Building from Source

Requirements: [Node.js v10](https://nodejs.org/en/download/ "Install Node.js v10"), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "Install Git") and [Yarn package manager](https://yarnpkg.com/lang/en/docs/install/ "Install Yarn package manager")


### Clone
```shell
$ git clone --depth 1 --single-branch --branch master https://github.com/ganeshrvel/openmtp.git

$ cd openmtp
```

```shell
$ yarn
```

### Run
A fresh clone might throw *undefined state* error. Run the following commands once to fix the issue.

```shell
# For Mac and Linux
$ UPGRADE_EXTENSIONS=1 npm run dev

# For Windows
$ set UPGRADE_EXTENSIONS=1 && npm run dev
```

```shell
# Development
$ yarn dev

# Pre-production
$ yarn start

```

### Package

Setup the *code signing* to build, package and publish the app.

**App Notarization for macOS** (skip this section for non macOS builds)
- Rename *sample.env* file as *.env*
- Update APPLEID in *.env* file
- Log into your [Apple Account](https://appleid.apple.com/account/manage "Apple Account")
- Goto **Security > App-Specific Passwords**
- Click on **Generate Password...**, enter a password label and click *Create*
- Copy the displayed *app-specific-password*
- Run
```shell
security add-generic-password -a "<apple-developer-account-username>" -w <app-specific-password*> -s "ELECTRON_NOTORIZE_PASSWORD"
```

- Log into your [Apple App Store Connect Account](https://appstoreconnect.apple.com/agreements/# "Apple App Store Connect Account") and accept the presented terms and conditions
- The statuses shall turn *Active*

**Sentry**

```shell
npm install -g @sentry/wizard
sentry-wizard --integration electron

# Upload Debug Information
# Everytime the electron.js version is upgraded run:
node sentry-symbols.js

sentry-cli login
```

**Packaging**
Instructions: [https://www.electron.build/code-signing](https://www.electron.build/code-signing "https://www.electron.build/code-signing")

```shell
$ export GH_TOKEN="<github token>"
```

```shell
# For local platform
$ yarn package

# For multiple platforms
$ yarn package-all
```


### Technical Features
- Built using Electron v11 and React v17
- Loadables, Dynamic Reducer Injection, Selectors for code splitting and performance optimization
- Hot module reload (HMR) for instant feedback
- Inbuilt error logging and profile/settings management
- Industry standard state management
- JSS, SASS/SCSS styling
- Port assigned: **4642**

### Configurations
- *config/env/env.dev.js* and *config/env/env.prod.js* contain the PORT number of the app.
- *config/dev-app-update.yml* file holds the GitHub repo variables required by *electron-updater*.
- *config/google-analytics-key.js* file contains the Google Analytics Tracking ID.
- *package.json* **build.publish** object holds the values for publishing the packaged application.
- *app/constants* folder contains all the constants required by the app.

### Debugging

#### **Debugging Guide**

[https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/400](https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/400 "Debugging Guide")

#### **Dispatching redux actions from the main process**

[https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/118](https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/118 "https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/118")

[https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/108](https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/108 "https://github.com/electron-react-boilerplate/electron-react-boilerplate/issues/108")

#### **VM112:2 Uncaught TypeError: Cannot read property 'state' of undefined error**

```shell
# For Mac and Linux
$ UPGRADE_EXTENSIONS=1 npm run dev

# For Windows
$ set UPGRADE_EXTENSIONS=1 && npm run dev
```

### Troubleshooting
#### Your device is not recognized
- Raise an issue if your device is undetected: https://github.com/ganeshrvel/openmtp/issues/new?template=contribute.md
#### The app goes blank while trying to connect a Samsung device
- Uninstall Samsung SmartSwitch, if installed: [https://farazfazli.medium.com/how-i-reverse-engineered-keis-and-sidesync-and-fixed-mtp-8949acbb1c29](https://farazfazli.medium.com/how-i-reverse-engineered-keis-and-sidesync-and-fixed-mtp-8949acbb1c29 "https://farazfazli.medium.com/how-i-reverse-engineered-keis-and-sidesync-and-fixed-mtp-8949acbb1c29"), [https://github.com/ganeshrvel/openmtp/issues/212](https://github.com/ganeshrvel/openmtp/issues/212 "https://github.com/ganeshrvel/openmtp/issues/212").

#### **Notarizing Electron apps throws - “You must first sign the relevant contracts online. (1048)” error**

[https://stackoverflow.com/questions/58358449/notarizing-electron-apps-throws-you-must-first-sign-the-relevant-contracts-on](https://stackoverflow.com/questions/58358449/notarizing-electron-apps-throws-you-must-first-sign-the-relevant-contracts-on "https://stackoverflow.com/questions/58358449/notarizing-electron-apps-throws-you-must-first-sign-the-relevant-contracts-on")

### More repos

- [npm: electron-root-path](https://github.com/ganeshrvel/npm-electron-root-path "Get the root path of an Electron Application")
- [Electron React Redux Advanced Boilerplate](https://github.com/ganeshrvel/electron-react-redux-advanced-boilerplate "Electron React Redux advanced boilerplate")
- [Tutorial Series by Ganesh Rathinavel](https://github.com/ganeshrvel/tutorial-series-ganesh-rathinavel "Tutorial Series by Ganesh Rathinavel")

### Credits

- Thanks to Ms [Ayushi Bothra](https://www.linkedin.com/in/ayushi-bothra-3103/ "Ayushi Bothra") for contributing to the documentation and pages.

- App logo was contributed by [Shubhendu Mitra](https://www.linkedin.com/in/shubhendum/ "Shubhendu Mitra - LinkedIn"). Make sure to check out more of his works on [Behance](https://www.behance.net/soponhara "Shubhendu Mitra - Behance").

- Thanks to [Vladimir Menshakov](https://github.com/whoozle "Vladimir Menshakov") for [android-file-transfer-linux](https://github.com/whoozle/android-file-transfer-linux "android-file-transfer-linux") (the MTP legacy Kernel)

- Shoutout to [@yennsarah](https://github.com/yennsarah "yennsarah"), [@h0tk3y](https://github.com/h0tk3y), [@riginoommen](https://github.com/riginoommen "riginoommen"), [@AjithKumarvm](https://github.com/AjithKumarvm "AjithKumarvm"), [@kiranshaji555](https://github.com/kiranshaji555), Dick Cowan, Kjell Dankert, Thorolf E.R. Weißhuhn and to all other community members who helped me test the application.

- This app was built upon [https://github.com/ganeshrvel/electron-react-redux-advanced-boilerplate](https://github.com/ganeshrvel/electron-react-redux-advanced-boilerplate "https://github.com/ganeshrvel/electron-react-redux-advanced-boilerplate") which is a heavily modified fork of [https://github.com/electron-react-boilerplate/electron-react-boilerplate](https://github.com/electron-react-boilerplate/electron-react-boilerplate "https://github.com/electron-react-boilerplate/electron-react-boilerplate").

- The icons used in the app were made by [flaticon](https://www.flaticon.com), [good-ware](https://www.flaticon.com/authors/good-ware) and [kiranshastry](https://www.flaticon.com/authors/kiranshastry) which is licensed under [CC 3.0 BY](https://creativecommons.org/licenses/by/3.0/ "Creative Commons BY 3.0").

- The "no image found" icon was made by [Phonlaphat Thongsriphong](https://www.iconfinder.com/phatpc "Phonlaphat Thongsriphong").


### Contribute
If you are interested in fixing issues and contributing directly to the code base, please see the [guidelines](https://github.com/ganeshrvel/openmtp/blob/master/CONTRIBUTING.md "guidelines").

### Support OpenMTP
Help me keep the app FREE and open for all.
- Donate Via PayPal: [paypal.me/ganeshrvel](https://paypal.me/ganeshrvel "https://paypal.me/ganeshrvel")
- Buy Me A Coffee (UPI, PayPal, Credit/Debit Cards, Internet Banking): [buymeacoffee.com/ganeshrvel](https://buymeacoffee.com/ganeshrvel "https://buymeacoffee.com/ganeshrvel")

### Contacts
Please feel free to contact me at ganeshrvel@outlook.com

### License
OpenMTP | Android File Transfer for macOS is released under [MIT License](https://github.com/ganeshrvel/openmtp/blob/master/LICENSE "MIT License").

Copyright © 2018-Present Ganesh Rathinavel
