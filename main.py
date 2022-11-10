#Python
from typing  import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr, SecretStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
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
  
class BasePerson(BaseModel):
  firts_name: str = Field(
    ...,
    min_length=1,
    max_length=50,
    example="Luisbel"
    )
  
  last_name: str = Field(
    ...,
    min_length=1,
    max_length=50,
    example = "Ramos"
  )
  
  age: int = Field(
    ...,
    le=60,
    ge=18
  )
  
  email: EmailStr = Field(example = "luisbelr9@gmail.com")
  hair_color: Optional[HairColor] = Field(default=None) 
  married: Optional[bool] = None
 
  

class Person(BasePerson):
  password: SecretStr = Field(min_length=8, title="Password")
  

@app.get(
  path="/",
  status_code=status.HTTP_200_OK)
def home():
  return {"Hello: world"}

@app.get(
  path="/ciudades",
  status_code=status.HTTP_200_OK)
def cuidades():
  return {"Venezuela": "Caracas"}

# Request and Response body

@app.post(
  path="/person/new", 
  response_model=BasePerson,
  status_code=status.HTTP_201_CREATED
  )
def create_person(person: Person = Body()):
  return person

# Validaciones: Query Parameters

@app.get(
  path="/person/detail",
  status_code=status.HTTP_200_OK)
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

@app.get(
  path="/person/detil/{person_id}",
  status_code=status.HTTP_202_ACCEPTED)
def show_person(
  person_id: int = Path(
    gt=0,
    title="This is to path parameters",
    description="This is my firts parameters"
    )
):
  return {person_id: "Exist"}

@app.put(
  path="/person/{person_id}",
  status_code=status.HTTP_202_ACCEPTED)
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt= 0
    ),
    person : BasePerson = Body(...),
    location : Location = Body(...)
):
    # Forma de hacerlo actualizando 
    result = person.dict()
    result.update(location.dict())
    return result
    