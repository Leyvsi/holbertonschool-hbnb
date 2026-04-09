#!/usr/bin/python3
import re
from app.models.base_model import BaseModel
from app import db, bcrypt
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    places = relationship('Place', backref='owner', lazy=True, cascade="all, delete-orphan")

    reviews = relationship('Review', backref='user', lazy=True, cascade="all, delete-orphan")
    
    def __init__(self, **kwargs):
        
        password = kwargs.pop('password', None)
        
        super().__init__(**kwargs)

        if not self.first_name or len(self.first_name) > 50:
            raise ValueError("First name is required (max 50 chars)")
        if not self.last_name or len(self.last_name) > 50:
            raise ValueError("Last name is required (max 50 chars)")

        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not self.email or not re.match(email_regex, self.email):
            raise ValueError("A valid email address is required")

        if password:
            self.hash_password(password)

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)