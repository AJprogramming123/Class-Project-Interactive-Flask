from flask import Flask
from .beginning import beginning_bp
# Flask will look relative to current working dir (no base_dir needed)


def create_app():
    app = Flask(
        __name__, 
        template_folder='../../frontend/templates', 
        static_folder='../../frontend/static'
    )

    app.register_blueprint(beginning_bp)

    return app

#"Heres the fully created and configured Flask application instance for you to run or import"
