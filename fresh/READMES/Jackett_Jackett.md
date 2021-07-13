# Jackett

[![GitHub issues](https://img.shields.io/github/issues/Jackett/Jackett.svg?maxAge=60&style=flat-square)](https://github.com/Jackett/Jackett/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/Jackett/Jackett.svg?maxAge=60&style=flat-square)](https://github.com/Jackett/Jackett/pulls)
[![Build Status](https://dev.azure.com/Jackett/Jackett/_apis/build/status/Jackett.Jackett?branchName=master)](https://dev.azure.com/jackett/jackett/_build/latest?definitionId=1&branchName=master)
[![GitHub Releases](https://img.shields.io/github/downloads/Jackett/Jackett/total.svg?maxAge=60&style=flat-square)](https://github.com/Jackett/Jackett/releases/latest)
[![Docker Pulls](https://img.shields.io/docker/pulls/linuxserver/jackett.svg?maxAge=60&style=flat-square)](https://hub.docker.com/r/linuxserver/jackett/)
[![Discord](https://img.shields.io/badge/discord-chat-7289DA.svg?maxAge=60&style=flat-square)](https://discord.gg/J865QuA)

This project is a new fork and is recruiting development help.  If you are able to help out please [contact us](https://github.com/Jackett/Jackett/issues/8180).

Please see our [troubleshooting and contributing guidelines](CONTRIBUTING.md) before submitting any issues or pull requests

Jackett works as a proxy server: it translates queries from apps ([Sonarr](https://github.com/Sonarr/Sonarr), [Radarr](https://github.com/Radarr/Radarr), [SickRage](https://sickrage.github.io/), [CouchPotato](https://couchpota.to/), [Mylar](https://github.com/evilhero/mylar), [Lidarr](https://github.com/lidarr/lidarr), [DuckieTV](https://github.com/SchizoDuckie/DuckieTV), [qBittorrent](https://www.qbittorrent.org/), [Nefarious](https://github.com/lardbit/nefarious) etc.) into tracker-site-specific http queries, parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps.

Developer note: The software implements the [Torznab](https://github.com/Sonarr/Sonarr/wiki/Implementing-a-Torznab-indexer) (with hybrid [nZEDb](https://github.com/nZEDb/nZEDb/blob/b485fa326a0ff1f47ce144164eb1f070e406b555/resources/db/schema/data/10-categories.tsv)/[Newznab](https://newznab.readthedocs.io/en/latest/misc/api/#predefined-categories) [category numbering](https://github.com/Jackett/Jackett/wiki/Jackett-Categories)) and [TorrentPotato](https://github.com/RuudBurger/CouchPotatoServer/wiki/Couchpotato-torrent-provider) APIs.

A third-party Golang SDK for Jackett is available from [webtor-io/go-jackett](https://github.com/webtor-io/go-jackett)

#### Supported Systems
* Windows 7 SP1 or greater
* Linux [supported operating systems here](https://github.com/dotnet/core/blob/master/release-notes/5.0/5.0-supported-os.md#linux)
* macOS 10.13 or greater

<details> <summary> <b> Supported Public Trackers </b> </summary>

 * 1337x
 * 7torrents
 * ACG.RIP
 * ACGsou (36DM)
 * Anidex
 * AniLibria
 * AnimeClipse
 * Animedia
 * Anime Tosho
 * AniRena
 * AniSource
 * AudioBook Bay (ABB)
 * Badass Torrents
 * BigFANGroup
 * BitRu
 * BT.etree
 * BT4G
 * BTDB
 * BTDIGG
 * BTSOW
 * Byrutor
 * CiliPro (LIAORENCILI)
 * comicat
 * ConCen
 * cpasbien
 * cpasbienClone
 * Demonoid
 * DivxTotal
 * dmhy
 * E-Hentai
 * elitetorrent
 * emtrek
 * EpubLibre
 * Erai-Raws
 * ETTV
 * EXT Torrents
 * ExtraTorrent.cd
 * ExtraTorrent.it
 * EZTV
 * Filebase
 * FireBit
 * Frozen Layer
 * GamesTorrents
 * GkTorrent
 * GloDLS
 * GTorrent
 * GTorrent.pro
 * HDhouse (HDReactor)
 * IBit
 * Idope
 * Il CorSaRo Blu
 * Il Corsaro Nero
 * Internet Archive (archive.org)
 * Isohunt2
 * iTorrent
 * kickasstorrents.ws
 * kickasstorrents.to
 * Legit Torrents
 * LePorno.info
 * LimeTorrents
 * LinuxTracker
 * MacTorrents
 * Magnet4You
 * MejorTorrent
 * MixTapeTorrent
 * Montorrent
 * MoviesDVDR
 * MovieTorrent
 * MyPornClub
 * NewPCT (aka: tvsinpagar, descargas2020, torrentlocura, torrentrapid, tumejortorrent, pctnew, etc)
 * Newstudio
 * Nitro
 * NNTT
 * NoNaMe Club (NNM-Club)
 * Nyaa-Pantsu
 * Nyaa.si
 * OnceSearch
 * OneJAV
 * OxTorrent
 * ParnuXi
 * PC-torrent
 * PiratBit
 * Pirateiro
 * Pornforall
 * PornLeech
 * PornoLive
 * PornoRip
 * PornoTor
 * Portugas
 * ProPorn
 * ProStyleX
 * Rapidzona
 * RARBG
 * RinTor
 * RinTorNeT
 * Rus-media
 * RuTor
 * RuTracker.RU
 * seleZen
 * Sexy-Pics
 * ShizaProject
 * shokweb
 * ShowRSS
 * SkyTorrents.to
 * Solid Torrents
 * sosulki
 * SubsPlease
 * sukebei-Pantsu
 * sukebei.Nyaa.si
 * The Pirate Bay (TPB)
 * TNTfork
 * Tokyo Tosho
 * Torlock
 * TOROS
 * Torrent Downloads (TD)
 * Torrent Oyun indir
 * Torrent Paradise (ML)
 * torrent-pirat
 * Torrent4You
 * Torrent9
 * Torrent9 clone
 * TorrentDownload
 * TorrentFunk
 * TorrentGalaxy (TGx)
 * TorrentKitty
 * TorrentMafya
 * TorrentMax (토렌트맥스)
 * TorrentParadise
 * TorrentProject2
 * TorrentQQ (토렌트큐큐)
 * Torrents.csv
 * TorrentSir (토렌트썰)
 * Torrentv
 * TorrentView (토렌트뷰)
 * TorrentWhiz ( 토렌트위즈)
 * truPornolabs
 * ttobogo
 * Underverse
 * UnionDHT
 * VSTHouse
 * VST Torrents
 * xxxAdultTorrent
 * xxxtor
 * xxxtorrents
 * YourBittorrent
 * YTS.ag
 * zetorrents
 * Zooqle
</details>

<details> <summary> <b> Supported Semi-Private Trackers </b> </summary>

 * AniDUB
 * Anime-Free
 * ArenaBG
 * BaibaKo
 * BookTracker
 * BootyTape
 * Catorrent
 * Darmowe torrenty
 * Deildu
 * DimeADozen (EzTorrent)
 * DXP (Deaf Experts)
 * EniaHD
 * Erzsebet.pl
 * ExKinoRay
 * Fou-Du-Cinema
 * FreeTorrent
 * Gay-Torrents.net
 * Genesis-Movement
 * HamsterStudio
 * HD-CzTorrent
 * HunTorrent
 * IV-Torrents
 * KinoNaVse100
 * Kinorun
 * Kinozal
 * LostFilm.tv
 * Magnetico (Local DHT) [[site](https://github.com/boramalper/magnetico)]
 * MVGroup Forum
 * MVGroup Main
 * Marine Tracker
 * Metal Tracker
 * MuziekFrabriek
 * NetHD (VietTorrent)
 * PornoLab
 * PussyTorrents
 * Rainbow Tracker
 * RGFootball
 * RiperAM
 * RockBox
 * RuTracker
 * Rustorka
 * Sharewood
 * SkTorrent
 * SkTorrent-org
 * themixingbowl (TMB)
 * Toloka.to
 * Torrent-Explosiv
 * Torrents-Local
 * TribalMixes
 * Union Fansub
 * YggTorrent (YGG)
 * Ztracker
</details>

<details> <summary> <b> Supported Private Trackers </b> </summary>

 * 0day.kiev
 * 1ptbar
 * 2 Fast 4 You [![(invite needed)][inviteneeded]](#)
 * 3ChangTrai (3CT) [![(invite needed)][inviteneeded]](#)
 * 3D Torrents (3DT) [![(invite needed)][inviteneeded]](#)
 * 4thD (4th Dimension)
 * 52PT
 * 720pier
 * Abnormal
 * ABtorrents (ABT + RNS)
 * Acid Lounge (A-L) [![(invite needed)][inviteneeded]](#)
 * AcrossTheTasman [![(invite needed)][inviteneeded]](#)
 * Aftershock
 * Aidoru!Online
 * Aither
 * AlphaRatio (AR)
 * AmigosShareClub
 * anasch.cc
 * AnimeBytes (AB)
 * AnimeTorrents (AnT)
 * AnimeWorld [![(invite needed)][inviteneeded]](#)
 * Anthelion
 * Araba Fenice (Phoenix) [![(invite needed)][inviteneeded]](#)
 * ArabP2P
 * AsianCinema
 * Asylum Share
 * AudioNews (AN)
 * Aussierul.es [![(invite needed)][inviteneeded]](#)
 * AvistaZ (AsiaTorrents)
 * Back-ups
 * bB
 * BakaBT
 * BeiTai
 * BeyondHD (BHD)
 * Bibliotik
 * BIGTorrent
 * Bit-City Reloaded [![(invite needed)][inviteneeded]](#)
 * BIT-HDTV
 * BiT-TiTAN
 * BitHUmen
 * BitTorrentFiles
 * BiTTuRK
 * Bithorlo (BHO)
 * Bitspyder
 * BJ-Share (BJ)
 * BlueBird [![(invite needed)][inviteneeded]](#)
 * Blutopia (BLU)
 * Borgzelle
 * Boxing Torrents
 * Brasil Tracker
 * BroadcasTheNet (BTN)
 * BroadCity
 * BrokenStones [![(invite needed)][inviteneeded]](#)
 * BTNext (BTNT)
 * BTSCHOOL
 * BWTorrents
 * Carp-Hunter
 * Carpathians
 * CartoonChaos (CC)
 * CasaTorrent [![(invite needed)][inviteneeded]](#)
 * CCFBits
 * CGPeers
 * CHDBits
 * ChileBT
 * Cinecalidad
 * CinemaMovieS_ZT
 * CinemaZ (EuTorrents)
 * Cinemageddon
 * Cinematik
 * Classix
 * Coastal-Crew
 * Concertos
 * CrazyHD
 * CrazySpirits
 * CrnaBerza
 * DANISH BYTES
 * Darius Tracker
 * Dark-Shadow
 * Dark Tracker
 * Das Unerwartete [![(invite needed)][inviteneeded]](#)
 * DataScene (DS)
 * DesiReleasers
 * DesiTorrents
 * Diablo Torrent
 * DICMusic
 * DigitalCore
 * DivTeam
 * Dragonworld Reloaded [![(invite needed)][inviteneeded]](#)
 * EbookParadijs
 * Ebooks-Shares
 * EfectoDoppler
 * Empornium (EMP) [![(invite needed)][inviteneeded]](#)
 * eShareNet
 * eStone (XiDER, BeLoad)
 * ExoticaZ (YourExotic)
 * ExtremeBits
 * ExtremeTorrents [![(invite needed)][inviteneeded]](#)
 * FANO.IN
 * Fantastic Heaven
 * FeedUrNeed
 * Femdomcult
 * FileList (FL)
 * Film-Paleis
 * FinElite (FE)
 * FinVip
 * FunFile (FF)
 * FunkyTorrents (FT)
 * Fuzer (FZ)
 * Gay-Torrents.org [![(invite needed)][inviteneeded]](#)
 * GAYtorrent.ru
 * GazelleGames (GGn) [![(invite needed)][inviteneeded]](#)
 * Generation-Free
 * GFXPeers
 * GigaTorrents
 * GimmePeers (formerly ILT)
 * GiroTorrent
 * GreekDiamond
 * Greek Team
 * HaiDan
 * HD Dolby
 * HD-Bits.com
 * HD-Forever (HDF)
 * HD-Olimpo
 * HD-Only (HDO)
 * HD-Space (HDS)
 * HD-Spain [![(invite needed)][inviteneeded]](#)
 * HD-Torrents (HDT)
 * HD4FANS [![(invite needed)][inviteneeded]](#)
 * HDArea (HDA)
 * HDAtmos
 * HDBits
 * HDC (HDCiTY)
 * HDCenter [![(invite needed)][inviteneeded]](#)
 * HDChina (HDWing)
 * HDCity
 * HDHome (HDBigger)
 * HDME
 * HDRoute [![(invite needed)][inviteneeded]](#)
 * HDSky
 * HDTime
 * HDTorrents.it
 * HDTurk
 * HDU
 * HDZone
 * Hebits
 * HellasTZ
 * Hon3y HD
 * HQSource (HQS)
 * HuSh [![(invite needed)][inviteneeded]](#)
 * IPTorrents (IPT)
 * ImmortalSeed (iS)
 * Immortuos
 * Insane Tracker
 * IPTorrents (IPT)
 * JPopsuki
 * JPTV
 * Karagarga
 * Keep Friends
 * LastFiles
 * LatinoP2P
 * Le Saloon
 * LearnFlakes
 * LegacyHD (HD4Free)
 * LemonHD
 * Libble
 * LibraNet (LN)
 * LinkoManija
 * LosslessClub
 * M-Team TP (MTTP)
 * MaDs Revolution [![(invite needed)][inviteneeded]](#)
 * magic-heaven
 * Magico (Trellas)
 * Majomparádé (TurkDepo)
 * MeseVilág (Fairytale World)
 * MicroBit (µBit)
 * Milkie
 * MMA-Torrents
 * MNV (Max-New-Vision)
 * Mononoké-BT [![(invite needed)][inviteneeded]](#)
 * MoreThanTV (MTV)
 * MyAnonamouse (MAM)
 * MySpleen [![(invite needed)][inviteneeded]](#)
 * NBTorrents [![(invite needed)][inviteneeded]](#)
 * NCore
 * Nebulance (NBL) (TransmiTheNet)
 * NetCosmo
 * NetLab
 * NorBits
 * Nordic+
 * Oasis
 * Obscure
 * oMg[WtF]trackr
 * OpenCD
 * Oppaitime [![(invite needed)][inviteneeded]](#)
 * Orpheus
 * OshenPT
 * Ourbits (HDPter)
 * P2PBG
 * P2PElite
 * PassThePopcorn (PTP)
 * Peers.FM
 * Pirata Digital
 * PirateTheNet (PTN)
 * PixelCove (Ultimate Gamer)
 * PiXELHD (PxHD) [![(invite needed)][inviteneeded]](#)
 * Pleasuredome
 * PolishSource (PS)
 * PolishTracker
 * PornBits (PB)
 * Pornbay [![(invite needed)][inviteneeded]](#)
 * PotUK
 * Pretome
 * PrivateHD (PHD)
 * ProAudioTorrents (PAT)
 * PTerClub
 * PTFiles (PTF)
 * PThome
 * PTMSG
 * PTSBAO
 * PTtime
 * PuntoTorrent
 * PuroVicio
 * Puur-Hollands
 * PWTorrents (PWT)
 * R3V WTF! [![(invite needed)][inviteneeded]](#)
 * Racing4Everyone (R4E)
 * RacingForMe (RFM)
 * RedBits
 * Red Star Torrent (RST) [![(invite needed)][inviteneeded]](#)
 * Redacted (PassTheHeadphones)
 * RetroFlix
 * RevolutionTT
 * ROFD
 * Romanian Metal Torrents (RMT) [![(invite needed)][inviteneeded]](#)
 * RPTorrents
 * SceneHD
 * ScenePalace (SP)
 * SceneRush
 * SceneTime
 * SDBits [![(invite needed)][inviteneeded]](#)
 * Secret Cinema
 * SeedFile (SF)
 * ShareFiles
 * Shareisland
 * Shazbat
 * SiamBIT
 * SnowPT (SSPT)
 * SoulVoice
 * SpeedApp (SceneFZ, XtreMeZone / MYXZ, ICE Torrent)
 * SpeedCD
 * Speedmaster HD
 * SpeedTorrent Reloaded
 * Spirit of Revolution [![(invite needed)][inviteneeded]](#)
 * SportHD [![(invite needed)][inviteneeded]](#)
 * SportsCult
 * SpringSunday
 * SugoiMusic
 * Superbits (SBS)
 * Tapochek
 * Tasmanit [![(invite needed)][inviteneeded]](#)
 * TeamHD
 * TeamOS
 * TEKNO3D [![(invite needed)][inviteneeded]](#)
 * TellyTorrent
 * teracod (Movie Zone)
 * The Falling Angels (TFA)
 * The Geeks
 * The Horror Charnel (THC)
 * The New Retro
 * The Occult [![(invite needed)][inviteneeded]](#)
 * The Place [![(invite needed)][inviteneeded]](#)
 * The Shinning (TsH)
 * The Show [![(invite needed)][inviteneeded]](#)
 * The Vault [![(invite needed)][inviteneeded]](#)
 * TheAudioScene
 * TheEmpire (TE)
 * TheLeachZone
 * TheScenePlace (TSP)
 * TJUPT
 * TLFBits [![(invite needed)][inviteneeded]](#)
 * ToTheGlory (TTG)
 * Torrent Network (TN)
 * Torrent Sector Crew (TSC)
 * Torrent Surf
 * Torrent-Syndikat [![(invite needed)][inviteneeded]](#)
 * TOrrent-tuRK (TORK)
 * Torrent.LT
 * TorrentBD
 * TorrentBytes (TBy)
 * TorrentCCF (TCCF)
 * TorrentDay (TD)
 * TorrentDB
 * Torrentech (TTH)
 * TorrentFactory
 * TorrentHeaven [![(invite needed)][inviteneeded]](#)
 * TorrentHR
 * Torrenting (TT) [![(invite needed)][inviteneeded]](#)
 * TotallyKids (TK)
 * Torrentland
 * TorrentLeech (TL)
 * TorrentLeech.pl
 * TorrentSeeds (TS)
 * Trackeros
 * TranceTraffic [![(invite needed)][inviteneeded]](#)
 * Trezzor
 * TTsWEB
 * TurkSeed
 * TurkTorrent (TT)
 * TV Chaos UK (TVCUK)
 * TV-Vault
 * TVstore
 * Twilight Torrents
 * Twilights Zoom
 * U2 (U2分享園@動漫花園) [![(invite needed)][inviteneeded]](#)
 * UHDBits
 * UnionGang [![(invite needed)][inviteneeded]](#)
 * UnlimitZ
 * Vizuk
 * WDT (Wrestling Desires Torrents / Ultimate Wrestling Torrents)
 * wOOt [![(invite needed)][inviteneeded]](#)
 * World-In-HD [![(invite needed)][inviteneeded]](#)
 * x-ite.me (XM) [![(invite needed)][inviteneeded]](#)
 * xBytesV2
 * XSpeeds (XS)
 * XWT-Classics
 * XWTorrents (XWT)
 * Xthor
 * YDYPT
 * Zamunda.net
 * Zelka.org
 * ZonaQ
</details>

Trackers marked with [![(invite needed)][inviteneeded]](#) have no active maintainer and may be missing features or be broken. If you have an invite for them please send it to garfieldsixtynine -at- gmail.com to get them fixed/improved.

### Aggregate indexers

A special "all" indexer is available at `/api/v2.0/indexers/all/results/torznab`.
It will query all configured indexers and return the combined results.

If your client supports multiple feeds it's recommended to add each indexer directly instead of using the all indexer.
Using the all indexer has no advantages (besides reduced management overhead), only disadvantages:
* you lose control over indexer specific settings (categories, search modes, etc.)
* mixing search modes (IMDB, query, etc.) might cause low-quality results
* indexer specific categories (>= 100000) can't be used.
* slow indexers will slow down the overall result
* total results are limited to 1000

To get all Jackett indexers including their capabilities you can use `t=indexers` on the all indexer. To get only configured/unconfigured indexers you can also add `configured=true/false` as a query parameter.

### Filter indexers

Another special "filter" indexer is available at `/api/v2.0/indexers/<filter>/results/torznab`
It will query the configured indexers that match the `<filter>` expression criterias and return the combined results as "all".

Supported filters
Filter | Condition
-|-
`type:<type>` | where the indexer type is equal to `<type>`
`tag:<tag>` | where the indexer tags contains `<tag>`
`lang:<tag>` | where the indexer language start with `<lang>`
`test:{passed\|failed}` | where the last indexer test performed `passed` or `failed`
`status:{healthy\|failing\|unknown}` | where the indexer state is `healthy` (succesfully operates in the last minutes), `failing` (generates errors in the recent call) or `unknown` (unused for a while)

Supported operators
Operator | Condition
-|-
`!<expr>` | where not `<expr>`
`<expr1>+<expr2>[+<expr3>...]` | where `<expr1>` and `<expr2>` [and `<expr3>`...]
`<expr1>,<expr2>[,<expr3>...]` | where `<expr1>` or `<expr2>` [or `<expr3>`...]

Example 1:
The "filter" indexer at `/api/v2.0/indexers/tag:group1,!type:private+lang:en/results/torznab` will query all the configured indexers tagged with `group1` or all the indexers not private and with `en` language (`en-en`,`en-us`,...)

Example 2:
The "filter" indexer at `/api/v2.0/indexers/!status:failing,test:passed` will query all the configured indexers not `failing` or which `passed` its last test.

## Installation on Windows
We recommend you install Jackett as a Windows service using the supplied installer. You may also download the zipped version if you would like to configure everything manually.

To get started with using the installer for Jackett, follow the steps below:

1. Check if you need any .NET prerequisites installed, see https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=net50#dependencies
2. Download the latest version of the Windows installer, "Jackett.Installer.Windows.exe" from the [releases](https://github.com/Jackett/Jackett/releases/latest) page.
3. When prompted if you would like this app to make changes to your computer, select "yes".
4. If you would like to install Jackett as a Windows Service, make sure the "Install as Windows Service" checkbox is filled.
5. Once the installation has finished, check the "Launch Jackett" box to get started.
6. Navigate your web browser to http://127.0.0.1:9117
7. You're now ready to begin adding your trackers and using Jackett.

When installed as a service the tray icon acts as a way to open/start/stop Jackett. If you opted to not install it as a service then Jackett will run its web server from the tray tool.

Jackett can also be run from the command line if you would like to see log messages (Ensure the server isn't already running from the tray/service). This can be done by using "JackettConsole.exe" (for Command Prompt), found in the Jackett data folder: "%ProgramData%\Jackett".


## Install on Linux (AMDx64)
On most operating systems all the required dependencies will already be present. In case they are not, you can refer to this page https://github.com/dotnet/core/blob/master/Documentation/linux-prereqs.md

### Install as service
1. Download and extract the latest `Jackett.Binaries.LinuxAMDx64.tar.gz` release from the [releases page](https://github.com/Jackett/Jackett/releases)
2. To install Jackett as a service, open a Terminal, cd to the jackett folder and run `sudo ./install_service_systemd.sh` You need root permissions to install the service. The service will start on each logon. You can always stop it by running `systemctl stop jackett.service` from Terminal. You can start it again it using `systemctl start jackett.service`. Logs are stored as usual under `~/.config/Jackett/log.txt` and also in `journalctl -u jackett.service`.

### Run without installing as a service
Download and extract the latest `Jackett.Binaries.LinuxAMDx64.tar.gz` release from the [releases page](https://github.com/Jackett/Jackett/releases), open a Terminal, cd to the jackett folder and run Jackett with the command `./jackett`

### home directory
If you want to run it with a user without a /home directory you need to add `Environment=XDG_CONFIG_HOME=/path/to/folder` to your systemd file, this folder will be used to store your config files.


## Install on Linux (ARMv7 or above)
On most operating systems all the required dependencies will already be present. In case they are not, you can refer to this page https://github.com/dotnet/core/blob/master/Documentation/linux-prereqs.md

### Install as service
1. Download and extract the latest `Jackett.Binaries.LinuxARM32.tar.gz` or `Jackett.Binaries.LinuxARM64.tar.gz` (32 bit is the most common on ARM) release from the [releases page](https://github.com/Jackett/Jackett/releases)
2. To install Jackett as a service, open a Terminal, cd to the jackett folder and run `sudo ./install_service_systemd.sh` You need root permissions to install the service. The service will start on each logon. You can always stop it by running `systemctl stop jackett.service` from Terminal. You can start it again it using `systemctl start jackett.service`. Logs are stored as usual under `~/.config/Jackett/log.txt` and also in `journalctl -u jackett.service`.

### Run without installing as a service
Download and extract the latest `Jackett.Binaries.LinuxARM32.tar.gz` or `Jackett.Binaries.LinuxARM64.tar.gz` (32 bit is the most common on ARM) release from the [releases page](https://github.com/Jackett/Jackett/releases), open a Terminal, cd to the jackett folder and run Jackett with the command `./jackett`

### home directory
If you want to run it with a user without a /home directory you need to add `Environment=XDG_CONFIG_HOME=/path/to/folder` to your systemd file, this folder will be used to store your config files.


## Installation on Linux (ARMv6 or below)
 1. Install [Mono 5.8](http://www.mono-project.com/download/#download-lin) or better (using the latest stable release is recommended)
       * Follow the instructions on the mono website and install the `mono-devel` and the `ca-certificates-mono` packages.
       * On Red Hat/CentOS/openSUSE/Fedora the `mono-locale-extras` package is also required.
 2. Install  libcurl:
       * Debian/Ubuntu: `apt-get install libcurl4-openssl-dev`
       * Redhat/Fedora: `yum install libcurl-devel`
       * For other distros see the  [Curl docs](http://curl.haxx.se/dlwiz/?type=devel).
 3. Download and extract the latest `Jackett.Binaries.Mono.tar.gz` release from the [releases page](https://github.com/Jackett/Jackett/releases) and run Jackett using mono with the command `mono --debug JackettConsole.exe`.
 4. (Optional) To install Jackett as a service, open the Terminal and run `sudo ./install_service_systemd_mono.sh` You need root permissions to install the service. The service will start on each logon. You can always stop it by running `systemctl stop jackett.service` from Terminal. You can start it again it using `systemctl start jackett.service`. Logs are stored as usual under `~/.config/Jackett/log.txt` and also in `journalctl -u jackett.service`.

If you want to run it with a user without a /home directory you need to add `Environment=XDG_CONFIG_HOME=/path/to/folder` to your systemd file, this folder will be used to store your config files.

Mono must be compiled with the Roslyn compiler (default), using MCS will cause "An error has occurred." errors (See https://github.com/Jackett/Jackett/issues/2704).


### Installation on Linux via Ansible

On a CentOS/RedHat 7 system: [jewflix.jackett](https://galaxy.ansible.com/jewflix/jackett)

On an Ubuntu 16 system: [chrisjohnson00.jackett](https://galaxy.ansible.com/chrisjohnson00/jackett)


## Installation on macOS

### Prerequisites
macOS 10.13 or greater

### Install as service
1. Download and extract the latest `Jackett.Binaries.macOS.tar.gz` release from the [releases page](https://github.com/Jackett/Jackett/releases).
2. Open the extracted folder and double-click on `install_service_macos`.
3. If the installation was a success, you can close the Terminal window.

The service will start on each logon. You can always stop it by running `launchctl unload ~/Library/LaunchAgents/org.user.Jackett.plist` from Terminal. You can start it again it using `launchctl load ~/Library/LaunchAgents/org.user.Jackett.plist`.
Logs are stored as usual under `~/.config/Jackett/log.txt`.

### Run without installing as a service
Download and extract the latest `Jackett.Binaries.macOS.tar.gz` release from the [releases page](https://github.com/Jackett/Jackett/releases) and run Jackett with the command `./jackett`.


## Installation using Docker
Detailed instructions are available at [LinuxServer.io Jackett Docker](https://hub.docker.com/r/linuxserver/jackett/). The Jackett Docker is highly recommended, especially if you are having Mono stability issues or having issues running Mono on your system e.g. QNAP, Synology. Thanks to [LinuxServer.io](https://linuxserver.io)


## Installation on Synology
Jackett is available as a beta package from [SynoCommunity](https://synocommunity.com/)


## Running Jackett behind a reverse proxy
When running jackett behind a reverse proxy make sure that the original hostname of the request is passed to Jackett. If HTTPS is used also set the X-Forwarded-Proto header to "https". Don't forget to adjust the "Base path override" Jackett option accordingly.

Example config for apache:
```
<Location /jackett>
    ProxyPreserveHost On
    RequestHeader set X-Forwarded-Proto expr=%{REQUEST_SCHEME}
    ProxyPass http://127.0.0.1:9117
    ProxyPassReverse http://127.0.0.1:9117
</Location>
```

Example config for Nginx:
```
location /jackett {
	proxy_pass http://127.0.0.1:9117;
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header X-Forwarded-Proto $scheme;
	proxy_set_header X-Forwarded-Host $http_host;
	proxy_redirect off;
}
```

## Search Cache
Jackett has an internal cache to increase search speed and to reduce the number of requests to the torrent sites.
The default values should be good for most users. If you have problems, you can reduce the TTL value in the
configuration or even disable the cache. Keep in mind that you can be banned by the sites if you make a lot of requests.
* **Cache TTL (seconds)**: (default 2100 / 35 minutes) It indicates how long the results can remain in the cache.
* **Cache max results per indexer**: (default 1000) How many results are kept in cache for each indexer. This limit is used to limit the use of RAM. If you make many requests and you have enough memory, increase this number.

## Configuring FlareSolverr
Some indexers are protected by CloudFlare or similar services and Jackett is not able to solve the challenges.
For these cases, [FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) has been integrated into Jackett. This service is in charge of solving the challenges and configuring Jackett with the necessary cookies.
Setting up this service is optional, most indexers don't need it.
* Install FlareSolverr service (following their instructions)
* Configure **FlareSolverr API URL** in Jackett. For example: http://172.17.0.2:8191

## Configuring OMDb
This feature is used as a fallback (when using the aggregate Indexer) to get the movie/series title if only the IMDB ID is provided in the request.
To use it, please just request a free API key on [OMDb](http://www.omdbapi.com/apikey.aspx) (1,000 daily requests limit) and paste the key in Jackett

## Command line switches

  You can pass various options when running via the command line:

<details> <summary> Command Line Switches </summary>

-   `-i, --Install`            Install Jackett windows service (Must be admin)
-   `-s, --Start`              Start the Jacket Windows service (Must be admin)
-   `-k, --Stop`               Stop the Jacket Windows service (Must be admin)
-   `-u, --Uninstall`          Uninstall Jackett windows service (Must be admin).

-   `-r, --ReserveUrls`        (Re)Register windows port reservations (Required for
                            listening on all interfaces).

-   `-l, --Logging`            Log all requests/responses to Jackett

-   `-t, --Tracing`            Enable tracing

-   `-c, --UseClient`          Override web client selection.
                            [automatic(Default)/httpclient/httpclient2]

-   `-x, --ListenPublic`       Listen publicly

-   `-z, --ListenPrivate`      Only allow local access

-   `-p, --Port`               Web server port

-   `-m, --MigrateSettings`    Migrate settings manually (Must be an admin on Windows)

-   `-n, --IgnoreSslErrors`    [true/false] Ignores invalid SSL certificates

-   `-d, --DataFolder`         Specify the location of the data folder (Must be an admin on Windows)
    - e.g. --DataFolder="D:\Your Data\Jackett\".
    - Don't use this on Unix (mono) systems. On Unix just adjust the HOME directory of the user to the datadir or set the XDG_CONFIG_HOME environment variable.

-   `--NoRestart`              Don't restart after update

-   `--PIDFile`                Specify the location of PID file

-   `--NoUpdates`              Disable automatic updates

-   `--help`                   Display this help screen.

-   `--version`                Display version information.
</details>

## Building from source

### Windows
* Install the .NET 5 [SDK](https://www.microsoft.com/net/download/windows)
* Clone Jackett
* Open PowerShell and from the `src` directory:
* - run `dotnet msbuild /restore`
* - then run `dotnet restore`
* - and run `dotnet build`
* Open the Jackett solution in Visual Studio 2019 (version 16.9 or above)
* Select **Jackett.Server** as the startup project
* In the drop-down menu of the run button select **Jackett.Server** instead of _IIS Express_
* Build/Start the project

### OSX


```bash
# manually install osx dotnet via:
https://dotnet.microsoft.com/download?initial-os=macos
# then:
git clone https://github.com/Jackett/Jackett.git
cd Jackett/src

# dotnet core version
dotnet publish Jackett.Server -f net5.0 --self-contained -r osx-x64 -c Debug # takes care of everything
./Jackett.Server/bin/Debug/net5.0/osx-x64/jackett # run jackett
```

### Linux


```bash
sudo apt install nuget msbuild dotnet-sdk-5.0 # install build tools (Debian/ubuntu)
git clone https://github.com/Jackett/Jackett.git
cd Jackett/src

# dotnet core version
dotnet publish Jackett.Server -f net5.0 --self-contained -r linux-x64 -c Debug # takes care of everything
./Jackett.Server/bin/Debug/net5.0/linux-x64/jackett # run jackett
```

## Screenshots

![screenshot](https://raw.githubusercontent.com/Jackett/Jackett/master/.github/jackett-screenshot1.png)

![screenshot](https://raw.githubusercontent.com/Jackett/Jackett/master/.github/jackett-screenshot2.png)

![screenshot](https://raw.githubusercontent.com/Jackett/Jackett/master/.github/jackett-screenshot3.png)

[inviteneeded]: https://raw.githubusercontent.com/Jackett/Jackett/master/.github/label-inviteneeded.png
