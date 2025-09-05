from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Integer, default=0)
    to_user_id = Column(Integer, ForeignKey("users.id"))

    to_user = relationship("User", back_populates="notifications")
