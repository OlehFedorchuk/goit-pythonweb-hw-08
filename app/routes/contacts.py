from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
import app.crud as crud
import app.schemas as schemas
from app.schemas import ContactCreate, ContactResponse

router = APIRouter(prefix="/contacts", tags=["contacts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ContactResponse)
def create(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)


@router.get("/", response_model=list[schemas.ContactResponse])
def all(db: Session = Depends(get_db)):
    return crud.get_contacts(db)


@router.get("/search/")
def search(q: str, db: Session = Depends(get_db)):
    return crud.search(db, q)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact_by_id(db, contact_id)

    if contact is None:
        raise HTTPException(
            status_code=404,
            detail="Contact not found"
        )
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
def update_contact(
    contact_id: int,
    contact_data: ContactCreate,
    db: Session = Depends(get_db)
):
    contact = crud.update_contact(db, contact_id, contact_data)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.get("/birthdays/upcoming", response_model=list[ContactResponse])
def upcoming_birthdays(db: Session = Depends(get_db)):
    return crud.get_upcoming_birthdays(db)


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.delete_contact(db, contact_id)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}
