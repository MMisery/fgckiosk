#Backend of the application, setting up the database and establishing the ORM.
from datetime import datetime

from sqlalchemy import Column, Integer, Unicode, ForeignKey, DateTime, Boolean, Time

#Grabbing db variable from init file
from . import db

class Person(db.Model):

	"""
	Generic model to interact with the database.
	Will be extending this for more specific cases
	"""

	name = Column(Unicode(100), primary_key=True)

	#Need to be able to take in a time. May be converting to and from 24-hour format.

	time_in = Column(Time)
	time_out = Column(Time)
	orientation = Column(Boolean)


	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Person %r>' % self.name

