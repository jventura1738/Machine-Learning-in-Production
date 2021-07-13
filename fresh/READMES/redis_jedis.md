[![Release](https://img.shields.io/github/release/redis/jedis.svg)](https://github.com/redis/jedis/releases/latest)
[![CircleCI](https://circleci.com/gh/redis/jedis/tree/master.svg?style=svg)](https://circleci.com/gh/redis/jedis/tree/master)
[![Maven Central](https://img.shields.io/maven-central/v/redis.clients/jedis.svg)](http://mvnrepository.com/artifact/redis.clients/jedis)
[![Javadocs](https://www.javadoc.io/badge/redis.clients/jedis.svg)](https://www.javadoc.io/doc/redis.clients/jedis)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)
[![Language grade: Java](https://img.shields.io/lgtm/grade/java/g/redis/jedis.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/redis/jedis/context:java)
[![codecov](https://codecov.io/gh/redis/jedis/branch/master/graph/badge.svg?token=pAstxAAjYo)](https://codecov.io/gh/redis/jedis)
[![Discord](https://img.shields.io/discord/697882427875393627?style=flat-square)](https://discord.gg/qRhBuY8Z)

# Jedis

Jedis is a blazingly small and sane [Redis](http://github.com/antirez/redis "Redis") java client.

Jedis was conceived to be EASY to use.

Jedis is fully compatible with redis 2.8.x, 3.x.x and above*.

## Community

Meet us on IRC: ##jedis on freenode.net

Join the mailing-list at [http://groups.google.com/group/jedis_redis](http://groups.google.com/group/jedis_redis)

## So what can I do with Jedis?
All of the following redis features are supported:

- Sorting
- Connection handling
- Commands operating on any kind of values
- Commands operating on string values
- Commands operating on hashes
- Commands operating on lists
- Commands operating on sets
- Commands operating on sorted sets
- Commands operating on streams
- Transactions
- Pipelining
- Publish/Subscribe
- Persistence control commands
- Remote server control commands
- Connection pooling
- Sharding (MD5, MurmurHash)
- Key-tags for sharding
- Sharding with pipelining
- Scripting with pipelining
- Redis Cluster

## How do I use it?

You can download the latest build at: 
    http://github.com/redis/jedis/releases

Or use it as a maven dependency:

### Official Releases

```xml
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>3.6.0</version>
</dependency>
```

### Snapshots

```xml
  <repositories>
    <repository>
      <id>snapshots-repo</id>
      <url>https://oss.sonatype.org/content/repositories/snapshots</url>
    </repository>
  </repositories>
```

and

```xml
  <dependencies>
    <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>3.7.0-SNAPSHOT</version>
    </dependency>
  </dependencies>
```

for upcoming major release

```xml
  <dependencies>
    <dependency>
      <groupId>redis.clients</groupId>
      <artifactId>jedis</artifactId>
      <version>4.0.0-SNAPSHOT</version>
    </dependency>
  </dependencies>
```


To use it just:
    
```java
Jedis jedis = new Jedis("localhost");
jedis.set("foo", "bar");
String value = jedis.get("foo");
```

For more usage examples check the tests.

Please check the [wiki](http://github.com/redis/jedis/wiki "wiki"). There are lots of cool things you should know, including information about connection pooling.

Latest release javadocs can be found here: https://www.javadoc.io/doc/redis.clients/jedis/latest/index.html

And you are done!

## Jedis Cluster

Redis cluster [specification](http://redis.io/topics/cluster-spec) is implemented

```java
Set<HostAndPort> jedisClusterNodes = new HashSet<HostAndPort>();
//Jedis Cluster will attempt to discover cluster nodes automatically
jedisClusterNodes.add(new HostAndPort("127.0.0.1", 7379));
JedisCluster jc = new JedisCluster(jedisClusterNodes);
jc.set("foo", "bar");
String value = jc.get("foo");
```

## FAQ

- Do you have strange stack traces?
- You're getting errors when running jedis in multi-threaded environments?
- Do you need further instructions about pipelining, transactions or sentinel?

Please check the [WIKI](https://github.com/redis/jedis/wiki) for more useful information.


## I want to contribute!

That is great!

Please see [CONTRIBUTING.md](https://github.com/redis/jedis/blob/master/.github/CONTRIBUTING.md) on project's root directory for follow up how to contribute to Jedis project.

Thanks for helping!

## Sponsorship

![RedisLabs Logo](logo-redislabs.png)

---

![YourKit Logo](https://cloud.githubusercontent.com/assets/1317309/4507430/7119527c-4b0c-11e4-9245-d72e751e26ee.png)

YourKit supports open source projects with its full-featured Java Profiler.
YourKit, LLC is the creator of [YourKit Java Profiler](http://www.yourkit.com/java/profiler/index.jsp) 
and [YourKit .NET Profiler](http://www.yourkit.com/.net/profiler/index.jsp),
innovative and intelligent tools for profiling Java and .NET applications.

## License

Copyright (c) 2011 Jonathan Leibiusky

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

