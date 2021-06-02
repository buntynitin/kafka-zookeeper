#!/bin/bash
python3 $BASE_DIR/env_properties.py
cat zookeeper.properties
$BASE_DIR/$KAFKA_DIR/bin/zookeeper-server-start.sh zookeeper.properties
