# selectinload for collections - better than joinedload for one-to-many.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, selectinload

engine = create_engine('sqlite:///selectin.db', echo=True)
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

# Create users with posts
user1 = User(username="alice")
user2 = User(username="bob")
for i in range(5):
    session.add(Post(title=f"Alice post {i}", author=user1))
    session.add(Post(title=f"Bob post {i}", author=user2))
session.add_all([user1, user2])
session.commit()

print("\n=== SELECTINLOAD (efficient for collections) ===")
# Load users and their posts efficiently
users = session.query(User).options(selectinload(User.posts)).all()

# Access posts - no additional queries
for user in users:
    print(f"{user.username} has {len(user.posts)} posts:")
    for post in user.posts:
        print(f"  - {post.title}")

session.close()

# Expected SQL:
# SELECT * FROM users
# SELECT * FROM posts WHERE posts.user_id IN (1, 2)
#
# 2 queries total. Much better than 1 + N.
#
# joinedload vs selectinload:
# - joinedload: 1 query with JOIN (can cause duplicate rows for one-to-many)
# - selectinload: 2 queries with IN clause (cleaner for collections)
# 
# Use selectinload for one-to-many collections (user.posts)
# Use joinedload for many-to-one relationships (post.author)
