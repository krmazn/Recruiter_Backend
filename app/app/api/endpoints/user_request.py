from fastapi import APIRouter
from app.schemas.pydantic_models import UserRequest, UserResponse, ScreeningResponse
from app.models import ScreeningRequest
from sqlalchemy import select
from ..deps import Session
from typing import List
from gigachatprompt.prompt import generate_questions

router = APIRouter()
@router.post("/screening", response_model=UserResponse)
async def create_screening_request(request: UserRequest, session: Session):
    screening_request = ScreeningRequest( 
        text=request.text, 
        questions=generate_questions('MjIyMWE1YjItZmExNi00ODNkLTlkYmEtNzYzNDU3NThjNjQ3OjYwYzYwOWExLTJmNTktNDhmOS1hNDYzLWI1OTY4MWUxZDQ5Mg==', f'"""{request.text}"""')
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