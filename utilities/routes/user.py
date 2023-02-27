from fastapi import APIRouter,Depends,Request
from utilities.schemas.schema import Esquema_user,TokenResponse
from utilities.conexion.connection import engine
from sqlalchemy.sql import text
from utilities.autentication.hash_password import HashPassword
from fastapi import HTTPException,status
from utilities.autentication.jwt_auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

User = APIRouter()
hasher = HashPassword()
    
def verificar_usuario_existe (email : str ) : 

    query = f"""

        SELECT * FROM users WHERE email = \'{email}\'
    """

    cursor = engine.cursor()

    datos = cursor.execute (query)
  
    return datos.fetchone()
    

def agregar_user (user : dict):

    
    password = hasher.create_hash(user.password)

    query = f"""

            INSERT INTO users (email,password) VALUES (\'{user.username}\',\'{password}\')
    
    
    """
    
    #conexion_db = engine.connect().execution_options(autocommit = True) 
    cursor = engine.cursor()
    cursor.execute(query)
    engine.commit()
    cursor.close()
        


@User.post ("/create_user")
async def agregar_usuario (user: Esquema_user):

    if len (verificar_usuario_existe (user.username)) == 0:
        agregar_user(user)
    
    else :

        raise HTTPException (status_code=  status.HTTP_406_NOT_ACCEPTABLE,detail= "usuario ya existe")
        
@User.post ("/signing")
async def signing_user (user: OAuth2PasswordRequestForm = Depends() ):

    password = user.password
    email = user.username

    usuario = verificar_usuario_existe (email)
    
    valido = hasher.verify_hash(password,usuario[1])

    if valido : 
       
        token = await create_access_token (email)
        return {"access_token": token, "token_type":"Bearer"}
    else:
        return {"result": "usuario no reconocido"}
