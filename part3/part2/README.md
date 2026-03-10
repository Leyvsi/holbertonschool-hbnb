HBnB Evolution - Business Logic & API Implementation
1. Introduction
Following the architectural blueprints defined in Part 1, this phase focuses on the actual implementation of the HBnB Evolution core. We transition from conceptual UML diagrams to a functional RESTful API. This stage implements the Business Logic Layer, the Presentation Layer, and an initial In-Memory Persistence Layer to validate the system's behavior.

2. Implementation Architecture
The codebase strictly follows the Layered Architecture and the Facade Pattern to ensure modularity:

Services (Facade): A unified interface that mediates between the API controllers and the underlying models.

Models: Python implementation of the User, Place, Review, and Amenity entities.

Data Validation: Logic to ensure data integrity (e.g., unique emails, valid ratings).

In-Memory Storage: A temporary repository used to store objects during runtime before the SQL integration in Part 3.

3. Core Entities & Business Rules
Every entity inherits from a BaseModel to provide a consistent structure:

User: Handles authentication and profile data.

Place: Manages listings, linked to a specific Owner (User).

Review: Links a User to a Place with a rating and comment.

Amenity: Represents individual features (e.g., "WiFi", "Air Conditioning").

4. API Endpoints (Presentation Layer)
The API is organized into versioned namespaces (/api/v1/). Key endpoints implemented in this phase:

/users/	POST	Create a new user profile
/places/	GET	Retrieve all property listings
/reviews/	POST	Submit feedback for a specific place
/amenities/	GET	List all available features

5. Development Setup
To run the application locally:

1.Environment: Ensure Python 3.10+ is installed.
2.Dependencies: Install the required packages:
 pip install -r requirements.txt

3.Run: Execute the main entry point:
 python run.py

 How to explore this implementation
Check the /models/ directory: To see the OOP implementation of the business entities.

Check the /api/ directory: To see how Flask-RESTX defines the endpoints and namespaces.

Check the /services/ directory: To see the Facade pattern in action, centralizing the app logic.
