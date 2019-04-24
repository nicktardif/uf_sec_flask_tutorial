from sec_app import app, db
from flask_api import status
from sec_app.models import Location
from flask import jsonify

class LocationView():
    @app.route('/api/v1/location/<int:location_id>')
    def get_location(location_id):
        """Get a specified Location from the database
        ---
        definitions:
            Location:
                type: object
                properties:
                    id:
                        type: integer
                        example: 3
                    name:
                        type: string
                        example: Dragonstone
            ErrorResponse:
                type: object
                properties:
                    error:
                        type: string
                        example: Description of error is here
        tags:
         - locations
        parameters:
            - in: query
              description: Location ID to retrieve
              name: location_id
              required: true
              type: integer
        responses:
            200:
                description: Returns the location with the specified ID
                schema:
                    $ref: "#/definitions/Location"
            404:
                description: No location was found with the input ID
                schema:
                    $ref: "#/definitions/ErrorResponse"
        """
        location = Location.query.get(location_id)
        if location:
            return jsonify(location), status.HTTP_200_OK
        else:
            message = 'Location with ID {} not found in the database'.format(location_id)
            return jsonify({'error': message}), status.HTTP_404_NOT_FOUND

    @app.route('/api/v1/locations')
    def get_all_locations():
        """Get all locations from the database
        ---
        tags:
         - locations
        responses:
            200:
                description: Returns all the locations
                schema:
                    type: array
                    items:
                        $ref: "#/definitions/Location"
            204:
                description: No locations were in the database
        """
        locations = Location.query.all()
        if locations:
            return jsonify(locations), status.HTTP_200_OK
        else:
            return '', status.HTTP_204_NO_CONTENT
