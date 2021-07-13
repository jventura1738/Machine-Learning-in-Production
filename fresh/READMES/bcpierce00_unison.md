# Unison File Synchronizer

[![Build Status](https://travis-ci.org/bcpierce00/unison.svg?branch=master)](https://travis-ci.org/bcpierce00/unison)
[![CICD](https://github.com/bcpierce00/unison/workflows/CICD/badge.svg)](https://github.com/bcpierce00/unison/actions?query=workflow%3ACICD)

***Please read this entire README before creating or commenting on a
github issue.  TL;DR: Do not ask questions or ask for help in
issues.***

## About

Unison is a file-synchronization tool for POSIX-compliant systems
(e.g. *BSD and GNU/Linux), macOS and Windows, with the caveat that the
platform must be supported by OCaml.  It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

Unison has been in use for over 20 years and many people use it to
synchronize data they care about.

Unison shares a number of features with tools such as configuration
management packages (CVS, Subversion, git, Mercurial, etc.),
distributed filesystems (Coda, etc.), uni-directional mirroring
utilities (rsync, etc.), and other synchronizers.  However, there are
several points where it differs:

 * Unison runs on almost any system with an OCaml compiler. Moreover,
   Unison works across platforms, allowing you to synchronize a
   Windows laptop with a Unix server, for example.

 * Unlike simple mirroring or backup utilities, Unison can deal with
   updates to both replicas of a distributed directory
   structure. Updates that do not conflict are propagated
   automatically. Conflicting updates are detected and displayed.

 * Unlike many network filesystems, Unison copies data so that
   already-synchronized data can be read and written while offline.

 * Unlike most distributed filesystems, Unison is a user-level program
   that simply uses normal systems calls: there is no need to modify
   the kernel, to have superuser privileges on either host, or to have
   a FUSE implementation.

 * Unison works between any pair of machines connected to the
   internet, typically communicating over ssh, but also directly over
   TCP.  It is careful with network bandwidth, and runs well over slow
   links such as PPP connections. Transfers of small updates to large
   files are optimized using a compression protocol similar to rsync.

 * Unison is resilient to failure. It is careful to leave the replicas
   and its own private structures in a sensible state at all times,
   even in case of abnormal termination or communication failures.

 * Unison has a clear and precise specification.

 * Unison is Free; full source code is available under the GNU Public
   License, Version 3.

Note that only a very small number of people are actively working on
maintaining unison.  An estimate is 2.5 people and 0.1 Full-Time
Equivalents.  This has a substantial impact on the handling of bug
reports and enhancement reports; see below.  Help in terms of
high-quality bug reports, fixes, and proposed changes is very welcome.

While much of Unison activity is now at
https://github.com/bcpierce00/unison/ additional information can be
found at: http://www.cis.upenn.edu/~bcpierce/unison

## Getting Unison

The Unison project provides Unison as source code.  Many packaging
systems (including GNU/Linux distributions) provide binary packages of
Unison.  Results from Continuous Integration builds, while performed
for the purposes of testing, are available for use on a limited set of
platforms.

See the manual in doc/ for building instructions, or read the CI
recipes.  (Currently, this is probably less well explained than it
should be.)

You may be able to find a pre-built binary for your operating system,
version, and CPU type.  For a list of sources, See
https://github.com/bcpierce00/unison/wiki/Downloading-Unison

Generally, you should use the most recent formal release, currently
2.51.X.  Earlier branches (e.g. 2.48) are no longer maintained, and
bug reports are not accepted about these versions.  This is true even
though many packaging systems (including GNU/Linux distributions)
continue to have 2.48.  There are sometimes release candidates.  There
is always the master branch in git, which historically has been quite
stable.

Beware that Unison uses OCaml's built-in data marshalling, and that
this facility is unstable across versions of "ocaml" (the standard
implementation of the OCaml language).  Additionally, Unison has
incompatible changes across minor releases (e.g. 2.48 vs 2.51, but
2.51.2 and 2.51.3 are compatible).  Therefore, you must use the same
Unison minor version built with the same ocaml version on all systems.

## Mailinglists

There are two mailinglists: unison-users and unison-hackers.
Descriptions and instructions are at
https://github.com/bcpierce00/unison/wiki/Mailing-Lists

## Asking for Help and Reporting Bugs

For an expanded discussion of asking for help, see
https://github.com/bcpierce00/unison/wiki/Reporting-Bugs-and-Feature-Requests

The issue tracker is for bug reports and (limited) enhancement
requests.  Specifically, this means that questions and requests for
help are not appropriate as issues; those should be directed to
unison-users (or unison-hackers if the discussion requires reading the
source code).

Unison's product is the source code.  A packaging system having an old
version is not a bug in Unison.  The CI-provided binaries exist for
Continuous Integration and are useful for users as a side benefit.
Therefore, the CI binaries not working on a particular operating
system is not a Unison bug.  (In general, binaries should be provided
by packaging systems.)

A bug means that the reporter can articulate how Unison should have
behaved and say what it did instead, either as a violation of an
explicit specification, or an implicit specification that is likely to
be widely viewed as valid.  Bugs should be phrased as "unison randomly
deletes files outside of the synchronization root", summarizing the
bad behavior (that's humor -- Unison has never even been accused of
doing that!).

An enhancement request should describe how Unison should do something
different or additional, phrased as an imperative as something like
"Change wire protocol to be independent of ocaml compiler version".
Enhancement requests are appropriate if they are clearly articulated,
and would bring benefits to users that are significant compared to
their likely implementation effort.  Speculative or "pie in the sky"
enhancement requests may be closed on the basis that their continued
presence in the issue tracker has too much cognitive load compared to
benefit, especially if the submitter doesn't intend to work on it.

## Development and Submitting Proposed Changes

If you want to play with the internals, have a look at the file
src/ROADMAP.txt for some basic orientation.  Discussion of the source
code, proposed changes, etc. is most appropriate on the unison-hackers
mailinglist.

Proposed code changes are also welcome (as pull requests).  For
significant changes, an enhancement request or bug report is likely in
order to provide the proposed semantics ahead of time.  For changes
that are likely to be widely viewed as clearly desired, that might be
enough.  Others should be discussed on unison-hackers.

Proposed changes should change documentation in concert with code, and
should pass CI.

Unison operates under the widely-used "inbound=outbound" contribution
license process.  Therefore, all contributions to Unison must be
licensed under the project's license, currently GPLv3 (unless a file
under a different license is being modified).  New files of
significance must have a copyright statement and grant permission to
copy under the project's license.  Significant changes should include
copyright statements and/or add authors.  Submitting a pull request or
posting a contribution on a mailinglist is an assertion that the
submitter has the authority to license their changes under the
project's license.  (This paragraph is intended to summarize the
normal conventions, and is not intended to create any new norms.  See
https://sfconservancy.org/blog/2014/jun/09/do-not-need-cla/ for a
longer discussion.)
