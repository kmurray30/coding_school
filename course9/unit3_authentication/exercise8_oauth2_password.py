# Use FastAPI's OAuth2PasswordBearer for standardized auth.

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fake user DB
users_db = {
    "alice": {
        "username": "alice",
        "hashed_password": pwd_context.hash("secret"),
        "user_id": 1
    }
}

def create_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + expires_delta
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="incorrect credentials")
    
    token = create_token({"sub": user["username"], "user_id": user["user_id"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
async def protected(current_user: dict = Depends(get_current_user)):
    return {"message": "authenticated", "user": current_user}

# Run with: uvicorn exercise8_oauth2_password:app --reload
#
# In /docs, click "Authorize" button, enter username=alice, password=secret
# Now all protected endpoints automatically include the token.
# 
# This is the standard OAuth2 Password flow. FastAPI integrates it into /docs UI.
