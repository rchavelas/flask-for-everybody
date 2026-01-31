"""
This is a boilerplate for doing very basic session management using 
the Flask-Login package. 

See: https://github.com/maxcountryman/flask-login?tab=readme-ov-file

Make sure to first install Flask-Login in the console with:
    
    'pip install flask-login'

"""
from flask import Flask, request, redirect, url_for, render_template_string
from flask_login import (LoginManager, login_required, current_user,
                         login_user, logout_user)
from models import User

# Authorized users (using a list as a simple representation of a database)
users = {"usr1@mail.com": User("usr1@mail.com", "secretPsw")}

app = Flask(__name__)
app.secret_key = "super secret string" # Change this!

# Define de login manager for Flask-login to work correctly
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(id):
    return users.get(id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = users.get(request.form['email'])
        if user is None or user.password != request.form['password']:
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('protected'))
    # If the request is not POST (thus, the default, GET)
    else:
        return """<form method=post>
                Email: <input name="email"><br><br>
                Password: <input name="password" type="password"><br><br>
                <button>Log In</button>
                </form>
                """

@app.route('/protected')
@login_required
def protected():
    return render_template_string(
        'Logged in as: {{ user.id }}',
        user=current_user
    )

@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'

if __name__ == '__main__':
    app.run()
