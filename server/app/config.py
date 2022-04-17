from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = "pg"
    db_name: str = "postgres"
    db_user: str = "postgres"
    db_password: str = "postgres"

    class Config:
        env_file = ".env"


settings = Settings()
