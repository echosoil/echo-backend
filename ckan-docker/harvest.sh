#!/bin/bash

# Define variables
CKAN_URL="https://localhost:8443"
API_KEY="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJBMkhWNFlXRXhwNGNoQnBuQlliTjJ3b0dCUkpvdXVvalRUZmJZeGlVZlFVIiwiaWF0IjoxNzIwMDkzNDIzfQ.yE39dpxxE24KChxVCmP7AwTsdkaZPMI3Nl9zk3wN6zg"

OWNER_ORG_NAME="someorg"  # Replace with your actual organization name
SOURCE_TYPE="ckan"  # Replace with your actual source type

# Function to get organization ID by name
get_organization_id() {
  echo "Getting organization ID for name: ${OWNER_ORG_NAME}..."
  response=$(curl -k -s -X GET "${CKAN_URL}/api/3/action/organization_show?id=${OWNER_ORG_NAME}" \
    -H "Authorization: ${API_KEY}" \
    -H "Content-Type: application/json")

  echo "Get Organization ID Response: $response"

  # Extract the organization ID
  ORGANIZATION_ID=$(echo $response | jq -r '.result.id')
  echo "Organization ID: $ORGANIZATION_ID"

  if [ -z "$ORGANIZATION_ID" ]; then
    echo "Organization ID not found."
    return 1
  else
    return 0
  fi
}

# Function to add a new harvest source
add_harvest_source() {
  echo "Adding new harvest source..."
  response=$(curl -k -s -X POST "${CKAN_URL}/api/3/action/harvest_source_create" \
    -H "Authorization: ${API_KEY}" \
    -H "Content-Type: application/json" \
    -d '{
          "url": "https://localhost:8444",
          "type": "ckan",
          "title": "European Data Portal",
          "name": "european-data-portal",
          "owner_org": "'${ORGANIZATION_ID}'",
          "source_type": "'${SOURCE_TYPE}'"
        }')

  echo "Add Harvest Source Response: $response"

  # Check if the response contains an error
  if echo $response | jq -e '.error' > /dev/null; then
    echo "Failed to add harvest source."
    return 0
  else
    echo "Successfully added harvest source."
    return 0
  fi
}

# Function to get the harvest source ID
get_harvest_source_id() {
  echo "Getting harvest source ID..."
  response=$(curl -k -s -X GET "${CKAN_URL}/api/3/action/harvest_source_list" \
    -H "Authorization: ${API_KEY}" \
    -H "Content-Type: application/json")

  echo "Get Harvest Source ID Response: $response"

  # Extract the harvest source ID
  HARVEST_SOURCE_ID=$(echo $response | jq -r '.result[] | select(.url=="https://data.europa.eu/data/datasets") | .id')
  echo "Harvest Source ID: $HARVEST_SOURCE_ID"

  if [ -z "$HARVEST_SOURCE_ID" ]; then
    echo "Harvest source ID not found."
    return 1
  else
    return 0
  fi
}

# Function to trigger the harvest job
trigger_harvest_job() {
  HARVEST_SOURCE_ID=$1
  echo "Triggering harvest job for source ID ${HARVEST_SOURCE_ID}..."
  response=$(curl -k -s -X POST "${CKAN_URL}/api/3/action/harvest_job_create" \
    -H "Authorization: ${API_KEY}" \
    -H "Content-Type: application/json" \
    -d "{\"source_id\": \"${HARVEST_SOURCE_ID}\"}")

  echo "Trigger Harvest Job Response: $response"

  # Check if the response contains an error
  if echo $response | jq -e '.error' > /dev/null; then
    echo "Failed to trigger harvest job."
    return 1
  else
    echo "Successfully triggered harvest job."
    return 0
  fi
}

# Main function
main() {
  if get_organization_id; then
    if add_harvest_source; then
      if get_harvest_source_id; then
        trigger_harvest_job $HARVEST_SOURCE_ID
      else
        echo "Error: Could not retrieve harvest source ID."
      fi
    else
      echo "Error: Could not add harvest source."
    fi
  else
    echo "Error: Could not retrieve organization ID."
  fi
}

# Run the main function
main
