from sqlalchemy.orm import Session

from . import schemas
from memes_app.models.meme import Meme


def get_meme(db: Session, meme_id: int):
    return db.query(Meme).filter(Meme.id == meme_id).first()


def delete_meme(db: Session, meme_id: int):
    obj = db.query(Meme).filter(Meme.id == meme_id).first()
    db.delete(obj)
    db.commit()
    return obj


def get_memes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Meme).offset(skip).limit(limit).all()


def create_meme(db: Session, meme: schemas.MemeCreate, filename: str):
    db_meme = Meme(title=meme.title, image=filename)
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme


def update_meme(db: Session, meme_id: int, meme: schemas.MemeUpdate):
    db_meme = db.query(Meme).filter(Meme.id == meme_id).first()
    if not db_meme:
        return None

    update_data = meme.dict(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            setattr(db_meme, key, value)
    db.commit()
    db.refresh(db_meme)
    return db_meme
