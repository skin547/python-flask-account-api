# Account API

## Overview
This project provides a solution for managing user accounts through two RESTful APIs: one for account creation and another for account verification. Implemented in Python using Flask and SQLAlchemy, the solution employs Docker for containerization.

## Features
1. **Create Account**: Register a new user account.
2. **Verify Account**: Authenticate user credentials.
3. **Error Handling & Validation**: Thorough input validation and proper error responses.
4. **Persistent Storage**: MySQL database management via SQLAlchemy.

## API Documentation

### 1. Create Account
- **Endpoint**: `/create`
- **Method**: `POST`
- **Request Payload**:
```
{
    "username": "example_user",
    "password": "example_password"
}
```

- **Response**:
- `201 Created`: Account successfully created.
- `400 Bad Request`: Invalid/missing input or username already taken.

### 2. Verify Account
- **Endpoint**: `/verify`
- **Method**: `POST`
- **Request Payload**:
```
{
    "username": "example_user",
    "password": "example_password"
}
```

- **Response**:
- `200 OK`: Credentials verified successfully.
- `401 Unauthorized`: Invalid credentials.

## Setup and Usage Instructions

### Prerequisites
1. Install [Docker](https://docs.docker.com/get-docker/).

### Building and Running the Docker Container
1. **Edit Environment Variables**: Update database credentials in the `.env` file as required.
2. **Build Docker Image**:
  ```
  docker build -t account-api .
  ```
3. **Run the Docker Container**:
  ```
  docker run -d -p 80:5000 --env-file .env account-api
  ```
4. **Or, To quickly set up the application and MySQL database locally with Docker Compose**:
  ```
  docker-compose up -d
  ```

### Testing the API
1. **Create Account**:
  ```
  curl -X POST http://localhost/create \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "TestPassword123!"}'
  ```
2. **Verify Account**:
  ```
  curl -X POST http://localhost/verify \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "TestPassword123!"}'
  ```