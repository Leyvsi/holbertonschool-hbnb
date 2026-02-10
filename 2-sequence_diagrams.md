```markdown
```mermaid
sequenceDiagram
    autonumber
    %% Participants for all scenarios
    participant Client
    participant API
    participant Facade
    participant DB

    %% 1. User Registration Flow
    Note over Client, DB: User Registration
    Client->>API: POST /users
    API->>Facade: register_user(data)
    Facade->>DB: check_email(email)
    DB-->>Facade: Not Found
    Facade->>DB: save_user(user)
    DB-->>Facade: Success
    Facade-->>API: User Object
    API-->>Client: 201 Created

    %% 2. Place Creation Flow
    Note over Client, DB: Place Creation
    Client->>API: POST /places
    API->>Facade: create_place(data)
    Facade->>DB: get_user(owner_id)
    DB-->>Facade: User exists
    Facade->>DB: save_place(place)
    DB-->>Facade: Success
    Facade-->>API: Place ID
    API-->>Client: 201 Created

    %% 3. Review Submission Flow
    Note over Client, DB: Review Submission
    Client->>API: POST /reviews
    API->>Facade: add_review(data)
    Facade->>DB: validate_entities(ids)
    DB-->>Facade: Valid
    Facade->>DB: save_review(review)
    DB-->>Facade: Success
    Facade-->>API: Success
    API-->>Client: 201 Created

    %% 4. Fetching Places Flow
    Note over Client, DB: Fetching Places
    Client->>API: GET /places
    API->>Facade: get_all_places()
    Facade->>DB: fetch_records()
    DB-->>Facade: List of objects
    Facade-->>API: JSON List
    API-->>Client: 200 OK
