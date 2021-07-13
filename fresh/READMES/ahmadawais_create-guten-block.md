<h4 align="center">
    <a href="https://github.com/ahmadawais/create-guten-block">
        <img src="https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/cgb.png" alt="create-guten-block" />
    </a><br><br><br><a href="https://github.com/ahmadawais/create-guten-block">
        <img src="https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/cgblogo.png" alt="create-guten-block" />
    </a><br><br>


`create-guten-block` is _zero configuration dev-toolkit_ (#0CJS) to develop WordPress Gutenberg blocks in a matter of minutes without configuring `React`, `webpack`, `ES6/7/8/Next`, `ESLint`, `Babel`, etc.
	
[![DOWNLOADS](https://img.shields.io/npm/dt/create-guten-block?label=DOWNLOADS%20%20%E2%9D%AF&colorA=216AFF&colorB=216AFF&style=flat)](https://www.npmjs.com/package/create-guten-block) [![Learn Node.js CLI Automation](https://img.shields.io/badge/-NodeCLI.com%20%E2%86%92-gray.svg?colorB=216AFF&style=flat)](https://nodecli.com/?utm_source=GitHubFOSS) [![Follow @MrAhmadAwais on Twitter](https://img.shields.io/badge/FOLLOW%20@MRAHMADAWAIS%20%E2%86%92-gray.svg?colorA=216AFF&colorB=216AFF&style=flat)](https://twitter.com/mrahmadawais/)

</h4>
<br>

# 📦 `create-guten-block`

>`create-guten-block` is _zero configuration dev-toolkit_ (#0CJS) to develop WordPress Gutenberg blocks in a matter of minutes without configuring `React`, `webpack`, `ES6/7/8/Next`, `ESLint`, `Babel`, etc.

Create Guten Block is not like other [starter-kits](https://github.com/ahmadawais/wpgulp) or [boilerplates](https://github.com/ahmadawais/Gutenberg-boilerplate). It's a developer's toolbox which is continuously updated. Since it has zero-configuration, you can always update it without any changes in your code.

`create-guten-block` is:

- 🥞 Versioned ✓
- 🤠 Updatable ✓
- 🗃 Set of sane-defaults ✓
- 🐎 ONE single `cgb-scripts` dependency ✓
- 💯 [100s of WordPress plugins built with `create-guten-block`](plugins.md) ✓

<br>

[![Start](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/rocket.png)](/)

## GETTING STARTED!

Let's create a WordPress block plugin...

#### ⚡️ Quick Overview

Run step `#1` and `#2` quickly in one go — Run inside local WP install   E.g. `/wp.local/wp-content/plugins/` directory.

```sh
npx create-guten-block my-block
cd my-block
npm start
```

([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) comes with npm 5.2+ and higher, see [instructions for older npm versions](https://gist.github.com/ahmadawais/e4c69b22561c7079c9d99faba90e3b23))

> 🎛   _If you want to study the detailed installation of step `#1` and `#2` — then take a look at the steps below_.

<details>
 <summary><strong> STEP #0</strong> — Don't have <code>Node.js</code> + <code>npm</code> installed? Read this. (CLICK TO EXPAND!)</summary>

In case you are an absolute beginner to the world of `Node.js`, JavaScript, and `npm` packages — all you need to do is go to the Node's site [download + install](https://nodejs.org/en/download/) Node on your system. This will install both `Node.js` and `npm`, i.e., node package manager — the command line interface of Node.js.

You can verify the install by opening your terminal app and typing...

```sh
node -v
# Results into v9.1.0 — make sure you have Node >= 8 installed.

npm -v
# Results into 5.6.0 — make sure you have npm >= 5.3 installed.
```

</details>

### → STEP #1

All you have to do is run the following command and it will create a WordPress block plugin. It's done by installing and running the `create-guten-block` command and providing it with a unique name for a WordPress plugin that will get created.

> ⚠️ Make sure run this command in your local WordPress install's plugins folder i.e. `/local_dev_site.tld/wp-content/plugins/` folder — since this command will produce a WordPress plugin that you can go to `WP Admin` ▶︎ `Plugins` to activate.

```sh
npx create-guten-block my-block
```

([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) comes with npm 5.2+ and higher, see [instructions for older npm versions](https://gist.github.com/ahmadawais/e4c69b22561c7079c9d99faba90e3b23))

[![npx block](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/cgb1.gif)](/)

_It'll take a couple of minutes to install._

>You’ll need to have Node >= 8 and npm >= 5.3 on your local development machine (but it’s not required on the server). You can use [nvm](https://github.com/creationix/nvm#installation) (macOS/Linux) or [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) to easily switch Node versions between different projects.

It will create a directory called `my-block` inside the current folder.
Inside that directory, it will generate the initial project structure and install the transitive dependencies:

```sh
INSIDE: /local_dev_site.tld/wp-content/plugins/my-block

├── .gitignore
├── plugin.php
├── package.json
├── readme.md
|
├── dist
|  ├── blocks.build.js
|  ├── blocks.editor.build.css
|  └── blocks.style.build.css
|
└── src
   ├── block
   |  ├── block.js
   |  ├── editor.scss
   |  └── style.scss
   |
   ├── blocks.js
   ├── common.scss
   └── init.php
```

No configuration or complicated folder structures, just the files you need to build your app.

### → STEP #2

Once the installation is done, you can open your project folder and run the start script.

_Let's do that._

```sh
cd my-block
npm start
```

_You can also use `yarn start` if that's your jam_.

[![cgb-npm-start](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/cgb2.gif)](/)

This runs the plugin in development mode. To produce production code run `npm run build`.
You will see the build messages, errors, and lint warnings in the console.

>And just like that, you're building your next WordPress plugin with Gutenberg, React.js, ES 6/7/8/Next, transpiled with Babel, which also has ESLint configurations for your code editor to pick up and use automatically.

<br>

[![More](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/workflow.png)](/)

### Workflow!

There are just three scripts that you can use in your `create-guten-block` workflow. With these three scripts, you can develop, build, and eject your plugin.

#### 👉  `npm start`

- Use to compile and run the block in development mode.
- Watches for any changes and reports back any errors in your code.

#### 👉  `npm run build`

- Use to build production code for your block inside `dist` folder.
- Runs once and reports back the gzip file sizes of the produced code.

#### 👉  `npm run eject`

- Use to eject your plugin out of `create-guten-block`.
- Provides all the configurations so you can customize the project as you want.
- It's a one-way street, `eject` and you have to maintain everything yourself.
- You don't normally have to `eject` a project because by ejecting you lose the connection with `create-guten-block` and from there onwards you have to update and maintain all the dependencies on your own.

_That's about it._

<br>

[![included](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/included.png)](/)

## What’s Included?

Your environment will have everything you need to build a modern next-gen WordPress Gutenberg plugin:

- React, JSX, and ES6 syntax support.
- webpack dev/production build process behind the scene.
- Language extras beyond ES6 like the object spread operator.
- Auto-prefixed CSS, so you don’t need `-webkit` or other prefixes.
- A build script to bundle JS, CSS, and images for production with source-maps.
- Hassle-free updates for the above tools with a single dependency `cgb-scripts`.

The tradeoff is that **these tools are preconfigured to work in a specific way**. If your project needs more customization, you can ["eject"](https://github.com/ahmadawais/create-guten-block#--npm-run-eject) and customize it, but then you will need to maintain this configuration.

<br>

[![Philosophy](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/philosophy.png)](/)

## Philosophy

- **One Dependency:** There is just one build dependency. It uses webpack, Babel, ESLint, and other amazing projects, but provides a cohesive curated experience on top of them.

- **No Configuration Required:** You don't need to configure anything. A reasonably good configuration of both development and production builds is handled for you so you can focus on writing code.

- **No Lock-In:** You can `eject` to a custom setup at any time. Run a single command, and all the configuration and build dependencies will be moved directly into your project, so you can pick up right where you left off.

<br>

[![Why](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/why.png)](/)

## Why `create-guten-block`?

Well, it's really hard to configure things like webpack, React, ES 6/7/8/Next, ESLint, Babel, etc. before you even start writing a Hello World Gutenberg block. Then there's the fact that you have to maintain and constantly update your configuration with all the new tools and growth in the JavaScript community.

`create-guten-block` hides all this configuration away in an optimized package that we call `cgb-scripts`. This package is the only dependency in your projects. We keep `cgb-scripts` up to date while you go ahead and create the next best WordPress themes and plugins.

<br>

[![tldr](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/tldr.png)](/)

## TL;DR

>Too long, didn't read? Here's a shorter version.

Open the terminal app and run the following commands.

- 🔰 **Install/Create**: `npx create-guten-block my-block` — Run inside local WP install   E.g. `/wp.local/wp-content/plugins/` directory.
- 📂 **Browse**: `cd my-block` — Open the newly created plugin directory.
- ♻️ **Run**: `npm start` — For development.
- 📦 **Run**: `npm run build` — For production build.
- ⏏ **Run**: `npm run eject` — To customize, update, and maintain all by yourself.

Create-Guten-Block has been tested to work on macOS, but must also work on Windows, and Linux.
If something doesn’t work, kindly file [an issue →](https://github.com/ahmadawais/create-guten-block/issues/new)

<!-- [![Create-guten-block](https://on.ahmda.ws/okiU/c)](/) -->

<br>

[![update](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/update.png)](/)

## Updating to New Releases

Create Guten Block is divided into two packages:

1. **`create-guten-block`** is a command-line utility that you use to create new WP Gutenberg plugins.
1. **`cgb-scripts`** is a development dependency in the generated plugin projects.

You never need to update `create-guten-block` itself as it's run via [`npx`](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) and it delegates all the setup to `cgb-scripts`.

When you run `create-guten-block`, it always creates the project with the latest version of `cgb-scripts` so you’ll get all the new features and improvements in newly created plugins automatically.

To update an existing project to a new version of `cgb-scripts`, open the [changelog](https://github.com/ahmadawais/create-guten-block#changelog), find the version you’re currently on (check package.json in your plugin's folder if you’re not sure), and apply the migration instructions for the newer versions.

In most cases bumping the `cgb-scripts` version in package.json and running `npm install` in this folder should be enough, but it’s good to consult the [changelog](https://github.com/ahmadawais/create-guten-block#changelog) for potential breaking changes.

We commit to keeping the breaking changes minimal so you can upgrade `cgb-scripts` painlessly.

<br>

[![Log](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/changelog.png)](/)

## Changelog

Read what's 📦 new, 👌 improved, 🐛 fixed, and  if 📖 docs got updated.

👉 Go read the entire changelog at this link — [CGB Changelog →](https://github.com/ahmadawais/create-guten-block/blob/master/changelog.md)

Nothing's ever complete, so bear with us while we keep iterating towards a better future.

> ```html
> 'Coz every night I lie in bed
> The brightest colors fill my head
> A million dreams are keeping me awake
> I think of what the world could be
> A vision of the one I see
> A million dreams is all it's gonna take
> A million dreams for the world we're gonna make ...
> ```
> ... _listen to → [A million dreams!](https://www.youtube.com/watch?v=pSQk-4fddDI)_

<br>

[![Hello](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/hello.png)](/)

#### **Hello, we're [The Dev Couple](https://TheDevCouple.com)**!

Me ([Ahmad Awais](https://twitter.com/mrahmadawais/)) and my incredible wife ([Maedah Batool](https://twitter.com/MaedahBatool/)) are two engineers who fell in love with open source and then with each other. You can read more [about me here](https://ahmadawais.com/about). If you or your company use any of my projects or like what I’m doing then consider backing me. I'm in this for the long run. An open-source developer advocate.

[![Ahmad on Twitter](https://img.shields.io/twitter/follow/mrahmadawais.svg?style=social&label=Follow%20@MrAhmadAwais)](https://twitter.com/mrahmadawais/)

### [NodeCLI.com][n] — Learn to build Node.js CLI Automation

> This repository is part of the [NodeCLI.com][n] course.

After building hundreds of developer automation tools used by millions of developers, I am sharing exactly how you can do it yourself with minimum effective effort. Learn to build Node.js & JavaScript based CLI (Command Line Interface) apps. Automate the grunt work, do more in less time, impress your manager, and help the community.
→ I'm sharing it all in this online video course. [Node CLI Automation
without wasting a 1,000 hours][n] →</p>

[![Node CLI](https://img.shields.io/badge/-NodeCLI.com%20%E2%86%92-gray.svg?colorB=488640&style=flat)][n]

[n]: https://NodeCLI.com?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block

[![Awais on Twitter](https://raw.githubusercontent.com/ahmadawais/stuff/master/sponsor/sponsor.jpg)](https://github.com/AhmadAwais/sponsor)

<br>

[![Partners](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/backers.png)](/)

### Project Backers & [TheDevCouple Partners](https://TheDevCouple.com/partners) ⚡️

This FOSS (free and open source software) project is updated and maintained with the help of awesome businesses listed below. Without the support from these amazing companies/individuals, this project would not have been possible.

— _What/How? [Read more about it →](https://TheDevCouple.com/partners)_

<table width='100%'>
	<tr>
		<td width='500'><a target='_blank' href='https://Awais.dev/kinsta'><img src='https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/kinsta.png' /></a></td>
		<td width='500'><a target='_blank' href='https://mythemeshop.com/?utm_source=TheDevCouple&utm_medium=Partner'><img src='https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/mts.png' /></a></td>
	</tr>
	
</table>

<br>

[![Thanks](https://raw.githubusercontent.com/ahmadawais/stuff/master/fix/license.png)](/)

## License & Attribution

- MIT © [Ahmad Awais](https://twitter.com/MrAhmadAwais/).
- [Code of Conduct](code-of-conduct.md).

<div align="left">
    <p><a href="https://github.com/ahmadawais"><img alt="GitHub @AhmadAwais" align="center" src="https://img.shields.io/badge/GITHUB-gray.svg?colorB=6cc644&colorA=6cc644&style=flat" /></a>&nbsp;<small><strong>(follow)</strong> TO STAY UP TO DATE ON FREE & OPEN SOURCE SOFTWARE</small></p>
    <p><a href="https://twitter.com/MrAhmadAwais/"><img alt="Twitter @MrAhmadAwais" align="center" src="https://img.shields.io/badge/TWITTER-gray.svg?colorB=1da1f2&colorA=1da1f2&style=flat" /></a>&nbsp;<small><strong>(follow)</strong> TO GET ONE DEV MINUTE DAILY HOT TIPS & TROLLS</small></p>
    <p><a href="https://www.youtube.com/AhmadAwais"><img alt="YouTube AhmadAwais" align="center" src="https://img.shields.io/badge/YOUTUBE-gray.svg?colorB=ff0000&colorA=ff0000&style=flat" /></a>&nbsp;<small><strong>(subscribe)</strong> TO TECH TALKS & ONE DEV MINUTE VIDEOS</small></p>
    <p><a href="https://AhmadAwais.com/"><img alt="Blog: AhmadAwais.com" align="center" src="https://img.shields.io/badge/MY%20BLOG-gray.svg?colorB=4D2AFF&colorA=4D2AFF&style=flat" /></a>&nbsp;<small><strong>(read)</strong> MOSTLY LONG FORM TECHNICAL ARTICLES</small></p>
    <p><a href="https://www.linkedin.com/in/MrAhmadAwais/"><img alt="LinkedIn @MrAhmadAwais" align="center" src="https://img.shields.io/badge/LINKEDIN-gray.svg?colorB=0077b5&colorA=0077b5&style=flat" /></a>&nbsp;<small><strong>(connect)</strong> WITH THE LINKEDIN PROFILE Y'ALL</small></p>
</div>

This project is inspired by the work of more people than I could mention here. But thank you, [Dan Abramov](https://twitter.com/dan_abramov) for Create React App, [Andrew Clark](https://twitter.com/acdlite), and [Christopher Chedeau](https://twitter.com/vjeux), [Sophie Alpert](https://twitter.com/sophiebits) from React.js team, [Kent C. Dodds](https://twitter.com/kentcdodds) for his open source evangelism, WordPress Core Contributors, [Gary](https://twitter.com/GaryPendergast) for keeping everyone sane, [Gutenberg](https://github.com/wordpress/gutenberg) developers [Matias](https://twitter.com/matias_ventura), [Riad](https://github.com/youknowriad), [Andrew](https://github.com/aduth), [Ella](https://twitter.com/ellaiseulde), [Joen](https://github.com/jasmussen), [Tammie](https://twitter.com/karmatosed), [Greg](https://twitter.com/gziolo) and contributors, and other WordPress community members like [Zac](https://twitter.com/zgordon) for his [course on Gutenberg](https://ahmda.ws/ZacGutenbergCourse), and also my friend [Morten](https://twitter.com/mor10) for all the #Guten-motivation, [Icons8](https://icons8.com/) for the awesome icons, [Maedah](https://twitter.com/MaedahBatool/) for managing this project, and to everyone I forgot.

_Follow me 👋 on Twitter for more updates and questions_ →  [![Tweet to say Hi](https://img.shields.io/twitter/follow/mrahmadawais.svg?style=social&label=Tweet%20@MrAhmadAwais)](https://twitter.com/mrahmadawais/)

<br />
<br />
<p align="center">
<strong>For anything else, tweet at <a href="https://twitter.com/MrAhmadAwais/" target="_blank" rel="noopener noreferrer">@MrAhmadAwais</a></strong>
</p>

<div align="center">
	<p>I have released a video course to help you learn how to create projects just like this one. Node.js and JavaScript based automation dev-tools and Command-line CLIs — <a href="https://NodeCLI.com/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">Learn to build Node.js CLIS →</a></p>
    <br />
  <a href="https://NodeCLI.com/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">
  <img src="https://raw.githubusercontent.com/ahmadawais/stuff/master/nodecli/featured.jpg" /><br>VSCode</a>

  _<small><a href="https://NodeCLI.com/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">Node CLI Automation →</a></small>_
</div>


<div align="center">
	<p>I have released a video course to help you become a better developer — <a href="https://VSCode.pro/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">Become a VSCode Power User →</a></p>
    <br />
  <a href="https://VSCode.pro/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">
  <img src="https://raw.githubusercontent.com/ahmadawais/shades-of-purple-vscode/master/images/vscodeproPlay.jpg" /><br>VSCode</a>

  _<small><a href="https://VSCode.pro/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block" target="_blank">VSCode Power User Course →</a></small>_
</div>

<br>

[![VSCode](https://img.shields.io/badge/-VSCode.pro%20%E2%86%92-gray.svg?colorB=4D2AFF&style=flat)](https://VSCode.pro/?utm_source=github&utm_medium=referral&utm_campaign=ahmadawais/create-guten-block)
[![Ahmad on Twitter](https://img.shields.io/twitter/follow/mrahmadawais.svg?style=social&label=Follow%20@MrAhmadAwais)](https://twitter.com/mrahmadawais/)
