# Cursor-based pagination: more efficient for large datasets.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///cursor_pagination.db', echo=False)
Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    created_at = Column(Integer)  # Unix timestamp for simplicity

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create 50 posts
import time
for i in range(1, 51):
    post = Post(title=f"Post {i}", created_at=1700000000 + i)
    session.add(post)
session.commit()

# Cursor pagination: Use last seen ID as cursor
page_size = 10

# First page: Start from beginning
print("Page 1:")
results = session.query(Post).order_by(Post.id).limit(page_size).all()
for post in results:
    print(f"  {post.id}: {post.title}")
last_id = results[-1].id
print(f"Last ID on this page: {last_id}")

# Next page: Start after last_id
print(f"\nPage 2 (after ID {last_id}):")
results = session.query(Post).filter(Post.id > last_id).order_by(Post.id).limit(page_size).all()
for post in results:
    print(f"  {post.id}: {post.title}")
last_id = results[-1].id
print(f"Last ID on this page: {last_id}")

# Next page
print(f"\nPage 3 (after ID {last_id}):")
results = session.query(Post).filter(Post.id > last_id).order_by(Post.id).limit(page_size).all()
for post in results:
    print(f"  {post.id}: {post.title}")

session.close()

# Cursor pagination advantages:
# ✅ No offset scanning (always fast, even at page 1000)
# ✅ Stable results even when data changes
# ✅ Efficient database queries (uses index on ID)
#
# Disadvantages:
# ❌ Can't jump to arbitrary page numbers
# ❌ Need to track cursor between requests
#
# When to use:
# Offset: Small datasets, need page numbers (1, 2, 3...)
# Cursor: Large datasets, infinite scroll, feeds
