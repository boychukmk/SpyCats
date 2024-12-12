from pydantic import BaseModel, Field, field_validator


class SpyCatBase(BaseModel):
    name: str
    years_of_experience: int = Field(..., gt=0, description='Years of experience ( not negative) ')
    breed: str
    salary: float = Field(..., gt=0, description='Salary in USD (positive) ')


class SpyCatCreate(SpyCatBase):
    pass


class SpyCatUpdate(SpyCatBase):
    salary: float = Field(..., gt=0, description='Salary in USD (positive) ')


class SpyCatInDB(SpyCatBase):
    id: int

    class Config:
        orm_mode = True


class SpyCatResponse(SpyCatBase):
    id: int
    name: str
    years_of_experience: int
    breed: str
    salary: float

    class Config:
        orm_mode = True
