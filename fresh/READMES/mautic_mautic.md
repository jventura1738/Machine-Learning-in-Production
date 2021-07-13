[![codecov](https://codecov.io/gh/mautic/mautic/branch/features/graph/badge.svg)](https://codecov.io/gh/mautic/mautic)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-37-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

About Mautic
============
Mautic is the world’s largest open source marketing automation project. With over 200,000 organisations using Mautic and over 1,000 community volunteers, we empower businesses by making it easy to manage their marketing across a range of channels. Stay up to date about initiatives, releases and strategy via our [blog][mautic-blog].

Marketing automation has historically been difficult to implement within organisations. The Mautic Community is an example of open source at its best, offering great software and a vibrant and caring community in which to learn and share knowledge.

Open source means more than open code. Open source provides equality for all and a chance for everyone to improve.

![Mautic](.github/readme_image.png "Mautic Open Source Marketing Automation")

Get Involved
=============
Before we tell you how to install and use Mautic, we like to shamelessly plug our awesome user and developer communities! Users, start [here][get-involved] for inspiration, or follow us on Twitter [@MauticCommunity][twitter] or Facebook [@MauticCommunity][facebook]. Once you’re familiar with using the software, maybe you will share your wisdom with others in our [Slack][slack] channel.

Calling all devs, testers and tech writers! Technical contributions are also welcome. First, read our [general guidelines][contributing] about contributing. If you want to contribute code, read our [CONTRIBUTING.md][contributing-md] or [Contributing Code][contribute-developer] docs then check out the issues with the [T1 label][t1-isssues] to get stuck in quickly and show us what you’re made of.

If you have questions, the Mautic Community can help provide the answers.

Installing and using Mautic
============================

## Supported Versions

| Branch | RC Release | Initial Release | Active Support Until | Security Support Until*
|--|--|--|--|--|
|2.15  | 27 Sep 2019 | 8 Oct 2019 | 8 Oct 2019 | 8 Oct 2019
|2.16  | 30 Jan 2020 | 13 Feb 2020 | 15 June 2020 | 15 December 2020
|3.x   | 27 Jan 2020 | 15 June 2020 | 15 June 2021 | 15 December 2021
|3.1   | 17 Aug 2020 | 24 Aug 2020 | 23 Nov 2020 | 30 Nov 2020
|3.2   | 23 Nov 2020 | 30 Nov 2020 | 16 Feb 2021 | 22 Feb 2021
|3.3   | 16 Feb 2021 | 22 Feb 2021 | 17 May 2021 | 24 May 2021
|4.x   | 17 May 2021 | 24 May 2021 | 24 May 2022 | 20 Dec 2022

`*`Security support for 2.16 will only be provided for Mautic itself, not for core dependencies that are EOL, such as Symfony 2.8.

## Software Downloads
The GitHub version is recommended for both development and testing. The production package (including all libraries) is available at [mautic.org/download][download-mautic].

## Installation
### Disclaimer
*Install from source only if you are comfortable using the command line. You'll be required to use various CLI commands to get Mautic working and keep it working. If the source/database schema gets out of sync with Mautic releases, the release updater may not work and will require manual updates. For production, we recommend the pre-packaged Mautic which is available at [mautic.org/download][download-mautic].*

*Also note that source code outside of a [tagged release][tagged-release] should be considered ‘alpha’. It may contain bugs, cause unexpected results, data corruption or loss, and is not recommended for use in a production environment. Use at your own risk.*

### How to install Mautic
You must already have [Composer v1][composer-v1] available on your computer because this is a development release and you'll need Composer to download the vendor packages. Note that Composer v2 is not yet supported.

Also note that if you have DDEV installed, you can run 'ddev config' followed by 'ddev start'. This will kick off the Mautic first-run process which will automatically install dependencies and configure Mautic for use. ✨ 🚀 Read more [here][ddev-mautic]

Installing Mautic is a simple three-step process:

1. [Download the repository zip][download-zip] then extract the zip to your web root.
2. Run the `composer install` command to install the required packages.
3. Open your browser and complete the installation through the web installer.

If you get stuck, check our our [general troubleshooting][troubleshooting] page. Still no joy? Join our lively [Mautic Community][community] for support and answers.

### User Documentation
Documentation on how to use Mautic is available at [docs.mautic.org][mautic-docs].

### Developer Docs
Developer documentation, including API reference docs, is available at [developer.mautic.org][dev-docs].


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://twitter.com/dennisameling"><img src="https://avatars.githubusercontent.com/u/17739158?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dennis Ameling</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=dennisameling" title="Code">💻</a> <a href="#userTesting-dennisameling" title="User Testing">📓</a></td>
    <td align="center"><a href="https://steercampaign.com"><img src="https://avatars.githubusercontent.com/u/12627658?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohammad Abu Musa</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=mabumusa1" title="Code">💻</a> <a href="#userTesting-mabumusa1" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Amabumusa1" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="http://johnlinhart.com"><img src="https://avatars.githubusercontent.com/u/1235442?v=4?s=100" width="100px;" alt=""/><br /><sub><b>John Linhart</b></sub></a><br /><a href="#userTesting-escopecz" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Aescopecz" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/mautic/mautic/commits?author=escopecz" title="Code">💻</a></td>
    <td align="center"><a href="https://www.webmecanik.com"><img src="https://avatars.githubusercontent.com/u/14075239?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Norman Pracht - Webmecanik</b></sub></a><br /><a href="#userTesting-npracht" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/commits?author=npracht" title="Code">💻</a></td>
    <td align="center"><a href="https://webmecanik.com"><img src="https://avatars.githubusercontent.com/u/462477?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Zdeno Kuzmany</b></sub></a><br /><a href="#userTesting-kuzmany" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Akuzmany" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/mautic/mautic/commits?author=kuzmany" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/stevedrobinson"><img src="https://avatars.githubusercontent.com/u/866855?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Steve Robinson</b></sub></a><br /><a href="#userTesting-stevedrobinson" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/snoblucha"><img src="https://avatars.githubusercontent.com/u/265586?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Petr Šnobl</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=snoblucha" title="Code">💻</a> <a href="https://github.com/mautic/mautic/issues?q=author%3Asnoblucha" title="Bug reports">🐛</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/luguenth"><img src="https://avatars.githubusercontent.com/u/9964009?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lukas Günther</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=luguenth" title="Code">💻</a> <a href="https://github.com/mautic/mautic/commits?author=luguenth" title="Documentation">📖</a> <a href="#userTesting-luguenth" title="User Testing">📓</a></td>
    <td align="center"><a href="https://www.ruthcheesley.co.uk"><img src="https://avatars.githubusercontent.com/u/2930593?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ruth Cheesley</b></sub></a><br /><a href="#userTesting-rcheesley" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Archeesley" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/mautic/mautic/commits?author=rcheesley" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/anton-vlasenko"><img src="https://avatars.githubusercontent.com/u/43744263?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Anton Vlasenko</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=anton-vlasenko" title="Code">💻</a> <a href="https://github.com/mautic/mautic/commits?author=anton-vlasenko" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/miroslavfedeles"><img src="https://avatars.githubusercontent.com/u/6388925?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Miroslav Fedeleš</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=fedys" title="Code">💻</a> <a href="https://github.com/mautic/mautic/commits?author=fedys" title="Tests">⚠️</a></td>
    <td align="center"><a href="https://github.com/gabepri"><img src="https://avatars.githubusercontent.com/u/73728034?v=4?s=100" width="100px;" alt=""/><br /><sub><b>gabepri</b></sub></a><br /><a href="https://github.com/mautic/mautic/issues?q=author%3Agabepri" title="Bug reports">🐛</a> <a href="https://github.com/mautic/mautic/commits?author=gabepri" title="Code">💻</a></td>
    <td align="center"><a href="https://incentfit.com"><img src="https://avatars.githubusercontent.com/u/13243272?v=4?s=100" width="100px;" alt=""/><br /><sub><b>incentfit</b></sub></a><br /><a href="#userTesting-incentfit" title="User Testing">📓</a></td>
    <td align="center"><a href="http://drahy.net"><img src="https://avatars.githubusercontent.com/u/12815758?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Lukáš Drahý</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=hluchas" title="Code">💻</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Ahluchas" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://about.me/alanhartless"><img src="https://avatars.githubusercontent.com/u/63312?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alan Hartless (he/him)</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=alanhartless" title="Code">💻</a></td>
    <td align="center"><a href="http://mohitaghera.in"><img src="https://avatars.githubusercontent.com/u/2618452?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mohit Aghera</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=mohit-rocks" title="Code">💻</a> <a href="#userTesting-mohit-rocks" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Amohit-rocks" title="Reviewed Pull Requests">👀</a></td>
    <td align="center"><a href="https://github.com/domparry"><img src="https://avatars.githubusercontent.com/u/19376765?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dom Parry</b></sub></a><br /><a href="#userTesting-domparry" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/sensalot"><img src="https://avatars.githubusercontent.com/u/6697244?v=4?s=100" width="100px;" alt=""/><br /><sub><b>sensalot</b></sub></a><br /><a href="#userTesting-sensalot" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/shinde-rahul"><img src="https://avatars.githubusercontent.com/u/1046788?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rahul Shinde</b></sub></a><br /><a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Ashinde-rahul" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-shinde-rahul" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/commits?author=shinde-rahul" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/jos0405"><img src="https://avatars.githubusercontent.com/u/4246909?v=4?s=100" width="100px;" alt=""/><br /><sub><b>jos0405</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=jos0405" title="Code">💻</a></td>
    <td align="center"><a href="http://veenhof.be"><img src="https://avatars.githubusercontent.com/u/161341?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nick Veenhof</b></sub></a><br /><a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Anickveenhof" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/patrykgruszka"><img src="https://avatars.githubusercontent.com/u/8580942?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Patryk Gruszka</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=patrykgruszka" title="Code">💻</a> <a href="https://github.com/mautic/mautic/commits?author=patrykgruszka" title="Documentation">📖</a> <a href="https://github.com/mautic/mautic/commits?author=patrykgruszka" title="Tests">⚠️</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Apatrykgruszka" title="Reviewed Pull Requests">👀</a> <a href="#userTesting-patrykgruszka" title="User Testing">📓</a></td>
    <td align="center"><a href="https://hartmut.io"><img src="https://avatars.githubusercontent.com/u/20030306?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alex Hammerschmied</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=alexhammerschmied" title="Code">💻</a></td>
    <td align="center"><a href="https://www.twentyzen.com"><img src="https://avatars.githubusercontent.com/u/1241376?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Dirk Spannaus</b></sub></a><br /><a href="https://github.com/mautic/mautic/issues?q=author%3Adsp76" title="Bug reports">🐛</a> <a href="#userTesting-dsp76" title="User Testing">📓</a></td>
    <td align="center"><a href="http://www.linkedin.com/in/rehannischal"><img src="https://avatars.githubusercontent.com/u/43839944?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Rehan Nischal</b></sub></a><br /><a href="https://github.com/mautic/mautic/issues?q=author%3ARehanNischal" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/Christophe9880"><img src="https://avatars.githubusercontent.com/u/82932885?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Christophe9880</b></sub></a><br /><a href="#userTesting-Christophe9880" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/dadarya0"><img src="https://avatars.githubusercontent.com/u/48244990?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Saurabh Gupta</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=dadarya0" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/ts-navghane"><img src="https://avatars.githubusercontent.com/u/54406786?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tejas Navghane</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=ts-navghane" title="Tests">⚠️</a> <a href="https://github.com/mautic/mautic/commits?author=ts-navghane" title="Code">💻</a> <a href="#userTesting-ts-navghane" title="User Testing">📓</a> <a href="https://github.com/mautic/mautic/pulls?q=is%3Apr+reviewed-by%3Ats-navghane" title="Reviewed Pull Requests">👀</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://www.webmecanik.com"><img src="https://avatars.githubusercontent.com/u/49391402?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Florent Petitjean - Webmecanik</b></sub></a><br /><a href="#userTesting-florentpetitjean" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/tobsowo"><img src="https://avatars.githubusercontent.com/u/5642737?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Oluwatobi Owolabi</b></sub></a><br /><a href="#eventOrganizing-tobsowo" title="Event Organizing">📋</a></td>
    <td align="center"><a href="https://www.linkedin.com/in/favour-kelvin/"><img src="https://avatars.githubusercontent.com/u/39309699?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Favour Kelvin</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=fakela" title="Documentation">📖</a> <a href="#tutorial-fakela" title="Tutorials">✅</a> <a href="#talk-fakela" title="Talks">📢</a></td>
    <td align="center"><a href="http://poisson.phc.dm.unipi.it/~mascellani"><img src="https://avatars.githubusercontent.com/u/101675?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Giovanni Mascellani</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=giomasce" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/RaphaelWoude"><img src="https://avatars.githubusercontent.com/u/47354694?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Raphael van der Woude</b></sub></a><br /><a href="#userTesting-RaphaelWoude" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/mannp"><img src="https://avatars.githubusercontent.com/u/4335298?v=4?s=100" width="100px;" alt=""/><br /><sub><b>mannp</b></sub></a><br /><a href="https://github.com/mautic/mautic/issues?q=author%3Amannp" title="Bug reports">🐛</a> <a href="#userTesting-mannp" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/MarketSmart"><img src="https://avatars.githubusercontent.com/u/85239715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>MarketSmart</b></sub></a><br /><a href="https://github.com/mautic/mautic/commits?author=MarketSmart" title="Code">💻</a></td>
  </tr>
  <tr>
    <td align="center"><a href="http://www.leuchtfeuer.com"><img src="https://avatars.githubusercontent.com/u/55587275?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Leon</b></sub></a><br /><a href="#userTesting-oltmanns-leuchtfeuer" title="User Testing">📓</a></td>
    <td align="center"><a href="https://github.com/bryanitamazonva"><img src="https://avatars.githubusercontent.com/u/79956709?v=4?s=100" width="100px;" alt=""/><br /><sub><b>bryanitamazonva</b></sub></a><br /><a href="https://github.com/mautic/mautic/issues?q=author%3Abryanitamazonva" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors][all-contributors] specification. Contributions of any kind welcome!

[mautic-blog]: <https://www.mautic.org/blog>
[get-involved]: <https://www.mautic.org/community/get-involved>
[twitter]: <https://twitter.com/MauticCommunity>
[facebook]: <https://www.facebook.com/MauticCommunity/>
[slack]: <https://www.mautic.org/community/get-involved/communication-channels>
[contributing]: <https://contribute.mautic.org/contributing-to-mautic>
[contributing-md]: <https://github.com/mautic/mautic/blob/feature/.github/CONTRIBUTING.md>
[contribute-developer]: <https://contribute.mautic.org/contributing-to-mautic/developer>
[t1-issues]: <https://github.com/mautic/mautic/issues?q=is%3Aissue+is%3Aopen+label%3AT1>
[download-mautic]: <https://www.mautic.org/download>
[tagged-release]: <https://github.com/mautic/mautic/releases>
[composer-v1]: <http://getcomposer.org/>
[download-zip]: <https://github.com/mautic/mautic/archive/refs/heads/features.zip>
[ddev-mautic]: <https://kb.mautic.org/knowledgebase/development/how-to-install-mautic-using-ddev>
[troubleshooting]: <https://docs.mautic.org/en/troubleshooting>
[community]: <https://www.mautic.org/community>
[mautic-docs]: <https://docs.mautic.org>
[dev-docs]: <https://developer.mautic.org>
[all-contributors]: <https://github.com/all-contributors/all-contributors>
