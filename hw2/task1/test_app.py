import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app import app
from database import get_db, Base
from models import User, AuthUser
from auth import get_password_hash

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

def override_get_db():
    """Override database dependency for testing"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)

@pytest.fixture
def db_session():
    """Database session fixture"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "id": 1,
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com",
        "address": {
            "street": "123 Test St",
            "suite": "Apt 1",
            "city": "Test City",
            "zipcode": "12345",
            "geo": {
                "lat": "40.7128",
                "lng": "-74.0060"
            }
        },
        "phone": "123-456-7890",
        "website": "test.com",
        "company": {
            "name": "Test Company",
            "catchPhrase": "Test phrase",
            "bs": "Test business"
        }
    }

@pytest.fixture
def auth_user(db_session):
    """Create an authentication user for testing"""
    hashed_password = get_password_hash("testpassword")
    user = AuthUser(
        name="Test Auth User",
        email="auth@example.com",
        password_hash=hashed_password
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def auth_token(client, auth_user):
    """Get authentication token for testing"""
    response = client.post("/auth/login", json={
        "email": "auth@example.com",
        "password": "testpassword"
    })
    return response.json()["access_token"]

class TestRootEndpoint:
    def test_root_endpoint(self, client):
        """Test root endpoint"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "JSONPlaceholder Clone API"
        assert data["version"] == "1.0.0"

class TestAuthentication:
    def test_register_user(self, client):
        """Test user registration"""
        response = client.post("/auth/register", json={
            "name": "New User",
            "email": "new@example.com",
            "password": "newpassword"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_register_duplicate_user(self, client, auth_user):
        """Test registration with duplicate email"""
        response = client.post("/auth/register", json={
            "name": "Another User",
            "email": "auth@example.com",
            "password": "password"
        })
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    def test_login_success(self, client, auth_user):
        """Test successful login"""
        response = client.post("/auth/login", json={
            "email": "auth@example.com",
            "password": "testpassword"
        })
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data

    def test_login_invalid_credentials(self, client):
        """Test login with invalid credentials"""
        response = client.post("/auth/login", json={
            "email": "wrong@example.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 401

class TestUserEndpoints:
    def test_get_users_unauthorized(self, client):
        """Test getting users without authentication"""
        response = client.get("/users")
        assert response.status_code == 401

    def test_get_users_authorized(self, client, auth_token):
        """Test getting users with authentication"""
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = client.get("/users", headers=headers)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_user_unauthorized(self, client):
        """Test getting specific user without authentication"""
        response = client.get("/users/1")
        assert response.status_code == 401

    def test_get_user_not_found(self, client, auth_token):
        """Test getting non-existent user"""
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = client.get("/users/999", headers=headers)
        assert response.status_code == 404

    def test_create_user(self, client, auth_token, sample_user_data):
        """Test creating a new user"""
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = client.post("/users", json=sample_user_data, headers=headers)
        assert response.status_code == 201
        data = response.json()
        assert data["id"] == sample_user_data["id"]
        assert data["name"] == sample_user_data["name"]

    def test_create_duplicate_user(self, client, auth_token, sample_user_data, db_session):
        """Test creating user with duplicate ID"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Try to create again
        response = client.post("/users", json=sample_user_data, headers=headers)
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"]

    def test_update_user(self, client, auth_token, sample_user_data, db_session):
        """Test updating a user"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Update the user
        update_data = {"name": "Updated Name"}
        response = client.put("/users/1", json=update_data, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Updated Name"

    def test_partial_update_user(self, client, auth_token, sample_user_data, db_session):
        """Test partial update of a user"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Partially update the user
        update_data = {"phone": "987-654-3210"}
        response = client.patch("/users/1", json=update_data, headers=headers)
        assert response.status_code == 200
        data = response.json()
        assert data["phone"] == "987-654-3210"
        assert data["name"] == sample_user_data["name"]  # Other fields unchanged

    def test_delete_user(self, client, auth_token, sample_user_data, db_session):
        """Test deleting a user"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Delete the user
        response = client.delete("/users/1", headers=headers)
        assert response.status_code == 204
        
        # Verify user is deleted
        get_response = client.get("/users/1", headers=headers)
        assert get_response.status_code == 404

class TestJSONPlaceholderCompatibility:
    def test_user_posts_endpoint(self, client, auth_token, sample_user_data, db_session):
        """Test JSONPlaceholder compatible posts endpoint"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Test posts endpoint (no auth required for compatibility)
        response = client.get("/users/1/posts")
        assert response.status_code == 200
        assert response.json() == []

    def test_user_todos_endpoint(self, client, auth_token, sample_user_data, db_session):
        """Test JSONPlaceholder compatible todos endpoint"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Test todos endpoint (no auth required for compatibility)
        response = client.get("/users/1/todos")
        assert response.status_code == 200
        assert response.json() == []

    def test_user_albums_endpoint(self, client, auth_token, sample_user_data, db_session):
        """Test JSONPlaceholder compatible albums endpoint"""
        # First create the user
        headers = {"Authorization": f"Bearer {auth_token}"}
        client.post("/users", json=sample_user_data, headers=headers)
        
        # Test albums endpoint (no auth required for compatibility)
        response = client.get("/users/1/albums")
        assert response.status_code == 200
        assert response.json() == []

if __name__ == "__main__":
    pytest.main([__file__])
