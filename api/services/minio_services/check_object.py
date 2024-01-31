# Desc: Check if an object exists in Minio
from api.config.s3 import storageClient


async def check_object(bucket: str, file_name: str):
    """
    Check if an object exists in Minio
    
    Parameters
    ----------
    bucket : str
        The name of the bucket where the file will be uploaded.
    file_name : str
        The name of the file to download.
        
    Returns
    -------
    bool
        Whether the file exists.
    """
    try:
        # Fetching the file from MinIO
        storageClient.stat_object(bucket, file_name)
        return True
    except Exception as e:
        return False
