from fastapi import FastAPI, Response
from Marcs import Marcs
from Users import Users, tests_connection
from Report import create_report, download_report
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

@app.post('/user')
async def create_user(input: UserModel):
    user = Users()
    user.create(input.name, input.email, input.password)
    return{'User':'Create'}

@app.get('/test')
async def test():
    return tests_connection()

@app.get('/report')
async def report():
    create_report()
    return {'report':'created'}

@app.get('/download')
async def report():
    repor = download_report()
    csv_content = repor.to_csv(index=False)
    response = Response(content=csv_content)
    response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    response.headers["Content-Type"] = "text/csv"

    return response