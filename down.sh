#!/bin/sh
docker compose down
docker image prune -a -f
docker container prune -f
docker volume prune -f
docker network prune -f
docker system prune -f
docker system prune --volumes -f
docker builder prune -f