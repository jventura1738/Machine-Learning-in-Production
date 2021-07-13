[![Build Status](https://travis-ci.org/ivre/ivre.svg)](https://travis-ci.org/ivre/ivre)
[![Documentation Status](https://readthedocs.org/projects/ivre/badge/?version=latest)](https://doc.ivre.rocks/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0116170aaaa54915a72aad286029250b)](https://app.codacy.com/app/p-l-/ivre)
[![Join the chat at Gitter](https://badges.gitter.im/ivre/ivre.svg)](https://gitter.im/ivre/ivre)
[![Follow on Twitter](https://img.shields.io/twitter/follow/IvreRocks.svg?logo=twitter)](https://twitter.com/IvreRocks)

# IVRE #

<img align="right" src="https://ivre.rocks/logo.png" alt="Logo"/> IVRE
(Instrument de veille sur les réseaux extérieurs) or DRUNK (Dynamic
Recon of UNKnown networks) is a network recon framework, including
tools for passive recon (flow analytics relying on
[Zeek](https://zeek.org/), [Argus](http://qosient.com/argus/),
[Nfdump](https://github.com/phaag/nfdump), and active recon (IVRE uses
[Nmap](http://nmap.org/) to run scans; IVRE can also import XML output
from Nmap and
[Masscan](https://github.com/robertdavidgraham/masscan)), and JSON
output from [ZGrab2](https://github.com/zmap/zgrab2) and
[ZDNS](https://github.com/zmap/zdns/).

The advertising slogans are:

-   (in French): IVRE, il scanne Internet.
-   (in English): Know the networks, get DRUNK!

The names IVRE and DRUNK have been chosen as a tribute to "Le
Taullier".

## Overview ##

You can have a look at the [project homepage](https://ivre.rocks/),
the
**[screenshot gallery](https://doc.ivre.rocks/en/latest/overview/screenshots.html)**,
and the
[quick video introduction](https://www.youtube.com/watch?v=GBu5QMq6ewY)
for an overview of the Web interface.

We have a **demonstration instance**, just [contact us](#contact) to
get an access.

A few
**[blog posts](http://pierre.droids-corp.org/blog/html/tags/ivre.html)**
have been written to show some features of IVRE.

## Documentation ##

[IVRE's documentation](https://doc.ivre.rocks/) is hosted by Read The
Docs, based on files from the [doc/](doc/) directory of the
repository.

On an IVRE web server, the `doc/*` files are available, rendered,
under `/doc/`.

On a system with IVRE installed, you can use a `--help` option with
most IVRE CLI tools, and `help(ivre.module)` with most IVRE Python
sub-modules.

## License ##

IVRE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

IVRE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
[along with IVRE](doc/license.rst). If not, see
[the gnu.org web site](http://www.gnu.org/licenses/).

## Support ##

Try `--help` for the CLI tools, `help()` under Python and the "HELP"
button in the web interface.

Have a look at the
[FAQ](https://doc.ivre.rocks/en/latest/overview/faq.html)!

Feel free to contact the author and offer him a beer if you need help!

If you don't like beer, a good scotch or any other good alcoholic
beverage will do (it is the author's unalienable right to decide
whether a beverage is good or not).

## Contributing ##

Code contributions (pull-requests) are of course welcome!

The project needs scan results and capture files that can be provided
as examples. If you can contribute some samples, or if you want to
contribute some samples and would need some help to do so, or if you
can provide a server to run scans, please contact the author.

## Contact ##

For both support and contribution, the
[repository](https://github.com/ivre/ivre) on Github should be
used: feel free to create a new issue or a pull request!

You can also join the
[Gitter conversation](https://gitter.im/ivre/ivre) (that is the
preferred way to get in touch for questions), or use the e-mail `dev`
on the domain `ivre.rocks`.

## Talking about IVRE ##

### Research ###

If you are using IVRE in you research, please cite it as follows:

Pierre Lalet, Emma Leroy, Florent Monjalet, Camille Mougey, Vincent
Ruello and Vivien Venuti. *IVRE, a network recon framework*.
[https://github.com/ivre/ivre](https://github.com/ivre/ivre),
2011-2021.

Here is the appropriate bibtex entry:

    @MISC{ivre,
        title = {{IVRE}, a network recon framework},
        author={Lalet, Pierre and Leroy, Emma and Monjalet, Florent and Mougey, Camille and Ruello, Vincent and Venuti, Viven},
        url = {https://ivre.rocks/},
        howpublished = {\url{https://github.com/ivre/ivre/}},
        institution = {{ANSSI}: the National Cybersecurity Agency of France and
                       {CEA}: the French Alternative Energies and Atomic Energy Commission},
        year = {2011--2021},
    }

### Technical documents & blog posts ###

You can mention "IVRE, a network recon framework", together with the
project homepage, [https://ivre.rocks/](https://ivre.rocks/) and/or
the repository,
[https://github.com/ivre/ivre](https://github.com/ivre/ivre).

On twitter, you can follow and/or mention
[@IvreRocks](https://twitter.com/IvreRocks).
