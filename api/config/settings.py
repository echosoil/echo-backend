from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    swagger_title: str = "Default name"
    swagger_description: str = "Default description"
    mongo_initdb_root_username:str = "admin"
    mongo_initdb_root_password: str = "1234"
    mode: str = "dev"
    minio_root_user: str = "admin"
    minio_root_password: str = "1234"

    @property
    def mongo_url(self) -> str:
        return f'mongodb://{self.mongo_initdb_root_username}:' + \
            f'{self.mongo_initdb_root_password}' + \
            '@mongodb:27017/?authMechanism=DEFAULT'

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
