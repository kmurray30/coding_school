# Practice the full migration workflow for evolving a schema over time.

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# PHASE 1: Initial schema
# -----------------------
# Start with a simple blog model

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(5000), nullable=False)

# Task 1:
# $ alembic revision --autogenerate -m "create posts table"
# $ alembic upgrade head


# PHASE 2: Add author tracking
# -----------------------------
# Add author field

# Uncomment this:
# class Post(Base):
#     __tablename__ = 'posts'
#     
#     id = Column(Integer, primary_key=True)
#     title = Column(String(200), nullable=False)
#     content = Column(String(5000), nullable=False)
#     author = Column(String(100), nullable=False)  # NEW

# Task 2:
# $ alembic revision --autogenerate -m "add author to posts"
# $ alembic upgrade head


# PHASE 3: Add publish status
# ----------------------------
# Track if post is published or draft

# Uncomment this:
# class Post(Base):
#     __tablename__ = 'posts'
#     
#     id = Column(Integer, primary_key=True)
#     title = Column(String(200), nullable=False)
#     content = Column(String(5000), nullable=False)
#     author = Column(String(100), nullable=False)
#     published = Column(Boolean, default=False)  # NEW

# Task 3:
# $ alembic revision --autogenerate -m "add published status"
# $ alembic upgrade head


# PHASE 4: Add timestamps
# -----------------------
# Track when posts were created/updated

# Uncomment this:
# class Post(Base):
#     __tablename__ = 'posts'
#     
#     id = Column(Integer, primary_key=True)
#     title = Column(String(200), nullable=False)
#     content = Column(String(5000), nullable=False)
#     author = Column(String(100), nullable=False)
#     published = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.utcnow)  # NEW
#     updated_at = Column(DateTime, onupdate=datetime.utcnow)  # NEW

# Task 4:
# $ alembic revision --autogenerate -m "add timestamps"
# $ alembic upgrade head


# PHASE 5: Add comments relationship
# -----------------------------------
# Posts can have many comments

# Uncomment this:
# class Comment(Base):
#     __tablename__ = 'comments'
#     
#     id = Column(Integer, primary_key=True)
#     post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
#     author = Column(String(100), nullable=False)
#     content = Column(String(1000), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
# 
# class Post(Base):
#     __tablename__ = 'posts'
#     
#     id = Column(Integer, primary_key=True)
#     title = Column(String(200), nullable=False)
#     content = Column(String(5000), nullable=False)
#     author = Column(String(100), nullable=False)
#     published = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, onupdate=datetime.utcnow)
#     
#     comments = relationship("Comment", back_populates="post")

# Task 5:
# $ alembic revision --autogenerate -m "add comments table"
# $ alembic upgrade head


# VERIFICATION:
# ------------
# $ alembic history  (see all migrations)
# $ alembic current  (see current version)
# $ psql course9_db
# \d posts     (should have all columns)
# \d comments  (should exist with foreign key to posts)


# PRACTICE ROLLBACK:
# -----------------
# $ alembic downgrade -1  (remove comments)
# $ alembic downgrade -1  (remove timestamps)
# $ alembic upgrade head  (re-apply all)


# This is the real workflow:
# 1. Change models
# 2. Generate migration
# 3. Review migration file
# 4. Apply migration
# 5. Test
# 6. Commit migration file to git
# 7. Repeat
