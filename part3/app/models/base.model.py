#!/usr/bin/python3
"""
BaseModel module
Provides the base class for all entities in the HBnB application.
"""
import uuid
from datetime import datetime
from hbnb.app.extensions import db

class BaseModel:
    """Base class that defines all common attributes/methods for other classes."""

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        """Initialize a new base model instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified."""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update object attributes based on a dictionary of new values."""
        for key, value in data.items():
            if hasattr(self, key) and key not in ['id', 'created_at', 'updated_at']:
                setattr(self, key, value)
    
    def to_dict(self):
        result = {}

        for column in self.__table__.columns:
            key = column.name
            value = getattr(self, key)

            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value

        return result
