from flask import Blueprint, render_template, request, redirect, url_for

from .api_request import check_email_breach  # relative import

beginning_bp = Blueprint('beginning', __name__)

@beginning_bp.route('/result/<email>')
def result(email):
    breach_data = check_email_breach(email)
    return render_template('result.html', email=email, breach_data=breach_data)

@beginning_bp.route('/alert/<email>')
def alert(email):
    return render_template('alert.html', email=email)

@beginning_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            breach_data = check_email_breach(user_input)
            if not breach_data or breach_data.get("message") == "Too many requests":
                return redirect(url_for('beginning.alert', email=user_input))
            return redirect(url_for('beginning.result', email=user_input))
    return render_template('index.html')

