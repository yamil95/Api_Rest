from passlib.context import CryptContext 
import os

schemes = os.getenv("schemes")
deprecated = os.getenv("deprecated")
pwd_context = CryptContext(schemes=[schemes],deprecated = deprecated)


class HashPassword:
    
    def create_hash(self, password: str): 
        return pwd_context.hash(password)
    
    def verify_hash(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)