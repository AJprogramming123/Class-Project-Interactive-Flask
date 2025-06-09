from flask import render_template, Blueprint, request

beginning_bp = Blueprint('beginning', __name__)

@beginning_bp.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
    return render_template('index.html', user_input=user_input)