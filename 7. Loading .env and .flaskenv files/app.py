"""
This is a boilerplate for a web application in Flask showing how to
store global variables in a .env file and retreiving them with the dotenv
package.

Make sure to first install python-dotenv in the console with:
    
    'pip install python-dotenv'

"""

from flask import Flask

app = Flask(__name__)

# Loads environment variables from config.py instead of hard coding them
# with app.config[SECRET_KEY]="VerySecretKey"
app.config.from_pyfile('config.py') 

@app.route('/')
def hello_config():
    return f'Secret key: {app.config['SECRET_KEY']}!'

if __name__ == '__main__':
    app.run()
    