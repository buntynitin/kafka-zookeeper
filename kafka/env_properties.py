import os


def main():
    env_properties = ["listeners", "advertised.listeners", "listener.security.protocol.map",
                      "log.flush.interval.messages", "log.flush.interval.ms", "inter.broker.listener.name"]
    properties = {}
    properties["broker.id"] = "0"
    properties["num.network.threads"] = "3"
    properties["num.io.threads"] = "8"
    properties["socket.send.buffer.bytes"] = "102400"
    properties["socket.receive.buffer.bytes"] = "102400"
    properties["socket.request.max.bytes"] = "104857600"
    properties["log.dirs"] = "/tmp/kafka-logs"
    properties["num.partitions"] = "1"
    properties["num.recovery.threads.per.data.dir"] = "1"
    properties["offsets.topic.replication.factor"] = "1"
    properties["transaction.state.log.replication.factor"] = "1"
    properties["transaction.state.log.min.isr"] = "1"
    properties["log.retention.hours"] = "168"
    properties["log.segment.bytes"] = "1073741824"
    properties["log.retention.check.interval.ms"] = "300000"
    properties["zookeeper.connect"] = "localhost:2181"
    properties["zookeeper.connection.timeout.ms"] = "18000"
    properties["group.initial.rebalance.delay.ms"] = "0"

    with open("server.properties", "w") as file_writer:
        for k, v in properties.items():
            env_prop_name = k.upper().replace(".", "_")
            env_value = os.getenv(env_prop_name)
            file_writer.write("{}={}\n".format(k, env_value or v))
        for prop in env_properties:
            env_prop_name = prop.upper().replace(".", "_")
            env_value = os.getenv(env_prop_name)
            if env_value:
                file_writer.write("{}={}\n".format(prop, env_value))


if __name__ == "__main__":
    main()

