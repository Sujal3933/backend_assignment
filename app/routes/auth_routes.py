from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserLogin
from app.database import users_collection
from app.auth import hash_password, verify_password, create_token
from fastapi import Depends
from app.auth import get_current_user
router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(400, "User exists")

    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hash_password(user.password),
        "role": "user"
    })

    return {"msg": "User created"}

@router.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(400, "Invalid credentials")

    token = create_token({"id": str(db_user["_id"]), "role": db_user["role"]})
    return {"token": token}



@router.get("/admin")
def admin_only(current_user=Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return {"msg": "Admin access granted"}
