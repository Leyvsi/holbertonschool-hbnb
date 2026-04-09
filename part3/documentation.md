# Documentation Technique - HBnB Project

## Schéma de la Base de Données (ER Diagram)

Voici la structure des tables et leurs relations générée avec Mermaid.js.

```mermaid
erDiagram
    USER ||--o{ PLACE : "owns"
    USER ||--o{ REVIEW : "writes"
    PLACE ||--o{ REVIEW : "receives"
    PLACE }o--o{ AMENITY : "has"

    USER {
        string id PK
        string first_name
        string last_name
        string email UK
        string password
        boolean is_admin
    }

    PLACE {
        string id PK
        string title
        string description
        float price
        float latitude
        float longitude
        string owner_id FK
    }

    REVIEW {
        string id PK
        string text
        int rating
        string user_id FK
        string place_id FK
    }

    AMENITY {
        string id PK
        string name UK
    }

    PLACE_AMENITY {
        string place_id FK
        string amenity_id FK
    }
