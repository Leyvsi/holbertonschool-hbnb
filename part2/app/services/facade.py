#!/usr/bin/python3
"""
Facade module for handling business logic and repository interactions.
"""
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

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

    def get_all_users(self):
        """Retrieve all users"""
        return self.user_repo.get_all()

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
        """Create a place with owner validation"""
        owner = self.get_user(place_data.get('owner_id'))
        if not owner:
            raise ValueError("Owner not found")

        data = place_data.copy()
        data.pop('owner_id', None)

        place = Place(owner=owner, **data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Retrieve place by ID"""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Retrieve all places"""
        return self.place_repo.get_all()

    # Review methods
    def create_review(self, review_data):
        """Create a review with user and place validation"""
        user = self.get_user(review_data.get('user_id'))
        place = self.get_place(review_data.get('place_id'))

        if not user or not place:
            raise ValueError("Invalid User or Place ID")

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            place=place,
            user=user
        )
        self.review_repo.add(review)
        return review

    def get_all_reviews(self):
        """Retrieve all reviews"""
        return self.review_repo.get_all()
