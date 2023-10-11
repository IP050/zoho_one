from pydantic import BaseModel, Field 
from typing import Optional 


class FormSubmissionCreate(BaseModel):
    firstname: str
    lastname: str
    company: str
    email: str
    phonenumber: str
    interest: str
    message: Optional[str] = None 
