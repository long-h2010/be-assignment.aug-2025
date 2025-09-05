from app.models import ProjectMember
from app.schemas import ProjectMemberCreate
from app.repositories.base_repository import BaseRepository

class ProjectMemberRepository(BaseRepository[ProjectMember, ProjectMemberCreate]):
    def __init__(self):
        super().__init__(ProjectMember)
