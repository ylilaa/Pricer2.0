from pydantic import BaseSettings


class AppConfig(BaseSettings):
    db_name: str 
    
    class Config:
        env_file = ".env"
        