#Python
from typing import Optional 

#Pydantic
from pydantic import BaseModel # Crear modelos 

#FastAPI
from fastapi import FastAPI
from fastapi import Body

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
  
  ''' Request body y response body ''' 
  
@app.post("/person/new")
def create_person(person: Person = Body (...) ): # Parametro person es de tipo Person y es de tipo body obligatorio
	return person

