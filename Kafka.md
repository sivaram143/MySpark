### Introduction

- Apache Kafka is a distributed streaming platform
- A streaming platform has three key capabilities:
    - Publish and subscribe to streams of records, similar to a message queue or enterprise messaging system.
    - Store streams of records in a fault-tolerant durable way.
    - Process streams of records as they occur.
- Use Cases: **Messaging** | **Website Activity Tracking** | **Metrics**|**Log Aggregation**|**Stream Processing** | **Event Sourcing**|**Commit Log**|

### Setup and Run
1. Download and install [Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/1.1.0/kafka_2.11-1.1.0.tgz)
2. Start the Server
   ```
   $ bin/zookeeper-server-start.sh config/zookeeper.properties ## To start [Zookeeper](https://zookeeper.apache.org/)
   
   $ bin/kafka-server-start.sh config/server.properties  ## Start Kakfa
   ```

### Commands
1. Create a Topic
   ```
   $ bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic weblogs
   ```
2. Display list  
   ```
   $ bin/kafka-topics --list --zookeeper localhost:2181
   ```
3. Describe the topic
   ```
   $ bin/kafka-topics.sh --describe --zookeeper localhost:2181 -–topic weblogs
   ```
4. Send some messages
  ```
  $ bin/kafka-console-producer.sh --broker-list localhost:9092 --topic weblogs
  test weblg entry1
  test weblg entry2
  ...
  ...
  ```
5. Start a consumer  to check the messages from the producer
   ```
   bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic weblogs --from-beginning
   ```
6. Delete a topic
   ```
   $ bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic <topic_name>
   $ kafka-topics --list --zookeeper localhost:2181
   ```
### References
- [Apache Kafka](https://kafka.apache.org)
