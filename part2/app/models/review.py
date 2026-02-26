#!/usr/bin/python3
"""Review module"""
from app.models.base_model import BaseModel

class Review(BaseModel):
    """Review entity for user feedback on places."""

    def __init__(self, text, rating, place, user):
        """Initialize Review with rating and existence validation."""
        super().__init__()
        if not text:
            raise ValueError("Review text is required")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        if place is None or user is None:
            raise ValueError("Review must be linked to a valid Place and User")

        self.text = text
        self.rating = int(rating)
        self.place = place # Place instance
        self.user = user   # User instance

def create_review(self, review_data):
    # Placeholder for logic to create a review, including valid* for user_id, place_id, and rating
    pass

def get_review(self, review_id):
    # Placeholder for logic to retrieve a review by ID
    pass

def get_all_reviews(self):
    # Placeholder for logic to retrieve all reviews
    pass

def get_reviews_by_place(self, place_id):
    # Placeholder for logic to retrieve all reviews for a specific place
    pass

def update_review(self, review_id, review_data):
    # Placeholder for logic to up a review
    pass

def delete_review(self, review_id):
    # Placeholder for logic to dl a review
    pass
