Linux kernel
============

There are several guides for kernel developers and users. These guides can
be rendered in a number of formats, like HTML and PDF. Please read
Documentation/admin-guide/README.rst first.

In order to build the documentation, use ``make htmldocs`` or
``make pdfdocs``.  The formatted documentation can also be read online at:

    https://www.kernel.org/doc/html/latest/

There are various text files in the Documentation/ subdirectory,
several of them using the Restructured Text markup notation.
See Documentation/00-INDEX for a list of what is contained in each file.

Please read the Documentation/process/changes.rst file, as it contains the
requirements for building and running the kernel, and information about
the problems which may result by upgrading your kernel.

============

The WSL 2 Linux kernel repo provides the additional infrastructure necessary 
to build and release the kernel component of WSL 2. It was never designed to 
replace the current existing community and feedback channels for WSL, 
especially through: https://github.com/microsoft/WSL. This is why we are not 
accepting issues or pull requests through this repository.
 
If you have an issue relating to WSL, or the WSL 2 Linux kernel configuration, 
please report it at the WSL GitHub: would like contribute to or report an issue 
on the WSL2 kernel, please do so at the WSL GitHub:

https://github.com/microsoft/WSL/issues/new/choose 
 
The WSL 2 Linux kernel is based on the Linux version from 
https://www.kernel.org/. If you would like to contribute to or report an issue 
on the Linux kernel in general, please do so on the upstream Linux GitHub:  

https://www.kernel.org/doc/html/latest/process/submitting-patches.html

