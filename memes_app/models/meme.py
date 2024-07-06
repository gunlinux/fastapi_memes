from sqlalchemy import Boolean, Column, Integer, String

from memes_app.core.database import Base


class Meme(Base):
    __tablename__ = "memes"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, index=True)
    image = Column(String, unique=True, index=True)
