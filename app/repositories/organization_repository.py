from app.models import Organization
from app.schemas import OrganizationCreate
from app.repositories.base_repository import BaseRepository

class OrganizationRepository(BaseRepository[Organization, OrganizationCreate]):
    def __init__(self):
        super().__init__(Organization)
