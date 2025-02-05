from fastapi import APIRouter, status
from uuid import UUID
from app.schemas.pydantic_models import UserRequest, UserResponse, ScreeningResponse
from app.models import ScreeningRequest
from sqlalchemy import delete, select
from ..deps import Session
from typing import List
from gigachatprompt.prompt import generate_questions

gigachat_key = None  # Insert unique key to access LLM services

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
async def create_screening_request(request: UserRequest, session: Session):
    screening_request = ScreeningRequest( 
        job_title=request.job_title,
        text=request.text, 
        questions=generate_questions(gigachat_key, f'"""{request.job_title}"""' , f'"""{request.text}"""')
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

@router.delete("/screening/{screening_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_screening_requests(session: Session, screening_id: UUID) -> None:
    screening = (
        await session.execute(
            select(ScreeningRequest).filter_by(id=screening_id)
        )
    ).scalar_one_or_none()
    if screening:
        await session.delete(screening)
        await session.commit()
