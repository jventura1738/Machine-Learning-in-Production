<!--
===============================================
vidgear library source-code is deployed under the Apache 2.0 License:

Copyright (c) 2019-2020 Abhishek Thakur(@abhiTronix) <abhi.una12@gmail.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
===============================================
-->

<h1 align="center">
  <img src="docs/overrides/assets/images/vidgear.png" alt="VidGear" title="Logo designed by Abhishek Thakur(@abhiTronix), under CC-BY-NC-SA 4.0 License" width="80%"/>
</h1>
<h2 align="center">
  <img src="docs/overrides/assets/images/tagline.svg" alt="VidGear tagline" width="40%"/>
</h2>

<div align="center">

[Releases][release]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Gears][gears]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Documentation][docs]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Installation][installation]&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[License](#license)

[![Build Status][github-cli]][github-flow] [![Codecov branch][codecov]][code] [![Build Status][appveyor]][app]

[![Azure DevOps builds (branch)][azure-badge]][azure-pipeline] [![PyPi version][pypi-badge]][pypi] [![Glitter chat][gitter-bagde]][gitter]

[![Code Style][black-badge]][black]
</div>

&nbsp;

VidGear is a **High-Performance Video Processing Python Library** that provides an easy-to-use, highly extensible, thoroughly optimised **Multi-Threaded + Asyncio Framework** on top of many state-of-the-art specialized libraries like *[OpenCV][opencv], [FFmpeg][ffmpeg], [ZeroMQ][zmq], [picamera][picamera], [starlette][starlette], [streamlink][streamlink], [pafy][pafy], [pyscreenshot][pyscreenshot], [aiortc][aiortc] and [python-mss][mss]* serving at its backend, and enable us to flexibly exploit their internal parameters and methods, while silently delivering **robust error-handling and real-time performance 🔥**

VidGear primarily focuses on simplicity, and thereby lets programmers and software developers to easily integrate and perform Complex Video Processing Tasks, in just a few lines of code.

&nbsp;

The following **functional block diagram** clearly depicts the generalized functioning of VidGear APIs:

<p align="center">
  <img src="docs/overrides/assets/images/gears_fbd.png" alt="@Vidgear Functional Block Diagram" />
</p>

&nbsp;

# Table of Contents

* [**TL;DR**](#tldr)
* [**Getting Started**](#getting-started)
* [**Gears: What are these?**](#gears-what-are-these)
  * [**CamGear**](#camgear)
  * [**PiGear**](#pigear)
  * [**VideoGear**](#videogear)
  * [**ScreenGear**](#screengear)
  * [**WriteGear**](#writegear)
  * [**StreamGear**](#streamgear)
  * [**NetGear**](#netgear)
  * [**WebGear**](#webgear)
  * [**WebGear_RTC**](#webgear_rtc)
  * [**NetGear_Async**](#netgear_async)
* [**Community Channel**](#community-channel)
* [**Contributions & Support**](#contributions--support)
  * [**Support**](#support)
  * [**Contributors**](#contributors)
* [**Citation**](#citation)
* [**Copyright**](#copyright)


&nbsp;

&nbsp;



# TL;DR
  
#### What is vidgear?

> *"VidGear is a High-Performance Framework that provides an one-stop **Video-Processing** solution for building complex real-time media applications in python."*

#### What does it do?

> *"VidGear can read, write, process, send & receive video files/frames/streams from/to various devices in real-time, and faster than underline libraries."*

#### What is its purpose?

> *"Write Less and Accomplish More"* — **VidGear's Motto**

> *"Built with simplicity in mind, VidGear lets programmers and software developers to easily integrate and perform **Complex Video-Processing Tasks** in their existing or newer applications without going through hefty documentation and in just a [few lines of code][switch_from_cv]. Beneficial for both, if you're new to programming with Python language or already a pro at it."*

&nbsp;

&nbsp;

## Getting Started

If this is your first time using VidGear, head straight to the [Installation ➶][installation] to install VidGear.

Once you have VidGear installed, **Checkout its Well-Documented Function-Specific [Gears ➶][gears]** 

Also, if you're already familiar with [OpenCV][opencv] library, then see [Switching from OpenCV Library ➶][switch_from_cv]

Or, if you're just getting started with OpenCV, then see [here ➶](https://abhitronix.github.io/vidgear/latest/help/general_faqs/#im-new-to-python-programming-or-its-usage-in-computer-vision-how-to-use-vidgear-in-my-projects)

&nbsp;

&nbsp;


## Gears: What are these?

> **VidGear is built with multiple APIs a.k.a [Gears][gears], each with some unique functionality.**

Each API is designed exclusively to handle/control/process different data-specific & device-specific video streams, network streams, and media encoders/decoders. These APIs provides the user an easy-to-use, dynamic, extensible, and exposed Multi-Threaded + Asyncio optimized internal layer above state-of-the-art libraries to work with, while silently delivering robust error-handling. 

**These Gears can be classified as follows:**

**A. Video-Capture Gears:**

  * [**CamGear:**](#camgear) Multi-Threaded API targeting various IP-USB-Cameras/Network-Streams/Streaming-Sites-URLs.
  * [**PiGear:**](#pigear) Multi-Threaded API targeting various Raspberry-Pi Camera Modules.
  * [**ScreenGear:**](#screengear) Multi-Threaded API targeting ultra-fast Screencasting.    
  * [**VideoGear:**](#videogear) Common Video-Capture API with internal [Video Stabilizer](https://abhitronix.github.io/vidgear/latest/gears/stabilizer/overview/) wrapper.

**B. Video-Writer Gears:**

  * [**WriteGear:**](#writegear) Handles Lossless Video-Writer for file/stream/frames Encoding and Compression.

**C. Streaming Gears:**

  * [**StreamGear**](#streamgear): Handles Transcoding of High-Quality, Dynamic & Adaptive Streaming Formats.

  * **Asynchronous I/O Streaming Gear:**

    * [**WebGear:**](#webgear) ASGI Video-Server that broadcasts Live MJPEG-Frames to any web-browser on the network.
    * [**WebGear_RTC:**](#webgear_rtc) Real-time Asyncio WebRTC media server for streaming directly to peer clients over the network.

**D. Network Gears:**

  * [**NetGear:**](#netgear) Handles High-Performance Video-Frames & Data Transfer between interconnecting systems over the network.

  * **Asynchronous I/O Network Gear:**

    * [**NetGear_Async:**](#netgear_async) Immensely Memory-Efficient Asyncio Video-Frames Network Messaging Framework.


&nbsp;

&nbsp;


## CamGear

<p align="center">
  <img src="docs/overrides/assets/images/camgear.png" alt="CamGear Functional Block Diagram" width="45%"/>
</p>

> *CamGear can grab ultra-fast frames from a diverse range of file-formats/devices/streams, which includes almost any IP-USB Cameras, multimedia video file-formats ([_upto 4k tested_][test-4k]), various network stream protocols such as `http(s), rtp, rstp, rtmp, mms, etc.`, and GStreamer's pipelines, plus direct support for live video streaming sites like YouTube, Twitch, LiveStream, Dailymotion etc.*

CamGear implements a flexible, high-level, multi-threaded framework around OpenCV's [VideoCapture class][opencv-vc] with access almost all of its available parameters. CamGear also employs [streamlink][streamlink] for [piping live videos][piping-live-videos] from various streaming services and also utilizies [pafy][pafy] with [youtube-dl][youtube-dl] at its backend for [YouTube pipelining][youtube-doc]. Furthermore, its framework relies exclusively on [**Threaded Queue mode**][TQM-doc] for ultra-fast, error-free, and synchronized video-frame handling.

### CamGear API Guide:

[**>>> Usage Guide**][camgear-doc]

&nbsp;

&nbsp;


## VideoGear

> *VideoGear API provides a special internal wrapper around VidGear's exclusive [**Video Stabilizer**][stablizer-doc] class.*

VideoGear also acts as a Common Video-Capture API that provides internal access for both [CamGear](#camgear) and [PiGear](#pigear) APIs and their parameters with an exclusive `enablePiCamera` boolean flag.

VideoGear is ideal when you need to switch to different video sources without changing your code much. Also, it enables easy stabilization for various video-streams _(real-time or not)_  with minimum effort and writing way fewer lines of code.


**Below is a snapshot of a VideoGear Stabilizer in action  (_See its detailed usage [here][stablizer-doc-ex]_):**

<p align="center">
  <img src="https://github.com/abhiTronix/Imbakup/raw/master/Images/stabilizer.gif" alt="VideoGear Stabilizer in action!"/>
  <br>
  <sub><i>Original Video Courtesy <a href="http://liushuaicheng.org/SIGGRAPH2013/database.html" title="opensourced video samples database">@SIGGRAPH2013</a></i></sub>
</p>

**Code to generate above result:**

```python
# import required libraries
from vidgear.gears import VideoGear
import numpy as np
import cv2

# open any valid video stream with stabilization enabled(`stabilize = True`)
stream_stab = VideoGear(source="test.mp4", stabilize=True).start()

# open same stream without stabilization for comparison
stream_org = VideoGear(source="test.mp4").start()

# loop over
while True:

    # read stabilized frames
    frame_stab = stream_stab.read()

    # check for stabilized frame if Nonetype
    if frame_stab is None:
        break

    # read un-stabilized frame
    frame_org = stream_org.read()

    # concatenate both frames
    output_frame = np.concatenate((frame_org, frame_stab), axis=1)

    # put text over concatenated frame
    cv2.putText(
        output_frame,
        "Before",
        (10, output_frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )
    cv2.putText(
        output_frame,
        "After",
        (output_frame.shape[1] // 2 + 10, output_frame.shape[0] - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2,
    )

    # Show output window
    cv2.imshow("Stabilized Frame", output_frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close both video streams
stream_org.stop()
stream_stab.stop()
```

### VideoGear API Guide:

[**>>> Usage Guide**][videogear-doc]

&nbsp;

&nbsp;


## PiGear

<p align="center">
  <img src="docs/overrides/assets/images/picam2.webp" alt="PiGear" width="50%" />
</p>

> *PiGear is similar to CamGear but made to support various Raspberry Pi Camera Modules *(such as [OmniVision OV5647 Camera Module][OV5647-picam] and [Sony IMX219 Camera Module][IMX219-picam])*.*

PiGear provides a flexible multi-threaded framework around complete [picamera](https://picamera.readthedocs.io/en/release-1.13/index.html) python library, and provide us the ability to exploit almost all of its parameters like `brightness, saturation, sensor_mode, iso, exposure, etc.` effortlessly. Furthermore, PiGear also supports multiple camera modules, such as in the case of Raspberry-Pi Compute Module IO boards.

Best of all, PiGear contains **Threaded Internal Timer** - that silently keeps active track of any frozen-threads/hardware-failures and exit safely, if any does occur. That means that if you're running PiGear API in your script and someone accidentally pulls the Camera-Module cable out, instead of going into possible kernel panic, API will exit safely to save resources.


**Code to open picamera stream with variable parameters in PiGear API:**

```python
# import required libraries
from vidgear.gears import PiGear
import cv2

# add various Picamera tweak parameters to dictionary
options = {
    "hflip": True,
    "exposure_mode": "auto",
    "iso": 800,
    "exposure_compensation": 15,
    "awb_mode": "horizon",
    "sensor_mode": 0,
}

# open pi video stream with defined parameters
stream = PiGear(resolution=(640, 480), framerate=60, logging=True, **options).start()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()

```
### PiGear API Guide:

[**>>> Usage Guide**][pigear-doc]

&nbsp;

&nbsp;


## ScreenGear

> *ScreenGear is designed exclusively for ultra-fast Screencasting, which means it can grab frames from your monitor in real-time, either by defining an area on the computer screen or full-screen, at the expense of inconsiderable latency. ScreenGear also seamlessly support frame capturing from multiple monitors as well as supports multiple backends.*

ScreenGear implements a multi-threaded wrapper around [**pyscreenshot**][pyscreenshot] & [**python-mss**][mss] python library API and also supports an easy and flexible direct internal parameter manipulation. 

**Below is a snapshot of a ScreenGear API in action:**

<p align="center">
  <img src="docs/overrides/assets/gifs/screengear.gif" alt="ScreenGear in action!"/>
</p>

**Code to generate the above results:**

```python
# import required libraries
from vidgear.gears import ScreenGear
import cv2

# open video stream with default parameters
stream = ScreenGear().start()

# loop over
while True:

    # read frames from stream
    frame = stream.read()

    # check for frame if Nonetype
    if frame is None:
        break

    # {do something with the frame here}

    # Show output window
    cv2.imshow("Output Frame", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# safely close video stream
stream.stop()
```

### ScreenGear API Guide:

[**>>> Usage Guide**][screengear-doc]


&nbsp;

&nbsp;



## WriteGear

<p align="center">
  <img src="docs/overrides/assets/images/writegear.png" alt="WriteGear Functional Block Diagram" width="70%" />
</p>

> *WriteGear handles various powerful Video-Writer Tools that provide us the freedom to do almost anything imaginable with multimedia data.*

WriteGear API provides a complete, flexible, and robust wrapper around [**FFmpeg**][ffmpeg], a leading multimedia framework. WriteGear can process real-time frames into a lossless compressed video-file with any suitable specification _(such as`bitrate, codec, framerate, resolution, subtitles,  etc.`)_. It is powerful enough to perform complex tasks such as [Live-Streaming][live-stream] _(such as for Twitch and YouTube)_ and [Multiplexing Video-Audio][live-audio-doc] with real-time frames in way fewer lines of code. 

Best of all, WriteGear grants users the complete freedom to play with any FFmpeg parameter with its exclusive **Custom Commands function** _(see this [doc][custom-command-doc])_ without relying on any third-party API.

In addition to this, WriteGear also provides flexible access to [**OpenCV's VideoWriter API**][opencv-writer] tools for video-frames encoding without compression.

**WriteGear primarily operates in the following two modes:**

  * **Compression Mode:** In this mode, WriteGear utilizes powerful [**FFmpeg**][ffmpeg] inbuilt encoders to encode lossless multimedia files. This mode provides us the ability to exploit almost any parameter available within FFmpeg, effortlessly and flexibly, and while doing that it robustly handles all errors/warnings quietly. **You can find more about this mode [here ➶][cm-writegear-doc]**

  * **Non-Compression Mode:**  In this mode, WriteGear utilizes basic [**OpenCV's inbuilt VideoWriter API**][opencv-vw] tools. This mode also supports all parameters manipulation available within VideoWriter API, but it lacks the ability to manipulate encoding parameters and other important features like video compression, audio encoding, etc. **You can learn about this mode [here ➶][ncm-writegear-doc]**

### WriteGear API Guide:

[**>>> Usage Guide**][writegear-doc]

&nbsp;

&nbsp;


## StreamGear

<p align="center">
  <img src="docs/overrides/assets/images/streamgear_flow.webp" alt="NetGear API" width=80%/>
</p>


> *StreamGear automates transcoding workflow for generating Ultra-Low Latency, High-Quality, Dynamic & Adaptive Streaming Formats (such as MPEG-DASH) in just few lines of python code.*

StreamGear provides a standalone, highly extensible, and flexible wrapper around [**FFmpeg**][ffmpeg] multimedia framework for generating chunked-encoded media segments of the content.

SteamGear easily transcodes source videos/audio files & real-time video-frames and breaks them into a sequence of multiple smaller chunks/segments of fixed length. These segments make it possible to stream videos at different quality levels _(different bitrates or spatial resolutions)_ and can be switched in the middle of a video from one quality level to another – if bandwidth permits – on a per-segment basis. A user can serve these segments on a web server that makes it easier to download them through HTTP standard-compliant GET requests.

SteamGear also creates a Manifest file _(such as MPD in-case of DASH)_ besides segments that describe these segment information _(timing, URL, media characteristics like video resolution and bit rates)_ and is provided to the client before the streaming session.

SteamGear currently only supports [**MPEG-DASH**](https://www.encoding.com/mpeg-dash/) _(Dynamic Adaptive Streaming over HTTP, ISO/IEC 23009-1)_ but other adaptive streaming technologies such as Apple HLS, Microsoft Smooth Streaming will be added soon.

**StreamGear primarily works in two Independent Modes for transcoding which serves different purposes:**

  * **Single-Source Mode:** In this mode, StreamGear transcodes entire video/audio file _(as opposed to frames by frame)_ into a sequence of multiple smaller chunks/segments for streaming. This mode works exceptionally well, when you're transcoding lossless long-duration videos(with audio) for streaming and required no extra efforts or interruptions. But on the downside, the provided source cannot be changed or manipulated before sending onto FFmpeg Pipeline for processing.  This mode can be easily activated by assigning suitable video path as input to `-video_source` attribute, during StreamGear initialization. ***Learn more about this mode [here ➶][ss-mode-doc]***

  * **Real-time Frames Mode:** When no valid input is received on `-video_source` attribute, StreamGear API activates this mode where it directly transcodes video-frames _(as opposed to a entire file)_, into a sequence of multiple smaller chunks/segments for streaming. In this mode, StreamGear supports real-time [`numpy.ndarray`](https://numpy.org/doc/1.18/reference/generated/numpy.ndarray.html#numpy-ndarray) frames, and process them over FFmpeg pipeline. But on the downside, audio has to added manually _(as separate source)_ for streams. ***Learn more about this mode [here ➶][rtf-mode-doc]***


### StreamGear API Guide:

[**>>> Usage Guide**][streamgear-doc]

&nbsp;

&nbsp;

## NetGear

<p align="center">
  <img src="docs/overrides/assets/images/netgear.png" alt="NetGear API" width=65%/>
</p>

> *NetGear is exclusively designed to transfer video-frames & data synchronously between interconnecting systems over the network in real-time.*

NetGear implements a high-level wrapper around [**PyZmQ**][pyzmq] python library that contains python bindings for [**ZeroMQ**][zmq] - a high-performance asynchronous distributed messaging library.

NetGear seamlessly supports [**Bidirectional data transmission**][netgear_bidata_doc] along with video-frames between receiver(client) and sender(server). 

NetGear can also robustly handle [**Multiple Server-Systems**][netgear_multi_server_doc] and [**Multiple Client-Systems**][netgear_multi_client_doc] and at once, thereby providing access to a seamless exchange of video-frames & data between multiple devices across the network at the same time.

NetGear also enables real-time [**JPEG Frame Compression**][netgear_compression_doc] capabilities for boosting performance significantly while sending video-frames over the network in real-time.

For security, NetGear implements easy access to ZeroMQ's powerful, smart & secure Security Layers that enable [**Strong encryption on data**][netgear_security_doc] and unbreakable authentication between the Server and the Client with the help of custom certificates.

**NetGear as of now seamlessly supports three ZeroMQ messaging patterns:**

* [**`zmq.PAIR`**][zmq-pair] _(ZMQ Pair Pattern)_ 
* [**`zmq.REQ/zmq.REP`**][zmq-req-rep] _(ZMQ Request/Reply Pattern)_
* [**`zmq.PUB/zmq.SUB`**][zmq-pub-sub] _(ZMQ Publish/Subscribe Pattern)_

Whereas supported protocol are: `tcp` and `ipc`.

### NetGear API Guide:

[**>>> Usage Guide**][netgear-doc]

&nbsp;

&nbsp;


## WebGear

> *WebGear is a powerful [ASGI](https://asgi.readthedocs.io/en/latest/) Video-Broadcaster API ideal for transmitting [Motion-JPEG](https://en.wikipedia.org/wiki/Motion_JPEG)-frames from a single source to multiple recipients via the browser.*

WebGear API works on [**Starlette**](https://www.starlette.io/)'s ASGI application and provides a highly extensible and flexible async wrapper around its complete framework. WebGear can flexibly interact with Starlette's ecosystem of shared middleware, mountable applications, [Response classes](https://www.starlette.io/responses/), [Routing tables](https://www.starlette.io/routing/), [Static Files](https://www.starlette.io/staticfiles/), [Templating engine(with Jinja2)](https://www.starlette.io/templates/), etc. 

WebGear API uses an intraframe-only compression scheme under the hood where the sequence of video-frames are first encoded as JPEG-DIB (JPEG with Device-Independent Bit compression) and then streamed over HTTP using Starlette's Multipart [Streaming Response](https://www.starlette.io/responses/#streamingresponse) and a [Uvicorn](https://www.uvicorn.org/#quickstart) ASGI Server. This method imposes lower processing and memory requirements, but the quality is not the best, since JPEG compression is not very efficient for motion video.

In layman's terms, WebGear acts as a powerful **Video Broadcaster** that transmits live video-frames to any web-browser in the network. Additionally, WebGear API also provides a special internal wrapper around [VideoGear](#videogear), which itself provides internal access to both [CamGear](#camgear) and [PiGear](#pigear) APIs, thereby granting it exclusive power of broadcasting frames from any incoming stream. It also allows us to define our custom Server as source to manipulate frames easily before sending them across the network(see this [doc][webgear-cs] example).

**Below is a snapshot of a WebGear Video Server in action on Chrome browser:**

<p align="center">
  <img src="docs/overrides/assets/gifs/webgear.gif" alt="WebGear in action!" width="80%" />
  <br>
  <sub><i>WebGear Video Server at <a href="http://localhost:8000/" title="default address">http://localhost:8000/</a> address.</i></sub>
</p>

**Code to generate the above result:**

```python
# import required libraries
import uvicorn
from vidgear.gears.asyncio import WebGear

# various performance tweaks
options = {
    "frame_size_reduction": 40,
    "frame_jpeg_quality": 80,
    "frame_jpeg_optimize": True,
    "frame_jpeg_progressive": False,
}

# initialize WebGear app
web = WebGear(source="foo.mp4", logging=True, **options)

# run this app on Uvicorn server at address http://localhost:8000/
uvicorn.run(web(), host="localhost", port=8000)

# close app safely
web.shutdown()
```

### WebGear API Guide:

[**>>> Usage Guide**][webgear-doc]


&nbsp;

&nbsp;


## WebGear_RTC

> *WebGear_RTC is similar to [WeGear API](#webgear) in many aspects but utilizes [WebRTC][webrtc] technology under the hood instead of Motion JPEG, which makes it suitable for building powerful video-streaming solutions for all modern browsers as well as native clients available on all major platforms.*

WebGear_RTC is implemented with the help of [**aiortc**][aiortc] library which is built on top of asynchronous I/O framework for Web Real-Time Communication (WebRTC) and Object Real-Time Communication (ORTC) and supports many features like SDP generation/parsing, Interactive Connectivity Establishment with half-trickle and mDNS support, DTLS key and certificate generation, DTLS handshake, etc.

WebGear_RTC can handle [multiple consumers][webgear_rtc-mc] seamlessly and provides native support for ICE _(Interactive Connectivity Establishment)_ protocol, STUN _(Session Traversal Utilities for NAT)_, and TURN _(Traversal Using Relays around NAT)_ servers that help us to easily establish direct media connection with the remote peers for uninterrupted data flow. It also allows us to define our custom Server as a source to manipulate frames easily before sending them across the network(see this [doc][webgear_rtc-cs] example).

WebGear_RTC API works in conjunction with [**Starlette**][starlette]'s ASGI application and provides easy access to its complete framework. WebGear_RTC can also flexibly interact with Starlette's ecosystem of shared middleware, mountable applications, [Response classes](https://www.starlette.io/responses/), [Routing tables](https://www.starlette.io/routing/), [Static Files](https://www.starlette.io/staticfiles/), [Templating engine(with Jinja2)](https://www.starlette.io/templates/), etc. 

Additionally, WebGear_RTC API also provides a special internal wrapper around [VideoGear](#videogear), which itself provides internal access to both [CamGear](#camgear) and [PiGear](#pigear) APIs.


**Below is a snapshot of a WebGear_RTC Media Server in action on Chrome browser:**

<p align="center">
  <img src="docs/overrides/assets/gifs/webgear_rtc.gif" alt="WebGear_RTC in action!" width="80%" />
  <br>
  <sub><i>WebGear_RTC Video Server at <a href="http://localhost:8000/" title="default address">http://localhost:8000/</a> address.</i></sub>
</p>

**Code to generate the above result:**

```python
# import required libraries
import uvicorn
from vidgear.gears.asyncio import WebGear_RTC

# various performance tweaks
options = {
    "frame_size_reduction": 30,
}

# initialize WebGear_RTC app
web = WebGear_RTC(source="foo.mp4", logging=True, **options)

# run this app on Uvicorn server at address http://localhost:8000/
uvicorn.run(web(), host="localhost", port=8000)

# close app safely
web.shutdown()
```

### WebGear_RTC API Guide:

[**>>> Usage Guide**][webgear-doc]


&nbsp;

&nbsp;

## NetGear_Async 

<p align="center">
  <img src="docs/overrides/assets/images/zmq_asyncio.png" alt="WebGear in action!" width="70%"/>
</p>
.

> _NetGear_Async can generate the same performance as [NetGear API](#netgear) at about one-third the memory consumption, and also provide complete server-client handling with various options to use variable protocols/patterns similar to NetGear, but it doesn't support any of [NetGear's Exclusive Modes][netgear-exm] yet._

NetGear_Async is built on [`zmq.asyncio`][asyncio-zmq], and powered by a high-performance asyncio event loop called [**`uvloop`**][uvloop] to achieve unmatchable high-speed and lag-free video streaming over the network with minimal resource constraints. NetGear_Async can transfer thousands of frames in just a few seconds without causing any significant load on your system. 

NetGear_Async provides complete server-client handling and options to use variable protocols/patterns similar to [NetGear API](#netgear) but doesn't support any [NetGear Exclusive modes][netgear-exm] yet. Furthermore, NetGear_Async allows us to define our custom Server as source to manipulate frames easily before sending them across the network(see this [doc][netgear_Async-cs] example).

NetGear_Async as of now supports [all four ZeroMQ messaging patterns](#attributes-and-parameters-wrench):
* [**`zmq.PAIR`**][zmq-pair] _(ZMQ Pair Pattern)_ 
* [**`zmq.REQ/zmq.REP`**][zmq-req-rep] _(ZMQ Request/Reply Pattern)_
* [**`zmq.PUB/zmq.SUB`**][zmq-pub-sub] _(ZMQ Publish/Subscribe Pattern)_ 
* [**`zmq.PUSH/zmq.PULL`**][zmq-pull-push] _(ZMQ Push/Pull Pattern)_

Whereas supported protocol are: `tcp` and `ipc`.

### NetGear_Async API Guide:

[**>>> Usage Guide**][netgear_async-doc]


&nbsp;

&nbsp;

# Contributions & Support

Contributions are welcome. We'd love to have your contributions to VidGear to fix bugs or to implement new features!  

Please see our **[Contribution Guidelines](contributing.md)** for more details.

### Support

<img src="docs/overrides/assets/images/help_us.png" alt="PiGear" width="50%" />

Donations help keep VidGear's Development alive. Giving a little means a lot, even the smallest contribution can make a huge difference.

[![ko-fi][kofi-badge]][kofi]

### Contributors

<a href="https://github.com/abhiTronix/vidgear/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=abhiTronix/vidgear" />
</a>


&nbsp;

&nbsp;


# Community Channel

If you've come up with some new idea, or looking for the fastest way troubleshoot your problems, then *join our [Gitter community channel ➶][gitter]*


&nbsp;

&nbsp;



# Citation

Here is a Bibtex entry you can use to cite this project in a publication:


```BibTeX
@misc{vidgear,
    author = {Abhishek Thakur},
    title = {vidgear},
    howpublished = {\url{https://github.com/abhiTronix/vidgear}},
    year = {2019-2021}
  }
```

&nbsp;

&nbsp;


# Copyright

**Copyright © abhiTronix 2019-2021**

This library is released under the **[Apache 2.0 License][license]**.




<!--
Badges
-->

[appveyor]:https://img.shields.io/appveyor/ci/abhitronix/vidgear.svg?style=for-the-badge&logo=appveyor
[codecov]:https://img.shields.io/codecov/c/github/abhiTronix/vidgear/testing?style=for-the-badge&logo=codecov
[github-cli]:https://img.shields.io/github/workflow/status/abhiTronix/vidgear/Run%20Linux%20CI-Tests%20for%20vidgear?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTAgMWE5IDkgMCAwMTkgOSA5IDkgMCAwMS05IDkgOSA5IDAgMDEtOS05IDkgOSAwIDAxOS05ek0yMyAxOWE2IDYgMCAxMTAgMTIgNiA2IDAgMDEwLTEyek0yMyAzNWE2IDYgMCAxMTAgMTIgNiA2IDAgMDEwLTEyeiIgc3Ryb2tlPSJ2YXIoLS1jb2xvci1tYXJrZXRpbmctaWNvbi1wcmltYXJ5LCAjMjA4OEZGKSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00MSAzNWE2IDYgMCAxMTAgMTIgNiA2IDAgMDEwLTEyeiIgc3Ryb2tlPSJ2YXIoLS1jb2xvci1tYXJrZXRpbmctaWNvbi1zZWNvbmRhcnksICM3OUI4RkYpIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjxwYXRoIGQ9Ik0yNS4wMzcgMjMuNjA3bC0zLjA3IDMuMDY1LTEuNDktMS40ODUiIHN0cm9rZT0idmFyKC0tY29sb3ItbWFya2V0aW5nLWljb24tcHJpbWFyeSwgIzIwODhGRikiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNDEgMTlhNiA2IDAgMTEwIDEyIDYgNiAwIDAxMC0xMnoiIHN0cm9rZT0idmFyKC0tY29sb3ItbWFya2V0aW5nLWljb24tcHJpbWFyeSwgIzIwODhGRikiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+PHBhdGggZD0iTTQzLjAzNiAyMy42MDdsLTMuMDY5IDMuMDY1LTEuNDktMS40ODVNNyA2LjgxMmExIDEgMCAwMTEuNTMzLS44NDZsNS4xMTMgMy4yMmExIDEgMCAwMS0uMDA2IDEuNjk3bC01LjExMyAzLjE3QTEgMSAwIDAxNyAxMy4yMDNWNi44MTN6TTkgMTl2MTVjMCAzLjg2NiAzLjE3NyA3IDcgN2gxIiBzdHJva2U9InZhcigtLWNvbG9yLW1hcmtldGluZy1pY29uLXByaW1hcnksICMyMDg4RkYpIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPjxwYXRoIGQ9Ik0xNi45NDkgMjZhMSAxIDAgMTAwLTJ2MnpNOCAxOS4wMzVBNi45NjUgNi45NjUgMCAwMDE0Ljk2NSAyNnYtMkE0Ljk2NSA0Ljk2NSAwIDAxMTAgMTkuMDM1SDh6TTE0Ljk2NSAyNmgxLjk4NHYtMmgtMS45ODR2MnoiIGZpbGw9InZhcigtLWNvbG9yLW1hcmtldGluZy1pY29uLXByaW1hcnksICMyMDg4RkYpIi8+PHBhdGggZD0iTTI5LjA1NSAyNWg1Ljk0NCIgc3Ryb2tlPSJ2YXIoLS1jb2xvci1tYXJrZXRpbmctaWNvbi1wcmltYXJ5LCAjMjA4OEZGKSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIxIDQwYTEgMSAwIDExLS4wMDEgMi4wMDFBMSAxIDAgMDEyMSA0MHpNMjUgNDBhMSAxIDAgMTEtLjAwMSAyLjAwMUExIDEgMCAwMTI1IDQweiIgZmlsbD0idmFyKC0tY29sb3ItbWFya2V0aW5nLWljb24tc2Vjb25kYXJ5LCAjNzlCOEZGKSIvPjxwYXRoIGQ9Ik0zNC4wMDUgNDEuMDA3bC0xLjAxMy4wMzMiIHN0cm9rZT0idmFyKC0tY29sb3ItbWFya2V0aW5nLWljb24tc2Vjb25kYXJ5LCAjNzlCOEZGKSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiLz48L3N2Zz4=
[prs-badge]:https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABC0lEQVRYhdWVPQoCMRCFX6HY2ghaiZUXsLW0EDyBrbWtN/EUHsHTWFnYyCL4gxibVZZlZzKTnWz0QZpk5r0vIdkF/kBPAMOKeddE+CQPKoc5Yt5cTjBMdQSwDQToWgBJAn3jmhqgltapAV6E6b5U17MGGAUaUj07TficMfIBZDV6vxowBm1BP9WbSQE4o5h9IjPJmy73TEPDDxVmoZdQrQ5jRhly9Q8tgMUXkIIWn0oG4GYQfAXQzz1PGoCiQndM7b4RgJay/h7zBLT3hASgoKjamQJMreKf0gfuAGyYtXEIAKcL/Dss15iq6ohXghozLYiAMxPuACwtIT4yeQUxAaLrZwAoqGRKGk7qDSYTfYQ8LuYnAAAAAElFTkSuQmCC
[twitter-badge]:https://img.shields.io/badge/Tweet-Now-blue.svg?style=for-the-badge&logo=twitter
[azure-badge]:https://img.shields.io/azure-devops/build/abhiuna12/942b3b13-d745-49e9-8d7d-b3918ff43ac2/2/testing?logo=azure-pipelines&style=for-the-badge
[pypi-badge]:https://img.shields.io/pypi/v/vidgear.svg?style=for-the-badge&logo=pypi
[gitter-bagde]:https://img.shields.io/badge/Chat-Gitter-blueviolet.svg?style=for-the-badge&logo=gitter
[Coffee-badge]:https://abhitronix.github.io/img/vidgear/orange_img.png
[kofi-badge]:https://www.ko-fi.com/img/githubbutton_sm.svg
[black-badge]:https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge&logo=github


<!--
Internal URLs
-->

[release]:https://github.com/abhiTronix/vidgear/releases/latest
[pypi]:https://pypi.org/project/vidgear/
[gitter]:https://gitter.im/vidgear/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge
[twitter-intent]:https://twitter.com/intent/tweet?url=https%3A%2F%2Fabhitronix.github.io%2Fvidgear&via%20%40abhi_una12&text=Checkout%20VidGear%20-%20A%20High-Performance%20Video-Processing%20Python%20Framework.&hashtags=vidgear%20%23videoprocessing%20%23python%20%23threaded%20%23asyncio
[coffee]:https://www.buymeacoffee.com/2twOXFvlA
[kofi]: https://ko-fi.com/W7W8WTYO
[license]:https://github.com/abhiTronix/vidgear/blob/master/LICENSE
[github-flow]:https://github.com/abhiTronix/vidgear/actions?query=workflow%3A%22Run+Linux+CI-Tests+for+vidgear%22
[azure-pipeline]:https://dev.azure.com/abhiuna12/public/_build?definitionId=2
[app]:https://ci.appveyor.com/project/abhiTronix/vidgear
[code]:https://codecov.io/gh/abhiTronix/vidgear

[test-4k]:https://github.com/abhiTronix/vidgear/blob/e0843720202b0921d1c26e2ce5b11fadefbec892/vidgear/tests/benchmark_tests/test_benchmark_playback.py#L65
[bs_script_dataset]:https://github.com/abhiTronix/vidgear/blob/testing/scripts/bash/prepare_dataset.sh

[faq]:https://abhitronix.github.io/vidgear/latest/help/get_help/#frequently-asked-questions
[doc-vidgear-purpose]:https://abhitronix.github.io/vidgear/latest/help/motivation/#why-is-vidgear-a-thing
[live-stream]:https://abhitronix.github.io/vidgear/latest/gears/writegear/compression/usage/#using-compression-mode-for-streaming-urls
[live-audio-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/compression/usage/#using-compression-mode-with-live-audio-input
[piping-live-videos]:https://abhitronix.github.io/vidgear/latest/gears/camgear/usage/#using-camgear-with-streaming-websites
[ffmpeg-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/compression/advanced/ffmpeg_install/
[youtube-doc]:https://abhitronix.github.io/vidgear/latest/gears/camgear/usage/#using-camgear-with-youtube-videos
[TQM-doc]:https://abhitronix.github.io/vidgear/latest/bonus/TQM/#threaded-queue-mode
[camgear-doc]:https://abhitronix.github.io/vidgear/latest/gears/camgear/overview/
[stablizer-doc]:https://abhitronix.github.io/vidgear/latest/gears/stabilizer/overview/
[stablizer-doc-ex]:https://abhitronix.github.io/vidgear/latest/gears/videogear/usage/#using-videogear-with-video-stabilizer-backend
[videogear-doc]:https://abhitronix.github.io/vidgear/latest/gears/videogear/overview/
[pigear-doc]:https://abhitronix.github.io/vidgear/latest/gears/pigear/overview/
[cm-writegear-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/compression/overview/
[ncm-writegear-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/non_compression/overview/
[screengear-doc]:https://abhitronix.github.io/vidgear/latest/gears/screengear/overview/
[streamgear-doc]:https://abhitronix.github.io/vidgear/latest/gears/streamgear/overview/
[writegear-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/introduction/
[netgear-doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/overview/
[webgear-doc]:https://abhitronix.github.io/vidgear/latest/gears/webgear/overview/
[netgear_async-doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear_async/overview/
[drop35]:https://github.com/abhiTronix/vidgear/issues/99
[custom-command-doc]:https://abhitronix.github.io/vidgear/latest/gears/writegear/compression/advanced/cciw/
[advanced-webgear-doc]:https://abhitronix.github.io/vidgear/latest/gears/webgear/advanced/
[netgear_bidata_doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/advanced/bidirectional_mode/
[netgear_compression_doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/advanced/compression/
[netgear_security_doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/advanced/secure_mode/
[netgear_multi_server_doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/advanced/multi_server/
[netgear_multi_client_doc]:https://abhitronix.github.io/vidgear/latest/gears/netgear/advanced/multi_client/
[netgear-exm]: https://abhitronix.github.io/vidgear/latest/gears/netgear/overview/#modes-of-operation
[stabilize_webgear_doc]:https://abhitronix.github.io/vidgear/latest/gears/webgear/advanced/#using-webgear-with-real-time-video-stabilization-enabled
[netgear_Async-cs]: https://abhitronix.github.io/vidgear/latest/gears/netgear_async/usage/#using-netgear_async-with-a-custom-sourceopencv
[installation]:https://abhitronix.github.io/vidgear/latest/installation/
[gears]:https://abhitronix.github.io/vidgear/latest/gears
[switch_from_cv]:https://abhitronix.github.io/vidgear/latest/switch_from_cv/
[ss-mode-doc]: https://abhitronix.github.io/vidgear/latest/gears/streamgear/usage/#a-single-source-mode
[rtf-mode-doc]: https://abhitronix.github.io/vidgear/latest/gears/streamgear/usage/#b-real-time-frames-mode
[webgear-cs]: https://abhitronix.github.io/vidgear/latest/gears/webgear/advanced/#using-webgear-with-a-custom-sourceopencv
[webgear_rtc-cs]: https://abhitronix.github.io/vidgear/latest/gears/webgear_rtc/advanced/#using-webgear_rtc-with-a-custom-sourceopencv
[webgear_rtc-mc]: https://abhitronix.github.io/vidgear/latest/gears/webgear_rtc/advanced/#using-webgear_rtc-as-real-time-broadcaster
[docs]: https://abhitronix.github.io/vidgear

<!--
External URLs
-->
[asyncio-zmq]:https://pyzmq.readthedocs.io/en/latest/api/zmq.asyncio.html
[uvloop]: https://github.com/MagicStack/uvloop
[streamlink]:https://streamlink.github.io/
[aiortc]:https://aiortc.readthedocs.io/en/latest/
[youtube-dl]:https://youtube-dl.org/
[pyscreenshot]:https://github.com/ponty/pyscreenshot
[uvloop-ns]: https://github.com/MagicStack/uvloop/issues/14
[ffmpeg]:https://www.ffmpeg.org/
[flake8]: https://flake8.pycqa.org/en/latest/
[black]: https://github.com/psf/black
[pytest]:https://docs.pytest.org/en/latest/
[opencv-writer]:https://docs.opencv.org/master/dd/d9e/classcv_1_1VideoWriter.html#ad59c61d8881ba2b2da22cff5487465b5
[OpenCV-windows]:https://www.learnopencv.com/install-opencv3-on-windows/
[OpenCV-linux]:https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/
[OpenCV-pi]:https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
[starlette]:https://www.starlette.io/
[uvicorn]:http://www.uvicorn.org/
[daphne]:https://github.com/django/daphne/
[hypercorn]:https://pgjones.gitlab.io/hypercorn/
[prs]:http://makeapullrequest.com
[opencv]:https://github.com/opencv/opencv
[picamera]:https://github.com/waveform80/picamera
[pafy]:https://github.com/mps-youtube/pafy
[pyzmq]:https://github.com/zeromq/pyzmq
[zmq]:https://zeromq.org/
[mss]:https://github.com/BoboTiG/python-mss
[pip]:https://pip.pypa.io/en/stable/installing/
[opencv-vc]:https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html#a57c0e81e83e60f36c83027dc2a188e80
[OV5647-picam]:https://github.com/techyian/MMALSharp/doc/OmniVision-OV5647-Camera-Module
[IMX219-picam]:https://github.com/techyian/MMALSharp/doc/Sony-IMX219-Camera-Module
[opencv-vw]:https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
[yt-dl]:https://github.com/ytdl-org/youtube-dl/
[numpy]:https://github.com/numpy/numpy
[zmq-pair]:https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pair.html
[zmq-req-rep]:https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/client_server.html
[zmq-pub-sub]:https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html
[zmq-pull-push]: https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pushpull.html#push-pull
[picamera-setting]:https://picamera.readthedocs.io/en/release-1.13/quickstart.html
[webrtc]:https://webrtc.org/