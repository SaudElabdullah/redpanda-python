#!/bin/bash

SCRIPTPATH="$(pwd)/app"

docker compose -f $SCRIPTPATH/docker-compose.yml down -v --remove-orphans
