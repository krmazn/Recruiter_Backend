from pydantic import BaseModel
from datetime import datetime

class UserRequest(BaseModel):
    text: str
    
    
class UserResponse(BaseModel):
    text: str
    questions: str
    

    class Config:
            orm_mode = True 