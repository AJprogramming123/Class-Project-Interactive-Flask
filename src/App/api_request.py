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
    decoded = html.unescape(raw_desc) #This actually converts these **entities** into their actual characters so the text is easier to read. 

    # Remove any HTML tags (if any)
    clean_text = re.sub(r'<.*?>', '', decoded)
    '''
    <.*> if for greedy matching (It will legit remove the setence between the <> tags)
    <.*?> its called lazy matching it leave the text behind but remove the tags itself making it easy and most usable
    '''
    # Replaces multiple spaces/newlines left from removing the HTML texts with a single space, strip edges
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text
#----------------------------------------------------------------------------------#



def check_email_breach(email): # [Test 1] through pytest to test my logic
    url = f"https://email-breach-search.p.rapidapi.com/rapidapi/search-email/{email}"
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "email-breach-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)


#If it returns None then something is wrong with the API itself [Test 2]
    if response.status_code != 200:
        return None
    raw_data = response.json() #It's json formatted for communication between the API
    
    if not raw_data or 'message' in raw_data:
        return None


#------------------------------------------------------------------------------------#
    processed_breaches = [] # summary: add one dictionary per breach into this list

    for breach in raw_data: #It gives the entire result and then from clean_summary the raw data becomes filtered out from there the most important part processed append to get what I want
        clean_summary = clean_description(breach.get("summary"))

 #In Python, you can keep updating a list as the loop runs. Every time the loop runs once, it appends one new item. That's how i know this is possible
        processed_breaches.append({ 
            "name": breach.get("name"),
            "breach_date": breach.get("breach_date"),
            "rows": breach.get("rows"),
            "summary": clean_summary,
            "icon": breach.get("icon") 
        })

    return processed_breaches

#I only really wanted 5 things from this API: Name, rows affected, summary, date, png image of the place that was breached


''' For Up top 
it adds a new item to the same list in memory without needing to re-declare or rebuild it. 
Unlike Java that used ArrayList if i wanted to do something similar its static requires one datatype unlike python which is why a for loop adding is possible and using any type of datatype
'''

'''

Example from the API itself to know its key and values names:

0:
id:"mathway.com-2020"
found:0:
field:"email"
value:"jaimesandres2011@gmail.com"
label:"Email"
fa_icon:"envelope"
sensitive:true
    1:
    field:"facebook"
    label:"Facebook ID"
    fa_icon:"facebook"
    sensitive:false
    2:
    field:"full_name"
    label:"Name"
    fa_icon:"user"
    sensitive:false
    breach_date:"2020-01-13T00:00:00.000Z"
    upload_date:"2024-12-01T00:00:00.000Z"
    name:"Mathway"
    rows:25695755
    summary:"In January 2020, Mathway experienced a data breach that exposed user records, which were later sold on a dark web marketplace."
    hibp_id:"Mathway"
    icon:"https://databreach.com/sites/mathway.com-2020.svg"

'''