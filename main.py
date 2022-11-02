#Python
from typing  import Optional

# Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body

app = FastAPI()

#Models

class Person(BaseModel):
  firts_name: str
  last_name: str
  age: int
  hair_color: Optional[str] = None
  married: Optional[bool] = None
  

@app.get("/")
def home():
  return {"Hello: world"}

@app.get("/ciudades")
def cuidades():
  return {"Venezuela": "Caracas"}

# Request and Response body

@app.post("/person/new")
def create_person(person: Person = Body()):
  return person