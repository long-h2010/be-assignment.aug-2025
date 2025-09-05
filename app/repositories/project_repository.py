from app.models import Project
from app.schemas import ProjectCreate
from app.repositories.base_repository import BaseRepository

class ProjectRepository(BaseRepository[Project, ProjectCreate]):
    def __init__(self):
        super().__init__(Project)
