#!/bin/bash

SCRIPTPATH="$(pwd)/redpanda"

docker compose -f $SCRIPTPATH/docker-compose.yml up -d

sleep 10
