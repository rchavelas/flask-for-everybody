"""
This is a boilerplate of a very simple Flask web application using  
Flask-WTF to show how to retrieve (request) information from forms using 
the WTForms integration to python. 
"""

from flask import Flask, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    input = StringField('input', validators=[DataRequired()])

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "very_secret_key"

    @app.route('/submit', methods=('GET', 'POST'))
    def submit():
        form = MyForm()
        if form.validate_on_submit():
            return "Success"
        return render_template_string('''
                    <form method="POST" action="/submit">
                        {{ form.csrf_token  }}
                        {{ form.input.label }} {{ form.input(size=20) }}
                        <input type="submit" value="Submit">
                    </form>''', form=form)

    return app
