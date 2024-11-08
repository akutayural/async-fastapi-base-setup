# **Async FastAPI with PostgreSQL Base Project**

This project is a template for building asynchronous FastAPI applications integrated with PostgreSQL. It includes pre-configured CRUD operations, authentication, and a modular structure to jump-start your development.

---

## **Table of Contents**

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Setup Instructions](#setup-instructions)
5. [API Endpoints](#api-endpoints)
6. [CRUD Explanation](#crud-explanation)
7. [Live Demo](#live-demo)

---

## **Project Overview**

This repository provides a baseline setup for asynchronous FastAPI applications with PostgreSQL. It's designed for scalability, maintainability, and ease of use, making it ideal for API development.

---

## **Features**

- **Asynchronous Programming**: Powered by FastAPI, SQLAlchemy (async), and `asyncpg`.
- **JWT Authentication**: Secure token-based authentication system.
- **Modular Design**: Separate layers for models, routers, schemas, and CRUD operations.
- **Swagger UI**: Interactive API documentation at `/docs`.
- **Pydantic Validation**: Data validation for requests and responses.
- **Pre-configured Database Setup**: PostgreSQL integration using SQLAlchemy.

---

## **Project Structure**

```plaintext
async-fastapi-base-setup/
├── app/
│   ├── core/                 # Core application logic (e.g., authentication)
│   │   └── user.py           # User authentication logic
│   ├── cruds/                # CRUD operations
│   │   ├── base.py           # Generic CRUDBase class
│   │   └── user.py           # User-specific CRUD
│   ├── models/               # SQLAlchemy database models
│   │   ├── base.py           # Base model (common fields)
│   │   └── user.py           # User-specific model
│   ├── routers/              # API endpoints
│   │   ├── auth.py           # Authentication routes
│   │   ├── user.py           # User routes
│   │   ├── default.py        # Default routes
│   │   └── __init__.py       # Router initialization
│   ├── schemas/              # Pydantic models for validation
│   │   ├── user.py           # User schemas (Create, Update, etc.)
│   │   └── __init__.py       # ResponseModel and enums
│   ├── database.py           # Database session and engine setup
│   ├── dependencies.py       # Dependency injection for routes
│   ├── __init__.py           # FastAPI app creation and router inclusion
├── config.py                 # Environment variables and configuration
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation

## **Setup Instructions**
Step 1: Clone the Repository
```bash
git clone https://github.com/akutayural/async-fastapi-base-setup.git
cd async-fastapi-base-setup
```

**Step 2: Create a Virtual Environment**
```bash
python3.12 -m venv venv
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Configure Environment Variables**
Set up your .env file or environment variables with the following values:
```bash
SQLALCHEMY_DATABASE_URL="insert-db-url"
```

Step 5: Run the Application
```bash
uvicorn app:app --reload
```


## **API Endpoints**

![image](https://github.com/user-attachments/assets/557bcde2-1405-4f65-8d6b-9aa24654c93f)


## **CRUD Explanation**
Base CRUD: The CRUDBase class provides reusable methods for Create, Read, Update, and Delete (CRUD) operations. It can be extended for entity-specific logic.
Key Methods:

	•	get: Fetch a single record by ID.
	•	get_multi: Fetch multiple records with pagination.
	•	create: Add a new record to the database.
	•	update: Modify an existing record.
	•	remove: Delete a record by ID.

## **Live Demo**

The project is already deployed on a live web server. You can directly access the Swagger documentation and test the APIs using the following URL:

[**Live Swagger API**](https://user-auth-crru.onrender.com/docs#/)


