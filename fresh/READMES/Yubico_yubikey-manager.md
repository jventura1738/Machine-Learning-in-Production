== YubiKey Manager CLI
image:https://github.com/Yubico/yubikey-manager/workflows/build/badge.svg["Build Status", link="https://github.com/Yubico/yubikey-manager/actions"]

Python 3.6 (or later) library and command line tool for configuring a YubiKey.
If you're looking for the full graphical application, which also includes the command line tool, it's https://developers.yubico.com/yubikey-manager-qt/[here].

=== Usage
For more usage information and examples, see the https://support.yubico.com/support/solutions/articles/15000012643-yubikey-manager-cli-ykman-user-guide[YubiKey Manager CLI User Manual].

....
Usage: ykman [OPTIONS] COMMAND [ARGS]...

  Configure your YubiKey via the command line.

  Examples:

    List connected YubiKeys, only output serial number:
    $ ykman list --serials

    Show information about YubiKey with serial number 0123456:
    $ ykman --device 0123456 info

Options:
  -v, --version                   Show version information about the app
  -d, --device SERIAL             Specify which YubiKey to interact with by serial number.
  -l, --log-level [DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  Enable logging at given verbosity level.
  --log-file FILE                 Write logs to the given FILE instead of standard error; ignored
                                  unless --log-level is also set.

  -r, --reader NAME               Use an external smart card reader. Conflicts with --device and list.
  --diagnose                      Show diagnostics information useful for troubleshooting.
  -h, --help                      Show this message and exit.

Commands:
  info     Show general information.
  list     List connected YubiKeys.
  config   Enable/Disable applications.
  fido     Manage the FIDO applications.
  oath     Manage the OATH Application.
  openpgp  Manage the OpenPGP Application.
  otp      Manage the OTP Application.
  piv      Manage the PIV Application.
....

The `--help` argument can also be used to get detailed information about specific
subcommands:

    ykman oath --help

=== Installation
YubiKey Manager can be installed independently of platform by using pip (or
equivalent):

  pip install --user yubikey-manager

On Linux platforms you will need `pcscd` installed and running to be able to
communicate with a YubiKey over the SmartCard interface. Additionally, you may
need to set permissions for your user to access YubiKeys via the HID interfaces.
More information available link:doc/Device_Permissions.adoc[here].

Some of the libraries used by yubikey-manager have C-extensions, and may require
additional dependencies to build, such as http://www.swig.org/[swig] and
potentially https://pcsclite.alioth.debian.org/pcsclite.html[PCSC lite].

=== Pre-build packages
Pre-built packages specific to your platform may be available from Yubico or
third parties. Please refer to your platforms native package manager for
detailed instructions on how to install, if available.

==== Windows
The command line tool ykman.exe is provided as part of the installer for the
https://developers.yubico.com/yubikey-manager-qt/[YubiKey Manager] on Windows.

==== MacOS
Packages for MacOS are available from Homebrew and MacPorts.

==== Linux
Packages are available for several Linux distributions by third party package
maintainers.
Yubico also provides packages for Ubuntu in the yubico/stable PPA (for amd64
ONLY, other architectures such as arm should use the general `pip` instructions
above instead):

  $ sudo apt-add-repository ppa:yubico/stable
  $ sudo apt update
  $ sudo apt install yubikey-manager

==== Source
To install from source, see the link:doc/Development.adoc[development]
instructions.

=== Shell completion

Experimental shell completion for the command line tool is available, provided
by the underlying CLI library (`click`) but it is not enabled by default. To
enable it, run this command once (for Bash):

  $ source <(_YKMAN_COMPLETE=bash_source ykman | sudo tee /etc/bash_completion.d/ykman)

More information on shell completion is available here:
https://click.palletsprojects.com/en/8.0.x/shell-completion

NOTE: If your version of the Click dependency is older than 8.0 you need to use
`source_bash` for the variable instead.
