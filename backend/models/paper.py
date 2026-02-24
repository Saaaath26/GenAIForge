from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    abstract = Column(Text, nullable=True)

    workspace_id = Column(Integer, ForeignKey("workspaces.id"))

    # Relationship (optional but good practice)
    workspace = relationship("Workspace", back_populates="papers")