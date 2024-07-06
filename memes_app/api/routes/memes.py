from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import memes_app.schemas as schemas
import memes_app.crud as crud
from memes_app.models.meme import Meme 
from memes_app.api.deps import get_db


router = APIRouter()

@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return {'ok'}
    #users = crud.get_users(db, skip=skip, limit=limit)
    #return users

'''
@router.post("/", response_model=schemas.Meme)
def create_meme(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    valid_user: schemas.UserCreate = Depends(verify_user_not_exists),
):
    return crud.create_user(db=db, user=valid_user)



@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    existing_user: User = Depends(get_user_by_id),
):
    return existing_user
'''
