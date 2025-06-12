from flask import Blueprint, render_template, request
from .api_request import check_email_breach
import re

beginning_bp = Blueprint('beginning', __name__)

# Basic regex for validating email format
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'





@beginning_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input') #from -index.html-

        # Check if input is not empty and looks like an email
        if user_input and re.match(email_regex, user_input): #re.match() is a method used in the package 're' purpose is to used to match values to make sure its allowed from different variables
            breach_data = check_email_breach(user_input)

            print("\nDEBUG breach_data: ", breach_data)  # checks if the output is accurate! If not this helps figure out why
            print()

            
    #--------Check for data retrieval--------#
            # Handle no data or empty breach list
            if not breach_data or (isinstance(breach_data, list) and len(breach_data) == 0): #A built-in Python function used to check the type of a variable
                return render_template('alert.html', email=f"No breach information found for {user_input}") #A pop up saying no!

            # If breaches found, show results page
            return render_template('result.html', email=user_input, breach_data=breach_data)


        else:
            # Invalid email format
            return render_template('alert.html', email="Invalid email format. Please use a proper email")
    
    # For GET request or no POST data, show the input form page
    return render_template('index.html')


'''
So 3 things are being set up:
 - the email better follow the regex
 - It gotta actually be an email found in the api database
 - It gotta be a proper email format

'''