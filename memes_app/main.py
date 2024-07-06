from fastapi import FastAPI
from memes_app.api.routes import memes
from memes_app.core.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(memes.router, prefix='/memes', tags=["memes"])
