from sqlalchemy.orm import Session
from app.models import Contact
from app.schemas import ContactCreate
from datetime import date, timedelta
from app.models import Contact

def create_contact(db: Session, contact: ContactCreate):
    obj = Contact(**contact.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_contacts(db: Session):
    return db.query(Contact).all()


def search(db: Session, q: str):
    return db.query(Contact).filter(
        (Contact.first_name.ilike(f"%{q}%")) |
        (Contact.last_name.ilike(f"%{q}%")) |
        (Contact.email.ilike(f"%{q}%"))
    ).all()


def update_contact(db: Session, contact_id: int, contact_data):

    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not contact:
        return None
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone = contact_data.phone
    contact.birthday = contact_data.birthday
    contact.additional_data = contact_data.additional_data

    db.commit()

    db.refresh(contact)

    return contact
def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(
        Contact.id == contact_id
    ).first()

def get_upcoming_birthdays(db: Session):
    today = date.today()
    next_week = today + timedelta(days=7)
    contacts = db.query(Contact).all()
    upcoming = []
    for contact in contacts:
        birthday_this_year = contact.birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1
            )
        if today <= birthday_this_year <= next_week:
            upcoming.append(contact)
    return upcoming

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()

    if contact:
        db.delete(contact)
        db.commit()

    return contact
