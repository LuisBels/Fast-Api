#Python
from typing  import Optional

# Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

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

# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
  name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person name",
        description="Its name of person"
                              ),
  age: int = Query(le=50, ge=18)
):
  return {name:age}

#Validaciones: Path Parameters

@app.get("/person/detil/{person_id}")
def show_person(
  person_id: int = Path(
    gt=0,
    title="This is to path parameters",
    description="This is my firts parameters"
    )
):
  return {person_id: "Exist"}