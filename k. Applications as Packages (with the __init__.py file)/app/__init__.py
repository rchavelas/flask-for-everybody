"""
This is a boilerplate for building applications as packages, it provides certain
advantages such as allowing for a more modular approach to the app, as well as 
for installing the application as a package

For further reading, see the patterns section of the Flask docs here:
https://flask.palletsprojects.com/en/2.3.x/patterns/packages/

"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World'

    from .bp import my_blueprint
    app.register_blueprint(my_blueprint)

    return app
