#!/usr/bin/python3
import unittest
import json
import uuid # Needed for unique emails
from app import create_app

class TestPlaceAPI(unittest.TestCase):
    def setUp(self):
        """Set up test client and a default user for ownership"""
        self.app = create_app()
        self.client = self.app.test_client()

        # Generate a unique email to avoid "Email already exists" errors
        unique_email = f"owner_{uuid.uuid4().hex[:6]}@hbnb.com"

        # This block must be indented to be inside setUp
        user_data = {
            "first_name": "Owner",
            "last_name": "User",
            "email": unique_email,
            "password": "password123"
        }

        # Create user and store the ID
        resp = self.client.post('/api/v1/users/', json=user_data)
        self.owner_id = json.loads(resp.data)['id']

    def test_create_place_success(self):
        """Test successful place creation with valid data"""
        place_data = {
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner_id": self.owner_id
        }
        # Simplified post call
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_price(self):
        """Test validation: negative price should fail"""
        place_data = {
            "title": "Cheap Room",
            "price": -10.0,
            "latitude": 0.0,
            "longitude": 0.0,
            "owner_id": self.owner_id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_coords(self):
        """Test validation: latitude out of bounds should fail"""
        place_data = {
            "title": "Mars Base",
            "price": 500.0,
            "latitude": 150.0, # Max is 90
            "longitude": 0.0,
            "owner_id": self.owner_id
        }
        response = self.client.post('/api/v1/places/', json=place_data)
        self.assertEqual(response.status_code, 400)
