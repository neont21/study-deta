from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from ..database import db

class User(BaseModel):
    name: str
    age: int
    hometown: str
    key: Optional[str] = None

router = APIRouter(prefix='/users', tags=['users'])

@router.post('', status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if user.key is None:
        del(user.key)
    created = db.put(user.dict())
    return created

@router.get('', response_model=User)
def get_user(key: str):
    user = db.get(key)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found')
    return user

@router.put('/{key}', response_model=User)
def update_user(key: str, user: User):
    user.key = key
    updated = db.put(user.dict())
    return updated 

@router.delete('/{key}')
def delete_user(key: str):
    db.delete(key)
