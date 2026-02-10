```mermaid
classDiagram
    %% Presentation Layer: Handles user interface and API requests
    class PresentationLayer {
        <<Package>>
        +ServiceAPI
        +Controllers
    }

    %% Business Logic Layer: Contains models and core application rules
    class BusinessLogicLayer {
        <<Package>>
        +HBnBFacade
        +User
        +Place
        +Review
        +Amenity
    }

    %% Persistence Layer: Manages data storage and database access
    class PersistenceLayer {
        <<Package>>
        +DatabaseAccess
        +Repository
    }

    %% Relationships between layers
    %% The Presentation layer calls the Business Logic layer via the Facade
    PresentationLayer ..> BusinessLogicLayer : Uses (via HBnBFacade)
 
    %% The Business Logic layer requests data storage from the Persistence layer
    BusinessLogicLayer ..> PersistenceLayer : Persists Data
 
    %% Note to explain the Facade pattern role
    note for BusinessLogicLayer "The HBnBFacade acts as the\nunique entry point for the Presentation Layer"
