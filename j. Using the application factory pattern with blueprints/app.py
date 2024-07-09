"""
This is a boilerplate for registering blueprints in flask applications

"""

from flask import Flask
from bp import my_blueprint

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World'

    app.register_blueprint(my_blueprint)    

    # You can validate current views with:
    print(app.url_map)

    return app
