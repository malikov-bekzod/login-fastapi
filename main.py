from fastapi import FastAPI
from database.database import engine
from database.database import Base
from auth import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)



