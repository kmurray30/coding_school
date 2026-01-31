# Detect and fix N+1 query problems in an API.

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session, joinedload

app = FastAPI()

engine = create_engine('sqlite:///n_plus_one.db', echo=True)
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Setup test data
def setup_data():
    session = SessionLocal()
    # Clear existing
    session.query(Book).delete()
    session.query(Author).delete()
    
    # Create 3 authors with 2 books each
    for i in range(1, 4):
        author = Author(name=f"Author {i}")
        book1 = Book(title=f"Book {i}A", author=author)
        book2 = Book(title=f"Book {i}B", author=author)
        session.add_all([author, book1, book2])
    session.commit()
    session.close()

# Call once to setup
setup_data()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# BROKEN: N+1 query problem
@app.get("/books/slow")
def list_books_slow(db: Session = Depends(get_db)):
    print("\n=== SLOW ENDPOINT (N+1 problem) ===")
    books = db.query(Book).all()  # 1 query
    result = []
    for book in books:
        # This triggers a query for EACH book!
        result.append({
            "title": book.title,
            "author": book.author.name  # N queries
        })
    return result

# FIXED: Eager loading
@app.get("/books/fast")
def list_books_fast(db: Session = Depends(get_db)):
    print("\n=== FAST ENDPOINT (fixed) ===")
    books = db.query(Book).options(joinedload(Book.author)).all()  # 1 query with join
    result = []
    for book in books:
        result.append({
            "title": book.title,
            "author": book.author.name  # Already loaded!
        })
    return result

# EXERCISE: Fix this endpoint (it has N+1 problem)
@app.get("/authors")
def list_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    result = []
    for author in authors:
        result.append({
            "name": author.name,
            "book_count": len(author.books),  # N+1 here!
            "books": [b.title for b in author.books]
        })
    return result

# Run with: uvicorn exercise5_n_plus_one_detection:app --reload
#
# Watch the console (echo=True):
# GET /books/slow → 7 queries (1 for books + 6 for authors)
# GET /books/fast → 1 query (with JOIN)
# GET /authors → 4 queries (1 for authors + 3 for books)
#
# Fix /authors endpoint using selectinload(Author.books)
