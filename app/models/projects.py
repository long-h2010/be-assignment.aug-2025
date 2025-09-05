from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"))

    organization = relationship("Organization", back_populates="projects")
    tasks = relationship("Task", back_populates="project")
    members = relationship("ProjectMember", back_populates="project")
