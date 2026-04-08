#!/usr/bin/python3
"""Review repository"""
from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository

class ReviewRepository(SQLAlchemyRepository):
    """Repository for Review operations using SQLAlchemy"""
    def __init__(self):
        super().__init__(Review)
