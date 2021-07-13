![alt tag](https://cdn.quantconnect.com/web/i/20180601-1615-lean-logo-small.png)
=========

[![Build Status](https://github.com/QuantConnect/Lean/workflows/Build%20%26%20Test%20Lean/badge.svg)](https://github.com/QuantConnect/Lean/actions?query=workflow%3A%22Build%20%26%20Test%20Lean%22) &nbsp;&nbsp;&nbsp; [![LEAN Forum](https://img.shields.io/badge/debug-LEAN%20Forum-53c82b.svg)](https://www.quantconnect.com/forum/discussions/1/lean) &nbsp;&nbsp;&nbsp; [![Slack Chat](https://img.shields.io/badge/chat-Slack-53c82b.svg)](https://www.quantconnect.com/slack)


[Lean Home - https://www.quantconnect.com/lean][1] | [Documentation][2] | [Download Zip][3] | [Docker Hub][8]
 
----------
 
## Introduction ##
  
Lean Engine is an open-source algorithmic trading engine built for easy strategy research, backtesting and live trading. We integrate with common data providers and brokerages so you can quickly deploy algorithmic trading strategies.

The core of the LEAN Engine is written in C#; but it operates seamlessly on Linux, Mac and Windows operating systems. It supports algorithms written in Python 3.6 or C#. Lean drives the web-based algorithmic trading platform [QuantConnect][4].

 
## Proudly Sponsored By ##

Want your company logo here? [Sponsor LEAN](https://github.com/sponsors/QuantConnect) to be part of radically open algorithmic-trading innovation.


## QuantConnect is Hiring! ##
Join the team and solve some of the most difficult challenges in quantitative finance. If you are passionate about algorithmic trading we'd like to hear from you. The below roles are open in our Seattle, WA office. When applying, make sure to mention you came through GitHub: 

- [**C# Engineer**](https://www.getonbrd.com/jobs/programming/c-c-software-engineer-quantconnect-remote): Contribute remotely to the core of LEAN through the open-source project LEAN. 

- [**UX Developer**](https://www.getonbrd.com/jobs/programming/full-stack-engineer-quantconnect-remote): Collaborate with QuantConnect to develop a world-leading online experience for a community of developers from all over the world.  

## System Overview ##

![alt tag](Documentation/2-Overview-Detailed-New.png)

The Engine is broken into many modular pieces which can be extended without touching other files. The modules are configured in config.json as set "environments". Through these environments, you can control LEAN to operate in the mode required. 

The most important plugins are:

 - **Result Processing** (IResultHandler)
   > Handle all messages from the algorithmic trading engine. Decide what should be sent, and where the messages should go. The result processing system can send messages to a local GUI, or the web interface.

 - **Datafeed Sourcing** (IDataFeed)
   > Connect and download the data required for the algorithmic trading engine. For backtesting this sources files from the disk, for live trading, it connects to a stream and generates the data objects.

 - **Transaction Processing** (ITransactionHandler)
   > Process new order requests; either using the fill models provided by the algorithm or with an actual brokerage. Send the processed orders back to the algorithm's portfolio to be filled.

 - **Realtime Event Management** (IRealtimeHandler)
   > Generate real-time events - such as the end of day events. Trigger callbacks to real-time event handlers. For backtesting, this is mocked-up a works on simulated time. 
 
 - **Algorithm State Setup** (ISetupHandler)
   > Configure the algorithm cash, portfolio and data requested. Initialize all state parameters required.

These are all configurable from the config.json file in the Launcher Project.

## Developing with Lean CLI ##

QuantConnect recommends using [Lean CLI](https://github.com/QuantConnect/lean-cli) for local algorithm development. This is because it is a great tool for working with your algorithms locally while still being able to deploy to the cloud and have access to Lean data. It is also able to run algorithms on your local machine with your data through our official docker images.

Reference QuantConnects documentation on Lean CLI [here](https://www.quantconnect.com/docs/v2/lean-cli/getting-started/lean-cli)

## Installation Instructions ##

This section will cover how to install lean locally for you to use in your own environment.

Refer to the following readme files for a detailed guide regarding using your local IDE with Lean:
* [VS Code](.vscode/readme.md)
* [VS](.vs/readme.md)
  

To install locally, download the zip file with the [latest master](https://github.com/QuantConnect/Lean/archive/master.zip) and unzip it to your favorite location. Alternatively, install [Git](https://git-scm.com/downloads) and clone the repo:

```
git clone https://github.com/QuantConnect/Lean.git
cd Lean
```

### macOS 

- Install [Visual Studio for Mac](https://www.visualstudio.com/vs/visual-studio-mac/)
- Open `QuantConnect.Lean.sln` in Visual Studio

Visual Studio will automatically start to restore the Nuget packages. If not, in the menu bar, click `Project > Restore NuGet Packages`.

- In the menu bar, click `Run > Start Debugging`.

Alternatively, run the compiled `dll` file. First, in the menu bar, click `Build > Build All`, then:
```
cd Lean/Launcher/bin/Debug
dotnet QuantConnect.Lean.Launcher.dll
```

### Linux (Debian, Ubuntu)

- Install [dotnet 5](https://docs.microsoft.com/en-us/dotnet/core/install/linux):
- Compile Lean Solution:
```
dotnet QuantConnect.Lean.sln
```
- Run Lean:
```
cd Launcher/bin/Debug
dotnet QuantConnect.Lean.Launcher.dll
```
- Interactive Brokers set up details

Make sure you fix the `ib-tws-dir` and `ib-controller-dir` fields in the `config.json` file with the actual paths to the TWS and the IBController folders respectively.

If after all you still receive connection refuse error, try changing the `ib-port` field in the `config.json` file from 4002 to 4001 to match the settings in your IBGateway/TWS.

### Windows

- Install [Visual Studio](https://www.visualstudio.com/en-us/downloads/download-visual-studio-vs.aspx)
- Open `QuantConnect.Lean.sln` in Visual Studio
- Build the solution by clicking Build Menu -> Build Solution (this should trigger the Nuget package restore)
- Press `F5` to run

### Python Support

A full explanation of the Python installation process can be found in the [Algorithm.Python](https://github.com/QuantConnect/Lean/tree/master/Algorithm.Python#quantconnect-python-algorithm-project) project.

### Local-Cloud Hybrid Development. 

Seamlessly develop locally in your favorite development environment, with full autocomplete and debugging support to quickly and easily identify problems with your strategy. For more information please see the [CLI Home](https://www.quantconnect.com/cli).

## Issues and Feature Requests ##

Please submit bugs and feature requests as an issue to the [Lean Repository][5]. Before submitting an issue please read others to ensure it is not a duplicate.

## Mailing List ## 

The mailing list for the project can be found on [LEAN Forum][6]. Please use this to request assistance with your installations and setup questions.

## Contributors and Pull Requests ##

Contributions are warmly very welcomed but we ask you to read the existing code to see how it is formatted, commented and ensure contributions match the existing style. All code submissions must include accompanying tests. Please see the [contributor guide lines][7].

All accepted pull requests will get a 2mo free Prime subscription on QuantConnect. Once your pull-request has been merged write to us at support@quantconnect.com with a link to your PR to claim your free live trading. QC <3 Open Source.

## Acknowledgements ##

The open-sourcing of QuantConnect would not have been possible without the support of the Pioneers. The Pioneers formed the core 100 early adopters of QuantConnect who subscribed and allowed us to launch the project into open source. 

Ryan H, Pravin B, Jimmie B, Nick C, Sam C, Mattias S, Michael H, Mark M, Madhan, Paul R, Nik M, Scott Y, BinaryExecutor.com, Tadas T, Matt B, Binumon P, Zyron, Mike O, TC, Luigi, Lester Z, Andreas H, Eugene K, Hugo P, Robert N, Christofer O, Ramesh L, Nicholas S, Jonathan E, Marc R, Raghav N, Marcus, Hakan D, Sergey M, Peter McE, Jim M, INTJCapital.com, Richard E, Dominik, John L, H. Orlandella, Stephen L, Risto K, E.Subasi, Peter W, Hui Z, Ross F, Archibald112, MooMooForex.com, Jae S, Eric S, Marco D, Jerome B, James B. Crocker, David Lypka, Edward T, Charlie Guse, Thomas D, Jordan I, Mark S, Bengt K, Marc D, Al C, Jan W, Ero C, Eranmn, Mitchell S, Helmuth V, Michael M, Jeremy P, PVS78, Ross D, Sergey K, John Grover, Fahiz Y, George L.Z., Craig E, Sean S, Brad G, Dennis H, Camila C, Egor U, David T, Cameron W, Napoleon Hernandez, Keeshen A, Daniel E, Daniel H, M.Patterson, Asen K, Virgil J, Balazs Trader, Stan L, Con L, Will D, Scott K, Barry K, Pawel D, S Ray, Richard C, Peter L, Thomas L., Wang H, Oliver Lee, Christian L..


  [1]: https://www.quantconnect.com/lean "Lean Open Source Home Page"
  [2]: https://www.quantconnect.com/lean/docs "Lean Documentation"
  [3]: https://github.com/QuantConnect/Lean/archive/master.zip
  [4]: https://www.quantconnect.com "QuantConnect"
  [5]: https://github.com/QuantConnect/Lean/issues
  [6]: https://www.quantconnect.com/forum/discussions/1/lean
  [7]: https://github.com/QuantConnect/Lean/blob/master/CONTRIBUTING.md
  [8]: https://hub.docker.com/orgs/quantconnect/repositories

