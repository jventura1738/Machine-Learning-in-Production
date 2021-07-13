Isomorphism -- Mathematics of Programming
====

2021/07

This book introduces the mathematics behind computer programming.

<img src="https://user-images.githubusercontent.com/332938/87840667-73856c80-c8d3-11ea-8d8b-0c5b366cde0f.png" width="400">

Contents
--------

The book can be downloaded in both English ([EN](https://github.com/liuxinyu95/unplugged/files/6754569/unplugged-en.pdf)) and Chinese ([中文](https://github.com/liuxinyu95/unplugged/files/6754570/unplugged-zh-cn.pdf)).

- Preface
- Chapter 1, Natural numbers. Peano Axiom, list and folding;
- Chapter 2, Recursion. Euclidean algorithm, Lambda calculus, and Y-combinator;
- Chapter 3, Symmetry. Group, Ring, and Field. Galois Theory;
- Chapter 4, Category theory and type system;
- Chapter 5, Deforest. Build-fold fusion law, optimization, and algorithm deduction;
- Chapter 6, Infinity. Set theory, Infinity and stream;
- Chapter 7, Logic paradox, Gödel's incompleteness theorems, and Turing halting problem.
- Answers to the exercise.

Install
--------

To build the book in PDF format from the sources, you need
the following software pre-installed.

- TeXLive, The book is built with XeLaTeX, a Unicode friendly version of TeX;

### Install TeXLive

In Debian/Ubuntu like Linux environment, do **NOT** install the TeXLive through apt-get. Go to TeXLive [official site](https://tug.org/texlive/) to download the setup script.

```bash
$ wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl.zip
$ unzip install-tl.zip
$ cd install-tl
$ sudo ./install-tl -gui text -repository http://mirror.ctan.org/systems/texlive/tlnet
```

In Windows, TeXLive provide a [gui based installer](https://tug.org/texlive/), in Mac OS X, there's a [MacTeX](https://www.tug.org/mactex/).

### Customize font (Optional)

If the host system fonts are available, e.g. under VM. they
could be imported as the following example:

```bash
$ sudo mkdir /usr/share/fonts/host-system
$ sudo cp /Host-System/Fonts/{FontName, fontname}* /usr/share/fonts/host-system/
$ fc-cache
```

### Others

You need the GNU make tool, in Debian/Ubuntu like Linux, it can be installed through the apt-get command:

```bash
$ sudo apt-get install build-essential
```

In Windows, you can install the MSYS for it. In Mac OS X, please install the developer tool from this command line:

```bash
$ xcode-select --install
```

### Build the PDF book

enter the folder contains the book TeX manuscript, run

```bash
$ make
```

This will generate unplugged-en.pdf and unplugged-zh-cn.pdf. If you only need the Chinese version for example, you can run `make cn` instead.

--

LIU Xinyu

liuxinyu95@gmail.com

``Cogito ergo sum''
