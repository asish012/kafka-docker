# Description:

This is a simplified fork of [wurstmeister/kafka-docker](https://github.com/wurstmeister/kafka-docker) and intended to be used just for playing around with docker based kafka cluster.

The `docker-compose.yml` file prepares a kafka container along with a zookeeper, a zoonavigator and a kafka-manager container instance. You can also increase the number of kafka brokers the same way as wurstmeister.

! The `docker-compose.yml` file expects appropriate kafka ang glibc lib in resources directory.


# Kafka and Zookeeper
<!-- https://github.com/wurstmeister/kafka-docker -->

**Updates in Dockerfile**

- Updates 1: Instead of automatically downloading Kafka libraries, I copy them in the container manually from local.
- Updates 2: Instead of automatically downloading Glibc libraries, I copy them in the container manually from local.

**Start a single kafka broker and a zookeeper container:**

> docker-compose up -d

Thats it. A single zookeeper node with a kafka broker will be started.
You can now use kafka scripts to create topics, or run console-producer and console-consumer, etc.

**To increase number of brokers**

> docker-compose scale kafka=3


# ZooNavigator
<!-- https://github.com/elkozmon/zoonavigator -->

Access ZooNavigator web ui at: [YOUR-IP:9001]


# KafkaManager
<!-- https://github.com/yahoo/CMAK -->

- Access KafkaManager web ui at: [YOUR-IP:9000]
! Creating a local cluster will fail because of some mutex issue.
! Original Error: Yikes! KeeperErrorCode = Unimplemented for /Kafka-Manager/mutex Try Again
! Run this following commands inside the zookeeper container to fix it:

> docker exec -it kafka-docker_zookeeper_1 bash

> ./bin/zkCli.sh

> ls /kafka-manager

> create /kafka-manager/mutex ""

> create /kafka-manager/mutex/locks ""

> create /kafka-manager/mutex/leases ""

Thats it!
Use your usual kafka scripts to create topics, or run console-producer and console-consumer, etc.
You can also use the [wurstmeister's readme](README_ORIGINAL.md) to get more details.
