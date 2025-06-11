from dotenv import load_dotenv
import os
import requests

load_dotenv()
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

def check_email_breach(email):
    url = f"https://email-breach-search.p.rapidapi.com/rapidapi/search-email/{email}"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "email-breach-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    raw_data = response.json()
    if not raw_data or 'message' in raw_data:
        return None

    processed_breaches = []

    for breach in raw_data:
        # Extract fields (which seem to be indexed keys like '0', '1', etc.)
        compromised_fields = []

        # The fields are numeric keys as strings — filter them
        for key, value in breach.items():
            if key.isdigit():  # Only these keys hold field info
                compromised_fields.append({
                    "field": value.get("field"),
                    "label": value.get("label"),
                    "fa_icon": value.get("fa_icon"),
                    "sensitive": value.get("sensitive", False),
                    "value": value.get("value"),
                    "found": value.get("found"),
                    "id": value.get("id")
                })

        processed_breaches.append({
            "name": breach.get("name"),
            "breach_date": breach.get("breach_date"),
            "upload_date": breach.get("upload_date"),
            "rows": breach.get("rows"),
            "summary": breach.get("summary"),
            "hibp_id": breach.get("hibp_id"),
            "icon": breach.get("icon"),
            "compromised_fields": compromised_fields
        })

    return processed_breaches
