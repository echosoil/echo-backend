from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ECHO API"
    mongo_port: int = 27017
    mongo_admin: str = "admin"
    mongo_admin_password: str = "yourpassword"
    mongo_host: str = "localhost"
    mode: str = "dev"

    @property
    def mongo_url(self) -> str:
        return f'mongodb://{self.mongo_admin}:' + \
            f'{self.mongo_admin_password}@{self.mongo_host}:' + \
            f'{self.mongo_port}/?authMechanism=DEFAULT'

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
