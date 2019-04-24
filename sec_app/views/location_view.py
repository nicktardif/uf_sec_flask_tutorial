from sec_app import app, db
from flask_api import status
from sec_app.models import Location
from flask import jsonify

class LocationView():
    @app.route('/api/v1/location/<int:location_id>')
    def get_location(location_id):
        location = Location.query.get(location_id) 
        if location:
            return jsonify(location), status.HTTP_200_OK
        else:
            message = 'Location with ID {} not found in the database'.format(location_id)
            return jsonify({'error': message}), status.HTTP_404_NOT_FOUND
