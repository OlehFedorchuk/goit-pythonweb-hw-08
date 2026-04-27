from fastapi import FastAPI
from app.database import Base, engine
from app.routes.contacts import router as contacts_router

app = FastAPI(title="Contacts API")

Base.metadata.create_all(bind=engine)

app.include_router(contacts_router)