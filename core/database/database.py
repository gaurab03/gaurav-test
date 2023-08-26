from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus 

username = "gaurab"
password = "gaurab@123"
hostname = "fl-ds-instance-dev.caz3rblbkur8.ap-south-1.rds.amazonaws.com" 

encoded_username = quote_plus(username)
encoded_password = quote_plus(password)
encoded_hostname = quote_plus(hostname) 

connection_url = f"postgresql://{encoded_username}:{encoded_password}@{encoded_hostname}/flash_learn_dev"

engine = create_engine(connection_url)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
        
