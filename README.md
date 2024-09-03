# CRUD API Development - Item (Django)
## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used]()
- [Setup Instructions]()
- [Running the Application]()
- [API Usage]()
- [Swagger Documentation]()

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
