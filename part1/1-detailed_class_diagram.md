```markdown
```mermaid
classDiagram
    %% Base class for common attributes
    class BaseModel {
        +UUID id
        +DateTime created_at
        +DateTime updated_at
        +save()
        +update(dict data)
    }

    %% User Entity: Manages profile and roles
    class User {
        +String first_name
        +String last_name
        +String email
        +String password
        +Boolean is_admin
        +register()
        +update_profile()
    }

    %% Place Entity: Represents property listings
    class Place {
        +String title
        +String description
        +Float price
        +Float latitude
        +Float longitude
        +create()
        +update()
        +list_amenities()
    }

    %% Review Entity: User feedback for places
    class Review {
        +int rating
        +String comment
        +create()
        +update()
    }

    %% Amenity Entity: Features of a place
    class Amenity {
        +String name
        +String description
        +create()
        +update()
    }

    %% Relationships and Inheritance
    BaseModel <|-- User : Inherits
    BaseModel <|-- Place : Inherits
    BaseModel <|-- Review : Inherits
    BaseModel <|-- Amenity : Inherits

    User "1" --> "0..*" Place : Owns
    User "1" --> "0..*" Review : Writes
    Place "1" --> "0..*" Review : Has
    Place "0..*" -- "0..*" Amenity : Associated with
