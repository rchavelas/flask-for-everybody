"""
This is a boilerplate for doing a very simple session management app using 
Flask-Login and Flask-SQLAlchemy.

Make sure to first install Flask-Login and Flask-SQLAlchemy in the console 
with:
    
    'pip install flask-login flask-sqlalchemy'

For a more traditional tutorial regarding the use of this packages see:
 - https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-5-creating-user-models
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = 'db.sqlite'
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'Very secret key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    # Registering blueprints
    from .auth import auth
    from .main import main
    app.register_blueprint(auth)
    app.register_blueprint(main)

    # Create db
    from .models import User
    create_database(app)

    # Initialize the login manager
    login_manager.init_app(app)
    @login_manager.user_loader
    def user_loader(id):
        return db.session.get(User,int(id))

    return app

def create_database(app):
    with app.app_context():
        if not os.path.exists(f'instance/{DB_NAME}'):
            db.create_all()
