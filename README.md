# Backend Assignment - Task Manager API

A scalable REST API built using **FastAPI** with JWT authentication, role-based access, and full CRUD functionality.  
This project also includes a simple frontend UI for interacting with the APIs.

---

#  Features

### Authentication
- User Registration
- User Login
- Password hashing (secure storage)
- JWT-based authentication

### Role-Based Access
- User role (default)
- Admin role (extendable)
- Protected routes using JWT

### Task Management (CRUD)
- Create Task
- Get All Tasks
- Update Task
- Delete Task

### Security
- JWT token validation
- Input validation using Pydantic
- Secure password hashing

### Frontend (Basic UI)
- Register & Login UI
- Create and view tasks
- API integration using Fetch

---

## Tech Stack

- Backend: FastAPI (Python)
- Authentication: JWT
- Database: MongoDB / SQLite (based on setup)
- Frontend: HTML, CSS, JavaScript
- API Testing: Swagger UI

---

## Project Structure
Backend-assignment/
│
├── app/
│ ├── main.py
│ ├── auth.py
│ ├── database.py
│ ├── schemas.py
│ ├── middleware.py
│ └── routes/
│ ├── auth_routes.py
│ └── task_routes.py
│
├── frontend/
│ └── index.html
│
├── requirements.txt
├── .env (ignored)
└── README.md


---

## How to Run Project

##1. Clone Repository
```bash
git clone https://github.com/your-username/backend_assignment.git
cd backend_assignment

###2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

##3.Install Dependencies
pip install -r requirements.txt

##4.Run Backend Server
uvicorn app.main:app --reload

##5.Open API Docs
http://127.0.0.1:8000/docs

##6. Run Frontend
frontend/index.html

##7.Environment Variables
Create .env file:
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url

##8.API Endpoints
Auth
POST /api/v1/auth/register
POST /api/v1/auth/login

Tasks
POST   /api/v1/tasks/
GET    /api/v1/tasks/
PUT    /api/v1/tasks/{id}
DELETE /api/v1/tasks/{id}

## Scalability

This project is designed with scalability in mind:

- Microservices architecture can be implemented to separate authentication and task services.
- Redis caching can be added to improve performance for frequently accessed tasks.
- PostgreSQL can replace current database for better relational data handling.
- Docker containerization can be used for easy deployment and scaling.
- Load balancers can be added to handle high traffic efficiently.


##Author
Sujal Sharma
Backend Developer Intern Aspirant


##Note
This project is built as part of an internship assignment to demonstrate:
-Backend API design
-Authentication systems
-CRUD operations
-Basic frontend integration
-Scalable architecture thinking

