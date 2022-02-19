from fastapi import FastAPI
from app.api_v1.routers import role, auth, user

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}


app.include_router(role.router)
app.include_router(auth.router)
app.include_router(user.router)
