"""
This is a boilerplate for doing a basic session management using
the Flask-Login module along with sqlite3. 

Make sure to open a terminal and run 'python init_db.py' to initialize the 
database before running the application.

Make sure to first install Flask-Login in the console with:
    'pip install flask-login'
"""

from flask import Flask, render_template_string, request, url_for, redirect
from flask_login import (LoginManager, UserMixin, login_user, 
                            login_required, logout_user, current_user)
import sqlite3

# Define a function to get a user from the db by its username
def get_user_by_username(username):
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    db_record = cursor.fetchone()
    conn.close()
    return db_record

# Define a basic User object for flask-login to hold user properties,
# this represents a user within the aplication (requires a unique user identifier)
class User(UserMixin):
    def __init__(self, id):
        self.id = id

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Create user instances from a loader callback to reload users from the
    # ID stored in the session
    @login_manager.user_loader
    def load_user(user_id):
        # Fetch against the database a user by 'user_id' 
        db_user = get_user_by_username(user_id)
        if db_user is not None:
            # Create and return a new object of 'User' class and return it.
           return User(id=db_user['username'])
        return None

    @app.route('/login', methods=('GET', 'POST'))
    def login():
        # Redirect to protected view if authenticated (nice to have option)
        if current_user.is_authenticated:
            return redirect(url_for('protected'))

        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            db_record = get_user_by_username(username)

            if db_record and password == db_record['password']:
                user = User(id=db_record['username'])
                login_user(user)
                return redirect(url_for('protected'))

        return """<form method=post>
                Username: <input name="username" type="text"><br><br>
                Password: <input name="password" type="password"><br><br>
                <button>Log In</button>
                </form>
                """

    @app.route('/protected')
    @login_required
    def protected():
        return render_template_string(
            'Logged in as: {{ user.id }}',
            user=current_user)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))


    return app
