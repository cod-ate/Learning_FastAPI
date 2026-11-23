
# dynamic routes and path parameters

from fastapi import FastAPI

app= FastAPI()

# Home page
@app.get("/users/{user_id}")
def get_user(user_id):
    return {"user_id": user_id,
            "username": "hello world"}
