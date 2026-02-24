from pydantic import BaseModel
from typing import Optional


# =========================
# Paper Import Schema
# =========================
class PaperImport(BaseModel):
    title: str
    abstract: Optional[str] = None
    workspace_id: int


# =========================
# Paper Response Schema
# =========================
class PaperResponse(BaseModel):
    id: int
    title: str
    abstract: Optional[str]
    workspace_id: int

    class Config:
        from_attributes = True