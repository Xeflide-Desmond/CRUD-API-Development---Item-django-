# CRUD API Development - Item (Django)
## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Usage](#api-usage)
- [Swagger Documentation](#swagger-documentation)
- [Assumptions and Design Decisions](#assumptions-and-design-decisions)

# Project Overview
This project is a Django-based CRUD (Create, Read, Update, Delete) API for managing items. It allows users to create, retrieve, update, and delete items, with built-in pagination, filtering, and validation features. The project is built with RESTful principles and integrates Swagger for API documentation.

# Features
- CRUD operations for items.
- User authentication and authorization.
- Input validation for unique item names.
- Swagger documentation for easy API testing and exploration.
- Pagination and filtering of item listings.

# Technologies Used
- Python
- Django
- Django REST Framework
- SQLite (or any preferred database)
- Swagger via drf_yasg

# Setup Instructions
- Prerequisites
- Python 3.x
- pip (Python package installer)
- Git
- Virtualenv (optional but recommended)

## Clone the Repository
- git clone https://github.com/Xeflide-Desmond/CRUD-API-Development---Item-django-.git
- cd CRUD-API-Development---Item-django-

## Create and Activate a Virtual Environment
- python -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install Dependencies
pip install -r requirements.txt

## Apply Migrations
- python manage.py migrate

## Create a Superuser
- python manage.py createsuperuser

# Running the Application
- python manage.py runserver
- The application will be accessible at http://127.0.0.1:8000/.

# API Usage
The API provides the following endpoints:

- Create Item: POST /api/items/
- List Items: GET /api/items/
- Retrieve Item: GET /api/items/<id>/
- Update Item: PUT /api/items/<id>/
- Delete Item: DELETE /api/items/<id>/

# Swagger Documentation
- The API documentation is available via Swagger. You can access it at:
  http://127.0.0.1:8000/swagger/

# Assumptions and Design Decisions
  ## User Model:
- The last_modified_by field in the Item model is a foreign key to the Django User model. This assumes that every item modification must be associated with a registered user.
  
  ## Unique Item Names:
- The name field in the Item model is unique. This ensures that no two items can have the same name, simplifying retrieval and update operations.
  
  ## Transaction Handling:
- Certain operations, such as creating or updating items, are wrapped in database transactions to ensure atomicity. If an error occurs during these operations, all changes are rolled back.
  
  ## Validation and Error Handling:
- Custom error messages are provided for validation failures, such as when trying to create an item with a duplicate name.
