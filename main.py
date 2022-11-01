from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {"Hello: world"}

@app.get("/ciudades")
def cuidades():
  return {"Venezuela": "Caracas"}