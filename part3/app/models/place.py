#!/usr/bin/python3
"""Place module"""
from app.models.base_model import BaseModel
from app import db

class Place(BaseModel):
    """Place entity representing property listings."""

    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, **kwargs):
        """Initialize Place with strict coordinate and price validation."""
        title = kwargs.get('title')
        price = kwargs.get('price', 0)
        latitude = kwargs.get('latitude', 0.0)
        longitude = kwargs.get('longitude', 0.0)


        if not title or len(title) > 100:
            raise ValueError("Title is required (max 100 chars)")
        if price <= 0:
            raise ValueError("Price must be a positive value")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90.0 and 90.0")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180.0 and 180.0")

        super().__init__(**kwargs)