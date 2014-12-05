
from charon import db, app, manager

db.init_app(app)

if __name__ == '__main__':

	#need to do some database table checks and creations here

	manager.run()