
from pydantic import BaseModel 
from typing import List


class Esquema_empleado (BaseModel):

    id : int
    name : str
    datetime : str
    departamento_id : int
    job_id : int


class Esquema_departamento (BaseModel):
    id: int
    name_department : str


class Esquema_job (BaseModel):

    id: int
    name_job : str

class Esquema_user (BaseModel):

    username: str
    password : str

class TokenResponse(BaseModel): 
    access_token: str 
    token_type: str


class List_Depar (BaseModel):

    items : List[Esquema_departamento]

class List_job (BaseModel):

    items : List[Esquema_job]

class List_empleados (BaseModel):

    items : List[Esquema_empleado]