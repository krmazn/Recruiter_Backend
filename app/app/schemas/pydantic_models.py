from pydantic import BaseModel
from datetime import datetime

class UserRequest(BaseModel):
    job_title: str
    text: str
    
    
class UserResponse(BaseModel):
    job_title: str
    text: str
    questions: str
    

    class Config:
            orm_mode = True 


class ScreeningResponse(BaseModel):
    id: int
    job_title: str
    text: str
    questions: str
    created_at: datetime

    class Config:
        orm_mode = True