#!/bin/bash

SCRIPTPATH="$(pwd)/app"

docker compose -f $SCRIPTPATH/docker-compose.yml up -d

docker exec redpanda-0 sh -c "rpk topic create test"