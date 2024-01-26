# Desc: Get all buckets from Minio
from minio.error import S3Error

from api.config.s3 import storageClient


async def get_buckets():
    """
    Get all buckets from Minio
    
    Returns
    -------
    bool
        Indicates whether the operation was successful.
    list
        A list of buckets.
        
    """
    try:
        # Retrieve the list of buckets from MinIO
        buckets = storageClient.list_buckets()
        return True, [bucket.name for bucket in buckets]
    except S3Error as e:
        # Return False and the error message for failures
        return False, f"An error occurred: {e}"
