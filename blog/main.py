from datetime import datetime
from typing import List
from fastapi import FastAPI,Depends,status,Response,HTTPException
from sqlalchemy.orm import Session
from . import schemas,models
from .database import engine,SessionLocal

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(get_db)):
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        published=request.published
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def all_blogs(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def show(id,response:Response,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':}
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
    
    blog.delete(synchronize_session=False)

    db.commit()

    return {'detail':'deleted successfully'}

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == 
    id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"blog with the id {id} is not found"
        )
    
    blog.update(
        {'title':request.title,
        'body':request.body,
        'published':request.published,
        'updated_at':datetime.now()
        },synchronize_session=False)
    db.commit()
    return {'detail':'updated successfully'}


@app.post('/user',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=request.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

