from fastapi import FastAPI
from app.routes.routes import router as api_router
from app.db.database import engine,Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="My Fast Api Project")

@app.get("/")
def health():
    return {"status": "ok"}

app.include_router(api_router)
