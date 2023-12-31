from fastapi import Depends, FastAPI, status
from schemas import Blog
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session, session



app = FastAPI()


models.Base.metadata.create_all(engine)

def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body) 
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
    
@app.get('/blog/{id}')
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


