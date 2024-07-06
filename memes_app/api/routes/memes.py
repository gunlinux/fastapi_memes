from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session

import memes_app.schemas as schemas
import memes_app.crud as crud
from memes_app.api.deps import get_db


router = APIRouter()


@router.get("/", response_model=list[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes


@router.get("/{id}", response_model=schemas.Meme)
def read_meme(id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@router.post("/", response_model=schemas.Meme)
def create_meme(
    file: UploadFile,
    title: str = Form(...),
    db: Session = Depends(get_db),
):
    meme_data = schemas.MemeCreate(title=title)
    print("Received file:", file.filename)
    return crud.create_meme(db=db, meme=meme_data, filename=file.filename)


@router.delete("/{id}", response_model=schemas.Meme)
def delete_meme(id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return crud.delete_meme(db, meme_id=id)


@router.put("/{id}", response_model=schemas.Meme)
def update_meme(id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id=id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return crud.update_meme(db, meme_id=id, meme=meme)
