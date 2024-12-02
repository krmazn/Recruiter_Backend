from fastapi import FastAPI, APIRouter
from app.schemas.pydantic_models import UserRequest, UserResponse
from app.models import ScreeningRequest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ..deps import Session

engine = create_engine("sqlite://", echo=True)

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
def create_screening_request(request: UserRequest, session: Session):
    hardcoded_questions = "1. Барбоскины или Смешарики? \n 2. Фиксики или ПинКод? \n 3. Какова основная проблема вселенной 'Маша и Медведь'?"
    screening_request = ScreeningRequest( 
        text=request.text, 
        questions=hardcoded_questions
        )
    session.add(screening_request)
    session.commit()
    session.refresh(screening_request)

    return screening_request
    