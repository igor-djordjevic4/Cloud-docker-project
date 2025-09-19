from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    name = Column(String, index = True)
    email = Column(String, unique= True, index = True)
    
    posts = relationship("Post", back_populates="user", cascade="all, delete")
    comments = relationship("Comment", back_populates="user", cascade="all,delete")   



    