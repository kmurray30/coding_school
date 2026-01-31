# Optimistic locking: handle concurrent updates with version numbers.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from time import sleep

engine = create_engine('sqlite:///optimistic.db', echo=False)
Base = declarative_base()

class Document(Base):
    __tablename__ = 'documents'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String(5000))
    version = Column(Integer, default=1)  # Version counter

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup
session = Session()
doc = Document(title="Shared Document", content="Original content", version=1)
session.add(doc)
session.commit()
session.close()

# Simulate two users editing the same document concurrently

# User A: Read document
session_a = Session()
doc_a = session_a.query(Document).filter_by(id=1).first()
print(f"User A reads: version={doc_a.version}, content='{doc_a.content}'")
original_version_a = doc_a.version

# User B: Read document
session_b = Session()
doc_b = session_b.query(Document).filter_by(id=1).first()
print(f"User B reads: version={doc_b.version}, content='{doc_b.content}'")
original_version_b = doc_b.version

# User B edits and saves first
doc_b.content = "User B's changes"
doc_b.version += 1
session_b.commit()
print(f"User B saves: version={doc_b.version}")
session_b.close()

# User A tries to save (but doc has been modified by B)
doc_a.content = "User A's changes"

# Check version before saving
current_doc = session_a.query(Document).filter_by(id=1).first()
if current_doc.version != original_version_a:
    print(f"ERROR: Version mismatch! Someone else modified the document.")
    print(f"Expected version {original_version_a}, but found version {current_doc.version}")
    print("User A must reload and re-apply changes.")
    session_a.rollback()
else:
    # Safe to save
    doc_a.version += 1
    session_a.commit()
    print("User A saves successfully")

session_a.close()

# Check final state
session = Session()
final_doc = session.query(Document).first()
print(f"\nFinal: version={final_doc.version}, content='{final_doc.content}'")
session.close()

# Expected output:
# User A reads: version=1, content='Original content'
# User B reads: version=1, content='Original content'
# User B saves: version=2
# ERROR: Version mismatch! Someone else modified the document.
# Expected version 1, but found version 2
# User A must reload and re-apply changes.
# 
# Final: version=2, content='User B's changes'
#
# This prevents lost updates. User A doesn't overwrite B's changes.
