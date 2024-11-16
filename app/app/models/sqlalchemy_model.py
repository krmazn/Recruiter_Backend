from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Базовый класс для всех моделей
class Base(DeclarativeBase):
    pass

# Модель ScreeningRequest
class ScreeningRequest(Base):
    __tablename__ = "screening_request"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String, nullable=False)
    questions: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return (
            f"ScreeningRequest(id={self.id!r}, text={self.text!r}, "
            f"questions={self.questions!r}, created_at={self.created_at!r})"
        )
