from pydantic import BaseModel, EmailStr
from typing import Optional

# Geo schema
class Geo(BaseModel):
    lat: str
    lng: str

# Address schema
class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo

# Company schema
class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str

# User schemas
class UserBase(BaseModel):
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

class UserCreate(UserBase):
    id: int

class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    address: Optional[Address] = None
    phone: Optional[str] = None
    website: Optional[str] = None
    company: Optional[Company] = None

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# Authentication schemas
class AuthUserBase(BaseModel):
    name: str
    email: str

class AuthUserCreate(AuthUserBase):
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
