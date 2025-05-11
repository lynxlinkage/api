# FastAPI Service with PostgreSQL and User Management

A simple FastAPI service with a health check endpoint, PostgreSQL database connection, and user management functionality.

## Features

- Health check endpoint
- PostgreSQL database integration with SQLAlchemy
- Complete user management
  - User registration
  - Authentication with JWT tokens
  - User profile management
  - Admin capabilities for user management

## Setup and Installation

### 1. Set up PostgreSQL

Make sure PostgreSQL is installed and running on your system. Create a database called `pms`:

```bash
createdb pms
```

### 2. Install dependencies

```bash
pip install -r requirement.txt
```

### 3. Initialize the database

Run the initialization script to create tables and set up the admin user:

```bash
python -m app.db.init_db
```

## Run the application

Start the FastAPI application with uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at http://localhost:8000

## API Endpoints

- Health check: `GET /health`
- API documentation: `GET /docs`
- Authentication: `POST /login/access-token`
- User management:
  - List users: `GET /users/`
  - Create user: `POST /users/`
  - Current user profile: `GET /users/me`
  - Update profile: `PUT /users/me`
  - User details: `GET /users/{user_id}`
  - Update user: `PUT /users/{user_id}`
  - Delete user: `DELETE /users/{user_id}`

## Default admin credentials

- Username: `admin`
- Password: `admin`
- Email: `admin@example.com`

**Note:** Make sure to change these in a production environment!