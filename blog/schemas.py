import datetime
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    published:bool=False
    
class ShowBlog(BaseModel):
    title:str
    body:str
    created_at:datetime.datetime
    updated_at:datetime.datetime
    published:bool
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
        