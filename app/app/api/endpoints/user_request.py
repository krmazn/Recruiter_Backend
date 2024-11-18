from fastapi import FastAPI, APIRouter
from app.schemas import UserRequest, UserResponse
from app.models import ScreeningRequest

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
def create_screening_request(request: UserRequest):
    hardcoded_questions = "1. Барбоскины или Смешарики? \n 2. Фиксики или ПинКод? \n 3. Какова основная проблема вселенной 'Маша и Медведь'?"
    new_request = ScreeningRequest(
        text=request.text,
        questions=hardcoded_questions
    )
