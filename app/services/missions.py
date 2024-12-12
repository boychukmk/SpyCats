from typing import Optional

from sqlalchemy.orm import Session
from app.models.missions import Mission
from app.schemas.missions import MissionCreate
from app.models.targets import Target


def create_mission(db: Session, mission: MissionCreate):
    new_mission = Mission(name=mission.name, cat_id=mission.cat_id)
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)

    for target_data in mission.targets:
        target = Target(**target_data.dict(), mission_id=new_mission.id)
        db.add(target)

    db.commit()
    db.refresh(new_mission)
    return new_mission


def delete_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission:
        return False
    if mission.cat_id is not None:
        return False  # Невозможно удалить, если миссия привязана к коту

    db.delete(mission)
    db.commit()
    return True


def update_target(db: Session, mission_id: int, target_id: int, complete: bool, notes: Optional[str]):
    target = db.query(Target).filter(Target.id == target_id, Target.mission_id == mission_id).first()
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
