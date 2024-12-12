from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.services.cats import (
    create_spy_cat, get_spy_cat, list_spy_cats, update_spy_cat, delete_spy_cat
)
from app.schemas.cats import SpyCatCreate, SpyCatResponse, SpyCatUpdate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SpyCatResponse)
def create_cat(cat: SpyCatCreate, db: Session = Depends(get_db)):
    return create_spy_cat(db, cat)


@router.get("/", response_model=list[SpyCatResponse])
def list_cats(db: Session = Depends(get_db)):
    return list_spy_cats(db)


@router.get("/{cat_id}", response_model=SpyCatResponse)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    cat = get_spy_cat(db, cat_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Spy Cat not found")
    return cat


@router.patch("/{cat_id}", response_model=SpyCatResponse)
def update_cat(cat_id: int, updates: SpyCatUpdate, db: Session = Depends(get_db)):
    cat = update_spy_cat(db, cat_id, updates)
    if not cat:
        raise HTTPException(status_code=404, detail="Spy Cat not found")
    return cat


@router.delete("/{cat_id}", status_code=204)
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    if not delete_spy_cat(db, cat_id):
        raise HTTPException(status_code=404, detail="Spy Cat not found")
