# CRM API

## Description

This folder contains a setup using postgres, fastapi and zoho's api to keep control over your forms, the entries in your database and still send them to zoho after. 

- Additional an example dockerfile. I use it with docker > azure containerapps and connect the containerapp api to my webapp. 

**What do I need to use this** 

- A zoho CRM account 
- CRM API client_id and client_id, the auth flow in crm_api.py covers the refresh + auth tokens

**When / why to use this** 

- You want to control whatever happens to your forms first, but capture the leads in zoho after
- You don't want unecesarry scripts on your webapp
- You don't want to host a zoho form
- You don't want to embed a zoho form

**I don't want to use docker** 

```
python -m pip install -r requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3500"]
```

