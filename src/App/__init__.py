from flask import Flask
from .beginning import beginning_bp

# Flask will look relative to current working dir (no base_dir needed)
app = Flask(__name__)

app.register_blueprint(beginning_bp)
