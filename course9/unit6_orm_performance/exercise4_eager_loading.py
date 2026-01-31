# Fix N+1 problem with eager loading (joinedload).

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, joinedload

engine = create_engine('sqlite:///eager.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create 3 users, each with 2 posts
for i in range(1, 4):
    user = User(username=f"user{i}")
    post1 = Post(title=f"Post {i}A", author=user)
    post2 = Post(title=f"Post {i}B", author=user)
    session.add_all([user, post1, post2])
session.commit()

print("\n=== EAGER LOADING (no N+1) ===")
# Use joinedload to load posts and authors in ONE query
posts = session.query(Post).options(joinedload(Post.author)).all()
print(f"Queried {len(posts)} posts")

# Access authors - NO additional queries!
for post in posts:
    print(f"{post.title} by {post.author.username}")  # Already loaded

session.close()

# Expected SQL:
# SELECT posts.*, users.* FROM posts LEFT OUTER JOIN users ON posts.user_id = users.id
# 
# Just 1 query! Loads posts and authors together.
# With 1000 posts, still just 1 query.
#
# Compare to exercise3 (lazy loading): 1001 queries → 1 query
# This is a massive performance improvement.
