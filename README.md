# HBnB Evolution - Technical Documentation

## 1. Introduction
The purpose of this document is to provide a comprehensive technical blueprint for the HBnB Evolution application. This project is a simplified version of an AirBnB-like system, focusing on user management, property listings, reviews, and amenities. This documentation guides the implementation phase by defining the architecture, data models, and interaction flows.

## 2. High-Level Architecture
The application follows a **Layered Architecture** to ensure a clean separation of concerns.
- **Presentation Layer**: Handles API requests and responses.
- **Business Logic Layer**: Contains the core logic and entities.
- **Persistence Layer**: Manages data storage.
- **Facade Pattern**: Used as a unified interface for communication between the Presentation and Business Logic layers.

[Link to Package Diagram](./0-high_level_package_diagram.md)

## 3. Business Logic Layer
The core of the system is built around several key entities:
- **User**: Manages profiles and administrative roles.
- **Place**: Represents property listings owned by users.
- **Review**: Stores user feedback and ratings for places.
- **Amenity**: Lists features available in places (e.g., WiFi, Pool).
All entities inherit from a **BaseModel** for consistent ID (UUID) and timestamp management.

[Link to Class Diagram](./1-detailed_class_diagram.md)

## 4. API Interaction Flow
The sequence diagrams illustrate how data flows through the system for the following operations:
1. **User Registration**: Creating a new account.
2. **Place Creation**: Listing a new property.
3. **Review Submission**: Rating a place.
4. **Fetching Places**: Retrieving the list of available properties.

[Link to Sequence Diagrams](./2-sequence_diagrams.md)

---

### How to use this documentation
1. Start with the **Package Diagram** to understand the global structure.
2. Review the **Class Diagram** to understand the data models.
3. Study the **Sequence Diagrams** to see how the code should behave during API calls.
