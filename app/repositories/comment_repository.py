from app.models import Comment
from app.schemas import CommentCreate
from app.repositories.base_repository import BaseRepository

class CommentRepository(BaseRepository[Comment, CommentCreate]):
    def __init__(self):
        super().__init__(Comment)
