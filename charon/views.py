#Creation of URIs, passing to templates to create the frontend.

from flask import current_app, render_template

#Grabbing variable app from init file
from charon import app

#Grabbing Person model from models file in same directory
from .models import Person

@app.route('/')
def index():
	return "DEBUG={}".format(current_app.config.get('DEBUG'))

@app.route('/punch')
def punch():
	error = None

	return render_template('punch.html', error=error)