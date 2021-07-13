//////////////////////////////////////////

  Licensed to the Apache Software Foundation (ASF) under one
  or more contributor license agreements.  See the NOTICE file
  distributed with this work for additional information
  regarding copyright ownership.  The ASF licenses this file
  to you under the Apache License, Version 2.0 (the
  "License"); you may not use this file except in compliance
  with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing,
  software distributed under the License is distributed on an
  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
  KIND, either express or implied.  See the License for the
  specific language governing permissions and limitations
  under the License.

//////////////////////////////////////////

= Apache Groovy
The Groovy development team
:revdate: 24-02-2014
:build-icon: https://ci.groovy-lang.org/app/rest/builds/buildType:(id:MasterTestJdk11)/statusIcon
:travis-build-icon: https://travis-ci.com/apache/groovy.svg?branch=master
:sonarcloud-icon: https://sonarcloud.io/api/project_badges/measure?project=apache_groovy&metric=sqale_rating
:noheader:
:groovy-www: https://groovy-lang.org/
:groovy-ci: https://ci.groovy-lang.org?guest=1
:travis-ci: https://travis-ci.com/apache/groovy
:sonarcloud: https://sonarcloud.io/dashboard?id=apache_groovy
:jdk: https://www.oracle.com/technetwork/java/javase/downloads
//:bintray-latest-version-image: https://api.bintray.com/packages/groovy/maven/groovy/images/download.png
//:bintray-latest-version-link: https://bintray.com/groovy/maven/groovy/_latestVersion
:apache-license-icon: https://img.shields.io/badge/license-APL2-blue.svg
:apache-license-link: https://www.apache.org/licenses/LICENSE-2.0.txt
:apache-groovy-twitter-icon: https://img.shields.io/twitter/follow/ApacheGroovy.svg?style=social
:apache-groovy-twitter-link: https://twitter.com/intent/follow?screen_name=ApacheGroovy
:jdk-icon: https://img.shields.io/badge/java-8+-4c7e9f.svg
//:bintray-download-icon: https://api.bintray.com/packages/groovy/maven/groovy/images/download.svg
:opencollective-link: https://opencollective.com/friends-of-groovy
:sponsors-silver-img: https://opencollective.com/friends-of-groovy/tiers/silver-sponsor.svg?avatarHeight=45&width=890
:sponsors-bronze-img: https://opencollective.com/friends-of-groovy/tiers/bronze-sponsor.svg?avatarHeight=40&width=890
:backers-monthly-img: https://opencollective.com/friends-of-groovy/tiers/backer.svg?avatarHeight=36&width=890
:backers-all-img: https://opencollective.com/friends-of-groovy/backers.svg?avatarHeight=32&width=890

[.left.text-left]
image::https://raw.githubusercontent.com/groovy/artwork/master/medium.png[]
image:{jdk-icon}[jdk, link={jdk}]
image:{apache-license-icon}[Apache License 2, link={apache-license-link}]
image:{build-icon}[teamcity build status, link={groovy-ci}]
image:{travis-build-icon}[travis build status, link={travis-ci}]
image:{sonarcloud-icon}[maintainability rating, link={sonarcloud}]
//image:{bintray-download-icon}[bintray download, link={bintray-latest-version-link}]
image:{apache-groovy-twitter-icon}[follow on Twitter, link={apache-groovy-twitter-link}]

{groovy-www}[Groovy] is a powerful multi-faceted programming language for the JVM platform.
It supports a spectrum of programming styles incorporating features from dynamic languages such as optional and duck typing, but also
static compilation and static type checking at levels similar to or greater than Java through its extensible static type checker.
It aims to greatly increase developer productivity with many powerful features but also a concise, familiar and easy to learn syntax.

It integrates smoothly with any Java class or library, and immediately delivers to your application powerful capabilities,
including scripting support, Domain-Specific Language authoring, runtime and compile-time meta-programming and functional programming. 

== Downloading

Distribution links are on the https://groovy.apache.org/download.html[download] page.

Maven, Gradle and Ivy dependency declaration snippets are available on specific files of a particular module.

== Obtaining the Source

You don't need the source code to use Apache Groovy but if you wish to explore its inner workings or build it for yourself
there are two ways to obtain the source files.

=== Checking out from Version Control

Apache Groovy uses Git. The official Git repository is at:

    https://gitbox.apache.org/repos/asf/groovy.git

