#!/usr/bin/python3
"""
Facade module for handling business logic and repository interactions.
"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity

class HBnBFacade:
    def __init__(self):
        """Initialize repositories"""
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create and return a new user"""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve user by ID"""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Retrieve user by email"""
        return self.user_repo.get_by_attribute('email', email)

    # Amenity methods
    def create_amenity(self, amenity_data):
        """Create and return a new amenity"""
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        """Retrieve amenity by ID"""
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """Retrieve all amenities"""
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """Update and return amenity"""
        amenity = self.get_amenity(amenity_id)
        if not amenity:
            return None
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
        self.amenity_repo.update(amenity_id, amenity_data)
        return amenity

    # Place methods
    def create_place(self, place_data):
        owner = self.get_user(place_data['owner_id'])
        if not owner:
            raise ValueError("Owner not found")

        # Remove owner_id to not confuse Place constructor
        data = place_data.copy()
        owner_id = data.pop('owner_id')

        place = Place(owner=owner, **data)
        self.place_repo.add(place)
        return place

    def get_all_places(self):
        return self.place_repo.get_all()
