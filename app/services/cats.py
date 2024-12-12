from typing import List, Type

import requests
from sqlalchemy.orm import Session
from app.models.cats import SpyCat
from app.schemas.cats import SpyCatCreate, SpyCatUpdate


def create_spy_cat(db: Session, spy_cat: SpyCatCreate) -> SpyCat:
    valid_breeds = get_valid_breeds_from_thecatapi()
    if spy_cat.breed not in valid_breeds:
        raise ValueError(f"Invalid breed: {spy_cat.breed}. Please choose a valid breed from TheCatAPI.")

    new_cat = SpyCat(**spy_cat.model_dump())
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat


def get_valid_breeds_from_thecatapi():
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    breeds = [breed["name"] for breed in response.json()]
    return breeds


def get_spy_cat(db: Session, cat_id: int) -> SpyCat | None:
    return db.query(SpyCat).filter(SpyCat.id == cat_id).first()


def list_spy_cats(db: Session) -> list[Type[SpyCat]]:
    return db.query(SpyCat).all()


def update_spy_cat(db: Session, cat_id: int, updates: SpyCatUpdate) -> SpyCat | None:
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not cat:
        return None
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(cat, key, value)
    db.commit()
    db.refresh(cat)
    return cat


def delete_spy_cat(db: Session, cat_id: int) -> bool:
    cat = db.query(SpyCat).filter(SpyCat.id == cat_id).first()
    if not cat:
        return False
    db.delete(cat)
    db.commit()
    return True