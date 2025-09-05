from sqlalchemy.orm import Session
from app import schemas
from app.repositories import AttachmentRepository, TaskRepository

att_repo = AttachmentRepository()
task_repo = TaskRepository()

class AttachmentService:
    async def upload_files(self, db: Session, task_id: int, files: list[bytes], upload_dir: str):
        if task_repo.get(db, task_id) is None:
            raise ValueError("Task does not exist")
        
        attachments = []
        for file in files:
            file_path = upload_dir / f"{task_id}_{len(attachments)}.dat"
            with open(file_path, "wb") as f:
                f.write(file)
            att_data = {"task_id": task_id, "file_path": str(file_path)}
            attachment = att_repo.create(db, att_data)
            attachments.append(attachment)
        return attachments
    
    def count_by_task(self, db: Session, task_id: int) -> int:
        return att_repo.count_by_task(db, task_id)
