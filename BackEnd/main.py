#Python
from typing import Optional 

#Pydantic
from pydantic import BaseModel # Crear modelos 

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path 

app = FastAPI()

''' Creamos los modelos '''

# Models

class Location(BaseModel):
	city: str
	cp: int
	state: str
	country: str

class Person(BaseModel):
	nombre: str
	apellido: str
	edad: int
	color_pelo: Optional[str] = None
	estado_civil: Optional[bool] = None

@app.get("/") #En el HOME se va a ejecutar x funcion 
def home():

  return {"Hola":"Mundo!"}
  
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
	gt=1,
	le=110,
	title="Person age",
	description="This is the person age. It's required, it's between 1 and 110"
		)
):
    return {name: age}

# Validation: Path Parameters 

@app.get("/person/detail/{person_id}")
def show_person(
	person_id: int = Path(
		...,
		gt=0,
		title="Person id",
		description="This is the person id. It's more than 0"
		)
):
	return {person_id: "It's good"}

# Validation: Request Body
## Tipo "put" actualiza la información cuando entres en el slug de a bajo indicado

@app.put("/person/{person_id}")
def update_person(
	person_id: int = Path(
		...,
		title="Person id",
		description="This is the person id",
		gt=0
	),
	person: Person = Body(...),
	location: Location = Body(...)
):

	''' Unir dos JSON '''

	results = person.dict()
    results.update(location.dict())	
	return result
