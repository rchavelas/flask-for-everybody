"""
This is a boilerplate for doing a basic session management using
the Flask-Login module along with sqlite3. 

Make sure to open a terminal and run 'python init_db.py' to initialize the 
database before running the application and make sure to first install 
Flask-Login in the terminal with:
    'pip install flask-login'
"""

from flask import Flask, render_template_string, request, url_for, redirect
from flask_login import (LoginManager, UserMixin, login_user, 
                            login_required, logout_user, current_user)
import sqlite3

# Define a function to get the user info from the db by its email
def get_user_by_email(email):
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    db_record = cursor.fetchone()
    conn.close()
    return db_record

# Define a basic User model for flask-login to hold user properties,
# this represents a user within the aplication (requires a unique user 
# identifier, which I find it easier to relate to the email of a user)
class User(UserMixin):
    def __init__(self, email):
        self.email = email
    
    def get_id(self):
        return self.email

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Create for each request a user instance based on the unique identifier 
    # stored in the session
    @login_manager.user_loader
    def load_user(email):
        # Fetch against the database a user by its 'email' field 
        db_user = get_user_by_email(email)
        if db_user is not None:
            # Create and return a new object of 'User' class.
           return User(email=db_user['email'])
        return None

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        # Redirect to protected view if authenticated (nice to have option)
        if current_user.is_authenticated:
            return redirect(url_for('protected'))

        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            db_record = get_user_by_email(email)

            if db_record and password == db_record['password']:
                user = User(email=db_record['email'])
                login_user(user)
                return redirect(url_for('protected'))

        return """<form method=post>
                Email: <input name="email" type="text"><br><br>
                Password: <input name="password" type="password"><br><br>
                <button>Log In</button>
                </form>
                """

    @app.route('/protected')
    @login_required
    def protected():
        return render_template_string(
            'Logged in as: {{ user.email }}',
            user=current_user)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    return app
