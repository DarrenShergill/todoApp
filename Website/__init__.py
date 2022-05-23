from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

db = SQLAlchemy()
DB_NAME = "database.db"

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "fjnakjqijd"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    #import the classes we use
    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    # where do we need to go if we are not logged in? where flasks redirects if user is not logged in and log in is required
    login_manager.login_view = "auth.login"
    # telling login manager which app we are using
    login_manager.init_app(app)

    #@decorator here is saying to use this function to load the user
    @login_manager.user_loader
    def load_user(id):
        # telling flask how we load a user. By default get looks for the primary key.
        return User.query.get(int(id))

    return app

def create_database(app):
    #use path module to check if database exists
    if not path.exists("website/" + DB_NAME):
    #if it doesn't exist, we create it. the reason we pass app is to tell sqlalchemy which app to create database for
        db.create_all(app=app)
        print(("Created Database!"))