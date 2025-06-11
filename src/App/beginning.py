from flask import Blueprint, render_template, request
from .api_request import check_email_breach

beginning_bp = Blueprint('beginning', __name__)

@beginning_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            breach_data = check_email_breach(user_input)
            print("DEBUG breach_data:", breach_data)  # Debug output for development

            # Handle no data or empty breach list
            if not breach_data or (isinstance(breach_data, list) and len(breach_data) == 0):
                return render_template('alert.html', email=user_input)

            # Optionally handle API messages, if your API could send a dict with a message key
            if isinstance(breach_data, dict) and breach_data.get("message") in ["No breach found", "Too many requests"]:
                return render_template('alert.html', email=user_input)

            
            # If breaches found, show results page
            return render_template('result.html', email=user_input, breach_data=breach_data)

    # For GET request or no POST data, show the input form page
    return render_template('index.html')
