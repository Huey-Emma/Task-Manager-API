from pydantic import BaseSettings


class Settings(BaseSettings):
    db_name: str
    db_username: str
    db_host: str
    db_password: str

    class Config:
        env_file = '.env'


settings = Settings()
