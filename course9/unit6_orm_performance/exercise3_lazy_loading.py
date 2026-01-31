# Lazy loading causes N+1 query problem. Watch it happen.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///lazy.db', echo=True)  # echo=True shows SQL
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

print("\n=== LAZY LOADING (N+1 problem) ===")
# Query all posts
posts = session.query(Post).all()  # 1 query
print(f"Queried {len(posts)} posts")

# Access each post's author - triggers separate query per post!
for post in posts:
    print(f"{post.title} by {post.author.username}")  # N queries (one per post)

session.close()

# Expected SQL:
# SELECT * FROM posts  (1 query - gets all posts)
# SELECT * FROM users WHERE id = 1  (query for first post's author)
# SELECT * FROM users WHERE id = 1  (query for second post's author - redundant!)
# SELECT * FROM users WHERE id = 2  (query for third post's author)
# ... and so on
#
# This is the N+1 problem:
# 1 query to get posts + N queries to get authors = 1 + N queries
# With 6 posts, that's 7 queries. With 1000 posts, that's 1001 queries.
# 
# This kills performance. Next exercise fixes it.
