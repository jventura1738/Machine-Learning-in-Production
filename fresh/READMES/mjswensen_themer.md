<p align="center">
  <a href="https://themer.dev">
    <img src="https://cdn.jsdelivr.net/gh/mjswensen/themer@4e78b9a50a00bab7605b4996e428b9a6c4a000b0/assets/icon.png" width="384" alt="Themer logo" />
  </a>
</p>

# themer ![CI](https://github.com/mjswensen/themer/workflows/CI/badge.svg?branch=main) [![Twitter Follow](https://img.shields.io/twitter/follow/themerdev?style=social)](https://twitter.com/themerdev)

`themer` takes a set of colors and generates [editor themes](#editorsides), [terminal themes](#terminals), [themes for other apps](#other), and [desktop/device wallpapers](#wallpapers).

![visual description](https://cdn.jsdelivr.net/gh/mjswensen/themer@a186c8585721d5defbf4cb1bc94165144d4dd35a/assets/themer-description.png)

## Table of Contents

* [Support `themer`](#support-themer)
* [Installation](#installation)
* [Usage](#usage)
  * [Example workflow](#example-workflow)
  * [Example usage with `npx`](#example-usage-with-npx)
* [Themer color sets](#themer-color-sets)
  * [Original color sets](#original-color-sets)
  * [Ports from third-party themes](#ports-from-third-party-themes)
  * [Create your own color set](#create-your-own-color-set)
    * [Color mappings](#color-mappings)
    * [Tips](#tips)
  * [Using base16 schemes with Themer](#using-base16-schemes-with-themer)
* [Themer templates](#themer-templates)
  * [Terminals](#terminals)
  * [Editors/IDEs](#editorsides)
  * [Wallpapers](#wallpapers)
  * [Other](#other)
  * [Community](#community)
  * [Create your own template](#create-your-own-template)
* [About](#about)
* [Contributing](#contributing)
* [Themer's Web UI](#themers-web-ui)

## Support `themer`

* ⭐️ Star [`themer` on GitHub](https://github.com/mjswensen/themer)
* 👋 Follow [@themerdev](https://twitter.com/themerdev) on Twitter
* 🦁 [Send a tip through the Brave Browser](https://brave.com/mjs684), either on [the repository page](https://github.com/mjswensen/themer) or [`themer`'s Web UI](https://themer.dev)
* 💳 Pay what you want when downloading your theme from [themer.dev](https://themer.dev)

## Installation

_Don't love the command-line? Check out [the Web UI](https://themer.dev)._

```sh
mkdir my-dotfiles && cd my-dotfiles
npm install themer
```

If you do not keep your dotfiles under version control, you can simply install themer globally with `npm -g install themer`.

`themer` can also be used without installing, via `npx`—see [example below](#example-usage-with-npx).

## Usage

Pass `themer` a color set, as many templates as you wish, and an output directory.

```sh
themer \
  --colors <npm package name OR file> \
  --template <npm package name OR file> \
  [--template <npm package name OR file>...] \
  --out <directory>
```

Your generated theme files, as well as a README on how to install them, will be written to the output directory.

`themer` can create themes from your custom color sets (see ["Create your own color set"](#create-your-own-color-set) below) or from color sets published on npm (see [@themer/colors-default](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-default)). The same is true for templates.

### Example workflow

Say you wanted to generate a vim theme and desktop background using `themer`'s default color set. First, install `themer`, the color set, and the templates:

```sh
cd my-dotfiles
npm install themer @themer/colors-default @themer/vim @themer/wallpaper-block-wave
```

Then edit your `package.json`:

```json
  ...
  "scripts": {
    "build": "themer -c @themer/colors-default -t @themer/vim -t @themer/wallpaper-block-wave -o gen"
  },
  ...
```

Then run your new script:

```sh
npm run build
```

Now check the `gen/` folder for your generated themes. Here's the result:

![example usage result](https://cdn.jsdelivr.net/gh/mjswensen/themer@a186c8585721d5defbf4cb1bc94165144d4dd35a/assets/example-usage.png)

### Example usage with `npx`

```sh
npx \
  -p themer \
  -p @themer/colors-default \
  -p @themer/vim \
  -p @themer/wallpaper-block-wave \
  themer \
  -c @themer/colors-default \
  -t @themer/vim \
  -t @themer/wallpaper-block-wave \
  -o output
```

## Themer color sets

### Original color sets

| Name | Dark Preview | Light Preview |
| --- | --- | --- |
| [@themer/colors-default](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-default) | ![@themer/colors-default dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-default-dark-swatch.svg) | ![@themer/colors-default light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-default-light-swatch.svg) |
| [@themer/colors-finger-paint](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-finger-paint) | ![@themer/colors-finger-paint dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-finger-paint-dark-swatch.svg) | ![@themer/colors-finger-paint light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-finger-paint-light-swatch.svg) |
| [@themer/colors-green-as-a-whistle](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-green-as-a-whistle) | ![@themer/colors-green-as-a-whistle dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@ec9afc6d21d689e49b4816880dbe670a0d655951/assets/preview/themer-colors-green-as-a-whistle-dark-swatch.svg) | ![@themer/colors-green-as-a-whistle light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@ec9afc6d21d689e49b4816880dbe670a0d655951/assets/preview/themer-colors-green-as-a-whistle-light-swatch.svg) |
| [@themer/colors-monkey](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-monkey) | ![@themer/colors-monkey dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-monkey-dark-swatch.svg) | ![@themer/colors-monkey light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-monkey-light-swatch.svg) |
| [@themer/colors-night-sky](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-night-sky) | ![@themer/colors-night-sky dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-night-sky-dark-swatch.svg) | (dark only) |
| [@themer/colors-polar-ice](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-polar-ice) | ![@themer/colors-polar-ice dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-polar-ice-dark-swatch.svg) | ![@themer/colors-polar-ice light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-polar-ice-light-swatch.svg) |
| [@themer/colors-right-in-the-teals](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-right-in-the-teals) | ![@themer/colors-right-in-the-teals dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-right-in-the-teals-dark-swatch.svg) | ![@themer/colors-right-in-the-teals light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-right-in-the-teals-light-swatch.svg) |

### Ports from third-party themes

| Name | Dark Preview | Light Preview |
| --- | --- | --- |
| [@themer/colors-dracula](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-dracula) | ![@themer/colors-dracula dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@0a1c71ce1fd01ec56daca72be8b04db6d81b16b5/assets/preview/themer-colors-dracula-dark-swatch.svg) | (dark only) |
| [@themer/colors-github-universe](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-github-universe) | ![!themer/colors-github-universe preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-github-universe-dark-swatch.svg) | (dark only) |
| [@themer/colors-lucid](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-lucid) | ![@themer/colors-lucid dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-lucid-dark-swatch.svg) | ![@themer/colors-lucid light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-lucid-light-swatch.svg) |
| [@themer/colors-mojave](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-mojave) | ![@themer/colors-mojave dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-mojave-dark-swatch.svg) | ![@themer/colors-mojave light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-mojave-light-swatch.svg) |
| [@themer/colors-nova](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-nova) | ![@themer/colors-nova preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-nova-dark-swatch.svg) | (dark only) |
| [@themer/colors-one](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-one) | ![@themer/colors-one dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-one-dark-swatch.svg) | ![@themer/colors-one light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-one-light-swatch.svg) |
| [@themer/colors-rivet](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-rivet) | ![@themer/colors-rivet dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-rivet-dark-swatch.svg) | ![@themer/colors-rivet light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-rivet-light-swatch.svg) |
| [@themer/colors-seti](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-seti) | ![@themer/colors-seti dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@a0deeb0588fd67dec53ad506b302df9e493ad837/assets/preview/themer-colors-seti-dark-swatch.svg) | (dark only) |
| [@themer/colors-solarized](https://github.com/mjswensen/themer/tree/main/cli/packages/colors-solarized) | ![@themer/colors-solarized dark preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-solarized-dark-swatch.svg) | ![@themer/colors-solarized light preview](https://cdn.jsdelivr.net/gh/mjswensen/themer@399430ac7b58691dc436761b1a03614898df92ba/assets/preview/themer-colors-solarized-light-swatch.svg) |

### Create your own color set

To create your own color set, create a JavaScript file that exports a `colors` object, like so:

```js
module.exports.colors = {

  // A color set can have both light and dark variants, but is only required
  // to have one.
  dark: {

    // Colors can be defined in any valid CSS format.

    // accent0-7 should be the main accent colors of your theme. See the table
    // in the "Color mappings" section for how the colors will be used in your
    // new themes.
    accent0: '#FF4050',
    accent1: '#F28144',
    accent2: '#FFD24A',
    accent3: '#A4CC35',
    accent4: '#26C99E',
    accent5: '#66BFFF',
    accent6: '#CC78FA',
    accent7: '#F553BF',

    // shade0-7 should be shades of the same hue, with shade0 being the
    // background and shade7 being the foreground. If you omit the
    // intermediate shades (1 through 6), they will be calculated automatically
    // for you.
    shade0: '#282629',
    shade1: '#474247',
    shade2: '#656066',
    shade3: '#847E85',
    shade4: '#A29DA3',
    shade5: '#C1BCC2',
    shade6: '#E0DCE0',
    shade7: '#FFFCFF'

  },

  // Same as above, except that shade0 should be the lightest and shade7 should
  // be the darkest.
  light: { ... },

};
```

_Pro Tip: you can use [`themer`'s Web UI](https://themer.dev) to more easily select your colors, then click the "Download" button to generate a `colors.js` file._

Then pass the path to your JS file to the `--colors` argument of `themer`.

```
themer -c path/to/my/colors.js ...
```

#### Color mappings

To help you choose colors for your own color set, this is approximately how most `themer` templates will utilize your colors:

| Color Key | Typical Usage | Conventional Color* |
| --------- | ------------- | ------------------- |
| `accent0` | error, VCS deletion | Red |
| `accent1` | syntax | Orange |
| `accent2` | warning, VCS modification | Yellow |
| `accent3` | success, VCS addition | Green |
| `accent4` | syntax | Cyan |
| `accent5` | syntax | Blue |
| `accent6` | syntax, caret/cursor | |
| `accent7` | syntax, special | Magenta |
| `shade0` | background color | |
| `shade1` | UI | |
| `shade2` | UI, text selection | |
| `shade3` | UI, code comments | |
| `shade4` | UI | |
| `shade5` | UI | |
| `shade6` | foreground text | |
| `shade7` | foreground text | |

_*Conventional color is suggested for consistency with ANSI color names in terminal themes, but is not a hard requirement._

See [`themer`'s Web UI](https://themer.dev) for a more visual representation of the color mappings.

#### Tips

* If you omit `shade1` through `shade6`, `themer` will interpolate them automatically for you, using [color-steps](https://github.com/mjswensen/color-steps).
* `themer` supports any valid CSS color format; that means you can use `chartreuse`, `rgb(127, 255, 0)`, `rgb(50%, 100%, 0%)`, `#7FFF00`, `hsl(90, 100%, 50%)`, etc.
* I would recommend checking your color set into your dotfiles repo. Once you've fine-tuned it, you might consider publishing it to npm for others to use! (If you do, consider naming your package starting with `themer-colors-` so that others can easily find it.)

### Using base16 schemes with Themer

In place of a themer color set file or npm package, you can also provide `themer` with any base16 scheme YAML file.

```
themer --colors path/to/base16-scheme.yml ...
```

Refer to the [base16 repository](https://github.com/chriskempson/base16#scheme-repositories) for a list of base16 schemes.

## Themer templates

### Terminals

* [@themer/alacritty](https://github.com/mjswensen/themer/tree/main/cli/packages/alacritty)
* [@themer/cmd](https://github.com/mjswensen/themer/tree/main/cli/packages/cmd)
* [@themer/conemu](https://github.com/mjswensen/themer/tree/main/cli/packages/conemu)
* [@themer/hyper](https://github.com/mjswensen/themer/tree/main/cli/packages/hyper)
* [@themer/iterm](https://github.com/mjswensen/themer/tree/main/cli/packages/iterm)
* [@themer/kitty](https://github.com/mjswensen/themer/tree/main/cli/packages/kitty)
* [@themer/konsole](https://github.com/mjswensen/themer/tree/main/cli/packages/konsole)
* [@themer/terminal](https://github.com/mjswensen/themer/tree/main/cli/packages/terminal)
* [@themer/terminator](https://github.com/mjswensen/themer/tree/main/cli/packages/terminator)
* [@themer/windows-terminal](https://github.com/mjswensen/themer/tree/main/cli/packages/windows-terminal)

### Editors/IDEs

* [@themer/atom-syntax](https://github.com/mjswensen/themer/tree/main/cli/packages/atom-syntax)
* [@themer/atom-ui](https://github.com/mjswensen/themer/tree/main/cli/packages/atom-ui)
* [@themer/bbedit](https://github.com/mjswensen/themer/tree/main/cli/packages/bbedit)
* [@themer/emacs](https://github.com/mjswensen/themer/tree/main/cli/packages/emacs)
* [@themer/sublime-text](https://github.com/mjswensen/themer/tree/main/cli/packages/sublime-text)
* [@themer/vim-lightline](https://github.com/mjswensen/themer/tree/main/cli/packages/vim-lightline)
* [@themer/vim](https://github.com/mjswensen/themer/tree/main/cli/packages/vim)
* [@themer/visual-studio](https://github.com/mjswensen/themer/tree/main/cli/packages/visual-studio)
* [@themer/vscode](https://github.com/mjswensen/themer/tree/main/cli/packages/vscode)
* [@themer/xcode](https://github.com/mjswensen/themer/tree/main/cli/packages/xcode)

### Wallpapers

* [@themer/wallpaper-block-wave](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-block-wave)
* [@themer/wallpaper-burst](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-burst)
* [@themer/wallpaper-circuits](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-circuits)
* [@themer/wallpaper-diamonds](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-diamonds)
* [@themer/wallpaper-dot-grid](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-dot-grid)
* [@themer/wallpaper-octagon](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-octagon)
* [@themer/wallpaper-shirts](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-shirts)
* [@themer/wallpaper-triangles](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-triangles)
* [@themer/wallpaper-trianglify](https://github.com/mjswensen/themer/tree/main/cli/packages/wallpaper-trianglify)

### Other

* [@themer/alfred](https://github.com/mjswensen/themer/tree/main/cli/packages/alfred)
* [@themer/brave](https://github.com/mjswensen/themer/tree/main/cli/packages/brave)
* [@themer/chrome](https://github.com/mjswensen/themer/tree/main/cli/packages/chrome)
* [@themer/css](https://github.com/mjswensen/themer/tree/main/cli/packages/css)
* [@themer/firefox-addon](https://github.com/mjswensen/themer/tree/main/cli/packages/firefox-addon)
* [@themer/firefox-color](https://github.com/mjswensen/themer/tree/main/cli/packages/firefox-color)
* [@themer/keypirinha](https://github.com/mjswensen/themer/tree/main/cli/packages/keypirinha)
* [@themer/prism](https://github.com/mjswensen/themer/tree/main/cli/packages/prism)
* [@themer/sketch-palettes](https://github.com/mjswensen/themer/tree/main/cli/packages/sketch-palettes)
* [@themer/slack](https://github.com/mjswensen/themer/tree/main/cli/packages/slack)
* [@themer/wox](https://github.com/mjswensen/themer/tree/main/cli/packages/wox)
* [@themer/xresources](https://github.com/mjswensen/themer/tree/main/cli/packages/xresources)

### Community

* [~0x52a1/themer-kitty](https://www.npmjs.com/package/themer-kitty)
* [~0x52a1/themer-termite](https://www.npmjs.com/package/themer-termite)
* [~agarrharr/themer-gnome-terminal](https://www.npmjs.com/package/themer-gnome-terminal)
* [~dguo/themer-colors-blood-moon](https://www.npmjs.com/package/themer-colors-blood-moon)
* [~dtkerr/themer-i3](https://www.npmjs.com/package/themer-i3)
* [~dtkerr/themer-m4](https://www.npmjs.com/package/themer-m4)
* [~jtroyer/themer-mattermost](https://www.npmjs.com/package/themer-mattermost)
* [~lafleurdeboum/themer-powerline-rs](https://www.npmjs.com/package/themer-powerline-rs)
* [~rubenverg/themer-windows-terminal](https://www.npmjs.com/package/themer-windows-terminal)
* [~tomselvi/themer-jetbrains](https://www.npmjs.com/package/themer-jetbrains)
* [~tomselvi/themer-mintty](https://www.npmjs.com/package/themer-mintty)
* [~tomselvi/themer-tmux](https://www.npmjs.com/package/themer-tmux)

### Create your own template

To create your own template, create a JavaScript file that exports a `render` function, like so:

```js
module.exports.render = function(colors, options) {

  // colors is an object that will have one or both keys: 'light' and
  // 'dark', each being an object with keys 'accent0' through 'accent7'
  // and 'shade0' through 'shade7'.

  // options is an object representing the original command-line args
  // passed to themer. This allows you to add special arguments that
  // will apply only to your template. An example of this is allowing a
  // themer user to specify custom resolutions for rendering a wallpaper.

  // This function should return an array of Promises, each Promise
  // resolving to an object of the following structure:
  // {
  //   name: '<the name of the file to be written>', // can include subdirectories, too
  //   contents: <a Buffer of the contents of the file to be written>,
  // }

};
```

Your JS file can then be passed to a `--template` argument of `themer`. That's it!

Here's an [example template render function](https://github.com/mjswensen/themer/blob/main/cli/packages/slack/lib/index.js) that generates a Slack sidebar theme from a `themer` color set.

Once you've developed your template, consider publishing it on npm (with repository name starting with `themer-`) so that others can use it!

## About

`themer` is inspired by [trevordmiller/nova](https://github.com/trevordmiller/nova/) and [chriskempson/base16](http://chriskempson.com/projects/base16/).

Conceptually, `themer` is very similar to [base16](http://chriskempson.com/projects/base16/), but:

1. It is lighter, and simpler to use.
2. It is more easily extensible with your own color sets and templates.
3. It integrates better with your dotfiles, especially if you keep them under version control.

## Contributing

For instructions on how to contribute to `themer`, see [CONTRIBUTING.md](https://github.com/mjswensen/themer/blob/main/.github/CONTRIBUTING.md) and [`themer`'s code of conduct](https://github.com/mjswensen/themer/blob/main/CODE_OF_CONDUCT.md).

## Themer's Web UI

If you'd prefer to develop your themes visually, check out [`themer`'s Web UI](https://themer.dev), an offline-ready Progressive Web App.
