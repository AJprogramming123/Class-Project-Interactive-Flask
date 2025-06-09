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
    return response.json()