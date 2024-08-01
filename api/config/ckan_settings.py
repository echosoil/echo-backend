from pydantic_settings import BaseSettings


class CKANSettings(BaseSettings):
    ckan_title: str = "Default dataset name"
    ckan_description: str = "Default dataset description"
    mode: str = "dev"

    @property
    def mongo_url(self) -> str:
        return f'mongodb://{self.mongo_initdb_root_username}:' + \
            f'{self.mongo_initdb_root_password}' + \
            '@mongodb:27017/?authMechanism=DEFAULT'

    class Config:
        env_file = ".env"
        extra = "allow"

ckan_settings = CKANSettings()
