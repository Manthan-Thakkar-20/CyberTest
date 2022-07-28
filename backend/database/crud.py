from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(models.User.email == email, models.User.password == password).first()

def create_user(db: Session, email: str, password: str):
    user = schemas.User(**{"email": email, "password": password})

    db_user = models.User(email = user.email, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
