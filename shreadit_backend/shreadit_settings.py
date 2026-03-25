import logging
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


log = logging.getLogger(__name__)

env = os.getenv("APP_ENV", "local")  # defaults to local
if env == "example":
    raise RuntimeError("Unable to run with an example environment file.")


# Load the correct .env file before pydantic-settings reads anything
env_files = {
    "test": ".env.test",
    "local": ".env.local",
    "dev": ".env.dev",
    "prod": ".env.prod"
}

log.info(f"Using APP_ENV={env} environment variable.")
log.info(f"Loading {env_files[env]}")
load_dotenv(env_files[env])


class ShreaditSettings(BaseSettings):
    environment: str = env
    secret_key: str
    frontend_url: str
    debug: str

    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_migration_user: str
    db_migration_password: str

    @property
    def is_testing(self) -> bool:
        return self.environment in ("test", "local")

shreadit_settings = ShreaditSettings(debug=os.getenv("DEBUG"),
                                     secret_key=os.getenv("SECRET_KEY"),
                                     frontend_url=os.getenv("FRONTEND_URL"),
                                     db_migration_user=os.getenv("DATABASE_MIGRATION_USER"),
                                     db_migration_password=os.getenv("DATABASE_MIGRATION_PASSWORD"),
                                     db_name=os.getenv("DATABASE_NAME"),
                                     db_user=os.getenv("DATABASE_USER"),
                                     db_password=os.getenv("DATABASE_PASSWORD"),
                                     db_host=os.getenv("DATABASE_HOST"),
                                     db_port=os.getenv("DATABASE_PORT"))