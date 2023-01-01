from fastapi import FastAPI
from fastapi import Request
import uvicorn
import json
#from utilities.models.model import Base,engine
from utilities.schemas.schema import List_empleados,List_Depar,List_job
from fastapi.middleware.cors import CORSMiddleware
from utilities.autentication.hash_password import HashPassword





app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.post('/job')
async def origin (job: List_job):
    dato = job.dict()
    return  dato

#if "__name__" == '__main__':
#    uvicorn.run("main:app", host="0.0.0.0", port=8080)

