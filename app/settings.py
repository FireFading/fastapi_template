from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv(dotenv_path="../")


class Settings(BaseSettings):
    database_url: str = Field(env="DATABASE_URL")

    postgres_db: str = Field(env="POSTGRES_DB")
    postgres_host: str = Field(env="POSTGRES_HOST")
    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")

    class Config:
        env_file = "../.env.example"
