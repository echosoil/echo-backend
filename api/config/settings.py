from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    swagger_title: str = "Defaull name"
    swagger_description: str = "Default description"
    mongo_initdb_root_username:str = "admin"
    mongo_initdb_root_password: str = "1234"
    mode: str = "dev"

    @property
    def mongo_url(self) -> str:
        return f'mongodb://{self.mongo_initdb_root_username}:' + \
            f'{self.mongo_initdb_root_password}' + \
            '@mongodb:27017/?authMechanism=DEFAULT'

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
