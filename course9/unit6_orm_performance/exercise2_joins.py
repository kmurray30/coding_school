# Query with joins to access related data.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///joins.db', echo=True)
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
Session = sessionmaker(bind=engine)
session = Session()

# Create data
herbert = Author(name="Frank Herbert")
gibson = Author(name="William Gibson")

book1 = Book(title="Dune", author=herbert)
book2 = Book(title="Neuromancer", author=gibson)
book3 = Book(title="Count Zero", author=gibson)

session.add_all([herbert, gibson, book1, book2, book3])
session.commit()

# Query with explicit join
result = session.query(Book).join(Author).filter(Author.name == "William Gibson").all()
print(f"Gibson books: {[b.title for b in result]}")

# Query and access relationship (causes additional query)
book = session.query(Book).first()
print(f"Book: {book.title}, Author: {book.author.name}")

session.close()

# Expected SQL:
# SELECT books.* FROM books JOIN authors ON books.author_id = authors.id WHERE authors.name = ?
# 
# Notice the join syntax combines two tables.
