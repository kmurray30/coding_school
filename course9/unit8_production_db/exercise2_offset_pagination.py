# Offset-based pagination: LIMIT and OFFSET.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///pagination.db', echo=False)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author = Column(String(100))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create 50 books
for i in range(1, 51):
    book = Book(title=f"Book {i}", author=f"Author {i % 10}")
    session.add(book)
session.commit()

# Paginate: Show 10 items per page
page_size = 10

# Page 1: Items 1-10
page = 1
offset_value = (page - 1) * page_size
results = session.query(Book).limit(page_size).offset(offset_value).all()
print(f"Page {page}: {[b.title for b in results]}")

# Page 2: Items 11-20
page = 2
offset_value = (page - 1) * page_size
results = session.query(Book).limit(page_size).offset(offset_value).all()
print(f"Page {page}: {[b.title for b in results]}")

# Page 3: Items 21-30
page = 3
offset_value = (page - 1) * page_size
results = session.query(Book).limit(page_size).offset(offset_value).all()
print(f"Page {page}: {[b.title for b in results]}")

session.close()

# How offset pagination works:
# LIMIT = how many items
# OFFSET = how many to skip
#
# Page 1: LIMIT 10 OFFSET 0 → items 1-10
# Page 2: LIMIT 10 OFFSET 10 → items 11-20
# Page 3: LIMIT 10 OFFSET 20 → items 21-30
#
# Formula: OFFSET = (page - 1) * page_size
#
# Problems with offset at scale:
# - Page 1000 with 10 items = OFFSET 9990 (database must scan 9990 rows to skip them)
# - If data changes between page views, items can be duplicated or skipped
# - Slow for large offsets
