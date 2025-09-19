from typing import List, Optional
from fastapi import APIRouter, Form, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.comments import CommentCreate, CommentOut
from app.schemas.posts import PostCreate, PostOut
from app.schemas.users import UserCreate, UserOut
from app.services.comment_service import create_comment, get_comments_by_post_service, get_comments_by_user_service
from app.services.post_service import create_post, get_all_posts, get_posts_service, read_post
from app.services.user_service import create_user, get_user_by_id

router = APIRouter()

@router.post("/users", response_model = UserOut)
def create(user: UserCreate = Form(...), db: Session = Depends(get_db)):
    return create_user(user, db)

@router.get("/users/{user_id}", response_model = UserOut)
def read_user(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User is not found")
    else:
        return user
    
@router.post("/users/{user_id}/posts", response_model = PostOut) # Create post for specific user 
def create_post_for_user(user_id: int, post: PostCreate = Form(...), db: Session = Depends(get_db)):
    return create_post (user_id, post, db)
    

@router.get("/posts/{post_id}", response_model=PostOut)
def read_posts(post_id: int, db: Session = Depends(get_db)):
    post = read_post(post_id, db)
    if not post:
        raise HTTPException(status_code=404, detail= f"Post was not found {post_id}")
    return post

# GET /posts?user_id=1&title=hello    
@router.get("/posts", response_model=List[PostOut])
def get_posts(db: Session = Depends(get_db)):
    posts =  get_posts_service(db)
    
    if not posts:
        raise HTTPException(404)
    
    return posts
    
@router.get("/users/{user_id}/posts", response_model = List[PostOut] )
def get_all_posts_by_user(user_id: int, db:Session = Depends(get_db)):
    posts = get_all_posts(user_id, db)
    if not posts:
        raise HTTPException(status_code=404, detail="Posts for that user does not exist")
    return posts


@router.post("/posts/{post_id}/comments", response_model = CommentOut) 
def create_comment_for_post(post_id: int, user_id: int, comment: CommentCreate = Form(...), db: Session = Depends(get_db)):
    return create_comment(comment, db, post_id, user_id)

@router.get("/users/{user_id}/comments", response_model = List[CommentOut]) 
def get_comments_by_user(user_id: int, db: Session = Depends(get_db)):
    comments = get_comments_by_user_service(db, user_id)
    if not comments: 
        raise HTTPException(status_code=404, detail = f"Comments were not found for user {user_id}")
    return comments

@router.get("/posts/{post_id}/comments", response_model = List[CommentOut]) 
def get_comments_by_user(post_id: int, db: Session = Depends(get_db)):
    comments = get_comments_by_post_service(db, post_id)
    if not comments: 
        raise HTTPException(status_code=404, detail = f"Comments were not found for post {post_id}")
    return comments


