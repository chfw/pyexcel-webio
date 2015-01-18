from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column , Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker

engine=create_engine("sqlite:///tmp.db")
Base=declarative_base()

class Signature(Base):
    __tablename__="signature"
    X=Column(Integer, primary_key=True)
    Y=Column(Integer)
    Z=Column(Integer)

class Signature2(Base):
    __tablename__="signature2"
    A=Column(Integer, primary_key=True)
    B=Column(Integer)
    C=Column(Integer)
    
Session=sessionmaker(bind=engine)

