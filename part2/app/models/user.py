#!/usr/bin/python3
"""User module"""
import re
from app.models.base_model import BaseModel

class User(BaseModel):
    """User entity with specific validation constraints."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        """Initialize User with required attributes and validation."""
        super().__init__()
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required (max 50 chars)")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required (max 50 chars)")

        # Email validation with regex
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not email or not re.match(email_regex, email):
            raise ValueError("A valid email address is required")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
