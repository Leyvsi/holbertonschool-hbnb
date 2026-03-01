#!/usr/bin/python3
"""
Main application factory and API initialization.
"""
from flask import Flask
from flask_restx import Api

# Import the namespaces from your API modules
from app.api.v1.users import ns as users_ns
# Future namespaces to be imported as you develop them:
# from api.v1.places import ns as places_ns
# from api.v1.amenities import ns as amenities_ns
# from api.v1.reviews import ns as reviews_ns

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Initialize the API with basic metadata and Swagger documentation path
    api = Api(app,
              version='1.0',
              title='HBnB API',
              description='HBnB Application API Documentation',
              doc='/api/v1/' # URL for the Swagger UI
    )

    # Register the namespaces with their specific URL prefixes
    # This ensures that /api/v1/users/ is correctly mapped
    api.add_namespace(users_ns, path='/api/v1/users')

    # Placeholder for registering other namespaces later
    # api.add_namespace(places_ns, path='/api/v1/places')
    # api.add_namespace(amenities_ns, path='/api/v1/amenities')
    # api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
