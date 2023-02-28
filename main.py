from fastapi import FastAPI,status
from fastapi import Request
from fastapi import Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
import uvicorn
from utilities.schemas.schema import List_empleados,List_Depar,List_job
from fastapi.middleware.cors import CORSMiddleware
from utilities.autentication.autenticacion import authenticate
from utilities.models.model_sync import crear_tablas,cargar_tabla,insert_log
from utilities.routes.user import User
from fastapi import HTTPException
from utilities.autentication.jwt_auth import verify_access_token 



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


async def validar_json (body : dict):

    return True if "items" in body.keys() and len(body["items"]) <=1000 else False 

@app.on_event("startup")
async def create_tables ():

    crear_tablas()
    print ("tablas creadas ")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    token = request.headers["authorization"]
    token = token.split()[1]
    decoded_token = await verify_access_token(token) 
    user= decoded_token["user"]
    insert_log(user,"error en el parseo del json")
    return PlainTextResponse(str(exc), status_code=400)


@app.post('/jobs')
async def origin (job: List_job ,user: str = Depends(authenticate)):

    datos = job.dict()

    if validar_json(datos):

        cargar_tabla ("job",datos["items"])
        cantidad = len (datos["items"])
        insert_log (user,f"se cargaron {cantidad} en tabla job")
        return ({"estado":"se cargaron items en tabla job"})
    else :
        insert_log(user,"demasiados campos")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="demasiados campos ")


@app.post('/departamentos')
async def origin (departamento: List_Depar  ,user: str = Depends(authenticate)):
    datos = departamento.dict()
    if validar_json(datos):

        cargar_tabla ("departamento",datos["items"])
        cantidad = len (datos["items"])
        insert_log (user,f"se cargaron {cantidad} en tabla departamento")
        return ({"estado":"se cargaron items en tabla departamento"})
    else:
        insert_log (user,"demasiados campos")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="demasiados campos ")
        



@app.post('/empleados')
async def origin (empleados: List_empleados  ,user: str = Depends(authenticate)):
    datos = empleados.dict()

    if validar_json(datos):

        cargar_tabla ("empleados",datos["items"])
        cantidad = len (datos["items"])
        insert_log (user,f"se cargaron {cantidad} en tabla empleados")
        return ({"estado":"se cargaron items en tabla empleados"})
        

    
    else :
        insert_log (user,"demasiados campos")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="demasiados campos ")
    
  

app.include_router(User,prefix="/user")

if "__name__" == '__main__':
  

  uvicorn.run("main:app", host="0.0.0.0", port=8080)

