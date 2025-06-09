from flask import Flask, render_template
from App.beginning import beginning_bp
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))
app.register_blueprint(beginning_bp)




