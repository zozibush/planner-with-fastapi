from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session
from models.users import User, UserSignIn
from typing import List
from sqlmodel import select

user_router = APIRouter(
    tags=["User"],
)
users = {}

@user_router.post("/signup")
async def sign_new_user(data: User, session=Depends(get_session)) -> dict:
    event = session.get(User, data.email)
    if event:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied email exists"
        )
    session.add(data)
    session.commit()
    session.refresh(data)

    return{
        "message":"User successfully registered!"
    }

@user_router.post("/signin")
async def sing_user_in(user: UserSignIn, session=Depends(get_session)) -> dict:
    info = session.get(User, user.email)

    if user.email != info.email:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exists"
        )
    if user.password != info.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    return{
        "message":"User signed in successfully."
    }