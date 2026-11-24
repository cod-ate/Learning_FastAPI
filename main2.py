from fastapi import FastAPI

app= FastAPI()

# Extentions of Query Parameter

# 1st Optional Paramater: it is used to handle unwanted errors
@app.get("/users")
def my_users(name: str= None):
    return {"Name":name}

# 2nd Default Parameter: it sets a default value if users does not provide any
@app.get("/products")
def my_prods(limit: int= 10):
    return {"Limit": limit}

# 3rd Multiple query Parameters: /items?name=laptop&price=1000
@app.get("/items")
def my_prods(name: str=None, price: int=0):
    return {"Name":name,
            "Price":price}

