from fastapi import APIRouter
from app.schemas.pydantic_models import UserRequest, UserResponse, ScreeningResponse
from app.models import ScreeningRequest
from sqlalchemy import select
from ..deps import Session
from typing import List

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
async def create_screening_request(request: UserRequest, session: Session):
    hardcoded_questions = "1. Барбоскины или Смешарики? \n 2. Фиксики или ПинКод? \n 3. Какова основная проблема вселенной 'Маша и Медведь'?"
    screening_request = ScreeningRequest( 
        text=request.text, 
        questions=hardcoded_questions
        )
    session.add(screening_request)
    await session.commit()
    await session.refresh(screening_request)

    return screening_request


@router.get("/screening", response_model=List[ScreeningResponse])
async def get_screening_requests(session: Session):
    result = await session.execute(
        select(ScreeningRequest).order_by(ScreeningRequest.created_at.desc())
    )
    screening_requests = result.scalars().all()

    return screening_requests