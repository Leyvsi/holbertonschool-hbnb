import unittest
from app import create_app

class TestUserAPI(unittest.TestCase):
    """Test suite for User API endpoints"""

    def setUp(self):
        # Set up a test client for the Flask app
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        # Send a POST request to create a user
        response = self.client.post('/api/v1/users/', json={
            "email": "new@hbnb.com",
            "first_name": "Alice",
            "last_name": "Smith"
        })

        # Check if the status code is 201 (Created)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Alice", response.get_data(as_text=True))
