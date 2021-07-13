[[http://hackage.haskell.org/package/xmobar][https://img.shields.io/hackage/v/xmobar.svg]]

* About

Xmobar is a minimalistic status bar. It was originally designed and
implemented by Andrea Rossato to work with [[http://xmonad.org][xmonad]], but it is actually
usable with any window manager.

Xmobar was inspired by the [[http://tuomov.iki.fi/software/][Ion3]] status bar, and supports similar
features, like dynamic color management, icons, output templates, and
extensibility through plugins.

These are some xmobar [[file:doc/screenshots][screenshots]] using the author's configuration:

[[file:doc/screenshots/xmobar-top.png]]

[[file:doc/screenshots/xmobar-bottom.png]]

[[file:doc/screenshots/xmobar-exwm.png]]

This is the [[https://xmobar.org/changelog.html][changelog]] for recent releases.

* Installation
** From your Systems Package Manager

Xmobar is probably available from your distributions package manager!
Most distributions compile xmobar with the =all_extensions= flag, so you
don't have to.

*** Arch Linux

#+begin_src shell
  pacman -S xmobar
#+end_src

*** Debian/Ubuntu based

#+begin_src shell
  apt install xmobar
#+end_src

*** OpenSUSE

#+begin_src shell
  zypper install xmobar
#+end_src

*** Void Linux

#+begin_src shell
  xbps-install xmobar
#+end_src

*** Gentoo
#+begin_src shell
  emerge --ask xmobar
#+end_src

** Using cabal-install

Xmobar is available from [[http://hackage.haskell.org/package/xmobar/][Hackage]], and you can install it using
=cabal-install=:

#+begin_src shell
  cabal install xmobar
#+end_src

Starting with version 0.35.1, xmobar now requires at least GHC version
8.4.x. to build. See [[https://github.com/jaor/xmobar/issues/461][this issue]] for more information.

See [[file:doc/compiling.org][compiling]] for a list of optional compilation flags that will enable
some optional plugins. For instance, to install xmobar with all the
bells and whistles (this is probably what you want), use:

#+begin_src shell
  cabal install xmobar --flags="all_extensions"
#+end_src

** From source

See [[file:doc/compiling.org][compiling]].

* Running xmobar

You can run xmobar with:

#+begin_src shell
  xmobar /path/to/config &
#+end_src

or

#+begin_src shell
  xmobar &
#+end_src

if you have the default configuration file saved as
=$XDG\_CONFIG\_HOME/xmobar/xmobarrc= (defaulting to
=~/.config/xmobar/xmobarrc=), or =~/.xmobarrc=.

** Signal Handling

Since 0.14 xmobar reacts to SIGUSR1 and SIGUSR2:

- After receiving SIGUSR1 xmobar moves its position to the next screen.

- After receiving SIGUSR2 xmobar repositions itself on the current
  screen.

* Configuration and Further Links

- If you want to jump straight into configuring xmobar, head over to the
  [[./doc/quick-start.org][quick-start]] guide.

- If you want to get a detailed overview of all available plugins and
  monitors, visit the [[./doc/plugins.org][plugins]] file.

- If you want to know how to contribute to the xmobar project, check out
  [[contributing.org][contributing]].

- If you want to write your own plugins, see [[./doc/write-your-own-plugin.org][write-your-own-plugin]].

* Authors and credits

Andrea Rossato originally designed and implemented xmobar up to version
0.11.1. Since then, it is maintained and developed by [[https://jao.io][jao]], with the help
of the greater xmobar and Haskell communities.

In particular, xmobar incorporates patches by Mohammed Alshiekh, Alex
Ameen, Axel Angel, Dhananjay Balan, Claudio Bley, Dragos Boca, Ben
Boeckel, Ivan Brennan, Duncan Burke, Roman Cheplyaka, Patrick Chilton,
Antoine Eiche, Nathaniel Wesley Filardo, John Goerzen, Reto Hablützel,
Juraj Hercek, Tomáš Janoušek, Ada Joule, Spencer Janssen, Roman Joost,
Jochen Keil, Sam Kirby, Lennart Kolmodin, Krzysztof Kosciuszkiewicz,
Dmitry Kurochkin, Todd Lunter, Vanessa McHale, Robert J. Macomber,
Dmitry Malikov, David McLean, Joan MIlev, Marcin Mikołajczyk, Dino
Morelli, Tony Morris, Eric Mrak, Thiago Negri, Edward O'Callaghan,
Svein Ove, Martin Perner, Jens Petersen, Alexander Polakov, Sibi
Prabakaran, Pavan Rikhi, Petr Rockai, Andrew Emmanuel Rosa,
Sackville-West, Amir Saeid, Markus Scherer, Daniel Schüssler, Olivier
Schneider, Alexander Shabalin, Valentin Shirokov, Peter Simons,
Alexander Solovyov, Will Song, John Soros, Felix Springer, Travis
Staton, Artem Tarasov, Samuli Thomasson, Edward Tjörnhammar, Sergei
Trofimovich, Thomas Tuegel, John Tyree, Jan Vornberger, Anton
Vorontsov, Daniel Wagner, Zev Weiss, Phil Xiaojun Hu, Edward Z. Yang
and Norbert Zeh.

** Thanks

*Andrea Rossato*:

Thanks to Robert Manea and Spencer Janssen for their help in
understanding how X works. They gave me suggestions on how to solve many
problems with xmobar.

Thanks to Claus Reinke for make me understand existential types (or at
least for letting me think I grasp existential types...;-).

*jao*:

Thanks to Andrea for creating xmobar in the first place, and for giving
me the chance to contribute.

* Related

- To understand the internal mysteries of xmobar you may try reading
  [[https://wiki.haskell.org/X_window_programming_in_Haskell][this tutorial]] on X Window Programming in Haskell.

* License

This software is released under a BSD-style license. See [[https://github.com/jaor/xmobar/raw/master/license][license]] for
more details.

Copyright © 2010-2020 Jose Antonio Ortega Ruiz

Copyright © 2007-2010 Andrea Rossato
