"""
AI-Based Employee Performance Analyzer
Application entrypoint — wires together config, database, routers,
exception handlers, and startup hooks.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db
from app.core.exceptions import register_exception_handlers

from app.api.routers import auth, employees, ai, ml, reports

app = FastAPI(
    title="AI-Based Employee Performance Analyzer",
    description=(
        "Employee Performance Management System with JWT auth, RBAC, "
        "Google Gemini-powered AI features, a scikit-learn performance "
        "predictor, and Excel/PDF reporting."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(auth.router)
app.include_router(employees.router)
app.include_router(ai.router)
app.include_router(ml.router)
app.include_router(reports.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "AI-Based Employee Performance Analyzer API",
        "docs": "/docs",
        "environment": settings.ENVIRONMENT,
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
