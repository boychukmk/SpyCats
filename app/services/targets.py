from typing import Optional

from sqlalchemy.orm import Session
from app.models.targets import Target
from app.schemas.targets import TargetBase


def create_target(db: Session, target: TargetBase, mission_id: int):
    new_target = Target(**target.dict(), mission_id=mission_id)
    db.add(new_target)
    db.commit()
    db.refresh(new_target)
    return new_target


def update_target(db: Session, target_id: int, complete: bool, notes: Optional[str]):
    target = db.query(Target).filter(Target.id == target_id).first()
    if not target:
        return None

    if target.complete:
        raise ValueError("Target is already completed. Notes cannot be updated.")

    target.complete = complete
    if notes:
        target.notes = notes

    db.commit()
    db.refresh(target)
    return target
