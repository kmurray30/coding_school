# Different column types for different data.

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///types.db', echo=False)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    priority = Column(Integer, default=1)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create some tasks
task1 = Task(title="Learn SQLAlchemy", completed=False, priority=1)
task2 = Task(title="Build an API", completed=True, priority=2)

session.add_all([task1, task2])
session.commit()

# Query tasks
tasks = session.query(Task).all()
for task in tasks:
    print(f"{task.title}: completed={task.completed}, priority={task.priority}, created={task.created_at}")

# Create a Book model with:
# - id (Integer, primary key)
# - title (String 300)
# - author (String 100)
# - year_published (Integer)
# - in_stock (Boolean, default True)

# Add 2-3 books and query them

...

session.close()

# Expected output:
# Learn SQLAlchemy: completed=False, priority=1, created=2024-01-...
# Build an API: completed=True, priority=2, created=2024-01-...
# (your books)
