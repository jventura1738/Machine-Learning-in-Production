Squally
=========
2D Platformer Game for Teaching Game Hacking.

Language: C++

Engine: Cocos-2dx

Platforms: Windows, OSX, and Linux

[Steam Page](https://store.steampowered.com/app/770200/Squally/) / Discord: https://discord.gg/3maVXN5

![Squally Gameplay 1](https://i.imgur.com/M2KMSZ9.png) | ![Squally Gameplay 2](https://i.imgur.com/8jsCkX2.png)
------------ | -------------
![Squally Gameplay 3](https://i.imgur.com/1hvYk3K.png) | ![Squally Gameplay 4](https://i.imgur.com/bOSKa7p.png)
![Squally Gameplay 5](https://i.imgur.com/D9aIKSJ.png) | ![Squally Gameplay 6](https://i.imgur.com/iYUfJGq.png)
![Squally Gameplay 7](https://i.imgur.com/wGVSBFR.png) | ![Squally Gameplay 8](https://i.imgur.com/U7C2fXh.png)

Contributing
------------
To show support and help us finish development, [get the game on Steam](https://store.steampowered.com/app/770200/Squally/).

For those that wish to help with development, just hop over to the Issues tab and look for things to improve:

Issues |
------------ |
[Easy](https://github.com/Squalr/Squally/labels/good%20first%20issue) |
[Intermediate](https://github.com/Squalr/Squally/labels/good%20first%20issue%20%28intermediate%29) |

To edit maps, download [Tiled](https://www.mapeditor.org/). Maps are kept in Resources/Platformer/Maps/*.tmx.

Compiling Squally
------------
To minimize cross-platform effort, we develop Squally using [VsCode](https://code.visualstudio.com/) with the following extensions:
- C/C++ for Visual Studio Code
- CMake Tools
- (Mac only) CodeLLDB is recommended, as this debugger works better than the default. Just be sure to go into Debug > Breakpoints > Disable C++: on throw

You will also need the following software to compile the project:
- Cmake (The CMake Tools extension does not include the cmake binaries)
    - Windows: Download the [installer](https://cmake.org/download/)
    - OSX: Use [Brew](https://brew.sh/) to install Cmake with the command `brew install cmake`
    - Linux: Install via the instructions [here](https://cgold.readthedocs.io/en/latest/first-step/installation.html)
- [Ninja](https://github.com/ninja-build/ninja/wiki/Pre-built-Ninja-packages)
- Python 2.7.x or 3.x -- all scripts should be compatible with either version.

Squally is comprised of several subrepos, including:
- Cocos2d-x
- Spriter2d-x / SpriterPlusPlus
- Breakpad / AFNetworking
- Vcpkg
- SquallyResources*

Additional dependencies are managed using vcpkg.

**Important:** We do not have the legal rights to distribute the art/sound in Squally. To get a copy of the `Resources/Private` folder, copy it from a purchased copy of the game. See the section below for details.

To do a fresh build and pull in dependencies:
```
git clone git@github.com:Squalr/Squally.git
cd Squally
git submodule update --init --recursive .
python dep.py init
```

From here, simply open the Squally/ folder in VsCode and compile using one of the following:
- OSX: Clang 7.0.x
- Windows: MSVC (VS2019 x86)
- Linux: GCC

To update dependencies later:
```
git submodule update --init --recursive .
python dep.py update
```

Getting the Resource Folder
------------
We could not include the `Resources/Private` folder in this repository, because a lot of the art in this game comes from asset stores. This means we have non-exclusive rights to the art, and cannot redistribute it for free. This means the Resources must be copied from a legally purchased copy of the game.

The `Resources/Private` folder in the Steam copy of Squally will correspond to the master branch of this repository.

To gain access to the `Resources/Private` folder being used in develop branch, do the following:
- Open Steam
- Right click on Squally and click Properties
- Go to the BETAS tab
- Opt into the 'resources' beta
- Switch to the Local Files tab
- Click 'browse Local files'
- Copy the `Private` folder into `Squally/Resources` in the git repository you created.
- Important: Revert back to NONE or alpha version of squally -- the 'resources' beta will not launch. Also, if Steam is not updating the files, try restarting Steam.

![Squally resource beta](https://i.imgur.com/012eDxg.png)
![Squally resource folder](https://i.imgur.com/5PaDZiG.png)

For those that contribute significantly to the project, we can give you access to the private `Resources/Private` Github repository. We're doing this sparringly because there are limted seats on Github.

Additional learning resources
------------
Learning game hacking? Check out content from our partner [Guided Hacking](https://guidedhacking.com/)
