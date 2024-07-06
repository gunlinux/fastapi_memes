from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile


class MemeBase(BaseModel):
    pass


class MemeCreate(MemeBase):
    title: str


class MemeUpdate(MemeBase):
    is_active: Optional[bool] = None
    title: Optional[str] = None

class Meme(MemeBase):
    id: int
    is_active: bool = True
    image: str
    title: str

    class Config:
        orm_mode = True
