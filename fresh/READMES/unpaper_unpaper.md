<!--
SPDX-FileCopyrightText: 2005 The unpaper authors

SPDX-License-Identifier: GPL-2.0-only
-->

unpaper
=======

[![Build
Status](https://travis-ci.com/unpaper/unpaper.svg?branch=main)](https://travis-ci.com/unpaper/unpaper)

Originally written by Jens Gulden — see AUTHORS for more information.
Licensed under GNU GPL v2 — see COPYING for more information.

Overview
--------

`unpaper` is a post-processing tool for scanned sheets of paper,
especially for book pages that have been scanned from previously
created photocopies.  The main purpose is to make scanned book pages
better readable on screen after conversion to PDF. Additionally,
`unpaper` might be useful to enhance the quality of scanned pages
before performing optical character recognition (OCR).

`unpaper` tries to clean scanned images by removing dark edges that
appeared through scanning or copying on areas outside the actual page
content (e.g.  dark areas between the left-hand-side and the
right-hand-side of a double- sided book-page scan).

The program also tries to detect misaligned centering and rotation of
pages and will automatically straighten each page by rotating it to
the correct angle. This process is called "deskewing".

Note that the automatic processing will sometimes fail. It is always a
good idea to manually control the results of unpaper and adjust the
parameter settings according to the requirements of the input. Each
processing step can also be disabled individually for each sheet.

See [further documentation][3] for the supported file formats notes.

Dependencies
------------

The only hard dependency of `unpaper` is [ffmpeg][4], which is used for
file input and output.

Building instructions
---------------------

`unpaper` uses [the Meson Build system](https://mesonbuild.com), which
can be installed using Python's package manage (`pip3` or `pip`):

    unpaper$ pip3 install --user 'meson >= 0.57' 'sphinx >= 3.4'
    unpaper$ CFLAGS="-march=native" meson --buildtype=debugoptimized builddir
    unpaper$ meson compile -C builddir

You can pass required optimization flags when creating the meson build
directory in the `CFLAGS` environment variable. Usage of Link-Time
Optimizations (Meson option `-Db_lto=true`) is recommended if
available.

Further optimizations such as `-ftracer` and `-ftree-vectorize` are
thought to work, but their effect has not been evaluated so your
mileage may vary.

Further Information
-------------------

You can find more information on the [basic concepts][1] and the
[image processing][2] in the available documentation.

[1]: doc/basic-concepts.md
[2]: doc/image-processing.md
[3]: doc/file-formats.md
[4]: https://www.ffmpeg.org/
