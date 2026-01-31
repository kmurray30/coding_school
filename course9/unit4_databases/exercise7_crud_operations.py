# CRUD: Create, Read, Update, Delete operations with SQLAlchemy.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///crud.db', echo=False)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    author = Column(String(100))
    year = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# CREATE - add new records
book1 = Book(title="Dune", author="Frank Herbert", year=1965)
book2 = Book(title="Neuromancer", author="William Gibson", year=1984)
session.add_all([book1, book2])
session.commit()
print("Created 2 books")

# READ - query records
all_books = session.query(Book).all()
print(f"All books: {len(all_books)}")
for book in all_books:
    print(f"  {book.title} by {book.author} ({book.year})")

# READ - filter
dune = session.query(Book).filter_by(title="Dune").first()
print(f"\nFound: {dune.title}")

# UPDATE - modify a record
dune.year = 1966  # Oops, wrong year
session.commit()
print(f"Updated Dune year to {dune.year}")

# DELETE - remove a record
session.delete(book2)
session.commit()
print("Deleted Neuromancer")

remaining = session.query(Book).count()
print(f"Remaining books: {remaining}")

# Now implement CRUD for a Product model:
# CREATE: Add 3 products
# READ: Query and print all products
# UPDATE: Change the price of one product
# DELETE: Remove one product

...

session.close()

# Expected output:
# Created 2 books
# All books: 2
#   Dune by Frank Herbert (1965)
#   Neuromancer by William Gibson (1984)
# Found: Dune
# Updated Dune year to 1966
# Deleted Neuromancer
# Remaining books: 1
