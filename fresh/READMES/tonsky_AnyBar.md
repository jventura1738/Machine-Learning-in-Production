# AnyBar: OS X menubar status indicator

AnyBar is a small indicator for your menubar that does one simple thing: it displays a colored dot. What the dot means and when to change it is up to you.

<img src="screenshot.png?raw=true" />

## Download

Version 0.2.3:

<a href="https://github.com/tonsky/AnyBar/releases/download/0.2.3/AnyBar-0.2.3.zip"><img src="AnyBar/Images.xcassets/AppIcon.appiconset/icon_128x128@2x.png?raw=true" style="width: 128px;" width=128/></a>

Or using [Homebrew Cask](https://github.com/Homebrew/homebrew-cask):

    brew install --cask anybar

## Support us

<a href="https://patreon.com/tonsky" target="_blank"><img src="./anybar_patreon.png"></a>

## Usage

AnyBar is controlled via a UDP port (1738 by default). Before any commands can be sent, AnyBar.app must be launched:

```sh
open -a AnyBar
```

Once launched, you may send it a message to change the style of the dot:

```sh
echo -n "black" | nc -4u -w0 localhost 1738
```

The following default commands change the style of the dot:

| Command       | Preview                                                             |
|---------------|---------------------------------------------------------------------|
| `white`       | <img src="AnyBar/Resources/white@2x.png?raw=true" width=15 />       |
| `red`         | <img src="AnyBar/Resources/red@2x.png?raw=true" width=15 />         |
| `orange`      | <img src="AnyBar/Resources/orange@2x.png?raw=true" width=15 />      |
| `yellow`      | <img src="AnyBar/Resources/yellow@2x.png?raw=true" width=15 />      |
| `green`       | <img src="AnyBar/Resources/green@2x.png?raw=true" width=15 />       |
| `cyan`        | <img src="AnyBar/Resources/cyan@2x.png?raw=true" width=15 />        |
| `blue`        | <img src="AnyBar/Resources/blue@2x.png?raw=true" width=15 />        |
| `purple`      | <img src="AnyBar/Resources/purple@2x.png?raw=true" width=15 />      |
| `black`       | <img src="AnyBar/Resources/black@2x.png?raw=true" width=15 />       |
| `question`    | <img src="AnyBar/Resources/question@2x.png?raw=true" width=15 />    |
| `exclamation` | <img src="AnyBar/Resources/exclamation@2x.png?raw=true" width=15 /> |
| `filled`      | <img src="AnyBar/Resources/filled@2x.png?raw=true" width=15 />      |
| `hollow`      | <img src="AnyBar/Resources/hollow@2x.png?raw=true" width=15 />      |

`black` and `white` always has black or white fill. On Big Sur, where text color of menubar might change depending on the wallpaper, you might want to use `filled` and `hollow` instead. They are inverted when menubar changes its appearance.

To quit, send `quit`.

## Alternative clients

Bash alias:

```sh
$ function anybar { echo -n $1 | nc -4u -w0 localhost ${2:-1738}; }

$ anybar red
$ anybar green 1739
```

Zsh with completion:

- [wookayin/anybar-zsh](https://github.com/wookayin/anybar-zsh)

Fish shell with completion:

- [matchai/anybar-fish](https://github.com/matchai/anybar-fish)

Go:

- [justincampbell/anybar](https://github.com/justincampbell/anybar)
- [johntdyer/anybar-go](https://github.com/johntdyer/anybar-go)

Node:

- [rumpl/nanybar](https://github.com/rumpl/nanybar)
- [sindresorhus/anybar](https://github.com/sindresorhus/anybar)
- [snippet by skibz](https://github.com/tonsky/AnyBar/issues/11)

PHP:

- [2bj/Phanybar](https://github.com/2bj/Phanybar)

Java:

- [cs475x/AnyBar4j](https://github.com/cs475x/AnyBar4j)

Python:

- [philipbl/pyanybar](https://github.com/philipbl/pyAnyBar)

Ruby:

- [davydovanton/AnyBar_rb](https://github.com/davydovanton/AnyBar_rb)

Rust:

- [urschrei/rust_anybar](https://github.com/urschrei/rust_anybar)
- [Feliix42/anybar-rs](https://github.com/Feliix42/anybar-rs)

Nim:

- [rgv151/anybar.nim](https://github.com/rgv151/anybar.nim)

Erlang:

- [kureikain/ebar](https://github.com/kureikain/ebar)

C:

- [onderweg/anybar-cli](https://github.com/onderweg/anybar-cli)

C#:

- [jenyayel/anybar-client](https://github.com/jenyayel/anybar-client)

Crystal:
- [davydovanton/AnyBar_cr](https://github.com/davydovanton/AnyBar_cr)

Emacs: 

- [rmuslimov/anybar.el](https://gist.github.com/rmuslimov/2d74cacd5e0ae827663e)
- [tie-rack/anybar-el](https://github.com/tie-rack/anybar-el) (Also on [Melpa](http://melpa.org/#/anybar))

AppleScript:

```
tell application "AnyBar" to set image name to "blue"

tell application "AnyBar" to set current to get image name as Unicode text
display notification current
```

Alfred:

- [https://github.com/raguay/MyAlfred](https://github.com/raguay/MyAlfred/blob/master/Alfred%204/AnyBar%20Workflow.alfredworkflow)

## Integrations

- Webpack build status plugin [roman01la/anybar-webpack](https://github.com/roman01la/anybar-webpack)
- boot-clj task [tonsky/boot-anybar](https://github.com/tonsky/boot-anybar)
- Idea plugin [denofevil/AnyBarIdea](https://github.com/denofevil/AnyBarIdea)
- Anybar-based CLI journal [Andrew565/anybar-icon-journal](https://github.com/Andrew565/anybar-icon-journal)
- Command monitoring [rvirani1/with_anybar](https://github.com/rvirani1/with_anybar)
- Monitor commands automatically, across several iterm tabs [stacycurl/anybar_bash](https://github.com/stacycurl/anybar-bash)
- Extension for ipython/jupyter/ipython notebook [ermakovpetr/ipython-anybar](https://github.com/ermakovpetr/ipython-anybar)

## Running multiple instances

You can run several instances of AnyBar as long as they listen on different ports. Use the `ANYBAR_PORT` environment variable to change the port and `open -na` to run several instances:

```sh
ANYBAR_PORT=1738 open -na AnyBar
ANYBAR_PORT=1739 open -na AnyBar
ANYBAR_PORT=1740 open -na AnyBar
```

## Environment variables to specify a title and the initial color of the dot

A title can be set to distinguish dots in the menubar:

```sh
ANYBAR_PORT=1738 ANYBAR_TITLE=First  open -na AnyBar
ANYBAR_PORT=1739 ANYBAR_TITLE=Second open -na AnyBar
ANYBAR_PORT=1740 ANYBAR_TITLE=Third  open -na AnyBar
```

And the initial color of the dot can also be set:

```sh
ANYBAR_INIT=blue open -na AnyBar
```

## Custom images

AnyBar can detect and use local custom images stored in the `~/.AnyBar` directory. For example, if you have a `~/.AnyBar/square@2x.png` image, send `square` to port 1738 and it will be displayed. Images should be 19×19 pixels for standard resolution, and 38x38 pixels for retina (@2x).

## Ports

- Ubuntu Unity [limpbrains/somebar](https://github.com/limpbrains/somebar)
- i3wm with i3pystatus [enkore/i3pystatus](https://github.com/enkore/i3pystatus)
- Windows 10 [PavelStefanov/NoteBar](https://github.com/PavelStefanov/NoteBar)
- Emacs [plexus/.../emybar.el](https://github.com/plexus/plexmacs/blob/master/emybar/emybar.el)

## License

Copyright © 2015 Nikita Prokopov

Licensed under Eclipse Public License (see [LICENSE](LICENSE)).
