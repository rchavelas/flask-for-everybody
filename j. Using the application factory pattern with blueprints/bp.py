from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/profile')
def profile():
    return 'Profile page'
