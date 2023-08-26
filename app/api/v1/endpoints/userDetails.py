from fastapi import APIRouter, status, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session
from core.database.database import SessionLocal
from models.models import UserCanonicaView 

router = APIRouter()

# Dependency to get the database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def read_root():
    return {"message": "Welcome to flashLearnAPI!"}

@router.get("/user_details_canonicalView/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_details(user_id:int, db: Session = Depends(get_db)):

    user_details_canoicalView = db.query(UserCanonicaView).filter(UserCanonicaView.user_id == user_id).first()
    if user_details_canoicalView is None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Student with this id cannot be found")
    
    user_details = {
        "User_id": user_details_canoicalView.user_id,
        "Mobile_no": user_details_canoicalView.mobile_no,

        "Device_id_latest": user_details_canoicalView.device_id,#toVerify

        "Last_login_date": user_details_canoicalView.last_login_date,

        "First_name": user_details_canoicalView.first_name,
        "Last_name": user_details_canoicalView.last_name,
        "Salutation_id": user_details_canoicalView.salutation_id,
        "Gender_id": user_details_canoicalView.gender_id,
        "Email_id": user_details_canoicalView.email_id,

        "Course_id": 121, #toVerify

        "Subjects":["Botany", "Physics", "Chemistry"]
       } 
    
    return user_details






    

