# QtPy: Abstraction layer for PyQt5/PyQt4/PySide2/PySide

[![license](https://img.shields.io/pypi/l/qtpy.svg)](./LICENSE)
[![pypi version](https://img.shields.io/pypi/v/qtpy.svg)](https://pypi.org/project/QtPy/)
[![conda version](https://img.shields.io/conda/vn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![download count](https://img.shields.io/conda/dn/conda-forge/qtpy.svg)](https://www.anaconda.com/download/)
[![OpenCollective Backers](https://opencollective.com/spyder/backers/badge.svg?color=blue)](#backers)
[![Join the chat at https://gitter.im/spyder-ide/public](https://badges.gitter.im/spyder-ide/spyder.svg)](https://gitter.im/spyder-ide/public)<br>
[![PyPI status](https://img.shields.io/pypi/status/qtpy.svg)](https://github.com/spyder-ide/qtpy)
[![Github build status](https://github.com/spyder-ide/qtpy/workflows/Tests/badge.svg)](https://github.com/spyder-ide/qtpy/actions)
[![Coverage Status](https://coveralls.io/repos/github/spyder-ide/qtpy/badge.svg?branch=master)](https://coveralls.io/github/spyder-ide/qtpy?branch=master)

*Copyright © 2009–2021 The Spyder Development Team*


## Description

**QtPy** is a small abstraction layer that lets you
write applications using a single API call to either PyQt or PySide.

It provides support for PyQt5, PyQt4, PySide2 and PySide using the Qt5 layout
(where the QtGui module has been split into QtGui and QtWidgets).

Basically, you can write your code as if you were using PySide2
but import Qt modules from `qtpy` instead of `PySide2` (or `PyQt5`)


### Attribution and acknowledgments

This project is based on the [pyqode.qt](https://github.com/pyQode/pyqode.qt)
project and the [spyderlib.qt](https://github.com/spyder-ide/spyder/tree/2.3/spyderlib/qt)
module from the [Spyder](https://github.com/spyder-ide/spyder) project, and
also includes contributions adapted from
[qt-helpers](https://github.com/glue-viz/qt-helpers), developed as part of the
[glue](http://glueviz.org) project.

Unlike `pyqode.qt` this is not a namespace package, so it is not tied
to a particular project or namespace.


### License

This project is released under the MIT license.


### Requirements

You need PyQt5, PyQt4, PySide2 or PySide installed in your system to make use
of QtPy. If several of these packages are found, PyQt5 is used by
default unless you set the `QT_API` environment variable.

`QT_API` can take the following values:

* `pyqt5` (to use PyQt5).
* `pyqt` or `pyqt4` (to use PyQt4).
* `pyside2` (to use PySide2)
* `pyside` (to use PySide).


### Installation

```bash
pip install qtpy
```

or

```bash
conda install qtpy
```


## Contributing

Everyone is welcome to contribute!


## Sponsors

Become a sponsor to get your logo on our README on Github.

[![Sponsors](https://opencollective.com/spyder/sponsors.svg)](https://opencollective.com/spyder#support)
