from sqlalchemy.orm import Session
from fastapi import HTTPException, requests
from app.models.comment import Comment
from app.models.post import Post
from app.models.user import User
from app.schemas.comments import CommentCreate


def create_comment(comment: CommentCreate, db: Session, post_id: int, user_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Check if user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Create the comment
    new_comment = Comment(content=comment.content, post_id=post.id, user_id=user.id)
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment
    

def get_comments_by_post_service(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def get_comments_by_user_service(db: Session, user_id: int):
    return db.query(Comment).filter(Comment.user_id == user_id).all()
