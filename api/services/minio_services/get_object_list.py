# Desc: Get all objects from a bucket in Minio
from minio.error import S3Error

from api.config.s3 import storageClient


async def get_object_list(bucket: str):
    """
    Get all objects from a bucket in Minio
    
    Parameters
    ----------
    bucket : str
        The name of the bucket.
    
    Returns
    -------
    bool
        Indicates whether the operation was successful.
    list
        A list of objects.
        
    """
    try:
        # Check if the bucket exists
        if not storageClient.bucket_exists(bucket):
            return False, "Bucket does not exist"

        # Retrieve the list of objects from MinIO
        objects = storageClient.list_objects(bucket)
        return True, [obj.object_name for obj in objects]
    except S3Error as e:
        # Return False and the error message for failures
        return False, f"An error occurred: {e}"
