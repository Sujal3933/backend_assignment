from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
import os

security = HTTPBearer()
SECRET = os.getenv("JWT_SECRET")

def get_current_user(creds: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = creds.credentials
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")