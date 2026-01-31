# Integrate SQLAlchemy with FastAPI. Database-backed CRUD API.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

app = FastAPI()

# Database setup
engine = create_engine('sqlite:///blog.db', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# SQLAlchemy model
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000), nullable=False)
    author = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

# Pydantic models for request/response
class PostCreate(BaseModel):
    title: str
    content: str
    author: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    
    class Config:
        from_attributes = True  # Allows reading from SQLAlchemy models

# Dependency to get database session
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

# Create a post
@app.post("/posts", response_model=PostResponse)
def create_post(post: PostCreate, database: Session = Depends(get_db)):
    db_post = Post(**post.model_dump())
    database.add(db_post)
    database.commit()
    database.refresh(db_post)  # Get the generated ID
    return db_post

# List all posts
@app.get("/posts", response_model=list[PostResponse])
def list_posts(database: Session = Depends(get_db)):
    return database.query(Post).all()

# Get a specific post
@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, database: Session = Depends(get_db)):
    post = database.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="post not found")
    return post

# Update a post
# Delete a post
# Add these endpoints yourself

...

# Run with: uvicorn exercise10_fastapi_database:app --reload
#
# Test in /docs:
# 1. POST /posts to create a post
# 2. GET /posts to list all
# 3. GET /posts/1 to get specific post
# 4. Implement UPDATE and DELETE
#
# The database persists between restarts (blog.db file)
