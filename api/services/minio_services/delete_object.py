# Desc: Delete an object in Minio
from minio.error import S3Error

from api.config.s3 import storageClient


async def delete_object(bucket_name: str, object_name: str):
    """
    Delete an object in Minio
    
    Parameters
    ----------
    bucket_name : str
        The name of the bucket to delete.
    object_name : str
        The name of the object to delete.
        
    Returns
    -------
    bool
        Indicates whether the operation was successful.
    str
        A message indicating the status of the operation.
        
    """
    try:
        # Check if the bucket exists
        if storageClient.bucket_exists(bucket_name):
            # If so, delete the object
            storageClient.remove_object(bucket_name, object_name)
            return True, f"Object '{object_name}' deleted successfully."
        else:
            return False, f"Bucket '{bucket_name}' does not exist."
    except S3Error as e:
        return False, f"Error occurred: {e}"
