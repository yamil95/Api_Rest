from fastapi import FastAPI,status
from fastapi import Request
from fastapi import Depends
import uvicorn
from utilities.schemas.schema import List_empleados,List_Depar,List_job
from fastapi.middleware.cors import CORSMiddleware
from utilities.autentication.autenticacion import authenticate
from utilities.models.model import crear_tablas,cargar_tabla
from utilities.routes.user import User
from fastapi import HTTPException




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


async def validar_json (body : dict):

    return True if "items" in body.keys() and len(body["items"]) < 4 else False 




async def  validate_request (request : Request):


    if request.method == "POST" :
        body = await request.json()
        valido = await validar_json(body)
        if valido:
            return body
        else :
            return None
    
        



@app.on_event("startup")
async def create_tables ():

    await crear_tablas()
    print ("tablas creadas ")


@app.post('/job')
async def origin (job: List_job  = Depends (validate_request),user: str = Depends(authenticate)):

    if job != None:

        await cargar_tabla ("public.job",job["items"])
        return ({"estado":"se cargaron items en tabla job"})
        
        
    
    else :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="demasiados campos ")

@app.post('/departamentos')
async def origin (departamento: List_Depar  = Depends (validate_request),user: str = Depends(authenticate)):

    if departamento != None:

        await cargar_tabla ("public.departamento",departamento["items"])
        return ({"estado":"se cargaron items en tabla departamento"})
        



@app.post('/empleados')
async def origin (empleados: List_empleados  = Depends (validate_request),user: str = Depends(authenticate)):

    if empleados != None:

        await cargar_tabla ("public.empleados",empleados["items"])
        return ({"estado":"se cargaron items en tabla empleados"})
        

    
    else :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="demasiados campos ")
    
  

app.include_router(User,prefix="/user")

#if "__name__" == '__main__':

#    uvicorn.run("main:app", host="0.0.0.0", port=8080)

