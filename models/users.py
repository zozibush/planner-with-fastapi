from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List
from models.events import Event

class User(SQLModel, table=True):
    email: str = Field(default=None, primary_key=True)
    password: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }

class UserSignIn(SQLModel):
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!"
            }
        }