And a mirror is hosted on Github:

    https://github.com/apache/groovy

The Github mirror is read-only and provides convenience to users and developers to explore the code and for the
community to accept contributions via Github Pull Requests.

Simply `git clone` the repo (or the repo you forked via the github website) and you will have the complete source.

=== Unpacking the src distribution

Alternatively, you can download the source distribution and unpack it.

If obtaining the source from the source distribution and you intend to build from source,
you also need to https://gradle.org/downloads/[download] and install https://gradle.org/[Gradle] and
use it to execute one bootstrap step.

==== Bootstrapping Gradle

As mentioned in the previous paragraph, if you download the source distribution
you need to bootstrap Gradle. This isn't needed if you clone from the Github repo.

Each version of Groovy is built and tested using a specific version of Gradle.
That version is specified by the `gradle_version` property defined in the `gradle.properties`
file within the root directory. Luckily you shouldn't need to know that version and,
after bootstrapping, you should use the `gradlew` command which will ensure the
correct version is always used.

The version of Gradle used for the bootstrap step has some flexibility though in general
you might need to download a version similar to the version of Groovy the build is
expecting.

To bootstrap Gradle, at the top directory of your unpacked source, run the command:

    gradle -p bootstrap

On Unix-like systems, use `./gradle`.

[NOTE]
At this point, the Gradle wrapper should be set up and from now on you should use
the `gradlew` command instead of `gradle`. (On Unix-like systems, use `./gradlew`).

== Building from Source

// Build is image:{build-icon}[build status, link={groovy-ci}].

To build you will need:

* {jdk}[JDK 10+]

To build everything using Gradle, use the following command (`./gradlew` on Unix-like systems):

    gradlew clean dist

[NOTE]
The gradlew command automatically downloads the correct Gradle version if needed, you do not need to download it first.

This will generate a distribution similar to the zip you can download on the Groovy download page.

To build everything and launch unit tests, use:

    gradlew test

If you want to launch one unit test, use this. <TestClassName> is like `groovy.GroovyMethodsTest`.

    gradlew :test --tests <TestClassName>

To build from IntelliJ IDEA:

    gradlew jar idea

Then open the generated project in IDEA.

To build from Eclipse:

    gradlew jar eclipse

Then open the generated project and the generated subprojects in Eclipse. But be aware that Eclipse tends to be more limited in its ability to reproduce a Gradle build structure. The generated project files may contain a circular dependency which may or may not prevent Eclipse from using them. It depends on the Eclipse version, if this is an issue or not.

To build the documentation (Groovy Language Documentation):

    gradlew asciidoc

All code samples of the documentation guide are pulled from actual test cases. To run a single documentation test case, take for example `src/spec/test/semantics/PowerAssertTest.groovy`

    gradlew testSinglePowerAssertTest

[NOTE]
The omission of package name: class is `semantics.PowerAssertTest` but only `PowerAssertTest` is added to `testSingle`.

== Verifying dependencies
To generate the missing verification metadata when add/bump dependencies:

    gradlew --write-verification-metadata pgp,sha512 --dry-run

then compare `verification-metadata.xml` with the generated `verification-metadata.dryrun.xml`, and merge the missing verification metadata into `verification-metadata.xml`
after the result of the above operation is reviewed.

== Continuous Integration Server

The official CI server runs {groovy-ci}[here] and is sponsored by https://www.jetbrains.com[JetBrains].

== Java Profiler

Groovy core team tunes performance through YourKit Java Profiler, which is sponsored by https://www.yourkit.com[YourKit].

== Friends of Groovy Open Collective
As an independent initiative, we have set up an open collective for Groovy:

https://opencollective.com/friends-of-groovy

This initiative is designed to complement the Apache project and the many contributions we get from our great community and supporters.

* Thank you to our Silver Sponsors:

image:{sponsors-silver-img}[]

* Thank you to our Bronze Sponsors:

image:{sponsors-bronze-img}[]

* Thank you to our backers (donating monthly):

image:{backers-monthly-img}[]

* Thank you to all our backers:

image:{backers-all-img}[]

== Stargazers over time

image::https://starcharts.herokuapp.com/apache/groovy.svg[Stargazers over time, link=https://starcharts.herokuapp.com/apache/groovy]

== License

Groovy is licensed under the terms of the http://www.apache.org/licenses/LICENSE-2.0.html[Apache License, Version 2.0]

