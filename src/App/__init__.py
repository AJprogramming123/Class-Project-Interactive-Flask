from flask import Flask, render_template
from App.beginning import beginning_bp
import os

# 🔧 Define the base directory relative to this file
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# ✅ Explicitly tell Flask where to find static and templates
app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)

# ✅ Register your blueprint(s)
app.register_blueprint(beginning_bp)
