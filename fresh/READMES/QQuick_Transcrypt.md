.. figure:: http://www.transcrypt.org/illustrations/ruler_banner2.png
    :alt: Logo
    :target: http://www.transcrypt.org
        
Python in the browser, precompiled for speed: http://www.transcrypt.org
=======================================================================

- Precompiled into highly readable, efficient JavaScript, downloads kB's rather than MB's
- Multiple inheritance, optional operator overloading, metaclasses, async/await, properties, decorators, hierarchical modules etc.
- Seamless integration with the universe of high-quality web-oriented JavaScript libraries, rather than the desktop-oriented Python ones
- Pure Python 3.7 syntax, using Python's native parser
- Debug directly from Python sourcecode, through integrated sourcemaps
- Generates JavaScript for humans, resembling the Python source line by line, optionally annotated with source line numbers
- Lightning fast JavaScript 6 code: call caching, for-loop optimization, in-line JavaScript etc.
- Integrated static typechecking and minification at the tip of a command line switch
- Also runs on top of node.js
- Extensive documentation with many code examples
- Apache 2.0 license
- Pip-install and go!

Latest stable release: London
=============================

`>>> GET STARTED!_ <http://www.transcrypt.org/#hello>`_
=======================================================

Thanks to everyone who contributed!

Readability
===========

As can be seen below, there's a simple parallel between the Python and the JavaScript code.
In combination with the use of sourcemaps, this enables efficient debugging.
Also, code can be tested from the command prompt using stubs.

.. figure:: http://www.transcrypt.org/illustrations/class_compare.png
    :alt: Screenshot of Python versus JavaScript code
    
    **Classic OO with multiple inheritance in JavaScript**

Main differences with CPython
=============================

- Web batteries: Seamless access to any existing JavaScript library has been favored over inclusion of many Python libraries in the distribution. There are some exceptions to this rule, e.g. math, cmath, random, itertools, re, time, datetime and turtle, and some more may follow, but in general the accent is on libraries that are relevant in the browser.
- No eval and exec of Python code. This is again part of the concept. Transcrypt code is compiled, optimized and minified in advance to warant fast page loads. In this respect its design goal is fundamentally different from tools that compile on the fly in the browser. Transcrypt is targeted towards building professional, extensive, real world web applications that load and run as fast as their JavaScript counterparts, but offers Pythonically clean, modular structure and maintainability.

License
=======

Copyright 2014 - 2018 Jacques de Hooge, GEATEC engineering, www.geatec.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

How to contribute
=================

Transcrypt started out as a personal repo, owned by Jacques de Hooge.
As the project caught on and the number of people contributing issues, ideas and code grew,
the repo was transferred to the QQuick organisation, to be able to form a developer team on GitHub.

There was also a clear message in this: Transcrypt isn't owned by anyone in particular.
It is the collective property of everyone using it or contributing to it.
At the same time the need was felt to keep a very firm grip on code quality, especially of the core.

Everything under ../transcrypt/modules/org/transcrypt plus the file ../transcrypt/\_\_main\_\_.py is considered to be part of Transcrypt's core.
A major design goal is to keep the core small and fast. This means that some CPython facilities were deliberately left out or simplified.
Core development is still mainly done by Jacques, but with the input of many great ideas submitted as issues.
If you want to improve something in the core, this is best initiated by first opening an issue for it.
Opening a pull request directly can lead to disappointment, although all effort is made to take good ideas seriously.

All other parts of Transcrypt are referred to as periphery.
While a good quality pull request for the periphery stands a reasonable chance of being accepted,
still it is wise to start an issue beforehand, allowing coordination and preventing waste of effort.

A special place is taken by implementing standard libraries. While Transcrypt mostly relies on browser-centric JavaScript libraries,
availability of a limited number of standard libraries will help acceptance by Python programmers. So you're most welcome to make a contribution here.
The design goal again is: better 90% complete, fast, small, and reliable, than 100% complete, slow, bulky and buggy.
If you contribute a library, please also contribute an autotest (see docs) and some documentation for it.
The supported platforms are Windows and Linux (and, with that, OsX).

While being open and respectful to any good ideas, the final say as to what gets in and what doesn't, is with Jacques.
So this is a dictatorial rather than a democratic project.
Being a sailer himself, Jacques values the notion of having one captain on a ship.
The captain doesn't own the ship, but he serves the passengers by consulting with the crew and plotting one stable course.

Another possibility to contribute libraries to Transcrypt is by submitting them as separate packages to PyPi.
In that case be sure to add the keyword Transcrypt to allow people to find your package.
Making your package pip-installable will also help it to catch on.
Contributing packages via PyPi of course means total freedom for the developer.

Development build status
========================

