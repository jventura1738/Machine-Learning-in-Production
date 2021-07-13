# jo

![jo logo](tests/jo-logo.png)

This is `jo`, a small utility to create JSON objects

```bash
$ jo -p name=jo n=17 parser=false
{
    "name": "jo",
    "n": 17,
    "parser": false
}
```

or arrays

```bash
$ seq 1 10 | jo -a
[1,2,3,4,5,6,7,8,9,10]
```

It has a [manual](jo.md), and you can read [why I wrote jo](http://jpmens.net/2016/03/05/a-shell-command-to-create-json-jo/).

## Build from Release tarball

To build from [a release](https://github.com/jpmens/jo/releases) you will need a C compiler to install from a source tarball which you download from the [Releases page](https://github.com/jpmens/jo/releases).

```bash
tar xvzf jo-1.3.tar.gz
cd jo-1.3
autoreconf -i
./configure
make check
make install
```


## Build from Github

[![Build Status](https://api.travis-ci.com/jpmens/jo.svg?branch=master)](https://travis-ci.com/github/jpmens/jo)

To install from the repository, you will need a C compiler as well as a relatively recent version of _automake_ and _autoconf_.

```bash
git clone git://github.com/jpmens/jo.git
cd jo
autoreconf -i
./configure
make check
make install
```

## Homebrew

```bash
brew install jo
```

## Ubuntu

```
apt-get install jo
```

## Gentoo

```
emerge jo
```

## Snap

Thanks to [Roger Light](https://twitter.com/ralight/status/1166023769623867398), _jo_ is available as a [snap package](https://snapcraft.io/jo). Use `snap install jo` from a Linux distro that supports snaps.

## Others

* [voidlinux](https://github.com/voidlinux/void-packages/tree/master/srcpkgs/jo)
* [ArchLinux](https://aur.archlinux.org/packages/jo/)
* [OpenBSD](http://openports.se/textproc/jo)
* [FreeBSD](https://www.freshports.org/textproc/jo)
* [Guix](https://guix.gnu.org/packages/jo-1.4/)
* [pkgsrc](http://pkgsrc.se/textproc/jo)
* [repology.org](https://repology.org/metapackage/jo/versions)
* [Docker](https://hub.docker.com/repository/docker/jpmens/jo)

## See also

* [gjo](https://github.com/skanehira/gjo)
* [rjo](https://github.com/dskkato/rjo)
* [jjo](https://github.com/memoryhole/jjo)

## Credits

* `json.[ch]` by 2011 Joseph A. Adams (joeyadams3.14159@gmail.com).
