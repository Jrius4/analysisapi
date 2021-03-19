from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit:int = 10,
        published:bool = True,
        sort:Optional[str]=None):
    if published:
        return {'data':{f"{limit} published blogs, which is {published}"}}
    else:
        return {'data':{f"{limit} blogs, which is {published}"}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]=False

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data':f"blog is created title as {blog.title}"}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id : int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id,limit:int=5):
    return {'data':{id,limit}}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)