from app.models import Attachment
from app.schemas import AttachmentCreate
from app.repositories.base_repository import BaseRepository

class AttachmentRepository(BaseRepository[Attachment, AttachmentCreate]):
    def __init__(self):
        super().__init__(Attachment)

    def count_by_task(self, db, task_id: int) -> int:
        return db.query(Attachment).filter(Attachment.task_id == task_id).count()
