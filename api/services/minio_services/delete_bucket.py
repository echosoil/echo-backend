# Desc: Delete a bucket in Minio
from minio.error import S3Error

from api.config.s3 import storageClient


async def delete_bucket(bucket_name: str):
    """
    Delete a bucket in Minio
    
    Parameters
    ----------
    bucket_name : str
        The name of the bucket to delete.
        
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
            # If so, delete the bucket
            storageClient.remove_bucket(bucket_name)
            return True, f"Bucket '{bucket_name}' deleted successfully."
        else:
            return False, f"Bucket '{bucket_name}' does not exist."
    except S3Error as e:
        return False, f"Error occurred: {e}"
