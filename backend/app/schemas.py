from datetime import date, datetime
from typing import Optional, List

from pydantic import BaseModel, Field



class UserCreate(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=120
    )


    code: str = Field(
        ...,
        min_length=2,
        max_length=50
    )


    role: str = Field(
        default="student",
        max_length=50
    )


    face_encoding: Optional[List[float]] = None


    image_base64: Optional[str] = None





class UserResponse(BaseModel):

    id:int

    name:str

    code:str

    role:str

    created_at:datetime


    class Config:

        from_attributes=True





class AttendanceRequest(BaseModel):

    image_base64:str

    lat:float

    lng:float

    code:Optional[str]=None





class AttendanceItem(BaseModel):

    id:int

    user_id:int

    name:str

    code:str

    role:str

    attendance_date:date

    created_at:datetime

    status:str

    lat:float

    lng:float

    distance_meters:Optional[float]=None
    
class EmotionResponse(BaseModel):

    emotion: str
    message: str