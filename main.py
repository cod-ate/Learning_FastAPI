from fastapi import FastAPI

app= FastAPI()

# Basic Query Paramater: add this to localhost address --> /users?parameter_name=any_name
@app.get("/users")
def my_users(name):
    return {"Name":name}


# real world uses: search, filter, pagination (in e-commerce sites, social media sites, etc)