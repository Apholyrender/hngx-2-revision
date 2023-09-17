from pathlib import Path
from typing import Union

from pydantic import AnyHttpUrl, DirectoryPath, PostgresDsn
from pydantic_settings import BaseSettings

from app.utils.type_extra import SQLiteDsn


class Settings(BaseSettings):
    database_url: Union[PostgresDsn, SQLiteDsn]
    port: int = 8001
    debug: bool = True
    base_dir: DirectoryPath = Path(__file__).resolve().parent.parent.parent
    reload: bool = True
    factory: bool = True
    db_echo: bool = False
    host: str = "localhost"
    workers_count: int = 4
    allowed_origins: list = ["*"]


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
