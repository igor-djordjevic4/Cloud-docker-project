from pydantic import BaseModel


class PostCreate(BaseModel):
    content: str
    title: str
    
class PostOut(BaseModel):
    id: int
    content: str
    title: str
    user_id: int    
    
    class Config:
        orm_model = True