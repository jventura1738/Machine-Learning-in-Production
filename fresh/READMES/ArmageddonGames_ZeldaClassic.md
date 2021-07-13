# Zelda Classic
Zelda Classic is a game and editing tool that lets you create custom Legend of Zelda quests.

Homepage:
http://zeldaclassic.com

The homepage contains information about the latest release, links to the latest binaries, and a repository of custom quests for you to enjoy. 

This repository contains the Zelda Classic source code, for use by the Zelda Classic developers and advanced users wanting to port ZC to new platforms. You do not need to download or compile the source if you want to play Zelda Classic or make quests on Windows, OS X, or (Debian) Linux.

## Building the Source

Because of Zelda Classic's extended development history and dependency on legacy libraries, the build process is somewhat involved. The instructions here are not comprehensive, but are intended to help you get started.

### General Comments

**1))** Zelda Classic uses CMake to build the source. Before getting started, you will need to install CMake (version 3.5 or later.) The scripts have been tested on the following operating systems and toolchains:

- **Windwos XP with MSVC 2008**
- **Windows 10 with MSVC 2016**
- **Ubuntu 16.04 with g++ 5.4**

You may need to tweak the configuration settings for other platforms.

**2))** The Zelda Classic project includes three executables and one library:
 - the zcsound library, which is used by all the other binaries;
 - zelda, the Zelda Classic player;
 - zquest, the Zelda Classic level editor;
 - romview, a utility for ripping tiles from SNES ROMs.
 
The included build scripts will build all four targets.

**3))** Included in this repository are pre-built libraries for many of ZC's dependencies, including Allegro and several Allegro add-on libraries for handling sound. These binaries are included for the most common platforms for convenience of the developers, but if you are using a different operating system or toolchain you may need to rebuild these binaries from source. There are (currently) no automated scripts for doing this, but the source packages are included in the `/other` directory.

Zelda Classic requires a modified version of the Allegro 4.2.2 library. Again, pre-built library binaries are available in `/libs`, and if you need to rebuild the library from source, it is contained in `./allegro/fixed/all422-fixed.zip`. A stripped-down version of the fixed library, containing only the header files needed to compile ZC, is in `./allegro`. **Do not try to link Zelda Classic against the standard 4.2.2 Allegro library. You must use the pre-built binaries, or the modified source.**

**4))** Zelda Classic works **only** when compiled for a 32-bit architecture (but the compiled binaries will run fine on 64-bit operating systems.) This means that to successfully compile ZC, you must set your compiler to generate 32-bit code, and you must **obtain 32-bit versions of all external libraries** (or build them yourself from source). For example, on 64-bit Ubuntu you may need to install the packages g++-multilib, libx11-dev:i386, libxext-dev:i386, libxcursor-dev:i386, libxxf86vm-dev:i386, libxpm-dev:i386, libasound2-dev:i386, and possibly others. If you are getting linker errors, check carefully for messages about binary incompatibility with the external libraries.

**5))** The ZScript parser included with ZQuest uses Flex and Bison to auto-generate its source code. You must download and install Flex and Bison to compile ZQuest with ZScript support. If you do not have these tools, compilation will not fail, but CMake will issue a warning and your ZQuest binary will be compiled without the ability to compile ZScripts.

For Windows user, win-flex and win-bison will work fine. Be sure to add the folder containing the binaries (e.g. `win-flex.exe`) to your PATH environment variable.

CMake will issue a warning if it cannot find Flex or Bison on your system.

### Quick-start: Windows with MSVC

Download CMake and run the CMake GUI. It will prompt your for the location of the source code, and the location in which to build the binaries. Specify the root (the folder containing this file) for the former and the `build` folder for the latter.

Click "Generate." This will create a Visual Studio project file for you in the build directory. You can then open up the project file in MSVC and do editing/compilation/debugging in MSVC. You do not need to touch CMake again unless you want to change project configuration options or add/remove source files.

### Quick-start: Linux with gcc

Ensure you have CMake 3.5+ install and execute the following commands:
```
cd build
cmake ..
make
```

Binaries will be created in the `build` folder.

## Running the Compiled Binaries

The compiled binaries **will not run** on their own without support files. These files are not (currently) included in this repository, due to copyright concerns. To run the compiled source, download the latest binary package from the project homepage, and copy the binaries from `build` into a folder also containing all of the data files from the binary package.

## Contributing to Zelda Classic

We encourage third-party submission of patches and new features! If you're interesting in contributing to Zelda Classic's development, please read the CONTRIBUTE file.

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.


