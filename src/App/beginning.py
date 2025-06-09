from flask import render_template, Blueprint

beginning_bp = Blueprint('beginning', __name__)

@beginning_bp.route('/')
def index():
    return render_template('index.html') 

