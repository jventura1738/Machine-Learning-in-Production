# Windows Precision Touchpad Implementation for Apple MacBook family/Magic Trackpad 2

[![Build Status](https://ligstd.visualstudio.com/_apis/public/build/definitions/7694e0d0-94e3-4fd2-b39a-ecd261e1ba2e/22/badge)](https://ligstd.visualstudio.com/Apple%20PTP%20Trackpad/_build?definitionId=22)

This project implements Windows Precision Touchpad Protocol for Apple MacBook family/Magic Trackpad 2 on Windows 10. Both USB (traditional and T2), SPI and Bluetooth trackpads are supported.

## Donation?

A few people asked me why I removed donation. My current financial situation doesn't require me to accept donation for the budget of future development. If you are considering donation, please consider other meaningful projects and foundations, such as [Electronic Frontier Foundation](https://www.eff.org/).

## Official Driver?

Bootcamp 6.1.5 offers official driver for T2-based model and Magic Trackpad 2. You can also consider using the official driver if you have such Mac. If you have an older model (e.g. MacBooks before 2018/2019), this is the only implementation for these models (yet). 

## Future Plans and feature tracking

Use the [Azure DevOps Board](https://ligstd.visualstudio.com/Apple%20PTP%20Trackpad/_workitems/) to track feature and device support plans. Bug reports should go to Github issues.

## See it in action (YouTube video)

[![Watch the video](https://img.youtube.com/vi/-GWlfw7omdo/hqdefault.jpg)](https://youtu.be/-GWlfw7omdo)

## Converged Installation Guide

**IMPORTANT:** Given changes in Microsoft driver code signing policy, and the compliance need of EV certificate, CI auto builds beyond 2021/01/06 04:00AM EST will not be automatically signed with normal code signing certificate. These builds are still supposed via TestSigning, but not recommended for normal users. Proper WHQL and EV dual-signed packages will be released manually, which can be downloaded from the release page.

0. Make sure you uninstalled `Trackpad++` completely if you have previously does so
1. Go to the release tab in Github and download the newest version for your architecture
2. Right click `AmtPtpDevice.inf` and install it
3. If you have a Magic Trackpad 2 and want to use it in Bluetooth mode: manaully pair it in PC Settings.

**Note: it is unnecessary to enable test signing, or install the certificate manually. Doing so may cause problems in installation. See [this issue](https://github.com/imbushuo/mac-precision-touchpad/issues/228#issuecomment-538689587) for detailed explanation.**

## Also Uninstallation (extremely important for reinstallation `Trackpad++` and such)

1. Go to device manager
2. Find the "Apple Precision Touch Device"
3. Right click "remove the device" and also check "uninstall driver"
4. Rescan devices

## Installation with Chocolatey

The drivers are available as a [Chocolatey package](https://chocolatey.org/packages/mac-precision-touchpad/). To install using [Chocolatey](https://chocolatey.org) run:

```
choco install mac-precision-touchpad
```

## For developers

- SPI/T2 version is kernel-mode driver, using KMDF Framework v1.23. Bluetooth driver uses KMDF Framework 1.15. Windows 10 Driver Development Kit Version 2004 is required for development and testing.
- USB version is a user-mode driver, using UMDF Framework v2.15. Windows 10 Driver Development Kit Version 2004 is required for development and testing.

## Device support

There is a bring-up issue for certain MacBook Pro and MacBook Air. I am looking into it. If you have such device with Windows installed, please contact me so I can look into the issue remotely (as I don't have many devices).

- [x] Non-Retina MacBook 
- [x] Some non-Retina MacBook Pro (2011 and 2012)
- [x] MacBook Pro with Retina Display (MacBookPro 10,1, MacBookPro10,2 & MacBookPro11,1)
- [x] All recent MacBook Air (Please report if your model is not supported)
- [x] MacBook Pro with Retina Display (2013, 2014, 2015, 13-inch & 15-inch)
- [x] New MacBook (12-inch)
- [x] MacBook Pro 2015, 2016, 2017 (a few SPI devices are in work-in-progress state)
- [x] T2-based devices: MacBook Air 2018, MacBook Pro 2017/2018/2019/2020: Use default fallback, experience might not be optimal. Open a issue if you encountered dead touch regions.
- [x] Magic Trackpad 2 (USB)
- [x] Magic Trackpad 2 (Bluetooth connection)

## Roadmap

- [x] Touchpad Device Power Management
- [x] Touchpad Protocol Stack Implementation
- [x] Touchpad Raw Input Output (in Driver Trace)
- [x] HID Protocol Implementation (PTP Touch)
- [x] HID Protocol Implementation (Configuration)
- [x] Device Test (Magic Trackpad 2)
- [x] Refine input experience (tip switch detection and pressure)
- [x] Refine input experience (gesture experience)
- [x] More Models
- [x] SPI
- [x] KM Driver cross-cert
- [x] Bluetooth
- [ ] Defuzz
- [ ] Input sensitivity configuration

## Acknowledgements

**UPDATE 2021/05**: She got a M1 Mac now.

People familiar with me know that I don't use Apple MacBook (so development work of this driver occurs on a Surface Pro 4). People probably think it doesn't make sense that I started this project. The motivation behind this project origin from complaints from my girlfriend. Hearing about frequent complains about Dell XPS 13's touchpad (though it passed Precision Touchpad certification), I decided to start this project, so by the time she switches to MacBook Pro, she will have excellent touchpad experience out-of-box, even on Windows. This driver is made for you, but also for everyone.

I would like to thank projects like [magictrackpad2-dkms](https://github.com/robbi5/magictrackpad2-dkms) and [macbook12-spi-driver](https://github.com/cb22/macbook12-spi-driver) that inspire me. I would also like to thank my friends for providing me immense help on devices and testing.
 
## License

- USB driver is licensed under [GPLv2](LICENSE-GPL.md).
- SPI driver is licensed under [MIT](LICENSE-MIT.md).

