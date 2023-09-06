from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from models.user import db
from flask_cors import CORS
from flask_migrate import Migrate
from .config import get_config


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, resources={r"/auth/*"})
    app.config.from_object(get_config(config_name))
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["JWT_SECRET_KEY"] = "super-secret"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "postgresql://postgres:BraianNico11@localhost/PetApp"

    db.init_app(app)
    JWTManager(app)
    Bcrypt(app)
    Migrate(app, db)

    from api.auth.auth import auth
    from api import api_bp

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app
