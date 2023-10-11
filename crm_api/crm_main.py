from fastapi import FastAPI, HTTPException, Depends, Security
from .crm_api import ZohoJPS
import os 


CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN")

zohoclient = ZohoJPS(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

app = FastAPI()
