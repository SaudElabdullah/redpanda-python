#!/bin/bash

SCRIPTPATH="$(pwd)/consumer"

docker compose -f $SCRIPTPATH/docker-compose.yml up -d