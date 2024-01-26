# Desc: Get an object from Minio
from minio.error import S3Error
from starlette.responses import StreamingResponse

from api.config.s3 import storageClient


async def get_object(bucket: str, file_name: str):
    """
    Get an object from Minio
    
    Parameters
    ----------
    bucket : str
        The name of the bucket where the file will be uploaded.
    file_name : str
        The name of the file to download.
        
    Returns
    -------
    bool
        Whether the file was successfully downloaded.
    StreamingResponse
        The file content.
    """
    try:
        # Fetching the file from MinIO
        response = storageClient.get_object(bucket, file_name)

        # Determine the content_type based on the file type, adjust this as needed
        content_type = "application/octet-stream"

        # Streaming the file content in chunks for efficient handling of large files
        return True, StreamingResponse(
            response.stream(32*1024), media_type=content_type)
    except S3Error as e:
        if e.code == 'NoSuchKey':
            return False, "Object does not exist."
        return False, str(e)