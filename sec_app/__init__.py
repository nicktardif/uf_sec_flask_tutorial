from sec_app.make_flask import app
from sec_app.make_database import db

from flask_migrate import Migrate
from sec_app.utilities import CustomJSONEncoder
from sec_app.views import LocationView

migrate = Migrate(app, db)
app.json_encoder = CustomJSONEncoder
