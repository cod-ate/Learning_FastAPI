from fastapi import FastAPI

app= FastAPI()

# Post API
@app.post("/createUser1")
def create_user(name:str, age:int):
    return {"Name":name,
            "Age":age,
            "Message":"Hi there"}


@app.post("/createUser2")
def create_user(user:dict):
    return {
        "Message":"User Created",
        "Data":user
    }