from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.missions import MissionCreate, MissionUpdate
from app.services.missions import create_mission, delete_mission, update_target
from app.db.base import SessionLocal
from app.models.missions import Mission

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MissionCreate)
def create_mission_endpoint(mission: MissionCreate, db: Session = Depends(get_db)):
    return create_mission(db, mission)


@router.delete("/{mission_id}", status_code=204)
def delete_mission_endpoint(mission_id: int, db: Session = Depends(get_db)):
    if not delete_mission(db, mission_id):
        raise HTTPException(status_code=400, detail="Mission is assigned to a cat or not found")


@router.patch("/targets/{target_id}", response_model=MissionUpdate)
def update_target_endpoint(target_id: int, complete: bool, notes: Optional[str], mission_id: int,
                           db: Session = Depends(get_db)):
    try:
        return update_target(db, mission_id, target_id, complete, notes)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[MissionCreate])
def get_all_missions(db: Session = Depends(get_db)):
    missions = db.query(Mission).all()
    return missions


@router.get("/{mission_id}", response_model=MissionCreate)
def get_mission_by_id(mission_id: int, db: Session = Depends(get_db)):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission
