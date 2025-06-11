from flask import Blueprint, render_template, request
from .api_request import check_email_breach
import re

beginning_bp = Blueprint('beginning', __name__)

# Basic regex for validating email format
email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

@beginning_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # Check if input is not empty and looks like an email
        if user_input and re.match(email_regex, user_input):
            breach_data = check_email_breach(user_input)
            print("DEBUG breach_data:", breach_data)  # Debug output for development

            # Handle no data or empty breach list
            if not breach_data or (isinstance(breach_data, list) and len(breach_data) == 0):
                return render_template('alert.html', email=user_input)

            # If breaches found, show results page
            return render_template('result.html', email=user_input, breach_data=breach_data)
        else:
            # Invalid email format
            return render_template('alert.html', email="Invalid email format. Please use a proper email atleast")
    
    # For GET request or no POST data, show the input form page
    return render_template('index.html')
