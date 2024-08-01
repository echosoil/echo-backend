#!/bin/bash

# Define variables
CKAN_URL="http://localhost:8443"
API_KEY="your-api-key"

# List of harvest source IDs
HARVEST_SOURCE_IDS=(
  "harvest-source-id-1"
  "harvest-source-id-2"
  "harvest-source-id-3"
  # Add more harvest source IDs as needed
)

# Loop through each harvest source ID and trigger the harvest job
for HARVEST_SOURCE_ID in "${HARVEST_SOURCE_IDS[@]}"
do
  curl -X POST "${CKAN_URL}/api/3/action/harvest_job_create" \
       -H "Authorization: ${API_KEY}" \
       -H "Content-Type: application/json" \
       -d "{\"source_id\": \"${HARVEST_SOURCE_ID}\"}"
  
  echo "Harvest job triggered for source ID ${HARVEST_SOURCE_ID} at $(date)"
done
