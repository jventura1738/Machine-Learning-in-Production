![PolarDB Banner](https://github.com/alibaba/PolarDB-for-PostgreSQL/blob/master/polardb.png)

## What is PolarDB for PostgreSQL?

PolarDB for PostgreSQL (PolarDB for short) is an open-source database system based on PostgreSQL. It extends PostgreSQL to become a share-nothing distributed database, which supports **global data consistency** and **ACID across database nodes**, **distributed SQL processing**, and **data redundancy** and **high availability** through Paxos based replication. PolarDB is designed to add values and new features to PostgreSQL in dimensions of high performance, scalability, high availability, and elasticity. At the same time, PolarDB remains SQL compatibility to standalone PostgreSQL with the best effort.

PolarDB will evolve and offer its functions and features in two major parts: an extension and a patch to PostgreSQL. The extension part includes components implemented outside the PostgreSQL kernel, such as distributed transaction management, global or distributed time service, distributed SQL processing, additional metadata, internal functions, and tools to manage database clusters and conduct fault tolerance or recovery. Having most of its functions in a PostgreSQL extension, PolarDB targets **easy upgrading**, **easy migration**, and **fast adoption**. The patch part includes the changes necessary to the kernel, such as distributed MVCC for different isolation levels. We expect functions and codes in the patch part is limited. As a result, PolarDB can be easily upgraded with newer PostgreSQL versions and maintained full compatibility with PostgreSQL.

- [Quick start with PolarDB](#quick-start-with-polardb)
- [Architecture & Roadmap](#architecture--roadmap)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Licensing](#licensing)
- [Acknowledgements](#acknowledgements)
- [Communications](#communications)

## Quick start with PolarDB

Three approaches are offered to quickly try out PolarDB: Alibaba Cloud service, deployment using Docker images, and deployment from source codes.

### Alibaba Cloud Service
TBD

### Deployment Using Docker Image
This section describes how to create a PolarDB-for-Postgresql image, and how to use the image for a quick start.

* build a PolarDB-for-Postgresql image.

```bash
docker build -t polardb-for-postgresql -f ./docker/Dockerfile .
```

* run PolarDB-for-Postgresql image on port 10001.

```bash
docker run --name polardb -p 10001:10001 -d polardb-for-postgresql:latest
```

* access PolarDB-for-Postgresql with local psql.

```bash
psql -d postgres -U postgres -h localhost -p 10001
```

* if psql is not installed locally, you can login the container to use it.

```bash
docker exec -it polardb /bin/bash
```

### Previous Preparation

* download source code from https://github.com/alibaba/PolarDB-for-PostgreSQL

* install dependent packages (use Centos as an example)

```bash
sudo yum install bison flex libzstd-devel libzstd zstd cmake openssl-devel protobuf-devel readline-devel libxml2-devel libxslt-devel zlib-devel bzip2-devel lz4-devel snappy-devel python-devel
```
* set up authorized key for fast access

Call ssh-copy-id installs an authorized key. Its purpose is help pgxc_ctl to provision access without requiring a password for each login.

```bash
ssh-copy-id username@IP
```

* set up environment variables

```bash
vi ~/.bashrc
export PATH="$HOME/polardb/polardbhome/bin:$PATH"
export LD_LIBRARY_PATH="$HOME/polardb/polardbhome/lib:$LD_LIBRARY_PATH"
source ~/.bashrc
```

### Fast Deployment(One-Key for all)
This script uses default configuration to compile PolarDB, to deploy binary, and to start a cluster of three nodes, including a leader and two followers.
before call this script, please check "environment variables, dependent packages, authorized key" at "Previous Preparation" first.

* run onekey.sh script

```bash
./onekey.sh all
```

* check running processes (1 leader, 2 follower), their replica roles and status

```bash
ps -ef|grep polardb
psql -p 10001 -d postgres -c "select * from pg_stat_replication;"
psql -p 10001 -d postgres -c "select * from polar_dma_cluster_status;"
```


### Deployment from Source Code

We extend a tool named pgxc_ctl from PG-XC/PG-XL open-source project to support cluster management, such as configuration generation, configuration modification, cluster initialization, starting/stopping nodes, and switchover. Its detail usage can be found [deployment](/doc/polardb/deployment.md).

* build and install binary

You can just call build script to build. If you get errors, please reference [deployment](/doc/polardb/deployment.md) for detail reasons.

```bash
./build.sh
```

* generate default configure file

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf prepare standalone
```

* deploy binary file

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf deploy all
```

* clean residual installation and init cluster

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf clean all
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf init all
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf monitor all
```

* install dependent packages for cluster management

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf deploy cm
```

* start cluster or node

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf start all
```

* stop cluster or node

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf stop all
```

* failover datanode

datanode_1 is node name configured in polardb_paxos.conf.

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf failover datanode datanode_1
```

* cluster health check

 check cluster status and start failed node.

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf healthcheck all
```

* examples of other command

```bash
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf kill all
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf log var datanodeNames
pgxc_ctl -c $HOME/polardb/polardb_paxos.conf show configuration all
```

* check and test

```bash
ps -ef | grep postgres
psql -p 10001 -d postgres -c "create table t1(a int primary key, b int);"
createdb test -p 10001
psql -p 10001 -d test -c "select version();"
```

reference [deployment](/doc/polardb/deployment.md) for detail instructions.

Regress and other test details can be found [here](/doc/polardb/regress.md). Some benchmarking example is [here](/doc/polardb/benchmark.md).

## Architecture & Roadmap

PolarDB uses a share-nothing architecture. Each node stores data and also executes queries, and they coordinate with each other through message passing. The architecture allows the database to be scaled by adding more nodes to the cluster.

PolarDB slices a table into shards by hashing its primary key. The number of shards is configurable. Shards are stored in PolarDB nodes. When a query accesses shards in many nodes, a distributed transaction and a transaction coordinator are used to maintain ACID across nodes.

Each shard is replicated to three nodes with each replica stored on a different node. In order to save costs, we can deploy two of the replicas to store complete data. The third replica only stores a write-ahead log (WAL), which participates in the election but cannot be chosen as the leader.

See [architecture design](/doc/polardb/arch.md) for more information

## Documentation

* [Architecture design](/doc/polardb/arch.md)
* [Roadmap](/doc/polardb/roadmap.md)
* Features and their design in PolarDB for PostgreSQL Version 1.0
  * [Paxos replication](/doc/polardb/ha_paxos.md)
  * [Cluster management](/doc/polardb/deployment.md)
  * [Timestamp based MVCC](/doc/polardb/cts.md)
  * [Parallel Redo](/doc/polardb/parallel_redo.md)
  * [Remote Recovery](/doc/polardb/no_fpw.md)


## Contributing

PolarDB is built on open-source projects and extends open-source PostgreSQL. Your contribution is welcome and appreciated. Please refer [contributing](/doc/polardb/contributing.md) for how to start coding and submit a PR.

## Licensing

PolarDB code is released under the Apache Version 2.0 License and the Licenses with PostgreSQL code.

The relevant licenses can be found in the comments at the top of each file.

Reference [License](LICENSE) and [NOTICE](NOTICE) for details.

## Acknowledgements

Some codes and design ideas were from other open-source projects, such as PG-XC/XL(pgxc_ctl), TBase (part of timestamp-based vacuum and MVCC), and Citus (pg_cron). Thanks for their contributions.


## Communications

* PolarDB for PostgreSQL at Slack
https://app.slack.com/client/T023NM10KGE/C023VEMKS02

* PolarDB Technial Promotion Group at DingDing
![PolarDB Technial Promotion Group](https://github.com/alibaba/PolarDB-for-PostgreSQL/blob/master/polardb_group.png)

___

Copyright © Alibaba Group, Inc.
