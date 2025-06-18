# JSONPlaceholder Clone API

A backend API that replicates the behavior and structure of [JSONPlaceholder](https://jsonplaceholder.typicode.com) with extended support for full REST operations, JWT-based authentication, structured user data storage, and containerized deployment.

## Features

- ✅ **Full REST API**: Complete CRUD operations for users
- ✅ **JWT Authentication**: Secure token-based authentication
- ✅ **PostgreSQL Database**: Robust data storage with JSON fields
- ✅ **Docker Containerization**: Easy deployment with Docker Compose
- ✅ **JSONPlaceholder Compatibility**: Maintains compatibility with original API
- ✅ **Comprehensive Testing**: Unit and integration tests
- ✅ **Input Validation**: Pydantic-based request/response validation
- ✅ **Auto-seeding**: Automatic database seeding with JSONPlaceholder data

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic
- **Testing**: pytest
- **Containerization**: Docker & Docker Compose

## Quick Start

### Using Docker (Recommended)

1. **Clone and navigate to the project**:
   ```bash
   cd task1
   ```

2. **Start the application**:
   ```bash
   docker-compose up --build
   ```

3. **Access the API**:
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/

### Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL database**:
   ```bash
   # Create database
   createdb jsonplaceholder
   
   # Set environment variable
   export DATABASE_URL="postgresql://postgres:password@localhost:5432/jsonplaceholder"
   ```

3. **Run the application**:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

## API Endpoints

### Authentication

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword"
}
```

### Users (Requires Authentication)

#### Get All Users
```http
GET /users
Authorization: Bearer <your-jwt-token>
```

#### Get User by ID
```http
GET /users/{id}
Authorization: Bearer <your-jwt-token>
```

#### Create User
```http
POST /users
Authorization: Bearer <your-jwt-token>
Content-Type: application/json

{
  "id": 11,
  "name": "New User",
  "username": "newuser",
  "email": "newuser@example.com",
  "address": {
    "street": "123 Main St",
    "suite": "Apt 1",
    "city": "New York",
    "zipcode": "10001",
    "geo": {
      "lat": "40.7128",
      "lng": "-74.0060"
    }
  },
  "phone": "123-456-7890",
  "website": "newuser.com",
  "company": {
    "name": "New Company",
    "catchPhrase": "Innovative solutions",
    "bs": "revolutionary paradigms"
  }
}
```

#### Update User (Full)
```http
PUT /users/{id}
Authorization: Bearer <your-jwt-token>
Content-Type: application/json

{
  "name": "Updated Name",
  "email": "updated@example.com"
}
```

#### Update User (Partial)
```http
PATCH /users/{id}
Authorization: Bearer <your-jwt-token>
Content-Type: application/json

{
  "phone": "987-654-3210"
}
```

#### Delete User
```http
DELETE /users/{id}
Authorization: Bearer <your-jwt-token>
```

### JSONPlaceholder Compatible Endpoints (No Auth Required)

#### Get User Posts
```http
GET /users/{id}/posts
```

#### Get User Todos
```http
GET /users/{id}/todos
```

#### Get User Albums
```http
GET /users/{id}/albums
```

## Data Models

### User Model
```typescript
interface Geo {
  lat: string;
  lng: string;
}

interface Address {
  street: string;
  suite: string;
  city: string;
  zipcode: string;
  geo: Geo;
}

interface Company {
  name: string;
  catchPhrase: string;
  bs: string;
}

interface User {
  id: number;
  name: string;
  username: string;
  email: string;
  address: Address;
  phone: string;
  website: string;
  company: Company;
}
```

## Database Schema

The application uses PostgreSQL with the following schema:

### Users Table
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR(255))
- `username` (VARCHAR(100), UNIQUE)
- `email` (VARCHAR(255), UNIQUE)
- `address` (JSONB) - Stores address object
- `phone` (VARCHAR(50))
- `website` (VARCHAR(255))
- `company` (JSONB) - Stores company object

### Auth Users Table
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR(255))
- `email` (VARCHAR(255), UNIQUE)
- `password_hash` (VARCHAR(255))

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest test_app.py

# Run with verbose output
pytest -v
```

### Test Coverage

The test suite covers:
- ✅ Authentication (register, login)
- ✅ User CRUD operations
- ✅ Authorization requirements
- ✅ Input validation
- ✅ Error handling
- ✅ JSONPlaceholder compatibility endpoints

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `postgresql://postgres:password@localhost:5432/jsonplaceholder` | Database connection string |
| `SECRET_KEY` | `your-secret-key-here-change-in-production` | JWT secret key |

## Development

### Project Structure
```
task1/
├── app.py              # Main FastAPI application
├── database.py         # Database configuration
├── models.py           # SQLAlchemy models
├── schemas.py          # Pydantic schemas
├── auth.py             # JWT authentication
├── seed_data.py        # Database seeding
├── test_app.py         # Test suite
├── requirements.txt    # Python dependencies
├── Dockerfile          # Application container
├── docker-compose.yml  # Multi-container setup
└── README.md           # This file
```

### Adding New Features

1. **Database Models**: Add to `models.py`
2. **API Schemas**: Add to `schemas.py`
3. **API Endpoints**: Add to `app.py`
4. **Tests**: Add to `test_app.py`

## Security Features

- **Password Hashing**: bcrypt with salt
- **JWT Tokens**: Secure token-based authentication
- **Input Validation**: Pydantic schema validation
- **SQL Injection Protection**: SQLAlchemy ORM
- **CORS Support**: Configurable CORS middleware

## Performance Features

- **Database Connection Pooling**: SQLAlchemy connection management
- **JSONB Fields**: Efficient JSON storage in PostgreSQL
- **Indexed Fields**: Primary keys and unique constraints
- **Health Checks**: Container health monitoring

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Ensure PostgreSQL is running
   - Check `DATABASE_URL` environment variable
   - Verify database exists

2. **Port Already in Use**:
   - Change port in `docker-compose.yml`
   - Or stop existing services using port 8000

3. **Authentication Errors**:
   - Verify JWT token is valid
   - Check token expiration (30 minutes default)
   - Ensure proper Authorization header format

### Logs

View application logs:
```bash
# Docker logs
docker-compose logs app

# Follow logs
docker-compose logs -f app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Run the test suite
6. Submit a pull request

## License

This project is for educational purposes and replicates the JSONPlaceholder API structure.
