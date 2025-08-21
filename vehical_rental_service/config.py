from pydantic import BaseSettings

class settings(BaseSettings):
    mongo_url:str
    mongo_db:str
    
    class config:
        env_file=".env"
        
settings=settings()        