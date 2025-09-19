from app.db.database import Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key= True, index=True)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    posts = relationship("Post", back_populates="comments")   
    user = relationship("User", back_populates="comments")   

    