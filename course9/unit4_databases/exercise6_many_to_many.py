# Many-to-many: students in courses. Needs an association table.

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///many_to_many.db', echo=False)
Base = declarative_base()

# Association table (no model class needed for simple cases)
student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # Many-to-many: student.courses gives list of courses
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # Many-to-many: course.students gives list of students
    students = relationship("Student", secondary=student_courses, back_populates="courses")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create students
alice = Student(name="Alice")
bob = Student(name="Bob")

# Create courses
python = Course(name="Python 101")
databases = Course(name="Databases 101")

# Enroll students in courses
alice.courses.extend([python, databases])  # Alice takes both
bob.courses.append(python)                 # Bob takes Python

session.add_all([alice, bob, python, databases])
session.commit()

# Query student's courses
student = session.query(Student).filter_by(name="Alice").first()
print(f"{student.name}'s courses:")
for course in student.courses:
    print(f"  - {course.name}")

# Query course's students
course = session.query(Course).filter_by(name="Python 101").first()
print(f"\nStudents in {course.name}:")
for student in course.students:
    print(f"  - {student.name}")

session.close()

# Expected output:
# Alice's courses:
#   - Python 101
#   - Databases 101
# 
# Students in Python 101:
#   - Alice
#   - Bob
