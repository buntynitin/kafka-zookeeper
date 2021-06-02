#!/bin/bash
python3 $BASE_DIR/env_properties.py
cat server.properties
$BASE_DIR/$KAFKA_DIR/bin/kafka-server-start.sh server.properties
