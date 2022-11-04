#Python
from typing  import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
  white = "White"
  black = "Black"
  red = "Red"
  brown = "Brown"

class Location(BaseModel):
  state: str
  country: str

class Person(BaseModel):
  firts_name: str = Field(
    ...,
    min_length=1,
    max_length=50
    )
  last_name: str = Field(
    ...,
    min_length=1,
    max_length=50
  )
  age: int = Field(
    ...,
    le=60,
    ge=18
  )
  hair_color: Optional[HairColor] = Field(default=None) 
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

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt= 0
    ),
    person : Person = Body(...),
    location : Location = Body(...)
):
    # Forma de hacerlo actualizando 
    result = person.dict()
    result.update(location.dict())
    return result
    