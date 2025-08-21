from pydantic_settings import BaseSettings

class settings(BaseSettings):
    mongo_url:str="mongodb://localhost:27017"
    mongo_db:str="vehical_rental"
    jwt_secret:str="super-secret"
    jwt_algorithm:str="HS256"
    jwt_expire_minutes:int=60
    
    class config:
        env_file=".env"
        
settings=settings()        