.. image:: https://travis-ci.org/QQuick/Transcrypt.svg?branch=master
    :target: https://travis-ci.org/QQuick/Transcrypt

The icon above shows the outcome of the continous integration test that is done on Linux after each commit.
The test consists of running a set of testlets, systematically covering all facilities of Transcrypt. Each testlet performs an automated back to back test against CPython.

The full set of testlets is described in the documentation and comes with the distribution.
Since the branching model has been deliberately kept simple, continuous integration may be transiently broken.
In that case you can use the latest passing version, that you'll find by clicking on the icon above and then on 'Build History'.

Each release, on the other hand, is preceded by at least the following tests:

- The automated back to back test described above, not only on Linux but also on Windows and, in case of relevant issues, on OsX.
- Automated compilation of the manual tests, human exercising of the resulting applications and a visual check of the results.
- Automated compilation of the demo's, human exercising of the resulting applications and a visual check of the results.
- A documentation build, followed by a visual sample check.

What's new in the latest commits
================================

- Parcel bundler demo simplified and added to demo directory, included in shipment test
- Executable comments: skip code either in CPython or, with the skip pragma, in Transcrypt (issue 602)
- Integration with Parcel bundler incl. auto-reload (issue 596)
- Correct formatting of None fixed, autotests added (issue 494, issue 515)
- Invalid link removed from doc (issue 595)
- Fix for ameclass with 'async' verified (issue 543)
- Fix for js_is and py_is aliases verified (issue 562)
- Selenium tests tab switching and alert handling fixed
- Compilation error reports fixed (pr584, issue 586)
- Module paths can now contain dots (issue 578 revisited)
- Module name can be reexported (pr 575)
- Exported vars can contain $ (issue 578)
- Import now can contain hyphens in filename (issue 576), (-am / -alimod switch)
- Import and re-export via __init__.py fixed (issue 559)
- Extension .py allowed for source file name on command line (issue 569)
- Minimal recompilation (make versus build) fixed, was broken after introduction of modules (pull request 560)
- -dl / -dlog "Log compiler messages to file" switch added
- Static typing tutorial repaired
- Builtin pow function added
- Context managers added + testcases
- Python 3.7 dataclasses added + testcases
- Everything written in __target__ subdir rather than installation dir
- Python modules now implemented as ES6 modules pervasively, multiple apps per page, runtime and libs only once
- String formatting mini language added as an option (-sf / --sform switch) + autotest
- Div internal improvements and fixes
- Time module made suitable for use in combination with Node.js
- Single line pragma's (issue 460) + doc + autotest
- Negative list indices allowed when operator overloading is enabled (issue 460)
- Added pragma's and switches jscall and nojscall, 30% speedup, use only locally for insulated methods in a class
- Fix for callable (None) (issue 450)
- Start made with /tutorials/baseline mini Python tutorial
- Fix for decorator from module (issue 448)
- Examples for datetime, time and re added to docs
- Module datetime added (pr 435)
- Conjugate of real now compiled correctly
- Property decorators now supported for getters and setters
- Metaclasses and method decorators now execute in correct order (issue 430)
- Complex numbers now support comparison operators and conjugate
- Max and min now accept sequences (issue 331)
- Aliasers more completely dealt with in combination with keyword args and getattr, setattr, hasattr, delattr (issue 414)
- Compiler switch -xt / --xtiny added to considerably reduce size of runtime if operator overloading isn't used
- Compiler switch -dn / --dnostrip added to avoid stripping comments in __builtin__ and __core__
- Comments in __builtin__ and __core__ JavaScript-only modules are now stripped by default
- Initial support for bytes and bytearrays added (issue 405 a.o.)
- Remark about heuristic interpretation of dictionary keys added to docs (issue 401)
- Fisher-Yates shuffle added to random module
- Exception type TypeError added, currently unused by Transcrypt itself (issue 365)
- Name of main program file now really doesn't need .py extension anymore... (issue 416, bugfix)
- Name of main program file doesn't need .py extension anymore (issue 416)
- DRY implementation of __module__, lean enough to remove the -mc / --modclass switch
- -mc / --modclass switch now controls generation of __module__ to prevent code bloat
- Issue 397 a.o., __module__ attribute added to classes, __name__ of main module is now '__main__',
- Enhancement for issue 399: __pragma__ ('keycheck') + command line switch + autotest
- Fixes for issues 398, 412, 413 + autotests
- __pragma__ ('xtrans', ...) added to facilitate partial translation by external tools (EXPERIMENTAL, issue 404, e.g. to deal with JSX)
- Default messages for ValueError and KeyError removed for better CPython compatibility (pr 395)
- Small fix of re module (issue 392)
- Conversion from bool to int now succeeds (issue 391)
- Overloadable operators __truediv__ and __floordiv__ added (issue 389)
- Class methods, static methods, class decorators, method decorators and static method decorators
- If an object doesn't have a specific string representation, function repr and str now return <object of type: object> rather than ???, and this case isn't reported as an error anymore
- Function len now calls __len__ if it exists (pr 378)
- More Pythonic truthyness when using -t (or --tconv) switch (pr 367 a.o.)
- Source file spec on command line can now be a full path (free afer pr #362)
- The zip function now also works for finite iterators (issue #369) + autotest
- -xc (or --confimp) switch added, to confine imported names to the directly importing module (so prevent imports from being be transitive)
- Cleaned up some generated files
- Module search order fixed, continuous integration functional again
- Regular expressions autotest workaround added for Python 3.6 enums
- Async/await added + manual test
- Made Python 3.6 the default in several places
- Pragma and command line switch added to augment module search path
- Better example of use of __getattr__ and __setattr__ added to autotest suite
- Method dict.values () added
- Demo added for three.js with encapsulated constructors
- Doc link repaired
- Fix for #317: Wrong exception type for aList ['aStringLiteral']
- Enhancement for #316: filter doesn't support None for func
- Enhancement for #314: float (' ') returns 0
- Enhancement for #310: hasattr () raises 'Uncaught TypeError'
- Enhancement for # 306: dict.popitem () added + autotest
- Integrated with newest API of mypy
- Fix for issue #304: Invalid JS when using global --opov flag
- Fix for issue #301: zip broken for strings
- Comment-like pragma's (issue #295) added: # \_\_pragma\_\_ (<parameters>)
- Fix for issue #284 (+= problem) and autotest case
- Bundled version 0.4.4 of mypy static typechecker replaced by dependency on mypy (currently 0.4.7)
- Added in-place overloads for @=, \*\*=, %=, \*=, /=, +=, -=, <<=, >>=, \|=, ^=
- Operator \*\*= added, a \*\*= b converted to a = a \*\* b
- Operator @= added, M3 @= M2 converted to M3 = M3 @ M2, same as for other augmented assignment ops
- Compilation error report now contains detailed import sequence
- Enhancement for issue #281: tuple keys allowed for dictionaries
- Enhancement for issue #26: super () added for unique path to single ancestor method
- Fix for issue #279: TypeError exists both in Python and JavaScrip, needs alias
- Fix for issue #277: Alias needed for new
- Fix for issue #274: Cannot delete unqualified property in strict mode
- Fix for issue #268: Module import trace missing in error messages
- Autotest for regular expression module made part of shipment test and CI test. Some parts commented out, marked with @JdeH
- Documentation updated, also on-line
- Fix for issue #256: Parenthesis aren't translated (before dot, e.g. in return)
- Option -b (or --blind) added to shipment test. Running it with -c (or --clean) -b (or --blind) will not show anything, just clean repo by removing all generated files. Meant for usage before a commit.
- [Release Paris (PyPi v3.6.4, GitHub #14): Support for Python 3.6, div. fixes and enhancements]
- Function globals () is now available to dynamically get and set module attribs, issue #251
- Demo for cyclejs was added, also to the shipment test
- Enhancement for issue #247: One web page can now hold multiple Transcrypt apps
- Regular expression module finished! (issue #98)
- Fixes for issues #254 and #252, both having to do with sourcemap being one line off in else clause
- Emulation of sync console I/O for educational purposes, text only
- Autotest output now in tabular form for easy comparison, incl. source line nrs
- Fix for issue #178: List Comprehensions / Operator Precedence Bug
- Div. enhancements and fixes for CI tests
- Enhancement for issue #139: 'yield from' now supported.
- Enhancement for issue #89 and #149: __getattr__ and __setattr__ are now supported, requiring the -e 6 switch. Testlet 'proxies' added.
- New aliases added to prevent name clashes. The orignal name can always be reached by prepending \js_. So e.g. if you need 'clear' in JS, use 'js_clear' in Python. A complete list of aliases is in the docs. Any alias can be undefined to maintain backward compatibility, e.g __pragma__ ('noalias', 'clear').
- Enhancement for issue #169: Add support for float('inf') and float('-inf')

Known bugs in latest commits
============================

None

Other packages you might like
=============================

- Htmltree - effective, minimalistic HTML generator running both on the server using CPython and Bottle and on the client using Transcrypt: https://github.com/Michael-F-Ellis/NearlyPurePythonWebAppDemo (demo) and https://github.com/Michael-F-Ellis/htmltree (package).
- Numscrypt - port of a microscopic part of NumPy to Transcrypt, using JavaScript typed arrays: https://github.com/QQuick/Numscrypt
- SimPyLC - PLC simulator with Arduino code generation: https://github.com/QQuick/SimPyLC
