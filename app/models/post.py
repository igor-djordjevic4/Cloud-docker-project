from datetime import datetime
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key = True, index = True)
    content = Column(String, nullable = False)
    title = Column(String, nullable = False)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="posts", cascade="all,delete")   

    