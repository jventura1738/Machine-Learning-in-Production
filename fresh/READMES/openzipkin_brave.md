[![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/openzipkin/zipkin)
[![Build Status](https://github.com/openzipkin/brave/workflows/test/badge.svg)](https://github.com/openzipkin/zipkin/actions?query=workflow%3Atest)
[![Maven Central](https://img.shields.io/maven-central/v/io.zipkin.brave/brave.svg)](https://search.maven.org/search?q=g:io.zipkin.brave%20AND%20a:brave)

# Brave

Brave is a distributed tracing instrumentation library. Brave typically intercepts production requests to gather timing data,
correlate and propagate trace contexts. While typically trace data is sent to [Zipkin server](https://github.com/openzipkin/zipkin/tree/master/zipkin-server), third-party plugins are available to send to alternate services such as [Amazon X-Ray](https://github.com/openzipkin/zipkin-aws/tree/master/storage/xray-udp).

This repository includes dependency-free Java libraries and instrumentation for common components used in production services. For example, this includes trace filters for Servlet and log correlation for Apache Log4J.

You can look at our [example project](https://github.com/openzipkin/brave-webmvc-example) for how to trace a simple web application.

## What's included

Brave's dependency-free [tracer library](brave/) works against JRE6+.
This is the underlying api that instrumentation use to time operations
and add tags that describe them. This library also includes code that
parses `X-B3-TraceId` headers.

Most users won't write tracing code directly. Rather, they reuse instrumentation
others have written. Check our [instrumentation](instrumentation/) and [Zipkin's list](https://zipkin.io/pages/tracers_instrumentation.html)
before rolling your own. Common tracing libraries like JDBC, Servlet
and Spring already exist. Instrumentation written here are tested and
benchmarked.

If you are trying to trace legacy applications, you may be interested in
[Spring XML Configuration](spring-beans/). This allows you to setup
tracing without any custom code.

You may want to put trace IDs into your log files, or change thread local
behavior. Look at our [context libraries](context/), for integration with
tools such as SLF4J.

## Version Compatibility policy
All Brave libraries match the minimum Java version of what's being
traced or integrated with, and adds no 3rd party dependencies. The goal
is to neither impact your projects' choices, nor subject your project
to dependency decisions made by others.

For example, even including a basic reporting library,
[zipkin-sender-urlconnection](https://github.com/openzipkin/zipkin-reporter-java), Brave transitively includes no json,
logging, protobuf or thrift dependency. This means zero concern if your
application chooses a specific version of SLF4J, Gson or Guava.
Moreover, the entire dependency tree including basic reporting in json,
thrift or protobuf is less than 512KiB of jars.

There is a floor Java version of 1.6, which allows older JREs and older
Android runtimes, yet may limit some applications. For example, Servlet
2.5 works with Java 1.5, but due to Brave being 1.6, you will not be
able to trace Servlet 2.5 applications until you use at least JRE 1.6.

All integrations set their associated library to "provided" scope. This
ensures Brave doesn't interfere with the versions you choose.

Some libraries update often which leads to api drift. In some cases, we
test versions ranges to reduce the impact of this. For example, we test
[gRPC](instrumentation/grpc) and [Kafka](instrumentation/kafka-clients) against multiple library versions.

## Artifacts
All artifacts publish to the group ID "io.zipkin.brave". We use a common
release version for all components.

### Library Releases
Snapshots are uploaded to [Sonatype](https://oss.sonatype.org/content/repositories/releases) which
synchronizes with [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22io.zipkin.brave%22)

### Library Snapshots
Snapshots are uploaded to [Sonatype](https://oss.sonatype.org/content/repositories/snapshots) after
commits to master.

### Version alignments
When using multiple brave components, you'll want to align versions in
one place. This allows you to more safely upgrade, with less worry about
conflicts.

You can use our Maven instrumentation BOM (Bill of Materials) for this:

Ex. in your dependencies section, import the BOM like this:
```xml
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>io.zipkin.brave</groupId>
        <artifactId>brave-bom</artifactId>
        <version>${brave.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>
```

Now, you can leave off the version when choosing any supported
instrumentation. Also any indirect use will have versions aligned:
```xml
<dependency>
  <groupId>io.zipkin.brave</groupId>
  <artifactId>brave-instrumentation-okhttp3</artifactId>
</dependency>
```

With the above in place, you can use the property `brave.version` to override dependency
versions coherently. This is most commonly to test a new feature or fix.

Note: If you override a version, always double check that your version
is valid (equal to or later) than what you are updating. This will avoid
class conflicts.
