from pydantic import BaseSettings


class AppConfig(BaseSettings):
    db_name: str
    api_url : str 
    
    class Config:
        env_file = ".env"
        