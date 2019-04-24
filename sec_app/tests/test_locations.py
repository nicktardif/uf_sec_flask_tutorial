from flask_api import status
from sec_app import app, db
from sec_app.models import Location
from sec_app.tests.sample_test_case import SampleTestCase
import unittest

class GetLocationTest(SampleTestCase):
    def test_get_location(self):
        # Fill the database with a fake location
        new_location = Location('Westeros')
        db.session.add(new_location)
        db.session.commit()

        location_id = new_location.id
        response = self.client.get('/api/v1/location/{}'.format(location_id))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json, new_location.toJSON())

    def test_get_location_invalid_id(self):
        location_id = 1
        response = self.client.get('/api/v1/location/{}'.format(location_id))
        expected_response = {'error': 'Location with ID {} not found in the database'.format(location_id)}
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.json, expected_response)

class GetAllLocationsTest(SampleTestCase):
    @unittest.skip('yolo')
    def test_get_location(self):
        pass

    @unittest.skip('yolo')
    def test_get_location_no_data(self):
        pass
