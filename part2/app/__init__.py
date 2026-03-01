#!/usr/bin/python3
"""
Main application factory and API initialization.
"""
from flask import Flask
from flask_restx import Api

from app.api.v1.users import ns as users_ns
from app.api.v1.amenities import ns as amenities_ns

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
    # 2. Register the namespaces HERE, after 'api' is defined
    # English comments: Registering user and amenity namespaces
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')


    return app
