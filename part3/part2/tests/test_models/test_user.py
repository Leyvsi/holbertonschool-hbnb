import unittest
from app.models.user import User

class TestUser(unittest.TestCase):
    """Test suite for the User model"""

    def test_user_initialization(self):
        # Create a new user instance
        user = User(email="test@hbnb.com", first_name="John", last_name="Doe")

        # Check if attributes are correctly assigned
        self.assertEqual(user.email, "test@hbnb.com")
        self.assertEqual(user.first_name, "John")
        self.assertIsNotNone(user.id) # ID should be generated automatically

    def test_user_id_uniqueness(self):
        # Ensure two users have different unique IDs
        user1 = User(email="u1@hbnb.com", first_name="A", last_name="B")
        user2 = User(email="u2@hbnb.com", first_name="C", last_name="D")
        self.assertNotEqual(user1.id, user2.id)
