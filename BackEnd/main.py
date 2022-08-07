from fastapi import FastAPI

app = FastAPI()

@app.get("/") #En el HOME se va a ejecutar x funcion 
def home():
  return {"Hola":"Mundo!"}