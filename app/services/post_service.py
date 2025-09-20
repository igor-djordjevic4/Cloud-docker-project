from typing import Optional
from sqlalchemy.orm import Session
from app.models.post import Post
from app.models.user import User
from app.schemas.posts import PostCreate


def create_post(user_id: int, post: PostCreate, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
   
    new_post = Post(title = post.title, content = post.content, user_id = user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(f"Saved post: {new_post.id}, {new_post.title}, user_id={new_post.user_id}")
    
    return new_post

def read_post(post_id: int, db: Session):
    return db.query(Post).filter(Post.id == post_id).first()
    
def get_all_posts(user_id: int, db: Session):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_posts_service(user_id: Optional[int], title: Optional [str], db: Session):
    
    query = db.query(Post)
    
    if user_id:
        query = query.filter(Post.user_id == user_id)
    if title:
        query = query.filter(Post.title.ilike(f"%{title}%"))
        
    return query.all()
