import requests
import json
from .crm_models import FormSubmissionCreate

class ZohoJPS:
    def __init__(self, clientid, clientsecret, refreshtoken):
        self.clientid = clientid
        self.clientsecret = clientsecret
        self.authtoken = ""
        self.refreshtoken = refreshtoken
        
    def refresh_tokens(self):
        url = "https://accounts.zoho.eu/oauth/v2/token"
        data = {
            'client_id': self.clientid,
            'client_secret': self.clientsecret,
            'refresh_token': self.refreshtoken,
            'grant_type': 'refresh_token',
        }
        r = requests.post(url, data=data)
        if r.status_code == 200:
            tokens = r.json()
            self.authtoken = tokens['access_token']
            # Only update refresh_token if a new one is provided
            if 'refresh_token' in tokens:
                self.refreshtoken = tokens['refresh_token']
            tokens['refresh_token'] = self.refreshtoken  # ensure refresh_token is always present in saved data
        else:
            raise Exception(f"Error refreshing tokens: {r.status_code}, {r.text}")
        
    def get_leads(self):
        self.refresh_tokens()  # refresh the tokens before making the request
        url = "https://www.zohoapis.eu/crm/v5/Leads?fields=Last_Name,Company,Email,Phone,"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.authtoken}',
        }
        print(headers)
        print(self.authtoken)
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(f"Error getting orgs: {r.status_code}, {r.text}")

    def post_leads(self, data: FormSubmissionCreate):
        self.refresh_tokens()
        url = 'https://www.zohoapis.eu/crm/v5/Leads'
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.authtoken}'
        }
        payload = json.dumps({
           "data": [
        {
            "Lead_Source": "Website",
            "Company": data.company,
            "Last_Name": data.lastname,
            "First_Name": data.firstname,
            "Email": data.email,
            "Phone": data.phonenumber,
            "Lead_Status": "Not Contacted",
            "Description" : data.interest
        }   ]  
}
)
        r = requests.request("POST", url, headers=headers, data=payload)
        if r.status_code == 201:
            return r.json()
        else:
            raise Exception(f"Error posting leads: {r}")
