from fastapi import FastAPI, APIRouter
from app.schemas import UserRequest, UserResponse
from app.models import ScreeningRequest
from datetime import datetime

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
def create_screening_request(request: UserRequest):
    hardcoded_questions = "1. Барбоскины или Смешарики? \n 2. Фиксики или ПинКод? \n 3. Какова основная проблема вселенной 'Маша и Медведь'?"
    return ScreeningRequest(
        id=id(request), 
        text=request.text, 
        questions=hardcoded_questions, 
        created_at=datetime.now()
        )

from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=True)

from sqlalchemy.orm import Session

with Session(engine) as session:
     results = create_screening_request()
     session.add([results])

     session.commit()