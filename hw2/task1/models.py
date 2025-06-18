from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from database import Base

class User(Base):
    """User model matching JSONPlaceholder structure"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    address = Column(JSON, nullable=False)  # Store address as JSON
    phone = Column(String(50), nullable=False)
    website = Column(String(255), nullable=False)
    company = Column(JSON, nullable=False)  # Store company as JSON

class AuthUser(Base):
    """Authentication user model for JWT authentication"""
    __tablename__ = "auth_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
