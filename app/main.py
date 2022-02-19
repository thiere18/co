from fastapi import FastAPI
from app.api_v1.routers import role, auth, user
from app.config import models
from app.config.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def test():
    return {"status": "ok"}


app.include_router(role.router)
app.include_router(auth.router)
app.include_router(user.router)
