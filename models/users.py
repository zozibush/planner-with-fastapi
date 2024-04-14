from sqlmodel import JSON, SQLModel, Field, Column
from pydantic import EmailStr
from typing import Optional, List
from models.events import Event

class User(SQLModel, table=True):
    email: EmailStr = Field(default=None, primary_key=True)
    password: str
    events: Optional[List[Event]] = Field(sa_column=Column(JSON))

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }

class UserSignIn(SQLModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }