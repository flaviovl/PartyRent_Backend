#!/bin/bash
#==========================================================
# Script Basico para remover todos os container/images
#
#  - Parar todos os containers que estao rodando
#  - remover containers
#  - remover images
#  - remover volumes
#==========================================================

echo '===================================================='
echo 'Parando todos os containers...'
docker stop $(docker ps -aq)

echo '===================================================='
echo 'Removendo containers containers ..'
docker rm $(docker ps -aq)

echo '===================================================='
echo 'removendo images ...'
docker rmi $(docker images -q)

echo '===================================================='
echo 'removendo volumes'
docker volume rm $(docker volume ls -q)


echo '===================================================='
echo 'Remove todos os containers, volumes, networks e images'
docker system prune -a --volumes