from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv


load_dotenv()

#connection_string = "DefaultEndpointsProtocol=https;AccountName=sandysearchstorage;AccountKey=q9j1r6q/QfifnyrE+Et4xD8/dRq0jJzYHvIEEwnkG5b80HuqJUglEWkONF4g416+DxFnS9DO72BH+AStM5LPzA==;EndpointSuffix=core.windows.net"
#container_name = "sandystoragesearch"
#directory_path = "Data"

blob_service_client = BlobServiceClient.from_connection_string(os.environ.get("AZURE_CONN_STRING"))

for root, dirs, files in os.walk(os.environ.get("DIRECTORY_PATH")):
    for file in files:
        file_path = os.path.join(root, file)
        blob_name = os.path.relpath(file_path, os.environ.get("DIRECTORY_PATH"))

        blob_client = blob_service_client.get_blob_client(
            container=os.environ.get("CONTAINER_NAME"), blob=blob_name
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)

        print(f"Data uploaded Successfully - File Path {file_path}  Filename {blob_name}")
