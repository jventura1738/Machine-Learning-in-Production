:documentation-url: https://docs.spring.io/spring-native/docs/current/reference/htmlsingle

image:https://ci.spring.io/api/v1/teams/spring-native/pipelines/spring-native/jobs/build-samples-stable-java11/badge["Build Status", link="https://ci.spring.io/teams/spring-native/pipelines/spring-native?group=builds"] image:https://img.shields.io/badge/documentation-blue.svg["Reference documentation", link="{documentation-url}"]

Spring Native provides beta support for compiling Spring applications to native executables using https://www.graalvm.org[GraalVM]
https://www.graalvm.org/reference-manual/native-image/[native-image] compiler, in order to provide a native deployment
option typically designed to be packaged in lightweight containers. In practice, the target is to support your Spring Boot application
, almost unmodified, on this new platform.

Watch the https://www.youtube.com/watch?v=96n_YpGx-JU[video] and read the https://spring.io/blog/2021/03/11/announcing-spring-native-beta[blog post] of Spring Native Beta announcement to learn more.
image:https://static.spring.io/blog/sdeleuze/20210311/announcing-spring-native-beta.png["Announcing Spring Native Beta!",align="center", width=640px, link="https://www.youtube.com/watch?v=96n_YpGx-JU"]

== Quick start

The easiest way to start with Spring Native is probably to go to https://start.spring.io/[start.spring.io], add the Spring Native dependency, and read the {documentation-url}[reference documentation]. Make sure to configure properly the https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/#spring-aot[Spring AOT Maven and Gradle plugins] that are mandatory to get proper native support for your Spring application.

=== Play with the samples

NOTE: You need to install the GraalVM `native-image` compiler, check {documentation-url}/#getting-started-native-image[the documentation] for more details.

- Download https://github.com/spring-projects-experimental/spring-native/tags[the latest release] of this repository.
- Go into the samples folder and pick one (e.g. `cd samples/commandlinerunner`)
- Run `./build.sh` which will run the regular JVM build, then a native image compilation, then test the result.

For more details on the samples see the {documentation-url}/index.html#samples[samples documentation].

== Contributing

If you have not previously done so, please sign the https://cla.pivotal.io/sign/spring[Contributor License Agreement]. You will be reminded automatically when you submit the pull request.

Contributions are welcome, especially for adding support via pull requests for libraries widely used in the Spring ecosystem not yet support. Please refer to the {documentation-url}#how-to-contribute[how to contribute] section for more details.

== License

https://www.apache.org/licenses/LICENSE-2.0[Apache License v2.0]
