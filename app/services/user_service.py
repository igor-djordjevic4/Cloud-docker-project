from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.users import UserCreate

def create_user(user: UserCreate, db:Session):
    new_user = User(name = user.name, email = user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()