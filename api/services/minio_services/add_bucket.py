# Desc: Create a new bucket in Minio
from minio.error import S3Error

from api.config.s3 import storageClient


async def add_bucket(bucket_name: str):
    """
    Create a new bucket in Minio
    
    Parameters
    ----------
    bucket_name : str
        The name of the bucket to create.
        
    Returns
    -------
    bool
        Indicates whether the operation was successful.
    str
        A message indicating the status of the operation.
        
    """
    try:
        # Check if the bucket already exists
        if not storageClient.bucket_exists(bucket_name):
            # If not, create the new bucket
            storageClient.make_bucket(bucket_name)
            return True, f"Bucket '{bucket_name}' created successfully."
        else:
            return False, f"Bucket '{bucket_name}' already exists."
    except S3Error as e:
        return False, f"Error occurred: {e}"
