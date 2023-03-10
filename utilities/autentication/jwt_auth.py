import time
from datetime import datetime
from fastapi import HTTPException, status 
import jwt
from fastapi import Depends, HTTPException, status 
from fastapi.security import OAuth2PasswordBearer
import os 
from utilities.models.model_sync import insert_log
SECRET_KEY = os.getenv("SECRET_KEY") 
ALGORI = os.getenv ("ALGORI")


async def create_access_token(user: str) -> str: 
    datos = {"user": user, "expires": time.time() + 3600 }
    token = jwt.encode(payload = datos,key= SECRET_KEY, algorithm=ALGORI) 
    return token


async def verify_access_token(token: str) -> dict: 
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORI])
        expire = data.get("expires") 
        if expire is None:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="error en la conformacion del token") 
        if datetime.utcnow() > datetime.utcfromtimestamp(expire): 
            insert_log ("none","se intento acceder con un token vencido")
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token vencido") 
        return data 
    except : 
        insert_log ("none","se intento acceder con un token no valido")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="token invalido")


