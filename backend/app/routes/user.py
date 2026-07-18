from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models
from app.database import get_db


router = APIRouter(
    tags=["Users"]
)



@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(
        models.User
    ).all()


    return [

        {

            "id": user.id,

            "name": user.name,

            "code": user.code,

            "role": user.role

        }

        for user in users

    ]