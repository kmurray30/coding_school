# Automatic rollback when errors occur in a transaction.

from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///rollback.db', echo=False)
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    balance = Column(Integer)
    
    # Constraint: balance can't go negative
    __table_args__ = (
        CheckConstraint('balance >= 0', name='positive_balance'),
    )

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Setup
session = Session()
alice = Account(name="Alice", balance=100)
session.add(alice)
session.commit()
session.close()

# Try to withdraw more than balance (should fail and rollback)
session = Session()
try:
    alice = session.query(Account).filter_by(name="Alice").first()
    print(f"Initial balance: ${alice.balance}")
    
    # Try to withdraw $200 (but only has $100)
    alice.balance -= 200  # This would make balance = -100
    
    # Commit will fail because of constraint
    session.commit()
    print("Withdrawal succeeded")
except Exception as e:
    # Rollback - balance stays at $100
    session.rollback()
    print(f"Withdrawal failed: constraint violation")
    print("Transaction rolled back - balance unchanged")
finally:
    session.close()

# Verify balance is still $100
session = Session()
alice = session.query(Account).filter_by(name="Alice").first()
print(f"Final balance: ${alice.balance}")
session.close()

# Expected:
# Initial balance: $100
# Withdrawal failed: constraint violation
# Transaction rolled back - balance unchanged
# Final balance: $100
#
# The constraint prevented invalid data.
# The rollback ensured the database stayed consistent.
