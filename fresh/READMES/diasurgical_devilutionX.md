<p align="center">
<img width="554" src="https://user-images.githubusercontent.com/204594/113575181-c946a400-961d-11eb-8347-a8829fa3830c.png">
</p>

---

[![Downloads](https://img.shields.io/github/downloads/diasurgical/devilutionX/total.svg)](https://github.com/diasurgical/devilutionX/releases)
[![GitHub Stars](https://img.shields.io/github/stars/diasurgical/devilutionX.svg)](https://github.com/diasurgical/devilutionX/stargazers)
[![Codecov](https://codecov.io/gh/diasurgical/devilutionX/branch/master/graph/badge.svg)](https://codecov.io/gh/diasurgical/devilutionX)
[![BCH compliance](https://bettercodehub.com/edge/badge/diasurgical/devilutionX?branch=master)](https://bettercodehub.com/)

![Discord Channel](https://avatars3.githubusercontent.com/u/1965106?s=16&v=4) [Discord Chat Channel](https://discord.gg/YQKCAYQ)

<p align="center">
<img width="838" src="https://user-images.githubusercontent.com/204594/113578478-26912400-9623-11eb-9ff6-9bd9717462b6.png">
</p>

<sub>*(The health-bar and XP-bar are off by default, but can be enabled in the [ini-file](https://github.com/diasurgical/devilutionX/wiki/DevilutionX-diablo.ini-configuration-guide). Widescreen and transparency can also be disabled if preferred)*</sub>

# What is DevilutionX

DevilutionX is a source port of Diablo and Hellfire that strives to make it simple to run the game while providing engine improvements, bugfixes, and some optional quality of life features.

Check out the [manual](https://github.com/diasurgical/devilutionX/wiki) for what features are available and how best to take advantage of them.

For a full list of changes see our [changelog](docs/CHANGELOG.md).

# How to Install

Note: You'll need access to the data from the original game. If you don't have an original CD then you can [buy Diablo from GoG.com](https://www.gog.com/game/diablo). Alternately you can use `spawn.mpq` from the [shareware](http://ftp.blizzard.com/pub/demos/diablosw.exe) version, in place of `DIABDAT.MPQ`, to play the shareware portion of the game.

Download the latest [DevilutionX release](https://github.com/diasurgical/devilutionX/releases) and extract the contents to a location of your choosing or [build from source](#building-from-source).

- Copy `DIABDAT.MPQ` from the CD or GOG-installation (or [extract it from the GoG installer](https://github.com/diasurgical/devilutionX/wiki/Extracting-the-.MPQs-from-the-GoG-installer)) to the DevilutionX folder.
- To run the Diablo: Hellfire expansion you will need to also copy `hellfire.mpq`, `hfmonk.mpq`, `hfmusic.mpq`, `hfvoice.mpq`.

For more detailed instructions: [Installation Instructions](./docs/installing.md).

# Contributing

We are always looking for more people to help with [coding](docs/CONTRIBUTING.md), [documentation](https://github.com/diasurgical/devilutionX/wiki), testing the [latest builds](https://app.circleci.com/pipelines/github/diasurgical/devilutionX?branch=master), spreading the word, or simply just hanging out on [the chat](https://discord.gg/YQKCAYQ).

# Mods

We hope to provide a good starting point for mods, in addition to the full Devilution source code we also provide modding tools. Also, check out the list of known [mods based on DevilutionX](https://github.com/diasurgical/devilutionX/wiki/Mods-and-related-projects).

# Test builds

If you want to help test the latest state of the next version you can fetch the build artifact from one of the build server:

[![CircleCI](https://circleci.com/gh/diasurgical/devilutionX.svg?style=shield)](https://circleci.com/gh/diasurgical/devilutionX)
[![AppVeyor](https://ci.appveyor.com/api/projects/status/1a0jus2372qvksht?svg=true)](https://ci.appveyor.com/project/AJenbo/devilutionx)
[![Linux_x86](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86.yml)
[![Linux_x86_64](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86_64.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86_64.yml)
[![Linux_x86_64_SDL1](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86_64_SDL1.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/Linux_x86_64_SDL1.yml)
[![MacOSX](https://github.com/diasurgical/devilutionX/actions/workflows/MacOSX.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/MacOSX.yml)
[![Windows_x64](https://github.com/diasurgical/devilutionX/actions/workflows/Windows_x64.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/Windows_x64.yml)
[![Windows_x86](https://github.com/diasurgical/devilutionX/actions/workflows/Windows_x86.yml/badge.svg)](https://github.com/diasurgical/devilutionX/actions/workflows/Windows_x86.yml)

# Building from Source

Want to compile the program by yourself? Great! Simply follow the [build instructions](./docs/building.md).

# Credits

- The original Devilution project [Devilution](https://github.com/diasurgical/devilution#credits)
- [Everyone](https://github.com/diasurgical/devilutionX/graphs/contributors) who worked on Devilution/DevilutionX
- [Nikolay Popov](https://www.instagram.com/nikolaypopovz/) who provided new backgrounds and icons
- And thanks to all who support the project, report bugs, and help spread the word ❤️

# Legal

DevilutionX is released to the Public Domain. The documentation and functionality provided by DevilutionX may only be utilized with assets provided by the ownership of Diablo.

The source code in this repository is for non-commercial use only. If you use the source code you may not charge others for access to it or any derivative work thereof.

Diablo® - Copyright © 1996 Blizzard Entertainment, Inc. All rights reserved. Diablo and Blizzard Entertainment are trademarks or registered trademarks of Blizzard Entertainment, Inc. in the U.S. and/or other countries.

DevilutionX and any of its maintainers are in no way associated with or endorsed by Blizzard Entertainment®.
