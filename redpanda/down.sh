#!/bin/bash

SCRIPTPATH="$(pwd)/redpanda"

docker compose -f $SCRIPTPATH/docker-compose.yml down -v --remove-orphans
