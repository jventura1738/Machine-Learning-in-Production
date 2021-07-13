Aeron
=====

[![GitHub](https://img.shields.io/github/license/real-logic/Aeron.svg)](https://github.com/real-logic/aeron/blob/master/LICENSE)
[![Javadocs](https://www.javadoc.io/badge/io.aeron/aeron-all.svg)](https://www.javadoc.io/doc/io.aeron/aeron-all)

[![Actions Status](https://github.com/real-logic/aeron/workflows/Continuous%20Integration/badge.svg)](https://github.com/real-logic/aeron/actions)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/real-logic/aeron.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/real-logic/aeron/alerts)
[![Code Quality: Java](https://img.shields.io/lgtm/grade/java/g/real-logic/aeron.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/real-logic/aeron/context:java)
[![Code Quality: C/C++](https://img.shields.io/lgtm/grade/cpp/g/real-logic/aeron.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/real-logic/aeron/context:cpp)

Efficient reliable UDP unicast, UDP multicast, and IPC message transport. Java and C++ clients are available in this
repository, and a [.NET client](https://github.com/AdaptiveConsulting/Aeron.NET) is available from a 3rd party. All
three clients can exchange messages across machines, or on the same machine via IPC, very efficiently. Message streams
can be recorded by the [Archive](https://github.com/real-logic/aeron/tree/master/aeron-archive) module to persistent
storage for later, or real-time, replay. Aeron [Cluster](https://github.com/real-logic/aeron/tree/master/aeron-cluster)
provides support for fault-tolerant services as replicated state machines based on the
[Raft](https://raft.github.io/) consensus algorithm.

Performance is the key focus. A design goal for Aeron is to be the highest throughput with the lowest and most
predictable latency of any messaging system. Aeron integrates with
[Simple Binary Encoding (SBE)](https://github.com/real-logic/simple-binary-encoding) for the best possible message
encoding and decoding performance. Many of the data structures used in the creation of Aeron have been factored out to
the [Agrona](https://github.com/real-logic/agrona) project.

For details of usage, protocol specification, FAQ, etc. please check out the
[Wiki](https://github.com/real-logic/aeron/wiki).

For those who prefer to watch a video then try [Aeron Messaging](https://www.youtube.com/watch?v=tM4YskS94b0) from
StrangeLoop 2014. Things have advanced quite a bit with performance and features, but the basic design still applies.

For the latest version information and changes see the [Change Log](https://github.com/real-logic/aeron/wiki/Change-Log)
with Java **downloads** at [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Caeron).

Commercial support, training, and development on Aeron is available from
[sales@real-logic.co.uk](mailto:sales@real-logic.co.uk?subject=Aeron). Premium features such as Solarflare ef_vi
transport bindings for a further 20-60% reduction in latency depending on usage and configuration, and security with
ATS (Aeron Transport Security) for encrypted communications is available to customers on commercial support.

### How do I use Aeron?

1. [Java Programming Guide](https://github.com/real-logic/aeron/wiki/Java-Programming-Guide)
1. [C++11 Programming Guide](https://github.com/real-logic/aeron/wiki/Cpp-Programming-Guide)
1. [Best Practices Guide](https://github.com/real-logic/aeron/wiki/Best-Practices-Guide)
1. [Monitoring and Debugging](https://github.com/real-logic/aeron/wiki/Monitoring-and-Debugging)
1. [Configuration Options](https://github.com/real-logic/aeron/wiki/Configuration-Options)
1. [Channel Specific Configuration](https://github.com/real-logic/aeron/wiki/Channel-Configuration)
1. [Aeron Archive (Durable/Persistent Stream Storage)](https://github.com/real-logic/aeron/wiki/Aeron-Archive)
1. [Aeron Cluster (Fault Tolerant Services)](https://github.com/real-logic/aeron/tree/master/aeron-cluster)
1. [Aeron Cookbook](https://aeroncookbook.com/) by Shaun Laurens.

### How does Aeron work?

1. [Transport Protocol Specification](https://github.com/real-logic/aeron/wiki/Transport-Protocol-Specification)
1. [Design Overview](https://github.com/real-logic/aeron/wiki/Design-Overview)
1. [Design Principles](https://github.com/real-logic/aeron/wiki/Design-Principles)
1. [Flow Control Semantics](https://github.com/real-logic/aeron/wiki/Flow-and-Congestion-Control)
1. [Media Driver Operation](https://github.com/real-logic/aeron/wiki/Media-Driver-Operation)

### How do I hack on Aeron?

1. [Hacking on Aeron](https://github.com/real-logic/aeron/wiki/Hacking-on-Aeron)
1. [Performance Testing](https://github.com/real-logic/aeron/wiki/Performance-Testing)

Build
-----

### Java Build

Build the project with [Gradle](http://gradle.org/) using this
[build.gradle](https://github.com/real-logic/aeron/blob/master/build.gradle) file.

You will require the Java 8+ to build Aeron:

* [JDK 8](https://adoptopenjdk.net/index.html) or later, Java versions before 1.8.0_65 are very buggy and can cause
tests to fail.

Full clean and build of all modules

```shell
    $ ./gradlew
```
    
### C++ Build

You require the following to build the C++ API for Aeron:

* 3.6.1 or higher of [CMake](http://www.cmake.org/)
* C++11 supported compiler for the supported platform
* C11 supported compiler for the supported platform
* Requirements to build [HdrHistogram_c](https://github.com/HdrHistogram/HdrHistogram_c). 
* JDK 8 or later to compile the SBE schema definitions used by the archive client.

__Note__: Aeron support is available for 64-bit Linux, OSX, and Windows. 

For convenience, the `cppbuild` script does a full clean, build, and test of all targets as a Release build.

```shell
    $ ./cppbuild/cppbuild
```

For those comfortable with CMake - then a clean, build, and test looks like:

```shell
    $ mkdir -p cppbuild/Debug
    $ cd cppbuild/Debug
    $ cmake ../..
    $ cmake --build . --clean-first
    $ ctest
```

#### C Media Driver

By default, the C Media Driver is built as part of the C++ Build. However, it can be disabled via the CMake
option `BUILD_AERON_DRIVER` being set to `OFF`.

__Note__: C Media Driver is supported on Mac and Linux, the Windows version is experimental.

For dependencies and other information, see the
[README](https://github.com/real-logic/aeron/blob/master/aeron-driver/src/main/c/README.md).

#### Documentation

If you have doxygen installed and want to build the Doxygen doc, there is a nice `doc` target that can be used.

```shell
    $ make doc
```
    
#### Packaging

If you would like a packaged version of the compiled API, there is the `package` target that uses CPack. If the doc
has been built previous to the packaging, it will be included. Packages created are "TGZ;STGZ", but can be changed
by running `cpack` directly.

```shell
    $ make package
```

Running Samples
---------------

Start up a media driver which will create the data and conductor directories. On Linux, this will probably be in
`/dev/shm/aeron` or `/tmp/aeron`.

```shell
    $ java -cp aeron-all/build/libs/aeron-all-${VERSION}.jar io.aeron.driver.MediaDriver
```

Alternatively, specify the data and conductor directories. The following example uses the shared memory 'directory' on
Linux, but you could just as easily point to the regular filesystem.

```shell
    $ java -cp aeron-all/build/libs/aeron-all-${VERSION}.jar -Daeron.dir=/dev/shm/aeron io.aeron.driver.MediaDriver
```

You can run the `BasicSubscriber` from a command line. On Linux, this will be pointing to the `/dev/shm` shared memory
directory, so be sure your `MediaDriver` is doing the same!

```shell
    $ java -cp aeron-all/build/libs/aeron-all-${VERSION}.jar io.aeron.samples.BasicSubscriber
```
    
You can run the `BasicPublisher` from a command line. On Linux, this will be pointing to the `/dev/shm` shared memory
directory, so be sure your `MediaDriver` is doing the same!

```shell
    $ java -cp aeron-all/build/libs/aeron-all-${VERSION}.jar io.aeron.samples.BasicPublisher
```

You can run the `AeronStat` utility to read system counters from a command line
    
```shell
    $ java -cp aeron-all/build/libs/aeron-all-${VERSION}.jar io.aeron.samples.AeronStat
```

For more samples and scripts to run them, see the [aeron-samples](https://github.com/real-logic/aeron/tree/master/aeron-samples) directory.

Media Driver Packaging
----------------------

The Media Driver is packaged by the default build into an application that can be found here

    aeron-driver/build/distributions/aeron-driver-${VERSION}.zip


Troubleshooting
---------------

1. On linux, the subscriber sample throws an exception
 
   ```
    java.lang.InternalError(a fault occurred in a recent unsafe memory access operation in compiled Java code)
   ```

   This is actually an out of disk space issue.
  
   To alleviate, check to make sure you have enough disk space.

   In the samples, on Linux, this will probably be either at `/dev/shm/aeron` or `/tmp/aeron` (depending on your settings).

   See this [thread](https://issues.apache.org/jira/browse/CASSANDRA-5737?focusedCommentId=14251018&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-14251018) for a similar problem.
  
   Note: if you are trying to run this inside a Linux Docker, be aware that, by default, [Docker only allocates 64 MB](https://github.com/docker/docker/issues/2606) to the [shared memory](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CB8QFjAA&url=http%3A%2F%2Fwww.cyberciti.biz%2Ftips%2Fwhat-is-devshm-and-its-practical-usage.html&ei=NBEPVcfzLZLWoASv8IKYCA&usg=AFQjCNHwBF2R9m4v_Z9pyNlunei2gH-ssA&sig2=VzzxpzRAGoHRjpH_MhRL8w&bvm=bv.88528373,d.cGU) space at `/dev/shm`. However, the samples will quickly outgrow this.
  
   You can work around this issue by using the `--shm-size` argument for `docker run` or `shm_size` in `docker-compose.yaml`.


License (See LICENSE file for full license)
-------------------------------------------
Copyright 2014-2021 Real Logic Limited.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.  
