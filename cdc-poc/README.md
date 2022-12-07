## Steps
1. Install strimzi operator
2. Install Kafka Cluster
3. Install Kafka Connect
4. Configure source database: https://debezium.io/documentation/reference/stable/connectors/mysql.html#setting-up-mysql
   1. update parameter group to enable full row level binlog replication
      1. binlog_format     = row
      2. binlog_row_image  = full
5. Configure KafkaConnector debezium source


## Open Questions
What should happen to the database if replication breaks?
- Bring down the database?
- Purge the log after some retention period? i.e., 10 days, 30 days, 45 days?