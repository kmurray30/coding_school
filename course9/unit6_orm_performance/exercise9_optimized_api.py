# Build a FastAPI endpoint with optimized queries.

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session, joinedload
from pydantic import BaseModel

app = FastAPI()

engine = create_engine('sqlite:///optimized.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True)  # Indexed for fast lookup
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'), index=True)  # Indexed FK
    author = relationship("User", back_populates="posts")

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Pydantic models
class PostResponse(BaseModel):
    id: int
    title: str
    author_username: str
    
    class Config:
        from_attributes = True

# Dependency
def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

# BAD: N+1 query problem
@app.get("/posts/slow", response_model=list[PostResponse])
def list_posts_slow(database: Session = Depends(get_db)):
    posts = database.query(Post).all()  # 1 query
    return [
        PostResponse(
            id=post.id,
            title=post.title,
            author_username=post.author.username  # N queries (one per post)
        )
        for post in posts
    ]

# GOOD: Eager loading, no N+1
@app.get("/posts/fast", response_model=list[PostResponse])
def list_posts_fast(database: Session = Depends(get_db)):
    posts = database.query(Post).options(joinedload(Post.author)).all()  # 1 query with join
    return [
        PostResponse(
            id=post.id,
            title=post.title,
            author_username=post.author.username  # Already loaded, no extra query
        )
        for post in posts
    ]

# Add an endpoint that lists users with their post count
# Optimize it properly - no N+1 queries

...

# Run with: uvicorn exercise9_optimized_api:app --reload
#
# Create test data first, then:
# GET /posts/slow → watch console, count queries (1 + N)
# GET /posts/fast → watch console, count queries (1)
#
# With 100 posts:
# slow endpoint: 101 queries
# fast endpoint: 1 query
