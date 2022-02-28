from fastapi import FastAPI

app = FastAPI()

@app.get("/")   # add app decorator, otherwise 404 Not Found error
def index():    # function for Api
    return {"data": { "Hey": "World"} }  # return JSON data

@app.get("/about")    # if post(), 405 Method Not Allowed
def about():
    return {"data": "about page" }