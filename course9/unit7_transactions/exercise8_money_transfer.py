# Build a money transfer API with proper transactions and error handling.

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from pydantic import BaseModel

app = FastAPI(title="Money Transfer API")

engine = create_engine('sqlite:///bank.db', echo=True)
Base = declarative_base()

class BankAccount(Base):
    __tablename__ = 'bank_accounts'
    
    id = Column(Integer, primary_key=True)
    account_number = Column(String(20), unique=True, nullable=False)
    owner_name = Column(String(100), nullable=False)
    balance = Column(Integer, default=0)
    
    __table_args__ = (
        CheckConstraint('balance >= 0', name='non_negative_balance'),
    )

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

# Pydantic models
class CreateAccountRequest(BaseModel):
    account_number: str
    owner_name: str
    initial_balance: int = 0

class TransferRequest(BaseModel):
    from_account: str
    to_account: str
    amount: int

# Dependency with transaction handling
def get_db():
    database = SessionLocal()
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()

# Create an account
@app.post("/accounts")
def create_account(request: CreateAccountRequest, database: Session = Depends(get_db)):
    # Check if account exists
    existing = database.query(BankAccount).filter_by(account_number=request.account_number).first()
    if existing:
        raise HTTPException(status_code=400, detail="account already exists")
    
    if request.initial_balance < 0:
        raise HTTPException(status_code=400, detail="initial balance cannot be negative")
    
    account = BankAccount(**request.model_dump())
    database.add(account)
    return {"message": "account created", "account_number": account.account_number}

# Get account balance
@app.get("/accounts/{account_number}")
def get_account(account_number: str, database: Session = Depends(get_db)):
    account = database.query(BankAccount).filter_by(account_number=account_number).first()
    if not account:
        raise HTTPException(status_code=404, detail="account not found")
    return {
        "account_number": account.account_number,
        "owner": account.owner_name,
        "balance": account.balance
    }

# Transfer money between accounts
@app.post("/transfer")
def transfer(request: TransferRequest, database: Session = Depends(get_db)):
    if request.amount <= 0:
        raise HTTPException(status_code=400, detail="amount must be positive")
    
    # Find both accounts
    from_account = database.query(BankAccount).filter_by(account_number=request.from_account).first()
    to_account = database.query(BankAccount).filter_by(account_number=request.to_account).first()
    
    if not from_account:
        raise HTTPException(status_code=404, detail=f"source account {request.from_account} not found")
    if not to_account:
        raise HTTPException(status_code=404, detail=f"destination account {request.to_account} not found")
    
    # Check sufficient balance
    if from_account.balance < request.amount:
        raise HTTPException(status_code=400, detail="insufficient funds")
    
    # Perform atomic transfer
    from_account.balance -= request.amount
    to_account.balance += request.amount
    
    # Transaction commits automatically via dependency
    # If any error occurs, both changes are rolled back
    
    return {
        "message": "transfer successful",
        "amount": request.amount,
        "from": {"account": from_account.account_number, "new_balance": from_account.balance},
        "to": {"account": to_account.account_number, "new_balance": to_account.balance}
    }

# Run with: uvicorn exercise8_money_transfer:app --reload
#
# Test flow:
# 1. POST /accounts {"account_number": "ACC001", "owner_name": "Alice", "initial_balance": 1000}
# 2. POST /accounts {"account_number": "ACC002", "owner_name": "Bob", "initial_balance": 500}
# 3. POST /transfer {"from_account": "ACC001", "to_account": "ACC002", "amount": 200}
#    → Alice: $800, Bob: $700
# 4. POST /transfer {"from_account": "ACC001", "to_account": "ACC002", "amount": 10000}
#    → 400 error (insufficient funds), both balances unchanged
# 5. GET /accounts/ACC001 → verify balance is still $800
#
# The transaction ensures atomic transfers - both accounts update or neither does.
