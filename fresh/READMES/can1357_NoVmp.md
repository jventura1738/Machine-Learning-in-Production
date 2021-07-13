<p align="center">
  <a href="https://www.vtil.org/">
    <img width="256" heigth="256" src="https://raw.githubusercontent.com/can1357/NoVmp/master/assets/logo.png">
  </a>
  
  <h1 align="center">NoVmp</h1>
  
  <p align="center">
    <a href="https://ci.appveyor.com/project/can1357/NoVmp">
      <img src="https://img.shields.io/appveyor/build/can1357/NoVmp?logo=appveyor&style=flat-square" alt="appveyor-ci"/>
    </a>
    <a href="https://github.com/can1357/NoVmp/blob/master/LICENSE.md">
      <img src="https://img.shields.io/github/license/can1357/NoVmp.svg?style=flat-square" alt="license"/>
    </a>
  </p>
  
  <p align="center">
    A static devirtualizer for VMProtect x64 3.x powered by VTIL.
  </p>
</p>

### VMProtect? Nope.
NoVmp is a project devirtualizing VMProtect x64 3.0 - 3.5 (latest) into optimized VTIL and optionally recompiling back to x64 using the [Virtual-machine Translation Intermediate Language](https://github.com/vtil-project/VTIL-Core) library. It is rather experimental and is mostly a PoC I wanted to release. Most things can be improved especially with the new NativeLifters repo, but it did not exist back in the time this was written.

# Usage
NoVmp  accepts **unpacked binaries**, so if your binary is packed you'll have to dump it first, additionally if you did dump it using a tool like Scylla, you'll have to provide the original image base using the `-base` parameter like so:

`-base 0x14000000` 

By default NoVmp will parse every single jump into a VM, if you are only interested in a number of **specific** virtualized routines you can use the `-vms` parameter like so with relative virtual addresses:

`-vms 0x729B81 0x72521`

These addresses should be pointing at the VMEnter, as shown below:

![VMEnter](https://raw.githubusercontent.com/can1357/NoVmp/master/assets/vmenter.png)

By default section discovery is automatic, but in case your calls are not being chained you should try adding the VMProtect section name into the section list using `-sections` as shown below:

`-sections .xxx0 .yyy0`

Note that the `.<vmp>1` section is the merged VMProtect DLL which should not be inputted.

Additionally you can use any of the following switches:
- `-noopt`: Disables optimization.
- `-opt:constant`: Optimizes the VMProtect Ultra constant obfuscation out.
- `-experimental:recompile`: Enables the experimental x64 compiler.

# Known bugs
- Known issues from VTIL-Core, mainly the lack of jump table support and propagation passes taking too long/not being great which are being worked on.
- Binaries compiled with relocations stripped are not fully supported yet.
- Experimental compiler is a borderline broken demo, issues related to it should not be submitted as it'll be reworked and will be in VTIL-Core.

# License
NoVmp is licensed under the GNU General Public License v3.
