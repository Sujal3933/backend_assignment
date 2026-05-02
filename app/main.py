from fastapi import FastAPI
from app.routes import auth_routes, task_routes
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # sab allow
    allow_credentials=True,
    allow_methods=["*"],   # OPTIONS, POST, GET sab allow
    allow_headers=["*"],
)

app.include_router(auth_routes.router, prefix="/api/v1/auth")
app.include_router(task_routes.router, prefix="/api/v1/tasks")

@app.get("/")
def home():
    return {"msg": "API running"}