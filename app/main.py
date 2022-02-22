from fastapi import FastAPI
from app.api_v1.routers import auth, user
from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "ok"}


# app.include_router(role.router)
app.include_router(auth.router)
app.include_router(user.router)
