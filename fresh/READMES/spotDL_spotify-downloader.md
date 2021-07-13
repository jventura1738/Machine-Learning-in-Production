<!--- mdformat-toc start --slug=github --->

<div align="center">

<img src="/docs/static/logo-transparent.png" alt="spotDL" width="200" />

# spotDL

Download your Spotify playlists and songs along with album art and metadata

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?style=flat-square&color=44CC11)](https://github.com/spotDL/spotify-downloader/blob/master/LICENSE)
[![pypi version](https://img.shields.io/pypi/pyversions/spotDL?color=%2344CC11&style=flat-square)](https://pypi.org/project/spotdl/)
![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/spotDL/spotify-downloader/latest?color=44CC11&style=flat-square)
[![pypi downloads](https://img.shields.io/pypi/dw/spotDL?label=downloads@pypi&color=344CC11&style=flat-square)](https://pypi.org/project/spotdl/)
![Contributors](https://img.shields.io/github/contributors/spotDL/spotify-downloader?style=flat-square)
[![Discord](https://img.shields.io/discord/771628785447337985?label=discord&logo=discord&style=flat-square)](https://discord.gg/xCa23pwJWY)

</div>

> The fastest, easiest, and most accurate command-line music downloader

## What spotDL does

1. Downloads music from YouTube as an MP3 file
2. Applies basic metadata gathered from Spotify such as:
   - Track Name
   - Track Number
   - Album
   - Album Cover
   - Genre
   - and more!

### Redesigned

spotDL is being redesigned! This means we are currently not accepting new feature requests. You can talk to us on [our Discord](https://discord.gg/xCa23pwJWY) if there is anything further.

## Prerequisites

- Python 3.6.1 or above (added to PATH)
- FFmpeg 4.2 or above (added to PATH)

> **_YouTube Music must be available in your country for spotDL to work. This is because we use YouTube Music to filter search results. You can check if YouTube Music is available in your country, by visiting [YouTube Music](https://music.youtube.com)._**

## Installation

### Installing FFmpeg

- [Windows Tutorial](https://windowsloop.com/install-ffmpeg-windows-10/)
- OSX - `brew install ffmpeg`
- Linux - `sudo snap install ffmpeg`

### Installing spotDL

- Recommended Stable Version:

  ```bash
  pip install spotdl
  ```

- Dev Version: **(NOT STABLE)**

  ```bash
  pip install https://codeload.github.com/spotDL/spotify-downloader/zip/dev
  ```

If you have trouble installing spotdl take a look at the extended installation guide
[here](/docs/INSTALLATION.md) or ask for help in our
[discord server](https://discord.gg/xCa23pwJWY)

#### On Termux

```bash
curl -L https://raw.githubusercontent.com/spotDL/spotify-downloader/master/termux/setup_spotdl.sh | sh
```

## Usage

- #### To download a song, run

  ```bash
  spotdl [trackUrl]
  ```

  example:

  ```bash
  spotdl https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b
  ```

- #### To download an album, run

  ```bash
  spotdl [albumUrl]
  ```

  example:

  ```bash
  spotdl https://open.spotify.com/album/4yP0hdKOZPNshxUOjY0cZj
  ```

- #### To download a playlist, run

  ```bash
  spotdl [playlistUrl]
  ```

  example:

  ```bash
  spotdl https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID
  ```

- #### To download all songs from an artist run

  ```bash
  spotdl [artistUrl]
  ```

  example:

  ```bash
  spotdl https://open.spotify.com/artist/1fZAAHNWdSM5gqbi9o5iEA
  ```

- #### To search for and download a song, run, **with quotation marks**

  ```bash
  spotdl '[songQuery]'
  ```

  example:

  ```bash
  spotdl 'The Weeknd - Blinding Lights'
  ```

  > _Note: This is not accurate and often causes errors._

- #### To resume a failed/incomplete download, run

  ```bash
  spotdl [pathToTrackingFile]
  ```

  example:

  ```bash
  spotdl 'The Weeknd - Blinding Lights.spotdlTrackingFile'
  ```

  > _Note: `.spotdlTrackingFile`s are automatically created when a download starts and deleted on completion_

- #### You can queue up multiple download tasks by separating the arguments with spaces

  ```bash
  spotdl [songQuery1] [albumUrl] [songQuery2] ... (order does not matter)
  ```

  example:

  ```bash
  spotdl 'The Weeknd - Blinding Lights' https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID ...
  ```

  > _Note: spotDL downloads up to 4 songs in parallel, so for a faster experience, download albums and playlist, rather than tracks._

- #### To download songs with different output format run

  ```bash
  spotdl [songUrl] --output-format mp3/m4a/flac/opus/ogg
  ```

  example:

  ```bash
  spotdl [songUrl] --output-format opus
  ```

- #### To use ffmpeg binary that is not on PATH run

  ```bash
  spotdl [songUrl] --ffmpeg path/to/your/ffmpeg.exe
  ```

  example:

  ```bash
  spotdl [songUrl] --ffmpeg C:\ffmpeg\bin\ffmpeg.exe
  ```

- #### To ignore your ffmpeg version run

  ```bash
  spotdl [songUrl] --ignore-ffmpeg-version
  ```

## `pipx` Isolated Environment Alternative

For users who are not familiar with `pipx`, it can be used to run scripts **without**
installing the spotDL package and all the dependencies globally with pip. (Effectively
skipping over the [spotDL Installation](#Installing-spotDL) step)

First, you will need to install `pipx` by running:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Next, you can jump directly to running spotDL with:

```bash
pipx run spotdl ...
```

## Contributor Guide

Interested in contributing? Check out our [CONTRIBUTING.md](docs/CONTRIBUTING.md) to find
resources around contributing along with a guide on how to set up a development
environment.

## Contributors

[![contributors](https://contributors-img.web.app/image?repo=spotdl/spotify-downloader)](https://github.com/spotdl/spotify-downloader/graphs/contributors)

## Authors

1. [@ritiek](https://github.com/ritiek) for creating and maintaining spotDL for 4 years
2. [@rocketinventor](https://github.com/rocketinventor) for figuring out YouTube Music
   querying
3. [@MikhailZex](https://github.com/MikhailZex) for, never mind...

## License

[MIT](/LICENSE)
