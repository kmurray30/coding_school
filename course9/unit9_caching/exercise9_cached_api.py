# Add caching to an API with proper invalidation.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel
import redis
import json
from datetime import datetime
from typing import Optional

app = FastAPI(title="Cached API")

# Database
engine = create_engine('sqlite:///cached_api.db')
Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String(5000))
    views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Redis
redis_pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

# Pydantic models
class ArticleCreate(BaseModel):
    title: str
    content: str

class ArticleResponse(BaseModel):
    id: int
    title: str
    content: str
    views: int
    
    class Config:
        from_attributes = True

# Dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

def get_redis():
    return redis.Redis(connection_pool=redis_pool)

# Create article (invalidate list cache)
@app.post("/articles", response_model=ArticleResponse)
def create_article(
    article: ArticleCreate,
    db: Session = Depends(get_db),
    cache: redis.Redis = Depends(get_redis)
):
    db_article = Article(**article.model_dump())
    db.add(db_article)
    db.flush()
    
    # Invalidate list cache (new article added)
    cache.delete('articles:list')
    
    return db_article

# List articles (cached)
@app.get("/articles")
def list_articles(
    db: Session = Depends(get_db),
    cache: redis.Redis = Depends(get_redis)
):
    cache_key = 'articles:list'
    
    # Try cache
    cached = cache.get(cache_key)
    if cached:
        return {"source": "cache", "articles": json.loads(cached)}
    
    # Cache miss - query database
    articles = db.query(Article).all()
    article_data = [
        {"id": a.id, "title": a.title, "content": a.content, "views": a.views}
        for a in articles
    ]
    
    # Cache for 5 minutes
    cache.set(cache_key, json.dumps(article_data), ex=300)
    
    return {"source": "database", "articles": article_data}

# Get single article (cached)
@app.get("/articles/{article_id}")
def get_article(
    article_id: int,
    db: Session = Depends(get_db),
    cache: redis.Redis = Depends(get_redis)
):
    cache_key = f'article:{article_id}'
    
    # Try cache
    cached = cache.get(cache_key)
    if cached:
        return {"source": "cache", "article": json.loads(cached)}
    
    # Cache miss
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="not found")
    
    article_data = {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "views": article.views
    }
    
    # Cache for 10 minutes
    cache.set(cache_key, json.dumps(article_data), ex=600)
    
    return {"source": "database", "article": article_data}

# Increment views (invalidate cache)
@app.post("/articles/{article_id}/view")
def increment_views(
    article_id: int,
    db: Session = Depends(get_db),
    cache: redis.Redis = Depends(get_redis)
):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="not found")
    
    article.views += 1
    db.flush()
    
    # Invalidate caches
    cache.delete(f'article:{article_id}')
    cache.delete('articles:list')
    
    return {"views": article.views}

# Cache stats
@app.get("/cache/stats")
def cache_stats(cache: redis.Redis = Depends(get_redis)):
    info = cache.info('stats')
    return {
        "keyspace_hits": info.get('keyspace_hits', 0),
        "keyspace_misses": info.get('keyspace_misses', 0),
        "hit_rate": round(
            info.get('keyspace_hits', 0) / 
            (info.get('keyspace_hits', 0) + info.get('keyspace_misses', 1)) * 100,
            2
        )
    }

# Run with: uvicorn exercise9_cached_api:app --reload
#
# Test flow:
# 1. POST /articles → create article
# 2. GET /articles → source: database (cache miss)
# 3. GET /articles → source: cache (cache hit)
# 4. GET /articles/1 → source: database
# 5. GET /articles/1 → source: cache
# 6. POST /articles/1/view → increments views, invalidates cache
# 7. GET /articles/1 → source: database (cache was invalidated)
# 8. GET /cache/stats → see hit rate
