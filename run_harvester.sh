#!/bin/bash

# Define the container name and the CKAN configuration file path
CONTAINER_NAME=ckan-docker-2-ckan2-1
CKAN_INI_PATH=/srv/app/ckan.ini

# Define the harvest job ID you want to run
HARVEST_JOB_ID=55bf438c-e724-4966-9f8d-0de8a591375f

# Run the harvester command inside the CKAN container
echo "$(date): Running harvester" >> logfile.log
docker exec -i $CONTAINER_NAME ckan --config=$CKAN_INI_PATH harvester run-test $HARVEST_JOB_ID
