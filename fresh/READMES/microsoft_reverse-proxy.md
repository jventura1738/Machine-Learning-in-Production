# Welcome to the YARP project

YARP (which stands for "Yet Another Reverse Proxy") is a project to create a reverse proxy server. We found a bunch of internal teams at Microsoft who were either building a reverse proxy for their service or had been asking about APIs and tech for building one, so we decided to get them all together to work on a common solution, this project.

YARP is a reverse proxy toolkit for building fast proxy servers in .NET using the infrastructure from ASP.NET and .NET. The key differentiator for YARP is that it's been designed to be easily customized and tweaked to match the specific needs of each deployment scenario. 

We expect YARP to ship as a library and project template that together provide a robust, performant proxy server. Its pipeline and modules are designed so that you can then customize the functionality for your needs. For example, while YARP supports configuration files, we expect that many users will want to manage the configuration programmatically based on their own backend configuration management system, YARP will provide a configuration API to enable that customization in-proc.  YARP is designed with customizability as a primary scenario, rather than requiring you to break out to script or having to rebuild from source.

# Updates

For regular updates, see our [releases page](https://github.com/microsoft/reverse-proxy/releases). Subscribe to release notifications on this repository to be notified of future updates (Watch -> Custom -> Releases).

# Build

To build the repo, you should only need to run `build.cmd` (on Windows) or `build.sh` (on Linux or macOS). The script will download the .NET SDK and build the solution.

For VS on Windows, you can run the `startvs.cmd` script to launch Visual Studio on Windows using the appropriate local copy of the .NET SDK.

To set up local development with Visual Studio, Visual Studio for Mac or Visual Studio Code, you need to put the local copy of the .NET SDK in your `PATH` environment variable. Our `Restore` script fetches the latest build of .NET 5 and installs it to a `.dotnet` directory *within* this repository.

We provide some scripts to set all this up for you. Just follow these steps:

1. Run the `restore.cmd`/`restore.sh` script to fetch the required .NET SDK locally (to the `.dotnet` directory within this repo)
1. "Dot-source" the `activate` script to put the local .NET SDK on the PATH
    1. For PowerShell, run: `. .\activate.ps1` (note the leading `. `, it is required!)
    1. For Linux/macOS/WSL, run: `. ./activate.sh`
    1. For CMD, there is no supported script. You can manually add the `.dotnet` directory **within this repo** to your `PATH`. Ensure `where dotnet` shows a path within this repository!
1. Launch VS, VS for Mac, or VS Code!

When you're done, you can run the `deactivate` function to undo the changes to your `PATH`.

If you're having trouble building the project, or developing in Visual Studio, please file an issue to let us know and we'll help out (and fix our scripts/tools as needed)!

# Getting started

- See our [Getting Started](https://microsoft.github.io/reverse-proxy/articles/getting-started.html) docs.
- Try our [previews](https://github.com/microsoft/reverse-proxy/releases).
- Try our latest [daily build](/docs/DailyBuilds.md).

# Roadmap

Coming Soon

# Reporting security issues and bugs

YARP is a preview project, and as such we expect all users to take responsibility for evaluating the security of their own applications.

Security issues and bugs should be reported privately, via email, to the Microsoft Security Response Center (MSRC) at `secure@microsoft.com`. You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Further information, including [the MSRC PGP key](https://www.microsoft.com/msrc/pgp-key-msrc), can be found at the [Microsoft Security Response Center](https://www.microsoft.com/msrc).

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
