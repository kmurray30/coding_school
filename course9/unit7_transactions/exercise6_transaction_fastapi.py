# Integrate transactions with FastAPI using dependency injection.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

app = FastAPI()

engine = create_engine('sqlite:///fastapi_transactions.db')
Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    balance = Column(Integer)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Pydantic models
class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: int

# Dependency with automatic rollback on error
def get_db():
    database = SessionLocal()
    try:
        yield database
        # If we get here without exception, commit
        database.commit()
    except Exception:
        # On any error, rollback
        database.rollback()
        raise
    finally:
        database.close()

@app.post("/accounts")
def create_account(name: str, initial_balance: int, database: Session = Depends(get_db)):
    account = Account(name=name, balance=initial_balance)
    database.add(account)
    # Auto-commit via dependency
    return {"id": account.id, "name": account.name, "balance": account.balance}

@app.post("/transfer")
def transfer_money(transfer: TransferRequest, database: Session = Depends(get_db)):
    # Find accounts
    from_acc = database.query(Account).filter_by(name=transfer.from_account).first()
    to_acc = database.query(Account).filter_by(name=transfer.to_account).first()
    
    if not from_acc or not to_acc:
        raise HTTPException(status_code=404, detail="account not found")
    
    if from_acc.balance < transfer.amount:
        raise HTTPException(status_code=400, detail="insufficient funds")
    
    # Perform transfer (atomic - both happen or neither)
    from_acc.balance -= transfer.amount
    to_acc.balance += transfer.amount
    
    # Auto-commit via dependency (or auto-rollback on error)
    return {
        "message": "transfer successful",
        "from": {"name": from_acc.name, "balance": from_acc.balance},
        "to": {"name": to_acc.name, "balance": to_acc.balance}
    }

# Run with: uvicorn exercise6_transaction_fastapi:app --reload
#
# Test:
# 1. POST /accounts?name=Alice&initial_balance=1000
# 2. POST /accounts?name=Bob&initial_balance=500
# 3. POST /transfer {"from_account": "Alice", "to_account": "Bob", "amount": 100}
#    → Both balances update atomically
# 4. POST /transfer {"from_account": "Alice", "to_account": "Bob", "amount": 10000}
#    → Fails, both balances unchanged (automatic rollback)
