from dotenv import load_dotenv
import os
import requests
import html
import re

load_dotenv()
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')

def clean_description(raw_desc):
    if not raw_desc:
        return ""
    # Unescape HTML entities like &nbsp;
    decoded = html.unescape(raw_desc)
    # Remove any HTML tags (if any)
    clean_text = re.sub(r'<.*?>', '', decoded)
    # Replace multiple spaces/newlines with a single space, strip edges
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

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
        compromised_fields = []

        for key, value in breach.items():
            if key.isdigit():
                compromised_fields.append({
                    "field": value.get("field"),
                    "label": value.get("label"),
                    "fa_icon": value.get("fa_icon"),
                    "sensitive": value.get("sensitive", False),
                    "value": value.get("value"),
                    "found": value.get("found"),
                    "id": value.get("id")
                })

        #WHERE THE FILTER IS USEDDDDD
        clean_summary = clean_description(breach.get("summary"))

        processed_breaches.append({
            "name": breach.get("name"),
            "breach_date": breach.get("breach_date"),
            "upload_date": breach.get("upload_date"),
            "rows": breach.get("rows"),
            "summary": clean_summary,   # Use cleaned summary
            "hibp_id": breach.get("hibp_id"),
            "icon": breach.get("icon"),
            "compromised_fields": compromised_fields
        })

    return processed_breaches
