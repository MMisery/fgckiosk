#Creation of URIs, passing to templates to create the frontend.

from flask import current_app, render_template

#Grabbing variable app from init file
from charon import app

#Grabbing Person model from models file in same directory
from .models import Person