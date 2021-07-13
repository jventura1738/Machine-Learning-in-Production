![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flare-floss)
[![CI status](https://github.com/fireeye/flare-floss/workflows/CI/badge.svg)](https://github.com/fireeye/flare-floss/actions?query=workflow%3ACI+event%3Apush+branch%3Amaster)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE.txt)

<img src="https://raw.githubusercontent.com/fireeye/flare-floss/master/resources/logo.png" width="350"/>

# FireEye Labs Obfuscated String Solver

Rather than heavily protecting backdoors with hardcore packers, many
malware authors evade heuristic detections by obfuscating only key
portions of an executable. Often, these portions are strings and resources
used to configure domains, files, and other artifacts of an infection.
These key features will not show up as plaintext in output of the `strings.exe` utility
that we commonly use during basic static analysis.

The FireEye Labs Obfuscated String Solver (FLOSS) uses advanced
static analysis techniques to automatically deobfuscate strings from
malware binaries. You can use it just like `strings.exe` to enhance
basic static analysis of unknown binaries.

Please review the theory behind FLOSS [here](doc/theory.md). Our [blog post](https://www.fireeye.com/blog/threat-research/2016/06/automatically-extracting-obfuscated-strings.html) talks more about the motivation behind FLOSS and details how the tool works.


## Quick Run
To try FLOSS right away, download a standalone executable file from the releases page:
https://github.com/fireeye/flare-floss/releases

For a detailed description of *installing* FLOSS, review the documentation
 [here](doc/installation.md).


## Usage
Extract obfuscated strings from a malware binary:

    $ floss /path/to/malware/binary

Display the help/usage screen to see all available switches.

    $ ./floss -h

For a detailed description of *using* FLOSS, review the documentation
 [here](doc/usage.md).

For a detailed description of *testing* FLOSS, review the documentation
 [here](doc/test.md).

## Sample Output

```
$ floss malware.bin
FLOSS static ASCII strings
!This program cannot be run in DOS mode.
_YY
RichYY
MdfQ
.text
`.rdata
@.data
.idata
.didat
.reloc
U  F
?;}
A@;E
_^[
HttHt-H
'9U
WS2_32.dll
FreeLibrary
GetProcAddress
LoadLibraryA
GetModuleHandleA
GetVersionExA
MultiByteToWideChar
WideCharToMultiByte
Sleep
GetLastError
DeleteFileA
WriteFile
[..snip...]

FLOSS static UTF-16 strings
,%d

FLOSS decoded 4 strings
WinSta0\Default
Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings
ProxyEnable
ProxyServer

FLOSS extracted 81 stack strings
WinSta0\Default
'%s' executed.
ERR '%s' error[%d].
Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings
ProxyEnable
ProxyServer
wininet.dll
InternetOpenA
0\A4
InternetSetOptionA
InternetConnectA
InternetQueryOptionA
Mozilla/4.0 (compatible; MSIE 7.0; Win32)
-ERR
FILE(%s) wrote(%d).
Invalid ojbect.
SetFilepoint error[%d].
b64_ntop error[%d].
GetFileSize error[%d].
Creates file error[%d].
KCeID5Y/96QTJc1pzi0ZhEBqVG83OnXaL+oxsRdymHS4bFgl7UrWfP2v=wtjNukM
[..snip...]
```
