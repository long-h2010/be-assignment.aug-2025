from app.models import Report
from app.schemas import ReportCreate
from app.repositories.base_repository import BaseRepository

class ReportRepository(BaseRepository[Report, ReportCreate]):
    def __init__(self):
        super().__init__(Report)
