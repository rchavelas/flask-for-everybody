"""
This is a boilerplate for using application factories within Flask.

If the factory is called create_app, flask automatically knows how to
run it, so it is possible to run the application with the standard command:

    'flask run --debug'

"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello, World'

    return app
