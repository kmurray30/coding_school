# Demonstrate isolation issues (conceptual - SQLite doesn't fully support all levels).

# This is a conceptual exercise showing why isolation levels matter.
# SQLite doesn't support all isolation levels, so we'll simulate the scenario.

# DIRTY READ SCENARIO (would happen with READ UNCOMMITTED)
# ---------------------------------------------------------

print("=== DIRTY READ SCENARIO ===\n")

print("Without proper isolation:")
print("Time 1: Transaction A updates price to $50 (not committed)")
print("Time 2: Transaction B reads price → sees $50")
print("Time 3: Transaction A encounters error, rolls back")
print("Time 4: Transaction B uses price $50 for calculations")
print("Result: B used data that never actually existed!\n")

print("With READ COMMITTED or higher:")
print("Time 1: Transaction A updates price to $50 (not committed)")
print("Time 2: Transaction B tries to read price → BLOCKS, waits for A")
print("Time 3: Transaction A rolls back")
print("Time 4: Transaction B now reads original price $100")
print("Result: B sees only committed data, safe!\n")


# NON-REPEATABLE READ SCENARIO
# -----------------------------

print("=== NON-REPEATABLE READ SCENARIO ===\n")

print("With READ COMMITTED:")
print("Time 1: Transaction A reads account balance → $1000")
print("Time 2: Transaction B updates balance to $500, commits")
print("Time 3: Transaction A reads balance again → $500")
print("Result: Same query, different result within one transaction\n")

print("With REPEATABLE READ:")
print("Time 1: Transaction A reads account balance → $1000")
print("Time 2: Transaction B tries to update balance → BLOCKS")
print("Time 3: Transaction A reads balance again → $1000 (consistent)")
print("Time 4: Transaction A commits")
print("Time 5: Transaction B can now update")
print("Result: A sees consistent data throughout\n")


# REAL CODE EXAMPLE (using explicit transactions)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///isolation.db', echo=False)
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup
session = Session()
product = Product(name="Widget", price=100)
session.add(product)
session.commit()
session.close()

print("=== DEMONSTRATING TRANSACTION BOUNDARIES ===\n")

# Transaction A: Long-running transaction
session_a = Session()
session_a.begin()
product_a = session_a.query(Product).first()
print(f"Transaction A reads price: ${product_a.price}")

# Transaction B: Quick update
session_b = Session()
product_b = session_b.query(Product).first()
product_b.price = 50
session_b.commit()
print("Transaction B updates price to $50 and commits")

# Transaction A reads again
session_a.expire_all()  # Force refresh from DB
product_a = session_a.query(Product).first()
print(f"Transaction A reads price again: ${product_a.price}")
print("(In READ COMMITTED, A sees new value. In REPEATABLE READ, A would still see $100)")

session_a.close()
session_b.close()

# Key lesson: Isolation level controls what concurrent transactions see.
