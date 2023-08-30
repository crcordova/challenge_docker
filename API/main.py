from fastapi import FastAPI
from Marcs import Marcs
from Users import Users
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

app =FastAPI(
    title='api-marks'
)
class status(str, Enum):
    in_status = "In"
    out_status = "Out"

class MarcModel(BaseModel):
    id_user: int
    tipo: status = Field(..., description="Status can only be 'in' or 'out'")

class UserModel(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
async def root():
    return {"version": '1.0'}

@app.get('/marcs')
async def marcs():
    marcas = Marcs()
    marcas = marcas.get_all_marcs()
    return marcas
    # return {'get':'marcas'}

@app.post('/marcs')
async def create_marc(input: MarcModel):
    marcas = Marcs()
    marcas = marcas.create_marc(input.id_user, input.tipo)
    return {'marcas':'add'}

@app.delete('/marcs')
async def delecte_marc(input:MarcModel):
    marcas = Marcs()
    marcas.delete_marc(input.id_user, input.tipo)
    return{'Marca':'Deleted'}

app.post('/users')
async def create_user(input: UserModel):
    users = Users()
    users = users.create(input.name, input.email, input.password)
    return {'users':'add'}