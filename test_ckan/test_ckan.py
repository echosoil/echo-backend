import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os

# Suppress only the single InsecureRequestWarning from urllib3 needed
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Configuration
CKAN_URL = 'https://localhost:8443'
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJmZlVPQXlqUExjc0xETGh3UXNmbldiTkdiZG1BM0x1eXB0ZXpYNUF6YzVjIiwiaWF0IjoxNzA2NjQ5NTAzfQ.YzEjD8riEw0coGfMtBVpp9RLTR33TkYtizWfBnQLfdM'
IS_CERT = False
DOWNLOAD_PATH = 'download'

# Function to create a dataset
def create_dataset(ckan_url, api_key, dataset_dict):
    headers = {'Authorization': api_key}
    response = requests.post(f"{ckan_url}/api/action/package_create", headers=headers, json=dataset_dict, verify=IS_CERT)
    return response.json()

def upload_resource(ckan_url, api_key, dataset_id, resource_path):
    headers = {'Authorization': api_key}
    files = {'upload': open(resource_path, 'rb')}
    data = {
        'package_id': dataset_id,
        'name': resource_path.split('/')[-1]  # Extracts file name
    }
    response = requests.post(f"{ckan_url}/api/action/resource_create", headers=headers, files=files, data=data, verify=IS_CERT)
    return response.json()

# Function to download a dataset
def download_dataset(ckan_url, dataset_id, download_folder):
    response = requests.get(f"{ckan_url}/api/action/package_show?id={dataset_id}", verify=IS_CERT)
    print('response1:', response)
    if response.status_code == 200:
        dataset = response.json()['result']
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        for resource in dataset['resources']:
            print(f"Downloading resource {resource['url']}")
            download = requests.get(resource['url'], verify=IS_CERT)
            file_path = os.path.join(download_folder, resource['name'])
            with open(file_path, 'wb') as f:
                f.write(download.content)
        print("Download completed.")
    else:
        print("Failed to download dataset.")

def get_dataset_id(ckan_url, api_key, dataset_name):
    headers = {'Authorization': api_key}
    response = requests.get(f"{ckan_url}/api/action/package_show?id={dataset_name}", headers=headers, verify=IS_CERT)
    if response.status_code == 200:
        return response.json()['result']['id']
    else:
        return None

# Function to get dataset details
def get_dataset_details(ckan_url, api_key, dataset_name):
    headers = {'Authorization': api_key}
    response = requests.get(f"{ckan_url}/api/3/action/package_show?id={dataset_name}", headers=headers, verify=IS_CERT)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return None

    
response = requests.get(f"{CKAN_URL}/api/3/action/organization_list", verify=IS_CERT)
organizations = response.json()["result"]
response = requests.get(f"{CKAN_URL}/api/3/action/organization_show?id={organizations[0]}", verify=IS_CERT)
organization_id = response.json()["result"]["id"]


# Example usage
example_dataset = {
    'name': 'example-dataset3',
    'title': 'Example Dataset',
    'notes': 'This is an example dataset.',
    'owner_org': organization_id,
    # Add other required fields and additional metadata as needed
    'extras': [{'key': 'uploader_name', 'value': 'oleg'}] 
}

# Check if dataset exists
dataset_name = example_dataset['name']
dataset_id = get_dataset_id(CKAN_URL, API_KEY, dataset_name)

# If dataset does not exist, create it
if not dataset_id:
    create_response = create_dataset(CKAN_URL, API_KEY, example_dataset)
    print(create_response)
    
    # Assuming dataset creation was successful
    dataset_id = create_response['result']['id']
else:
    print(f"Dataset '{dataset_name}' already exists with ID {dataset_id}.")

# Get dataset details
dataset_details = get_dataset_details(CKAN_URL, API_KEY, dataset_name)
if dataset_details:
    print('dataset_details', dataset_details)  # This will print all details of the dataset
    # print(dataset_details['uploader_name'])
else:
    print("Failed to retrieve dataset details.")


# Upload a resource
file_path = 'test_csv.csv'  
upload_response = upload_resource(CKAN_URL, API_KEY, dataset_id, file_path)
print(upload_response)

# Download a dataset
download_dataset(CKAN_URL, 'example-dataset1', DOWNLOAD_PATH)