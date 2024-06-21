from flask_login import UserMixin

# Define a basic User class
class User(UserMixin):
    def __init__(self, email, password):
        self.id = email
        self.password = password
