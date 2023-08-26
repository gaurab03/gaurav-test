from sqlalchemy import Column, Integer, String, DateTime
from core.database.database import Base, engine 

def create_table():
    Base.metadata.create_all(engine)

class UserCanonicaView(Base):
    __table_args__ = {"schema":"flash_learn"}
    __tablename__ = "mvw_user_info" 

    device_id = Column(String(100),nullable=False)
    device_activate_dt = Column(DateTime)
    device_status = Column(String(15),nullable=False)
    license_start_date = Column(DateTime)
    license_end_date = Column(DateTime)
    license_status = Column(String(15),nullable=False)
    license_comments = Column(String(100),nullable=False)
    last_login_date = Column(DateTime)
    login_status = Column(String(15),nullable=False)
    user_id = Column(Integer,nullable=False)
    first_name = Column(String(50),nullable=False)
    last_name = Column(String(50),nullable=False)
    salutation_id = Column(Integer,nullable=False)
    country_id = Column(Integer,nullable=False)
    mobile_no = Column(String(15),nullable=False,primary_key=True)
    email_id = Column(String(100),nullable=False)
    ip_address = Column(String(30),nullable=False)
    gender_id = Column(Integer,nullable=False)
    reg_date = Column(DateTime)
    reg_device_id = Column(String(30),nullable=False)
    device_details = Column(String(50),nullable=False)
    mbl_otp_valid = Column(Integer,nullable=False)
    email_otp_valid = Column(Integer,nullable=False)










