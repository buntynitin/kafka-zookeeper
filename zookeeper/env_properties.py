import os


def main():
    env_properties = ["admin.serverPort"]
    properties = {}
    properties["dataDir"] = "/tmp/zookeeper-data"
    properties["clientPort"] = "2181"
    properties["maxClientCnxns"] = "0"
    properties["admin.enableServer"] = "false"

    with open("zookeeper.properties", "w") as file_writer:
        for k, v in properties.items():
            env_value = os.getenv(k)
            file_writer.write("{}={}\n".format(k, env_value or v))
        for prop in env_properties:
            env_value = os.getenv(prop)
            if env_value:
                file_writer.write("{}={}\n".format(prop, env_value))


if __name__ == "__main__":
    main()

