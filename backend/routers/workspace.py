from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from routers.auth import get_current_user
from models.workspace import Workspace
from schemas.workspace import WorkspaceCreate

router = APIRouter()


# CREATE WORKSPACE
@router.post("/create")
def create_workspace(
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    new_workspace = Workspace(
        name=workspace.name,
        owner_id=1   # Temporary (we’ll link real user later)
    )

    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)

    return new_workspace


# GET USER WORKSPACES
@router.get("/my")
def get_workspaces(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):

    workspaces = db.query(Workspace).all()
    return workspaces