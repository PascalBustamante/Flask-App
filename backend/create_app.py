from flask import Flask
from flask_jwt_extended import JWTManager
from os import path
from flask_login import LoginManager
from database.models import db, User, Event
#from ..config import Config_dev  ##maybe move config file to same directory?



DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config["JWT_SECRET_KEY"] = "super-secret" 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:BraianNico11@localhost/PetApp'
    db.init_app(app)
    jwt = JWTManager(app)

    from general.views import views
    from auth.auth import auth 
    from api.api import api_petfinder
    from database.views import database

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(database, url_prefix='/')
    #app.register_blueprint(api_petfinder, url_prefix='/')

    with app.app_context():
        db.create_all()
        #db.reflect()    #no idea what it does


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
