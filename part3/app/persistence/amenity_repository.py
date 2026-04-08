#!/usr/bin/python3
"""Amenity repository"""
from app.models.amenity import Amenity
from app.persistence.repository import SQLAlchemyRepository

class AmenityRepository(SQLAlchemyRepository):
    """Repository for Amenity operations using SQLAlchemy"""
    def __init__(self):
        super().__init__(Amenity)
