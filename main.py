from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI() # app: instance of FastAPI

# called route or endpoints or path in FastAPI
# @app: path operation decorator
# get: operation
# "/": path
# index(): path operation function, name doesn't matter
@app.get("/blog")   # add app decorator, otherwise 404 Not Found error
def index(limit: int, published: bool, sort: Optional[str]=None): 
    # specify the para types, otherwise str
    print(type(published))
    if published:
        return {"data": f"{limit} published blogs from the db" } 
    return {"data": f"{limit} blogs from the db" }  # return JSON data

@app.get("/blog/unpublished")
def unpublished():
    return {"blog": "all unpublished blogs"}

@app.get("/blog/{id}")    # if post(), 405 Method Not Allowed error
def display(id: int):          # accept parameter id, default str
    # fetch blog with id = id
    return {"data": id }

@app.get("/blog/{id}/comments")
def comments(id, limit=10):      # id is from path, but limit must be provided in Query
    return {"data": {id: f"{limit} comments"}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blogs")
def create_blog(request: Blog):
    # return request
    return { "data": f"Blog is created with {request.title}" }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)