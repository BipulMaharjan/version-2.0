from flask import Flask
from app.models.database import Database

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = "simple-secret-key"

    Database()  # Initialize database connection (currently not used)

    # Register blueprints
    from app.routes.auth import AuthRoutes

    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.register_routes())

    return app