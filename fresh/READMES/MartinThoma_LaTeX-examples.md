LaTeX-examples
==============

More than 570 examples for the usage of LaTeX. You can check that with the
following command:

```bash
$ find . -type d | sort | awk '$0 !~ last "/" {print last} {last=$0} END {print last}' | grep -v .git | wc -l
```


Many examples can be found on [my Wikpedia Commons user page](http://commons.wikimedia.org/wiki/User:MartinThoma#Galerie).

You might also be interested in [my Blog](http://martin-thoma.com/tag/tikz/).


Usage
=====

Every LaTeX file is in a seperate folder and has its own Makefile.
So you can simply generate the PDF by typing `make` in the terminal.

If you want to get all examples offline, you have to execute

```bash
$ git clone --recursive https://github.com/MartinThoma/LaTeX-examples.git
```


Requirements
============

* You should have the latest LaTeX version. Here are
  [LaTeX installation instructions](http://martin-thoma.com/how-to-install-the-latest-latex-version/).
* If you want to use the Makefiles, you have to have make installed.


Contact
=======
If you have examples or suggestions for improving given examples, please send
them to info@martin-thoma.de.


Re-use
=======
Feel free to use and modify the examples in this repository,
but please add a link to this repository or martin-thoma.com.

*Most* of the content was created completely by me. But check
the Readme files in each specific folder to make sure you can use it.

Other resources
===============
* [LaTeX Templates](http://www.latextemplates.com/)
* [LaTeX templates for writing a thesis](http://tex.stackexchange.com/q/326/5645)
