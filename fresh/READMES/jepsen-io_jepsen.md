# Jepsen

Breaking distributed systems so you don't have to.

Jepsen is a Clojure library. A test is a Clojure program which uses the Jepsen
library to set up a distributed system, run a bunch of operations against that
system, and verify that the history of those operations makes sense. Jepsen has
been used to verify everything from eventually-consistent commutative databases
to linearizable coordination systems to distributed task schedulers. It can
also generate graphs of performance and availability, helping you characterize
how a system responds to different faults. See
[jepsen.io](https://jepsen.io/analyses) for examples of the sorts of analyses
you can carry out with Jepsen.

[![Build Status](https://travis-ci.com/jepsen-io/jepsen.svg?branch=master)](https://travis-ci.com/jepsen-io/jepsen)

## Design Overview

A Jepsen test runs as a Clojure program on a *control node*. That program uses
SSH to log into a bunch of *db nodes*, where it sets up the distributed system
you're going to test using the test's pluggable *os* and *db*.

Once the system is running, the control node spins up a set of logically
single-threaded *processes*, each with its own *client* for the distributed
system. A *generator* generates new operations for each process to perform.
Processes then apply those operations to the system using their clients. The
start and end of each operation is recorded in a *history*. While performing
operations, a special *nemesis* process introduces faults into the system--also
scheduled by the generator.

Finally, the DB and OS are torn down. Jepsen uses a *checker* to analyze the
test's history for correctness, and to generate reports, graphs, etc. The test,
history, analysis, and any supplementary results are written to the filesystem
under `store/<test-name>/<date>/` for later review. Symlinks to the latest
results are maintained at each level for convenience.

## Documentation

This [tutorial](doc/tutorial/index.md) walks you through writing a Jepsen test
from scratch.

For reference, see the [API documentation](http://jepsen-io.github.io/jepsen/).

## Setting up a Jepsen Environment

So, you've got a Jepsen test, and you'd like to run it! Or maybe you'd like to start learning how to write tests. You've got several options:

### AWS

If you have an AWS account, you can launch a full Jepsen cluster---control and
DB nodes---from the [AWS
Marketplace](https://aws.amazon.com/marketplace/pp/Jepsen-LLC-Jepsen/B01LZ7Y7U0).
Click "Continue to Subscribe", "Continue to Configuration", and choose
"CloudFormation Template". You can choose the number of nodes you'd like to
deploy, adjust the instance types and disk sizes, and so on. These are full
VMs, which means they can test clock skew.

The AWS marketplace clusters come with an hourly fee (generally $1/hr/node),
which helps fund Jepsen development.

### Docker

You can run a full Jepsen cluster on a single machine using Docker Compose. See the [Docker](/docker) directory for more details. Docker containers don't have real clocks, so you generally can't use them to test clock skew.

### LXC

You can set up your DB nodes as LXC containers, and use your local machine as
the control node. See the [LXC documentation](doc/lxc.md) for guidelines. This
might be the easiest setup for hacking on tests: you'll be able to edit source
code, run profilers, etc on the local node. Containers don't have real clocks, so you generally can't use them to test clock skew.

### VMs, Real Hardware, etc.

You should be able to run Jepsen against almost any machines which have:

- A TCP network
- An SSH server
- Sudo or root access

Each DB node should be accessible from the control node via SSH: you need to be
able to run `ssh myuser@some-node`, and get a shell. By default, DB nodes are
named n1, n2, n3, n4, and n5, but that (along with SSH username, password,
identity files, etc) is all definable in your test, or at the CLI. The account
you use on those boxes needs sudo access to set up DBs, control firewalls, etc.

BE ADVISED: tests may mess with clocks, add apt repos, run killall -9 on
processes, and generally break things, so you shouldn't, you know, point Jepsen
at your prod machines unless you like to live dangerously, or you wrote the
test and know exactly what it's doing.

NOTE: Most Jepsen tests are written with more specific requirements in
mind---like running on Debian, using `iptables` for network manipulation, etc.
See the specific test code for more details.

### Setting Up Control Nodes

For AWS and Docker installs, your control node comes preconfigured with all the
software you'll need to run most Jepsen tests. If you build your own control
node (or if you're using your local machine as a control node), you'll need a
few things:

- A [JVM](https://openjdk.java.net/install/)---version 1.8 or higher.
- JNA, so the JVM can talk to your SSH.
- [Leiningen](https://leiningen.org/): a Clojure build tool.
- [Gnuplot](http://www.gnuplot.info/): how Jepsen renders performance plots.
- [Graphviz](https://graphviz.org/): how Jepsen renders transactional anomalies.

On Debian, try:

```
sudo apt-get install openjdk-8-jre openjdk-8-jre-headless libjna-java gnuplot graphviz
```

... to get the basic requirements in place. Debian's Leiningen packages are
anchient, so download lein from the web instead.

## Running a Test

Once you've got everything set up, you should be able to run `cd aerospike;
lein test`, and it'll spit out something like

```clj
INFO  jepsen.core - Analysis invalid! (ﾉಥ益ಥ）ﾉ ┻━┻

{:valid? false,
 :counter
 {:valid? false,
  :reads
  [[190 193 194]
   [199 200 201]
   [253 255 256]
   ...}}
```

## FAQ

### JSCH auth errors

If you see `com.jcraft.jsch.JSchException: Auth fail`, this means something
about your test's `:ssh` map is wrong, or your control node's SSH environment
is a bit weird.

0. Confirm that you can ssh to the node that Jepsen failed to connect to. Try
   `ssh -v` for verbose information--pay special attention to whether it uses a
   password or private key.
1. If you intend to use a username and password, confirm that they're specified
   correctly in your test's `:ssh` map.
2. If you intend to log in with a private key, make sure your SSH agent is
   running.
   - `ssh-add -l` should show the key you use to log in.
   - If your agent isn't running, try launching one with `ssh-agent`.
   - If your agent shows no keys, you might need to add it with `ssh-add`.
   - If you're SSHing to a control node, SSH might be forwarding your local
     agent's keys rather than using those on the control node. Try `ssh -a` to
     disable agent forwarding.

If you've SSHed to a DB node already, you might also encounter a jsch bug which
doesn't know how to read hashed known_hosts files. Remove all keys for the DB
hosts from your `known_hosts` file, then:

```sh
ssh-keyscan -t rsa n1 >> ~/.ssh/known_hosts
ssh-keyscan -t rsa n2 >> ~/.ssh/known_hosts
ssh-keyscan -t rsa n3 >> ~/.ssh/known_hosts
ssh-keyscan -t rsa n4 >> ~/.ssh/known_hosts
ssh-keyscan -t rsa n5 >> ~/.ssh/known_hosts
```

to add unhashed versions of each node's hostkey to your `~/.ssh/known_hosts`.

### SSHJ auth errors

If you get an exception like `net.schmizz.sshj.transport.TransportException:
Could not verify 'ssh-ed25519' host key with fingerprint 'bf:4a:...' for 'n1'
on port 22`, but you're sure you've got the keys in your `~/.ssh/known-hosts`,
this is because (I think) SSHJ tries to verify only the ed25519 key and
*ignores* the RSA key. You can add the ed25519 keys explicitly via:

```sh
ssh-keyscan -t ed25519 n1 >> ~/.ssh/known_hosts
...
```

## Other Projects

Additional projects that may be of interest:

- [Jecci](https://github.com/michaelzenz/jecci): A wrapper framework around Jepsen
- [Porcupine](https://github.com/anishathalye/porcupine): a linearizability checker written in Go.
