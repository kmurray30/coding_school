# One-to-many relationship: one user has many posts.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///relationships.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    
    # Relationship: access user's posts with user.posts
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'))  # Links to users.id
    
    # Relationship: access post's author with post.author
    author = relationship("User", back_populates="posts")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a user and posts
alice = User(username="alice")
post1 = Post(title="First Post", content="Hello world", author=alice)
post2 = Post(title="Second Post", content="More content", author=alice)

session.add_all([alice, post1, post2])
session.commit()

# Query user and access their posts
user = session.query(User).filter_by(username="alice").first()
print(f"User: {user.username}")
for post in user.posts:
    print(f"  - {post.title}: {post.content}")

# Query post and access its author
post = session.query(Post).filter_by(title="First Post").first()
print(f"\nPost: {post.title}")
print(f"Author: {post.author.username}")

# Create another user with posts
# Then query and print their relationship

...

session.close()

# Expected output:
# User: alice
#   - First Post: Hello world
#   - Second Post: More content
# 
# Post: First Post
# Author: alice
