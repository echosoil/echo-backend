from minio import Minio
from api.config.settings import settings

storageClient = Minio(
    "minio:9000",  # Change to your server information
    access_key=settings.minio_root_user,
    secret_key=settings.minio_root_password,
    secure=False  # Change to True if you are using https
)
