from fastapi import APIRouter, Depends
from app.schemas import TaskCreate
from app.database import tasks_collection
from app.middleware import get_current_user
from bson import ObjectId

router = APIRouter()

@router.post("/")
def create_task(task: TaskCreate, user=Depends(get_current_user)):
    task_dict = task.dict()
    task_dict["user_id"] = user["id"]
    result = tasks_collection.insert_one(task_dict)
    return {"id": str(result.inserted_id)}

@router.get("/")
def get_tasks(user=Depends(get_current_user)):
    tasks = list(tasks_collection.find({"user_id": user["id"]}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks

@router.put("/{task_id}")
def update_task(task_id: str, task: TaskCreate):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    return {"msg": "Updated"}

@router.delete("/{task_id}")
def delete_task(task_id: str):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return {"msg": "Deleted"}