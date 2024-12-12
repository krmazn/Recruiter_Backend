from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

# Модель ScreeningRequest
class ScreeningRequest(Base):
    __tablename__ = "screening_request"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    job_title: Mapped[str] = mapped_column(String, default="", server_default="")
    text: Mapped[str] = mapped_column(String, nullable=False)
    questions: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return (
            f"ScreeningRequest(id={self.id!r}, text={self.text!r}, "
            f"questions={self.questions!r}, created_at={self.created_at!r})"
        )
