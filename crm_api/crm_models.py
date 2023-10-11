from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, DateTime, Float, VARCHAR, func
# from .database import Base 


class FormSubmission(): #base
    __tablename__ = 'form_submissions'

    id = Column(BigInteger, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    company = Column(String)
    email = Column(String)
    phonenumber = Column(String)
    interest = Column(String)
    message = Column(String)
