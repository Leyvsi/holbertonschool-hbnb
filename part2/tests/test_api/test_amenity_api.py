import unittest
import json
from app import create_app

class TestAmenityAPI(unittest.TestCase):
    def setUp(self):
        """Set up the test client before each test."""
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        """Test successful amenity creation."""
        response = self.client.post('/api/v1/amenities/', 
                                    data=json.dumps({'name': 'WiFi'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('WiFi', str(response.data))

    def test_get_amenities(self):
        """Test retrieving the list of amenities."""
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
