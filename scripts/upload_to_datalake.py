import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()
account_name = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
account_key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")  # Retrieve from .env

# Validate the key
if not account_key:
    raise ValueError("Environment variable AZURE_STORAGE_ACCOUNT_KEY is not set.")

container_name = "bronze"

# Local directory containing files
base_dir = os.path.dirname(os.path.dirname(__file__))  # Navigate up one level from scripts/
data_dir = os.path.join(base_dir, "data", "raw")  # data/raw/ folder

# List files to upload
files_to_upload = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]

# Create a BlobServiceClient
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Upload files
for file_path in files_to_upload:
    file_name = os.path.basename(file_path)  # Extract only the file name (e.g., customers.csv)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"Uploaded {file_name} to container {container_name}.")