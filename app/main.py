from fastapi import FastAPI
from app.db.base import Base, engine
from app.routers import cats, missions, targets


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Spy Cat Agency",
    description="A management system for spy cats, missions, and targets",
    version="1.0.0",
)

app.include_router(cats.router, prefix="/cats", tags=["Cats"])
app.include_router(missions.router, prefix="/missions", tags=["Missions"])

app.include_router(targets.router, prefix="/targets", tags=["targets"])


@app.get("/")
def root():
    return {"message": "Welcome to the Spy Cat Agency!"}
