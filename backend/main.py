from fastapi import FastAPI

from core.database import engine, Base

# Import models first to ensure they're registered with SQLAlchemy
from models.user import User
from models.workspace import Workspace
from models.paper import Paper

# Routers
from routers.auth import router as auth_router
from routers.workspace import router as workspace_router
from routers.papers import router as papers_router
from routers.chat import router as chat_router

app = FastAPI(title="ResearchPilot AI Backend")

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth_router)
app.include_router(workspace_router)
app.include_router(papers_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "ResearchPilot AI Backend Running"
    }