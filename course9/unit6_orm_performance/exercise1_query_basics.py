# Query building with SQLAlchemy: filters, ordering, limiting.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///queries.db', echo=True)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author = Column(String(100))
    year = Column(Integer)
    rating = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
books = [
    Book(title="Dune", author="Frank Herbert", year=1965, rating=5),
    Book(title="Neuromancer", author="William Gibson", year=1984, rating=5),
    Book(title="Snow Crash", author="Neal Stephenson", year=1992, rating=4),
    Book(title="Foundation", author="Isaac Asimov", year=1951, rating=5),
]
session.add_all(books)
session.commit()

# Filter by author
herbert_books = session.query(Book).filter_by(author="Frank Herbert").all()
print(f"Frank Herbert books: {[b.title for b in herbert_books]}")

# Filter with comparison
modern_books = session.query(Book).filter(Book.year > 1980).all()
print(f"Books after 1980: {[b.title for b in modern_books]}")

# Order by year
ordered = session.query(Book).order_by(Book.year).all()
print(f"Ordered by year: {[(b.title, b.year) for b in ordered]}")

# Limit results
top_3 = session.query(Book).order_by(Book.rating.desc()).limit(3).all()
print(f"Top 3 rated: {[b.title for b in top_3]}")

# Combine: filter, order, limit
query = session.query(Book).filter(Book.rating >= 5).order_by(Book.year).limit(2).all()
print(f"Best 2 oldest: {[(b.title, b.year) for b in query]}")

session.close()

# Expected output (watch SQL in console):
# SELECT * FROM books WHERE author = ?
# SELECT * FROM books WHERE year > ?
# SELECT * FROM books ORDER BY year
# SELECT * FROM books ORDER BY rating DESC LIMIT 3
# SELECT * FROM books WHERE rating >= 5 ORDER BY year LIMIT 2
