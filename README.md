# flask-for-everybody
A collection of (tested) snippets for using Flask

Each folder has a unique Flask app with the functionalities described in 
the folder name. The folder names are structured to provide a clear indication 
of the app's  purpose and the functionalities it includes.

Each folder tries to include only one or two new functionalities as standalone
applications, with the minimum code to perform such functionality. 

To run an app, download it, go to the folder and then execute it in the console 
with the 'flask run --debug' flag. If no flag is required, the app.py or 
__ init __.py will specify how to run the app; otherwise, use this command 
from the command line in each directory:

    flask run --debug

The following snippets are provided: 

a. The simplest Flask web application
b. Rendering HTML Templates (via the render_template function)
c. Template inheritance
d. Using forms and GET-POST requests
e. flash() messages
f. Using variables in routes
g. Loading .env and .flaskenv files
h. Basic user session management with Flask-Login
i. Using the application factory pattern
j. Using the application factory pattern with blueprints
p. User session management with Flask-Login and Flask-SQLAlchemy
q. User session management with Flask-Login, Flask-SQLAlchemy and Flask-Bcrypt