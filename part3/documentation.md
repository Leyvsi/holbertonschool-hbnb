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
        varchar id PK
        varchar first_name
        varchar last_name
        varchar email UK
        varchar password
        boolean is_admin
    }

    PLACE {
        varchar id PK
        varchar title
        varchar description
        float price
        float latitude
        float longitude
        varchar owner_id FK
    }

    REVIEW {
        varchar id PK
        varchar text
        int rating
        varchar user_id FK
        varchar place_id FK
    }

    AMENITY {
        varchar id PK
        varchar name UK
    }

    PLACE_AMENITY {
        varchar place_id FK
        varchar amenity_id FK
    }
