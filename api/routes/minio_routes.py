import io
from fastapi import APIRouter, File, UploadFile, HTTPException, Path
from minio.error import S3Error

from api.config.s3 import storageClient
from api.services.minio_services import get_buckets, get_object_list, \
    add_bucket, get_object, add_object
from api.routes.decorators import count_route_usage


router = APIRouter()


@router.post("/{bucket}",
             summary="Upload a file to the MinIO storage.",
             description="Upload a file to the MinIO storage.",
             status_code=201,
             responses={
                 404: {
                     "description": "Bucket does not exist."
                 },
                 500: {
                     "description": "Internal server error."
                 }
             })
async def upload_file(
    bucket: str = Path(..., description="he name of the bucket."),
    file: UploadFile = File(...)):
    """
    Upload a file to a specified MinIO bucket.

    Args:
    - bucket (str): The name of the bucket where the file will be uploaded.
    - file (UploadFile): The file to upload.
    """
    status, message = await add_object(bucket, file.filename, await file.read())
    if status:
        return message
    else:
        if message == f"Bucket '{bucket}' does not exist.":
            raise HTTPException(status_code=404, detail=message)
        raise HTTPException(status_code=500, detail=message)


@router.get("/{bucket}/{file_name}",
            summary="Download a file from the MinIO storage.",
            description="Download a file from the MinIO storage.",
            status_code=200,
            responses={
                404: {
                    "description": "File does not exist."
                },
                500: {
                    "description": "Internal server error."
                }
            })
async def download_file(bucket: str, file_name: str):
    """
    Download a file from the MinIO storage.
    """
    status, file = await get_object(bucket, file_name)
    if status:
        return file
    else:
        if file == "Object does not exist.":
            raise HTTPException(status_code=404, detail="File does not exist.")
        raise HTTPException(status_code=500, detail=file)


@router.post("/buckets/{bucket}",
             summary="Create a new bucket in the MinIO storage.",
             description="Create a new bucket in the MinIO storage.",
             status_code=201,
             responses={
                 400: {
                        "description": "Bucket name cannot be 'buckets'."
                    },
                 500: {
                     "description": "Internal server error."
                 }
             })
@count_route_usage("POST /buckets/", dynamic_path="bucket")
async def create_bucket(bucket: str = Path(
    ..., description="The name of the bucket.")):
    """
    Create a new bucket in the MinIO storage.
    """
    # Bucket cannt be 'buckets'
    if bucket == "buckets":
        raise HTTPException(
            status_code=400, detail="Bucket name cannot be 'buckets'")
    status, message = await add_bucket(bucket)
    if status:
        return message
    else:
        raise HTTPException(status_code=500, detail=message)


@router.get("/buckets",
            summary="List all buckets in the MinIO storage.",
            description="List all buckets in the MinIO storage.",
            status_code=200,
            responses={
                500: {
                    "description": "Internal server error."
                }
            })
@count_route_usage("GET /buckets/")
async def list_buckets():
    """
    List all buckets in the MinIO storage.
    """
    status, buckets = await get_buckets()
    if status:
        return buckets
    else:
        raise HTTPException(status_code=500, detail=buckets)


@router.get("/{bucket}",
            summary="List all files in a bucket.",
            description="List all files in a bucket.",
            status_code=200,
            responses={
                404: {
                    "description": "Bucket does not exist."
                },
                500: {
                    "description": "Internal server error."
                }
            })
@count_route_usage("GET /bucket", dynamic_path="bucket")
async def list_files(bucket: str = Path(
    ..., description="The name of the bucket.")):
    status, objects = await get_object_list(bucket)
    if status:
        return objects
    else:
        if objects == "Bucket does not exist":
            raise HTTPException(status_code=404, detail=objects)
        raise HTTPException(status_code=500, detail=objects)