#kafka
kubectl apply -f https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/examples/kafka/kafka-persistent.yaml -n kafka-deployments

#kafka connect
kubectl apply -f https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/examples/connect/kafka-connect.yaml -n kafka-deployments

#kafka connector
kubectl apply -f https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/examples/connect/source-connector.yaml -n kafka-deployments
