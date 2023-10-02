from flask import Flask, current_app
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate


from flask_sqlalchemy import SQLAlchemy


from config import get_config
from database.database import DatabaseManager


db_manager = DatabaseManager()


def create_app(config_name):
    app = Flask(__name__)
    CORS(app, resources={r"/auth/*"})
    app.config.from_object(get_config(config_name))
    app.config["SECRET_KEY"] = "hjshjhdjah kjshkjdhjs"
    app.config["JWT_SECRET_KEY"] = "super-secret"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "postgresql://postgres:BraianNico11@localhost/PetApp"

    db_manager.init_app(app)
    print(db_manager)
    JWTManager(app)
    Bcrypt(app)
    Migrate(app, db_manager)

    from api.auth.auth import auth
    from api import api_bp

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(api_bp)

    with app.app_context():
        db_manager.create_all()
        current_app.db = db_manager
        print(current_app.db, db_manager)
    return app
