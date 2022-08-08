from pydantic import BaseSettings


class AppConfig(BaseSettings):
    db_titres: str
    db_echeanciers : str
    api_url : str 
    
    class Config:
        env_file = ".env"
        