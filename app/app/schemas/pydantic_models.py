from pydantic import BaseModel
from datetime import datetime

class UserRequest(BaseModel):
    text: str
    
    
class UserResponse(BaseModel):
    text: str
    questions: str
    

    class Config:
            orm_mode = True 


class ScreeningResponse(BaseModel):
    id: int
    text: str
    questions: str
    created_at: datetime

    class Config:
        orm_mode = True