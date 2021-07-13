<p align="center"><img src="https://raw.githubusercontent.com/sdushantha/qr-filetransfer/master/logo.png"><br></p>
<p align="center">
<a href="https://pypi.org/project/qr-filetransfer/"><img src="https://img.shields.io/badge/release-v2.5-blue.svg"></a>
<a href="https://pepy.tech/badge/qr-filetransfer"><img src="https://pepy.tech/badge/qr-filetransfer"></a>
<a href="./LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
<a href="https://img.shields.io/badge/support-Linux%20|%20MacOS%20|%20Windows%20-blue.svg"><img src="https://img.shields.io/badge/support-Linux%20|%20MacOS%20|%20Windows%20-blue.svg"></a>
</p>
<p align="center">✨Transfer files over WiFi between your computer and your smartphone from the terminal✨</p>


<p align="center"><img src="http://giphygifs.s3.amazonaws.com/media/RdKsqWjGD20ubji5z6/giphy.gif"></p>

## Installation

You will find the most updated version of ```qr-filetransfer``` here. But if you want the most stable version, use ```pip``` to install it

### Pip Install

Global Install

```pip3 install qr-filetransfer[extras]```

Local Install

```pip3 install --user qr-filetransfer[extras]```

If you run into problems during the install, try removing the optional `[extras]` at the end of the command.

### Git Install

```bash
# clone the repo
$ git clone https://github.com/sdushantha/qr-filetransfer.git

# change the working directory to qr-filetransfer
$ cd qr-filetransfer

# install the requirements
$ pip3 install -r requirements.txt
```


## Usage
```
usage: qr-filetransfer [-h] [--debug] [--receive] [--port PORT]
                       [--ip_addr {192.168.0.105}] [--auth AUTH]
                       file_path

Transfer files over WiFi between your computer and your smartphone from the
terminal

positional arguments:
  file_path             path that you want to transfer or store the received
                        file.

optional arguments:
  -h, --help            show this help message and exit
  --debug, -d           show the encoded url.
  --receive, -r         enable upload mode, received file will be stored at
                        given path.
  --port PORT, -p PORT  use a custom port
  --ip_addr {192.168.0.105}
                        specify IP address
  --auth AUTH           add authentication, format: username:password
  --no-force-download   Allow browser to handle the file processing instead of
                        forcing it to download.
```

**Note:** Both devices needs to be connected to the same network

**Exiting**

To exit the program, just press ```CTRL+C```.

---

Transfer a single file
```bash
$ qr-filetransfer /path/to/file.txt
```


Transfer a full directory. **Note:** the directory gets zipped before being transferred
```bash
$ qr-filetransfer /path/to/directory/
```

Receive/upload a file from your phone to your computer
```bash
$ qr-filetransfer -r /path/to/receive/file/to/
```

![](https://user-images.githubusercontent.com/27065646/56946075-7444ae00-6b29-11e9-9387-06ae063e1361.png)

## Credits
Inspired by the Go project [qr-filetransfer](https://github.com/claudiodangelis/qr-filetransfer)

## License
MIT License

Copyright © 2019 Siddharth Dushantha

Active contributer - [Yu-Chen Lin](https://github.com/npes87184)
