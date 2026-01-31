# Transactions: commit on success, rollback on error.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///transactions.db', echo=True)
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    balance = Column(Integer)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup: Create two accounts
session = Session()
alice = Account(name="Alice", balance=1000)
bob = Account(name="Bob", balance=500)
session.add_all([alice, bob])
session.commit()
session.close()

print("Initial balances:")
session = Session()
for account in session.query(Account).all():
    print(f"  {account.name}: ${account.balance}")
session.close()

# Transaction: Transfer money
session = Session()
try:
    # Deduct from Alice
    alice = session.query(Account).filter_by(name="Alice").first()
    alice.balance -= 100
    
    # Add to Bob
    bob = session.query(Account).filter_by(name="Bob").first()
    bob.balance += 100
    
    # Commit transaction - both changes happen atomically
    session.commit()
    print("Transfer succeeded!")
except Exception as e:
    # Rollback on any error - neither change happens
    session.rollback()
    print(f"Transfer failed, rolled back: {e}")
finally:
    session.close()

# Check final balances
session = Session()
print("\nFinal balances:")
for account in session.query(Account).all():
    print(f"  {account.name}: ${account.balance}")
session.close()

# Expected:
# Alice: $900 (was $1000)
# Bob: $600 (was $500)
#
# If anything failed between deduct and add, both would be rolled back.
# That's atomicity.
