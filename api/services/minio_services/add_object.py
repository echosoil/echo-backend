# Desc: Add an object to Minio
import io
from minio.error import S3Error

from api.config.s3 import storageClient


async def add_object(bucket: str, file_name: str, file_content: bytes):
    """
    Add an object to Minio
    
    Parameters
    ----------
    bucket : str
        The name of the bucket where the file will be uploaded.
    file_name : str
        The name of the file to upload.
    file_content : bytes
        The file content.
        
    Returns
    -------
    bool
        Indicates whether the operation was successful.
    str
        A message indicating the status of the operation.
        
    """
    try:
        # Check if the bucket exists
        if not storageClient.bucket_exists(bucket):
            return False, f"Bucket '{bucket}' does not exist."

        # Convert bytes to a stream-like object
        file_stream = io.BytesIO(file_content)

        # Upload the file to MinIO
        storageClient.put_object(
            bucket_name=bucket,
            object_name=file_name,
            data=file_stream,
            length=len(file_content),
            content_type="application/octet-stream",
        )
        return True, f"File '{file_name}' uploaded successfully."
    except S3Error as e:
        return False, str(e)