from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # Get form information
        email = request.form.get('email')
        password = request.form.get('password')
        # Validate if user exists
        user = db.session.scalars(db.select(User).where(User.email==email)).first()
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))
        # Login user
        login_user(user)
        return redirect(url_for('main.profile'))
    return render_template('login.html')

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        # Get form information
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        # Validate if user already exists
        user = db.session.scalars(db.select(User).where(User.email==email)).first()
        if user:
            return redirect(url_for('auth.login'))
        # Validate if both passwords submitted are the same
        if password != confirm_password:
            return redirect(url_for('auth.signup'))
        # Create new user
        new_user = User(email=email, password=
                        generate_password_hash(password, 
                                               method='scrypt'))
        db.session.add(new_user)
        db.session.commit()
        # Redirect to login page
        return redirect(url_for('auth.login'))    
    return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
