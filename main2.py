from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class MyUser(BaseModel):
    name: str
    age: int

@app.post("/createUser")
def create_user(user: MyUser):
    return {"Message":"Hello World",
            "Data": user}