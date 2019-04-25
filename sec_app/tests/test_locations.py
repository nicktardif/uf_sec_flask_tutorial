from flask import jsonify
from flask_api import status
from sec_app import app, db
from sec_app.models import Location
from sec_app.tests.sample_test_case import SampleTestCase
import unittest

def populate_database(db):
    # Add some fake locations
    locations = []
    for name in ['Winterfell', 'The Wall', 'Hardhome']:
        new_location = Location(name)
        db.session.add(new_location)
        locations.append(new_location)
    db.session.commit()

class GetLocationTest(SampleTestCase):
    def test_get_location(self):
        populate_database(db)

        location_id = 1
        location = Location.query.get(location_id)

        response = self.client.get('/api/v1/locations/{}'.format(location_id))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json, location.toJSON())

    def test_get_location_invalid_id(self):
        location_id = 1
        response = self.client.get('/api/v1/locations/{}'.format(location_id))
        expected_response = {'error': 'Location with ID {} not found in the database'.format(location_id)}
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.json, expected_response)

class GetAllLocationsTest(SampleTestCase):
    def test_get_location(self):
        populate_database(db)

        locations = Location.query.all()

        response = self.client.get('/api/v1/locations')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json, jsonify(locations).json)

    def test_get_location_no_data(self):
        response = self.client.get('/api/v1/locations')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class CreateLocationTest(SampleTestCase):
    def test_create_location(self):
        data = {'name': 'Highgarden'}
        response = self.client.post('/api/v1/locations', data=data)

        expected_location_id = 1
        expected_response = Location.query.get(expected_location_id)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json, jsonify(expected_response).json)

    def test_create_location_missing_name(self):
        data = {'incorrect_field': 'bad'}
        response = self.client.post('/api/v1/locations', data=data)

        expected_response = {'error': 'Did not supply name in the data field'}
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json, jsonify(expected_response).json)

    def test_create_location_no_data_field(self):
        response = self.client.post('/api/v1/locations')

        expected_response = {'error': 'Request did not include a data form, try again'}
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json, jsonify(expected_response).json)

class UpdateLocationTest(SampleTestCase):
    def test_update_location(self):
        populate_database(db)

        location_id = 1
        data = {'name': 'Sunspear'}
        response = self.client.patch('/api/v1/locations/{}'.format(location_id), data=data)

        location = Location.query.get(location_id)

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json, jsonify(location).json)

    def test_update_location_invalid_id(self):
        location_id = 1
        data = {'name': 'Sunspear'}
        response = self.client.patch('/api/v1/locations/{}'.format(location_id), data=data)

        expected_response = {'error': 'Location with the ID {} does not exist in the database'.format(location_id)}
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.json, jsonify(expected_response).json)

    def test_update_location_no_name(self):
        location_id = 1
        data = {'library': 'Oldtown'}
        response = self.client.patch('/api/v1/locations/{}'.format(location_id), data=data)

        expected_response = {'error': 'Did not supply name in the data field'}
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json, jsonify(expected_response).json)

    def test_update_location_no_data(self):
        location_id = 1
        response = self.client.patch('/api/v1/locations/{}'.format(location_id))

        expected_response = {'error': 'Request did not include a data form, try again'}
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json, jsonify(expected_response).json)

class DeleteLocationTest(SampleTestCase):
    def test_delete_location(self):
        populate_database(db)
        location_id = 1
        response = self.client.delete('/api/v1/locations/{}'.format(location_id))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        # Check that the location is not in the database
        location = Location.query.get(location_id)
        self.assertEquals(location, None)

    def test_delete_location_invalid_id(self):
        location_id = 1
        response = self.client.delete('/api/v1/locations/{}'.format(location_id))

        expected_response = {'error': 'Location with the ID {} does not exist in the database'.format(location_id)}
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.json, jsonify(expected_response).json)
