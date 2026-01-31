# Production-ready API with all database best practices.

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Index
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

app = FastAPI(title="Production Database API")

# Production-ready engine configuration
engine = create_engine(
    'sqlite:///./production.db',
    pool_size=10,              # Connection pool
    max_overflow=20,           # Extra connections for spikes
    pool_pre_ping=True,        # Check connection health
    pool_recycle=3600,         # Recycle connections hourly
    echo=False                 # Disable SQL logging in production
)

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, index=True)  # Indexed for search
    content = Column(String(5000))
    author = Column(String(100), index=True)  # Indexed for filtering
    published = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Composite index for common queries
    __table_args__ = (
        Index('idx_author_published', 'author', 'published'),
    )

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Pydantic models
class ArticleCreate(BaseModel):
    title: str
    content: str
    author: str

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str
    published: datetime
    
    class Config:
        from_attributes = True

# Database dependency with proper cleanup
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

# Create article
@app.post("/articles", response_model=ArticleResponse, status_code=201)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    db_article = Article(**article.model_dump())
    db.add(db_article)
    db.flush()  # Get ID before commit
    return db_article

# List articles with cursor pagination
@app.get("/articles", response_model=list[ArticleResponse])
def list_articles(
    author: Optional[str] = None,
    after_id: Optional[int] = Query(None, description="Cursor for pagination"),
    limit: int = Query(10, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(Article)
    
    # Filter by author if provided
    if author:
        query = query.filter(Article.author == author)
    
    # Cursor pagination
    if after_id:
        query = query.filter(Article.id > after_id)
    
    # Order and limit
    query = query.order_by(Article.id).limit(limit)
    
    return query.all()

# Get single article
@app.get("/articles/{article_id}", response_model=ArticleResponse)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="article not found")
    return article

# Update article
@app.put("/articles/{article_id}", response_model=ArticleResponse)
def update_article(
    article_id: int,
    update: ArticleCreate,
    db: Session = Depends(get_db)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="article not found")
    
    for key, value in update.model_dump().items():
        setattr(article, key, value)
    
    db.flush()
    return article

# Delete article
@app.delete("/articles/{article_id}", status_code=204)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="article not found")
    
    db.delete(article)
    return None

# Health check (important for production)
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Test database connection
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"unhealthy: {str(e)}")

# Run with: uvicorn exercise8_production_api:app --reload
#
# Production features:
# ✅ Connection pooling configured
# ✅ Indexes on frequently queried columns
# ✅ Cursor pagination for scalability
# ✅ Proper session management
# ✅ Transaction handling (auto commit/rollback)
# ✅ Health check endpoint
# ✅ Input validation with Pydantic
# ✅ Proper HTTP status codes
# ✅ Error handling
