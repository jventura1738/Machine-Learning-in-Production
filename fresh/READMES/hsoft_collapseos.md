# Collapse OS

*Bootstrap post-collapse technology*

Collapse OS is a Forth operating system and a collection of tools and
documentation with a single purpose: preserve the ability to program micro-
controllers through civilizational collapse.

It it designed to:

1. Run on minimal and improvised machines.
2. Interface through improvised means (serial, keyboard, display).
3. Edit text files.
4. Compile assembler source files for a wide range of MCUs and CPUs.
5. Read and write from a wide range of storage devices.
6. Assemble itself and deploy to another machine.

Additionally, the goal of this project is to be as self-contained as possible.
With a copy of this project, a capable and creative person should be able to
manage to build and install Collapse OS without external resources (i.e.
internet) on a machine of her design, built from scavenged parts with low-tech
tools.

## Git repository no longer updated

In the wake of my rejection of modern software and complexity, I've stopped
using git to manage versioning in Collapse OS because I consider RCS to be
sufficient. The commit adding this message is therefore the last I'm adding.

Further improvements of Collapse OS are available on [Collapse OS' website][web]
as tarballs of the project including RCS metadata. Those tarballs are updated
regularly.

## Getting started

Documentation is in text files in `doc/`. Begin with `intro.txt`.

Collapse OS can run on any POSIX platform and builds easily.
See `/cvm/README.md` for instructions.

Alternatively, there's also [Michael Schierl's JS Collapse OS emulator][jsemul]
which is awesome and allows you to run Collapse OS from your browser, but it
isn't always up to date. The "Javascript Forth" version is especially awesome:
it's not a z80 emulator, but a *javascript port of Collapse OS*!

## Organisation of this repository

* `blk.fs`: Collapse OS filesystem's content. See below.
* `cvm`: A C implementation of Collapse OS, allowing it to run natively on any
         POSIX platform.
* `doc`: Documentation.
* `arch`: collection of makefiles that assemble Collapse OS on different
          machines.
* `tools`: Tools for working with Collapse OS from "modern" environments. For
           example, tools for facilitating data upload to a Collapse OS machine
           through a serial port.
* `emul`: Tools for running Collapse OS in an emulated environment.
* `tests`: Automated test suite for the whole project.

## blk.fs

This file is a big text file containing the "real deal", that is, the contents
of Collapse OS' filesystem. That filesystem contains everything that a
post-collapse computer would manage, that is, all Forth and assembler source
code for the tools it needs to fulfill its goals.

The Collapse OS filesystem is a simple sequence of 1024 bytes blocks. That is
not very workable in the text editor of a modern system. `blk.fs` represents an
"unpacked" view of that block system. Each block (16 lines max per block, 64
chars max per line) begins with a marker indicating the block number of the
contents that follow.

Blocks must be in ascending order.

That file can be "packed" to a real blkfs with `/tools/blkpack`. A real blkfs
can be "unpacked" to its text file form with `/tools/blkunpack`.

## Status

The project unfinished but is progressing well! See [Collapse OS' website][web]
for more information.

## Looking for the assembler version?

The Forth-based Collapse OS is the second incarnation of the concept. The first
one was entirely written in z80 assembly. If you're interested in that
incarnation, checkout the `z80asm` branch.

[web]: https://collapseos.org
[jsemul]: https://schierlm.github.io/CollapseOS-Web-Emulator/
