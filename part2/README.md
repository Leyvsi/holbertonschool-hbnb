HBnB - BL and API
Part 2: Business Logic & API Development
This phase marks the transition from design to implementation. We are building the core of the HBnB Evolution application using the Flask framework, focusing on the Business Logic Layer and the Presentation Layer (RESTful API).

Key Features
Layered Architecture: Strict separation between the Presentation (API), Business Logic (Services/Models), and Persistence layers.

Core Entities: Implementation of User, Place, Review, and Amenity classes with full validation.

Repository Pattern: Implementation of an in-memory storage system to abstract data access before the database integration.

RESTful API: Development of endpoints to perform CRUD (Create, Read, Update, Delete) operations on all entities.

Example : 
# Implementation of the User model with business rules
class User(BaseModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        # Validate email format and uniqueness
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        # Placeholder for associated reviews
        self.reviews = []

API EndpointsThe API is structured to handle requests following REST principles:
Entity,Method,Endpoint,Description
User,POST,/api/v1/users/,Register a new user
Place,GET,/api/v1/places/,Retrieve a list of all places
Review,POST,/api/v1/reviews/,Post a new review for a place
Amenity,PUT,/api/v1/amenities/<id>,Update an amenity's details

How to Run and Test
Install Dependencies:
pip install -r requirements.txt
Start the Flask Server:
python run.py

API Documentation: Access the interactive Swagger documentation at http://localhost:5000/api/v1/docs.
