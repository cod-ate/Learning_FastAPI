
# creating multiple routes

from fastapi import FastAPI

app= FastAPI()

# Home page
@app.get("/")
def my_home():
    return {"message":"My home page"}

# About page
@app.get("/about")
def my_about():
    return {"message":"My about page"}

# Users page
@app.get("/users")
def my_users():
    return {"users_data":['A','B','C']}