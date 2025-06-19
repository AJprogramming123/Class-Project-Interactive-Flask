import os
from flask import Flask
from .beginning import beginning_bp
# Flask will look relative to current working dir (no base_dir needed)


def create_app():
    # Absolute path to the frontend directory (two levels up from current file)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend'))
    template_folder = os.path.join(base_dir, 'templates')
    static_folder = os.path.join(base_dir, 'static')

    app = Flask(
        __name__,
        template_folder=template_folder,
        static_folder=static_folder
    )

    app.register_blueprint(beginning_bp)
    return app
#"Heres the fully created and configured Flask application instance for you to run or import"
