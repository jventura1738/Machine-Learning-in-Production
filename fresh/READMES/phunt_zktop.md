h1. ZooKeeper top

*Author: "Patrick Hunt":http://people.apache.org/~phunt/* (follow me on "twitter":http://twitter.com/phunt)

h2. Summary

"This project":http://github.com/phunt/zktop provides a unix "top" like utility for ZooKeeper. It is compatible with Python2.6, Python2.7 and Python3.

h3. Example

Prereq:

Ensure zoo.cg on all nodes whitelists the minimum "four letter words":https://zookeeper.apache.org/doc/r3.3.3/zookeeperAdmin.html#sc_zkCommands for zktop to work:

<pre>
4lw.commands.whitelist=stat,srst
</pre>

Running:

<pre>
./zktop.py --servers "localhost:2181,localhost:2182,localhost:2183"
</pre>

or - omitting the port numbers, defaulting to 2181 -

<pre>
./zktop.py --servers "server1,server2,server3"
</pre>

or, for a ZK-style configuration file:

<pre>
./zktop.py --config zk.conf
</pre>

shows a screen like:

<pre>
Ensemble -- nodecount:10 zxid:0x1300000001 sessions:4

SERVER           PORT M      OUTST    RECVD     SENT CONNS MINLAT AVGLAT MAXLAT
localhost        2181 F          0       93       92     2      2      7     13
localhost        2182 F          0       37       36     1      0      0      0
localhost        2183 L          0       36       35     1      0      0      0

CLIENT           PORT I   QUEUE RECVD  SENT
127.0.0.1       34705 1       0    56    56
127.0.0.1       35943 1       0     1     0
127.0.0.1       33999 1       0     1     0
127.0.0.1       37988 1       0     1     0
</pre>

h3. What's Apache ZooKeeper?

From the "official site":http://hadoop.apache.org/zookeeper/: "ZooKeeper is a high-performance coordination service for distributed applications."

It exposes common services - such as naming, configuration management, synchronization, and group services - in a simple interface so you don't have to write them from scratch. You can use it off-the-shelf to implement consensus, group management, leader election, and presence protocols.

h2. zktop.py

0) Top line is overall cluster status
1-n) Lines 1-n are for the n servers
n+1 and below are for client connections

h3. Usage

<pre>
Usage: zktop.py [options]

Options:
  -h, --help            show this help message and exit
  --servers=SERVERS     comma separated list of host:port (default
                        localhost:2181)
  -n, --names           resolve session name from ip (default False)
  --fix_330             workaround for a bug in ZK 3.3.0
  -v VERBOSITY, --verbosity=VERBOSITY
                        log level verbosity (DEBUG, INFO, WARN(ING), ERROR, CRITICAL/FATAL))
  -l LOGFILE, --logfile=LOGFILE
                        directory in which to place log file, or empty for
                        none
  -c CONFIGFILE, --config=CONFIGFILE
                        zookeeper configuration file to lookup servers from
</pre>

--fix_330 works around a bug in ZooKeeper 3.3.0, it is only necessary if running the server against that version of ZooKeeper.

The screen refreshes every 3 seconds.
* 'h' help
* 'q' quits
* 'r' resets the server stats
* spacebar updates immediately

h2. PyPi

zktop is now installable from PyPi

<pre>
pip install zktop
</pre>

h2. License

This project is licensed under the Apache License Version 2.0
