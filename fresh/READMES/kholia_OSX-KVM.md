### Note

This `README.md` documents the process of creating a `Virtual Hackintosh`
system.

Note: All blobs and resources included in this repository are re-derivable (all
instructions are included!).

:green_heart: Looking for **commercial** support with this stuff? I am [available
over email](mailto:dhiru.kholia@gmail.com?subject=[GitHub]%20OSX-KVM%20Commercial%20Support%20Request&body=Hi%20-%20We%20are%20interested%20in%20purchasing%20commercial%20support%20options%20for%20your%20project.) for a chat for **commercial support options only**.

Working with `Proxmox` and macOS? See [Nick's blog for sure](https://www.nicksherlock.com/).

Yes, we support offline macOS installations now 🎉


### Contributing Back

This project can always use your help, time and attention. I am looking for
help (pull-requests!) with the following work items:

* Documentation around running macOS on popular cloud providers (Hetzner, GCP,
  AWS). See the `Is This Legal?` section and associated references.

* Document (share) how you use this project to build + test open-source
  projects / get your stuff done.

* Document how to use this project for XNU kernel debugging and development.

* Document the process to launch a bunch of headless macOS VMs (build farm).

* Document usage of [munki](https://github.com/munki/munki) to deploy software
  to such a `build farm`.

* Enable VNC + SSH support out of the box or more easily.

* Robustness improvements are always welcome!

* (Not so) crazy idea - automate the macOS installation via OpenCV.


### Requirements

* A modern Linux distribution. E.g. Ubuntu 20.04 LTS 64-bit or later.

* QEMU >= 4.2.0

* A CPU with Intel VT-x / AMD SVM support is required (`egrep '(vmx|svm)' /proc/cpuinfo`)

* A CPU with SSE4.1 support is required for >= macOS Sierra

* A CPU with AVX2 support is required for >= macOS Mojave

Note: Older AMD CPU(s) are known to be problematic. AMD FX-8350 works but
Phenom II X3 720 does not. Ryzen processors work just fine.


### Installation Preparation

* KVM may need the following tweak on the host machine to work.

  ```
  echo 1 | sudo tee /sys/module/kvm/parameters/ignore_msrs
  ```

  To make this change permanent, you may use the following command.

  ```
  sudo cp kvm.conf /etc/modprobe.d/kvm.conf  # for intel boxes only
  ```

* Install QEMU and other packages.

  ```
  sudo apt-get install qemu uml-utilities virt-manager git \
      wget libguestfs-tools p7zip-full -y
  ```

  This step may need to be adapted for your Linux distribution.

* Add user to the `kvm` group (might be needed).

  ```
  sudo usermod -aG kvm $(whoami)
  ```

* Clone this repository on your QEMU system. Files from this repository are
  used in the following steps.

  ```
  cd ~

  git clone --depth 1 --recursive https://github.com/kholia/OSX-KVM.git

  cd OSX-KVM
  ```

* Fetch macOS installer.

  ```
  ./fetch-macOS-v2.py
  ```

  ATTENTION: Installing `Big Sur` is NOT recommended at this time, unless you
  are a Hackintosh developer! Let the `Big Sur` setup sit at the `Country
  Selection` screen and other similar places for a while ;)

  You can choose your desired macOS version here. After executing this step,
  you should have the `BaseSystem.dmg` file in the current folder.

  Sample run:

  ```
  $ ./fetch-macOS-v2.py
  1. High Sierra (10.13)
  2. Mojave (10.14)
  3. Catalina (10.15) - RECOMMENDED
  4. Latest (Big Sur - 11)

  Choose a product to download (1-4): 3
  ```

  Note: Modern NVIDIA GPUs are supported on HighSierra but not on later
  versions.

* Convert the downloaded `BaseSystem.dmg` file into the `BaseSystem.img` file.

  ```
  qemu-img convert BaseSystem.dmg -O raw BaseSystem.img
  ```

* Create a virtual HDD image where macOS will be installed. If you change the
  name of the disk image from `mac_hdd.img` to something else, the boot scripts
  will need to be updated to point to the new image name.

  ```
  qemu-img create -f qcow2 mac_hdd_ng.img 128G
  ```

  NOTE: Create this HDD image file on a fast SSD/NVMe disk for best results.

* Now you are ready to install macOS 🚀


### Installation

- CLI method (primary). Just run the `OpenCore-Boot.sh` script to start the
  installation process.

  ```
  ./OpenCore-Boot.sh
  ```

  Note: This same script works for Big Sur, Catalina, Mojave, and High Sierra.

- You are all set! 🙌

- (OPTIONAL) Use this macOS VM disk with libvirt (virt-manager / virsh stuff).

  - Edit `macOS-libvirt-Catalina.xml` file and change the various file paths (search
    for `CHANGEME` strings in that file). The following command should do the
    trick usually.

    ```
    sed "s/CHANGEME/$USER/g" macOS-libvirt-Catalina.xml > macOS.xml

    virt-xml-validate macOS.xml
    ```

  - Create a VM by running the following command.

    ```bash
    virsh --connect qemu:///system define macOS.xml
    ```

  - Launch `virt-manager` and start the `macOS` virtual machine.

    Note: You may need to run `sudo ip link delete tap0` command before
    `virt-manager` is able to start the `macOS` VM.


### Setting Expectations Right

Nice job on setting up a `Virtual Hackintosh` system! Such a system can be used
for a variety of purposes (e.g. software builds, testing, reversing work), and
it may be all you need, along with some tweaks documented in this repository.

However, such a system lacks graphical acceleration, a reliable sound sub-system,
USB (3) functionality and other similar things. To enable these things, take a
look at our [notes](notes.md). We would like to resume our testing and
documentation work around this area. Please [reach out to us](mailto:dhiru.kholia@gmail.com?subject=[GitHub]%20OSX-KVM%20Funding%20Support)
if you are able to fund this area of work.

It is possible to have 'beyond-native-apple-hw' performance but it does require
work, patience, and a bit of luck (perhaps?).


### Post-Installation

* See [networking notes](networking-qemu-kvm-howto.txt) to setup guest networking.

  I have the following commands present in `/etc/rc.local`.

  ```
  #!/usr/bin/env bash

  sudo ip tuntap add dev tap0 mode tap
  sudo ip link set tap0 up promisc on
  sudo ip link set dev virbr0 up
  sudo ip link set dev tap0 master virbr0
  ```

  This has been enough for me so far.

  Note: You may need to enable the `rc.local` functionality manually on modern
  Ubuntu versions. Check out the [notes](notes.md) included in this repository
  for details.

* To passthrough GPUs and other devices, see [these notes](notes.md).

* Need a different resolution? Check out the [notes](notes.md) included in this repository.

* Trouble with iMessage? Check out the [notes](notes.md) included in this repository.


### Is This Legal?

The "secret" Apple OSK string is widely available on the Internet. It is also included in a public court document [available here](http://www.rcfp.org/sites/default/files/docs/20120105_202426_apple_sealing.pdf). I am not a lawyer but it seems that Apple's attempt(s) to get the OSK string treated as a trade secret did not work out. Due to these reasons, the OSK string is freely included in this repository.

Please review the ['Legality of Hackintoshing' documentation bits from Dortania's OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/why-oc.html#legality-of-hackintoshing).

Gabriel Somlo also has [some thoughts](http://www.contrib.andrew.cmu.edu/~somlo/OSXKVM/) on the legal aspects involved in running macOS under QEMU/KVM.

You may also find [this 'Announcing Amazon EC2 Mac instances for macOS' article](https://aws.amazon.com/about-aws/whats-new/2020/11/announcing-amazon-ec2-mac-instances-for-macos/
) interesting.


### Motivation

My aim is to enable macOS based educational tasks, builds + testing, kernel
debugging, reversing, and macOS security research in an easy, reproducible
manner without getting 'invested' in Apple's closed ecosystem (too heavily).

These `Virtual Hackintosh` systems are not intended to replace the genuine
physical macOS systems.

Personally speaking, this repository has been a way for me to 'exit' the Apple
ecosystem. It has helped me to test and compare the interoperability of `Canon
CanoScan LiDE 120` scanner, and `Brother HL-2250DN` laser printer. And these
devices now work decently enough on modern versions of Ubuntu (Yay for free
software). Also, a long time back, I had to completely wipe my (then) brand new
`MacBook Pro (Retina, 15-inch, Late 2013)` and install Xubuntu on it - as the
`OS X` kernel kept crashing on it!

Backstory: I was a (poor) student in Canada in a previous life and Apple made [my work on cracking Apple Keychains](https://github.com/openwall/john/blob/bleeding-jumbo/src/keychain_fmt_plug.c) a lot harder than it needed to be. This is how I got interested in Hackintosh systems.
