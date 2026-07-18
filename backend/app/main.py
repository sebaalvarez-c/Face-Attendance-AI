from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.database import Base, engine
from app.routes import attendance, user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Face Attendance AI System",
    description="Sistema de asistencia mediante reconocimiento facial y geolocalización.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(attendance.router)


@app.get("/")
def home():
    return {
        "message": "Sistema de Asistencia con IA activo",
        "endpoints": [
            "/register-user",
            "/mark-attendance",
            "/get-attendance",
            "/users"
        ]
    }
