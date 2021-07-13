# IPsec VPN Server Auto Setup Scripts

[![Build Status](https://img.shields.io/github/workflow/status/hwdsl2/setup-ipsec-vpn/vpn%20test.svg?cacheSeconds=3600)](https://github.com/hwdsl2/setup-ipsec-vpn/actions) [![GitHub Stars](https://img.shields.io/github/stars/hwdsl2/setup-ipsec-vpn.svg?cacheSeconds=86400)](https://github.com/hwdsl2/setup-ipsec-vpn/stargazers) [![Docker Stars](https://img.shields.io/docker/stars/hwdsl2/ipsec-vpn-server.svg?cacheSeconds=86400)](https://github.com/hwdsl2/docker-ipsec-vpn-server) [![Docker Pulls](https://img.shields.io/docker/pulls/hwdsl2/ipsec-vpn-server.svg?cacheSeconds=86400)](https://github.com/hwdsl2/docker-ipsec-vpn-server)

Set up your own IPsec VPN server in just a few minutes, with IPsec/L2TP, Cisco IPsec and IKEv2 on Ubuntu, Debian and CentOS. All you need to do is provide your own VPN credentials, and let the scripts handle the rest.

An IPsec VPN encrypts your network traffic, so that nobody between you and the VPN server can eavesdrop on your data as it travels via the Internet. This is especially useful when using unsecured networks, e.g. at coffee shops, airports or hotel rooms.

We will use [Libreswan](https://libreswan.org/) as the IPsec server, and [xl2tpd](https://github.com/xelerance/xl2tpd) as the L2TP provider.

[**&raquo; See also: IPsec VPN Server on Docker**](https://github.com/hwdsl2/docker-ipsec-vpn-server)

*Read this in other languages: [English](README.md), [简体中文](README-zh.md).*

#### Table of Contents

- [Quick start](#quick-start)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Next steps](#next-steps)
- [Important notes](#important-notes)
- [Upgrade Libreswan](#upgrade-libreswan)
- [Manage VPN users](#manage-vpn-users)
- [Advanced usage](#advanced-usage)
- [Bugs & Questions](#bugs--questions)
- [Uninstallation](#uninstallation)
- [See also](#see-also)
- [License](#license)

## Quick start

First, prepare your Linux server\* with a fresh install of one of the following OS.

Use this one-liner to set up an IPsec VPN server:

<details open>
<summary>
Ubuntu & Debian
</summary>

```bash
wget https://git.io/vpnsetup -O vpn.sh && sudo sh vpn.sh && sudo ikev2.sh --auto
```
</details>

<details>
<summary>
CentOS & RHEL
</summary>

```bash
wget https://git.io/vpnsetup-centos -O vpn.sh && sudo sh vpn.sh && sudo ikev2.sh --auto
```
</details>

<details>
<summary>
Amazon Linux 2
</summary>

```bash
wget https://git.io/vpnsetup-amzn -O vpn.sh && sudo sh vpn.sh && sudo ikev2.sh --auto
```
</details>

Your VPN login details will be randomly generated, and displayed on the screen when finished.

For other installation options and how to set up VPN clients, read the sections below.

\* A dedicated server or virtual private server (VPS). OpenVZ VPS is not supported.

## Features

- **New:** The faster IPsec/XAuth ("Cisco IPsec") and IKEv2 modes are supported
- **New:** A pre-built [Docker image](https://github.com/hwdsl2/docker-ipsec-vpn-server) of the VPN server is now available
- Fully automated IPsec VPN server setup, no user input needed
- Encapsulates all VPN traffic in UDP - does not need ESP protocol
- Can be directly used as "user-data" for a new Amazon EC2 instance
- Includes `sysctl.conf` optimizations for improved performance
- Tested with Ubuntu, Debian, CentOS/RHEL and Amazon Linux 2

## Requirements

A newly created [Amazon EC2](https://aws.amazon.com/ec2/) instance, from one of these images:
- [Ubuntu 20.04 (Focal) or 18.04 (Bionic)](https://cloud-images.ubuntu.com/locator/)
- [Debian 10 (Buster)](https://wiki.debian.org/Cloud/AmazonEC2Image)[\*](#debian-10-note)[ or 9 (Stretch)](https://wiki.debian.org/Cloud/AmazonEC2Image)
- [CentOS 8](https://wiki.centos.org/Cloud/AWS)[\*\*](#centos-8-note)[ or 7](https://wiki.centos.org/Cloud/AWS)
- [Red Hat Enterprise Linux (RHEL) 8 or 7](https://aws.amazon.com/partners/redhat/faqs/)
- [Amazon Linux 2](https://aws.amazon.com/amazon-linux-2/)

See [detailed instructions](https://blog.ls20.com/ipsec-l2tp-vpn-auto-setup-for-ubuntu-12-04-on-amazon-ec2/#vpnsetup) and [EC2 pricing](https://aws.amazon.com/ec2/pricing/). Alternatively, you may also deploy rapidly using [CloudFormation](aws/README.md).

**-OR-**

A dedicated server or virtual private server (VPS), freshly installed with one of the above OS. OpenVZ VPS is not supported, users could instead try [OpenVPN](https://github.com/Nyr/openvpn-install).

This also includes Linux VMs in public clouds, such as [DigitalOcean](https://blog.ls20.com/digitalocean), [Vultr](https://blog.ls20.com/vultr), [Linode](https://blog.ls20.com/linode), [Google Compute Engine](https://cloud.google.com/compute/), [Amazon Lightsail](https://aws.amazon.com/lightsail/), [Microsoft Azure](https://azure.microsoft.com), [OVH](https://www.ovhcloud.com/en/vps/) and [IBM Cloud](https://www.ibm.com/cloud/virtual-servers).

[![Deploy to AWS](docs/images/aws-deploy-button.png)](aws/README.md) [![Deploy to Azure](docs/images/azure-deploy-button.png)](azure/README.md) [![Deploy to DigitalOcean](docs/images/do-install-button.png)](http://dovpn.carlfriess.com/) [![Deploy to Linode](docs/images/linode-deploy-button.png)](https://cloud.linode.com/stackscripts/37239)

[**&raquo; I want to run my own VPN but don't have a server for that**](https://blog.ls20.com/ipsec-l2tp-vpn-auto-setup-for-ubuntu-12-04-on-amazon-ec2/#gettingavps)

Advanced users can set up the VPN server on a [Raspberry Pi](https://www.raspberrypi.org). See [[1]](https://elasticbyte.net/posts/setting-up-a-native-cisco-ipsec-vpn-server-using-a-raspberry-pi/) [[2]](https://www.stewright.me/2018/07/create-a-raspberry-pi-vpn-server-using-l2tpipsec/).

<a name="debian-10-note"></a>
\* Debian 10 users should [use the standard Linux kernel](docs/clients.md#debian-10-kernel). If using Debian 10 on EC2, you must first switch to the standard Linux kernel before running the VPN setup script.   
<a name="centos-8-note"></a>
\*\* Support for CentOS Linux 8 [will end on December 31, 2021](https://wiki.centos.org/About/Product).

:warning: **DO NOT** run these scripts on your PC or Mac! They should only be used on a server!

## Installation

First, update your system with `apt-get update && apt-get dist-upgrade` (Ubuntu/Debian) or `yum update` and reboot. This is optional, but recommended.

To install the VPN, please choose one of the following options:

**Option 1:** Have the script generate random VPN credentials for you (will be displayed when finished):

<details open>
<summary>
Ubuntu & Debian
</summary>

```bash
wget https://git.io/vpnsetup -O vpn.sh && sudo sh vpn.sh
```
</details>

<details>
<summary>
CentOS & RHEL
</summary>

```bash
yum -y install wget
wget https://git.io/vpnsetup-centos -O vpn.sh && sudo sh vpn.sh
```
</details>

<details>
<summary>
Amazon Linux 2
</summary>

```bash
wget https://git.io/vpnsetup-amzn -O vpn.sh && sudo sh vpn.sh
```
</details>

After successful installation, it is recommended to [set up IKEv2](docs/ikev2-howto.md):

```bash
sudo ikev2.sh --auto
```

**Option 2:** Edit the script and provide your own VPN credentials:

<details open>
<summary>
Ubuntu & Debian
</summary>

```bash
wget https://git.io/vpnsetup -O vpn.sh
nano -w vpn.sh
[Replace with your own values: YOUR_IPSEC_PSK, YOUR_USERNAME and YOUR_PASSWORD]
sudo sh vpn.sh
```
</details>

<details>
<summary>
CentOS & RHEL
</summary>

```bash
yum -y install wget nano
wget https://git.io/vpnsetup-centos -O vpn.sh
nano -w vpn.sh
[Replace with your own values: YOUR_IPSEC_PSK, YOUR_USERNAME and YOUR_PASSWORD]
sudo sh vpn.sh
```
</details>

<details>
<summary>
Amazon Linux 2
</summary>

```bash
wget https://git.io/vpnsetup-amzn -O vpn.sh
nano -w vpn.sh
[Replace with your own values: YOUR_IPSEC_PSK, YOUR_USERNAME and YOUR_PASSWORD]
sudo sh vpn.sh
```
</details>

**Note:** A secure IPsec PSK should consist of at least 20 random characters.

After successful installation, it is recommended to [set up IKEv2](docs/ikev2-howto.md):

```bash
sudo ikev2.sh --auto
```

**Option 3:** Define your VPN credentials as environment variables:

<details open>
<summary>
Ubuntu & Debian
</summary>

```bash
# All values MUST be placed inside 'single quotes'
# DO NOT use these special characters within values: \ " '
wget https://git.io/vpnsetup -O vpn.sh
sudo VPN_IPSEC_PSK='your_ipsec_pre_shared_key' \
VPN_USER='your_vpn_username' \
VPN_PASSWORD='your_vpn_password' \
sh vpn.sh
```
</details>

<details>
<summary>
CentOS & RHEL
</summary>

```bash
# All values MUST be placed inside 'single quotes'
# DO NOT use these special characters within values: \ " '
yum -y install wget
wget https://git.io/vpnsetup-centos -O vpn.sh
sudo VPN_IPSEC_PSK='your_ipsec_pre_shared_key' \
VPN_USER='your_vpn_username' \
VPN_PASSWORD='your_vpn_password' \
sh vpn.sh
```
</details>

<details>
<summary>
Amazon Linux 2
</summary>

```bash
# All values MUST be placed inside 'single quotes'
# DO NOT use these special characters within values: \ " '
wget https://git.io/vpnsetup-amzn -O vpn.sh
sudo VPN_IPSEC_PSK='your_ipsec_pre_shared_key' \
VPN_USER='your_vpn_username' \
VPN_PASSWORD='your_vpn_password' \
sh vpn.sh
```
</details>

After successful installation, it is recommended to [set up IKEv2](docs/ikev2-howto.md):

```bash
sudo ikev2.sh --auto
```

**Note:** If unable to download via `wget`, you may also open [vpnsetup.sh](vpnsetup.sh), [vpnsetup_centos.sh](vpnsetup_centos.sh) or [vpnsetup_amzn.sh](vpnsetup_amzn.sh), and click the **`Raw`** button on the right. Press `Ctrl-A` to select all, `Ctrl-C` to copy, then paste into your favorite editor.

## Next steps

Get your computer or device to use the VPN. Please refer to:

[**Configure IPsec/L2TP VPN Clients**](docs/clients.md)

[**Configure IPsec/XAuth ("Cisco IPsec") VPN Clients**](docs/clients-xauth.md)

[**Guide: How to Set Up and Use IKEv2 VPN**](docs/ikev2-howto.md)

If you get an error when trying to connect, see [Troubleshooting](docs/clients.md#troubleshooting).

Enjoy your very own VPN! :sparkles::tada::rocket::sparkles:

## Important notes

*Read this in other languages: [English](README.md#important-notes), [简体中文](README-zh.md#重要提示).*

**Windows users**: A [one-time registry change](docs/clients.md#windows-error-809) is required if the VPN server or client is behind NAT (e.g. home router).

**Android users**: If you encounter connection issues, try [these steps](docs/clients.md#android-mtumss-issues).

The same VPN account can be used by your multiple devices. However, due to an IPsec/L2TP limitation, if you wish to connect multiple devices simultaneously from behind the same NAT (e.g. home router), you must use only [IPsec/XAuth mode](docs/clients-xauth.md), or [set up IKEv2](docs/ikev2-howto.md).

If you wish to view or update VPN user accounts, see [Manage VPN users](docs/manage-users.md). Helper scripts are included for convenience.

For servers with an external firewall (e.g. [EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)/[GCE](https://cloud.google.com/vpc/docs/firewalls)), open UDP ports 500 and 4500 for the VPN. Aliyun users, see [#433](https://github.com/hwdsl2/setup-ipsec-vpn/issues/433).

Clients are set to use [Google Public DNS](https://developers.google.com/speed/public-dns/) when the VPN is active. If another DNS provider is preferred, you may [use alternative DNS servers](docs/advanced-usage.md).

Using kernel support could improve IPsec/L2TP performance. It is available on [all supported OS](#requirements). Ubuntu users should install the `linux-modules-extra-$(uname -r)` (or `linux-image-extra`) package and run `service xl2tpd restart`.

The scripts will backup existing config files before making changes, with `.old-date-time` suffix.

## Upgrade Libreswan

The additional scripts in [extras/](extras/) can be used to upgrade [Libreswan](https://libreswan.org) ([changelog](https://github.com/libreswan/libreswan/blob/master/CHANGES) | [announce](https://lists.libreswan.org/mailman/listinfo/swan-announce)). The latest supported version is `4.4`. Check which version is installed: `ipsec --version`.

<details open>
<summary>
Ubuntu & Debian
</summary>

```bash
wget https://git.io/vpnupgrade -O vpnup.sh && sudo sh vpnup.sh
```
</details>

<details>
<summary>
CentOS & RHEL
</summary>

```bash
wget https://git.io/vpnupgrade-centos -O vpnup.sh && sudo sh vpnup.sh
```
</details>

<details>
<summary>
Amazon Linux 2
</summary>

```bash
wget https://git.io/vpnupgrade-amzn -O vpnup.sh && sudo sh vpnup.sh
```
</details>

## Manage VPN users

See [Manage VPN users](docs/manage-users.md).

- [View or update the IPsec PSK](docs/manage-users.md#view-or-update-the-ipsec-psk)
- [View VPN users](docs/manage-users.md#view-vpn-users)
- [Manage VPN users using helper scripts](docs/manage-users.md#manage-vpn-users-using-helper-scripts)
- [Manually manage VPN users](docs/manage-users.md#manually-manage-vpn-users)

## Advanced usage

See [Advanced usage](docs/advanced-usage.md).

- [Use alternative DNS servers](docs/advanced-usage.md#use-alternative-dns-servers)
- [DNS name and server IP changes](docs/advanced-usage.md#dns-name-and-server-ip-changes)
- [Internal VPN IPs and traffic](docs/advanced-usage.md#internal-vpn-ips-and-traffic)
- [Split tunneling](docs/advanced-usage.md#split-tunneling)
- [Access VPN server's subnet](docs/advanced-usage.md#access-vpn-servers-subnet)
- [IKEv2 only VPN](docs/advanced-usage.md#ikev2-only-vpn)
- [Modify IPTables rules](docs/advanced-usage.md#modify-iptables-rules)

## Bugs & Questions

- Got a question? Please first search other people's comments [in this Gist](https://gist.github.com/hwdsl2/9030462#comments) and [on my blog](https://blog.ls20.com/ipsec-l2tp-vpn-auto-setup-for-ubuntu-12-04-on-amazon-ec2/#disqus_thread).
- Ask VPN related questions on the [Libreswan](https://lists.libreswan.org/mailman/listinfo/swan) or [strongSwan](https://lists.strongswan.org/mailman/listinfo/users) mailing list, or read these wikis: [[1]](https://libreswan.org/wiki/Main_Page) [[2]](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-securing_virtual_private_networks) [[3]](https://wiki.strongswan.org/projects/strongswan/wiki/UserDocumentation) [[4]](https://wiki.gentoo.org/wiki/IPsec_L2TP_VPN_server) [[5]](https://wiki.archlinux.org/index.php/Openswan_L2TP/IPsec_VPN_client_setup).
- If you found a reproducible bug, open a [GitHub Issue](https://github.com/hwdsl2/setup-ipsec-vpn/issues?q=is%3Aissue) to submit a bug report.

## Uninstallation

See [Uninstall the VPN](docs/uninstall.md).

## See also

- [IPsec VPN Server on Docker](https://github.com/hwdsl2/docker-ipsec-vpn-server)

## License

Copyright (C) 2014-2021 [Lin Song](https://github.com/hwdsl2) [![View my profile on LinkedIn](https://static.licdn.com/scds/common/u/img/webpromo/btn_viewmy_160x25.png)](https://www.linkedin.com/in/linsongui)   
Based on [the work of Thomas Sarlandie](https://github.com/sarfata/voodooprivacy) (Copyright 2012)

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/3.0/88x31.png)](http://creativecommons.org/licenses/by-sa/3.0/)   
This work is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/)  
Attribution required: please include my name in any derivative and let me know how you have improved it!
