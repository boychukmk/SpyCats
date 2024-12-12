from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.targets import TargetBase
from app.services.targets import create_target, update_target
from app.db.base import SessionLocal
from app.models.targets import Target

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=TargetBase)
def create_target_endpoint(target: TargetBase, mission_id: int, db: Session = Depends(get_db)):
    return create_target(db, target, mission_id)


@router.patch("/{target_id}", response_model=TargetBase)
def update_target_endpoint(target_id: int, complete: bool, notes: Optional[str], db: Session = Depends(get_db)):
    return update_target(db, target_id, complete, notes)


@router.get("/", response_model=list[TargetBase])
def get_all_targets(db: Session = Depends(get_db)):
    targets = db.query(Target).all()
    return targets


@router.get("/{target_id}", response_model=TargetBase)
def get_target_by_id(target_id: int, db: Session = Depends(get_db)):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    return target


@router.delete("/{target_id}", status_code=204)
def delete_target_endpoint(target_id: int, db: Session = Depends(get_db)):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")

    db.delete(target)
    db.commit()
    return {"message": "Target deleted successfully"}
