About
-----

Kore (https://kore.io) is an easy to use web application platform for
writing scalable web APIs in C. Its main goals are security, scalability
and allowing rapid development and deployment of such APIs.

Because of this Kore is an ideal candidate for building robust, scalable and secure web things.

Key Features
------------
* Supports SNI
* Supports HTTP/1.1
* Websocket support
* Privseps by default
* TLS enabled by default
* Optional background tasks
* Built-in parameter validation
* Optional asynchronous PostgreSQL support
* Optional support for page handlers in Python
* Reload private keys and certificates on-the-fly
* Automatic X509 certificates via ACME (with privsep)
* Private keys isolated in separate process (RSA and ECDSA)
* Default sane TLS ciphersuites (PFS in all major browsers)
* Modules can be reloaded on-the-fly, even while serving content
* Worker processes sandboxed on OpenBSD (pledge) and Linux (seccomp)
* Event driven (epoll/kqueue) architecture with per CPU worker processes
* Build your web application as a precompiled dynamic library or single binary

And lots more.

License
-------
* Kore is licensed under the ISC license

Documentation
--------------
[Read the documentation](https://docs.kore.io/4.1.0/)

Performance
-----------
Read the [benchmarks](https://blog.kore.io/posts/benchmarks) blog post.

Platforms supported
-------------------
* Linux
* OpenBSD
* FreeBSD
* MacOS

Kore only supports x64, arm and aarch64 architectures.

Building Kore
-------------
Clone this repository or get the latest release at [https://kore.io/releases/4.1.0](https://kore.io/releases/4.1.0).

Requirements
* openssl 1.1.1 or libressl 3.x

Requirement for asynchronous curl (optional)
* libcurl (7.64.0 or higher)

Requirements for background tasks (optional)
* pthreads

Requirements for pgsql (optional)
* libpq

Requirements for python (optional)
* Python 3.6+

Normal compilation and installation:

```
$ cd kore
$ make
# make install
```

If you would like to build a specific flavor, you can enable
those by setting a shell environment variable before running **_make_**.

* ACME=1 (compiles in ACME support)
* CURL=1 (compiles in asynchronous curl support)
* TASKS=1 (compiles in task support)
* PGSQL=1 (compiles in pgsql support)
* DEBUG=1 (enables use of -d for debug)
* NOHTTP=1 (compiles Kore without HTTP support)
* NOOPT=1 (disable compiler optimizations)
* JSONRPC=1 (compiles in JSONRPC support)
* PYTHON=1 (compiles in the Python support)

Note that certain build flavors cannot be mixed together and you will just
be met with compilation errors.

Example applications
-----------------
You can find example applications under **_examples/_**.

The examples contain a README file with instructions on how
to build or use them.

Mailing lists
-------------

**patches@kore.io** - Send patches here, preferably inline.

**users@kore.io** - Questions regarding kore.


If you want to signup to those mailing lists send an empty email to
	listname+subscribe@kore.io


Other mailboxes (these are **not** mailing lists):

**security@kore.io** - Mail this email if you think you found a security problem.

**sponsor@kore.io** - If your company would like to sponsor part of Kore development.

More information can be found on https://kore.io/
