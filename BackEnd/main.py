#Python
from typing import Optional 

#Pydantic
from pydantic import BaseModel # Crear modelos 

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path 

app = FastAPI()

''' Creamos los modelos '''

class Person(BaseModel):
	nombre: str
	apellido: str
	edad: int
	color_pelo: Optional[str] = None
	estado_civil: Optional[bool] = None

@app.get("/") #En el HOME se va a ejecutar x funcion 
def home():

  return {"Hola":"Mundo!"}

  return {"Hola":"Mundo"}
  
# body y response body 
  
@app.post("/person/new")
def create_person(person: Person = Body (...) ): # Parametro person es de tipo Person y es de tipo body obligatorio
	return person

# Validación: Query Paramete

@app.get("/person/detail")
def show_person(
	name: Optional[str] = Query(
		None,
		min_length=1,
		max_length=40,
		title="Person name",
		description="This is the person name. It's between 1 and 40 characters"
		),
	age: int = Query(
	...,
	title="Person age",
	description="This is the person age. It's required"
		)
):
    return {name: age}

# Validation: Path Parameters 

@app.get("/person/detail/{person_id}")
def show_person(
	person_id: int =(
		...,
		gt=0
	)
):
	return {person_id: "It's good"}