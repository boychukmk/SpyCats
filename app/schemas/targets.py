from pydantic import BaseModel
from typing import Optional


class TargetBase(BaseModel):
    id: int
    name: str
    country: str
    notes: Optional[str] = None
    complete: bool = False

    class Config:
        orm_mode = True
