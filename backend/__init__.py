from flask import Flask
from os import path
from flask_login import LoginManager
from .database.models import db
#from ..config import Config_dev  ##maybe move config file to same directory?



DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:BraianNico11@localhost/PetApp'
    db.init_app(app)

    from .general.views import views
    from .auth.auth import auth
    from .api.api import api_petfinder

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    #app.register_blueprint(api_petfinder, url_prefix='/')

    from .database.models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
