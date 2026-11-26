
# dynamic routes and path parameters

from fastapi import FastAPI

app= FastAPI()

# Home page
@app.get("/users/{user_id}") # ex: write address as /users/101
def get_user(user_id: int): # this enforces user to give integer id only else 
                            # it will generate validation error
    return {"user_id": user_id,
                "username": "hello world"}

# function is same but output changes depending on the ID (like: 101,105,1002,etc)