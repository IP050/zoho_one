from fastapi import FastAPI, HTTPException, Depends, Security
from .crm_schemas import FormSubmissionCreate
from .crm_api import ZohoJPS
import traceback
import os 


CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN")

zohoclient = ZohoJPS(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

app = FastAPI()


@app.post("/submit-form/")
async def post_form_endpoint(form_data: FormSubmissionCreate):
    try: 
        zohoclient.post_leads(form_data)
        return {"message": "Success"}
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
