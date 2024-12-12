from pydantic import BaseModel
from typing import List, Optional


class TargetBase(BaseModel):
    name: str
    country: str
    notes: Optional[str] = None
    complete: bool = False

    class Config:
        orm_mode = True


class MissionCreate(BaseModel):
    name: str
    cat_id: Optional[int] = None
    targets: List[TargetBase]

    class Config:
        orm_mode = True


class MissionUpdate(BaseModel):
    name: Optional[str] = None
    cat_id: Optional[int] = None
    complete: Optional[bool] = None
    targets: Optional[List[TargetBase]] = None

    class Config:
        orm_mode = True
