from flask_migrate import Migrate
from sec_app.make_flask import app
from sec_app.make_database import db
from sec_app.models import Location

migrate = Migrate(app, db)
