# Elevator System

This is a Django-based elevator system that allows the management of elevators in a building. It provides APIs for initializing the elevator system, managing elevators, handling user requests, and monitoring elevator status.

## Table of Contents

- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Database Modeling](#database-modeling)
- [API Contracts](#api-contracts)
- [Dependencies](#dependencies)
- [Plugins or Libraries](#plugins-or-libraries)
- [Setup and Deployment](#setup-and-deployment)
- [Testing](#testing)


## Architecture

The elevator system is built using Django, a popular Python web framework, along with Django Rest Framework (DRF) for building RESTful APIs. The system follows a Model-View-Controller (MVC) architecture pattern, with models representing the database structure, views handling the API requests, and serializers for data serialization/deserialization.

## Repository Structure

The repository has the following structure:

elevator_system/
├── core/ # Core Django app (base models, utilities, etc.)
├── elevator_workflow/ # Elevator workflow app (Elevator, Floor, Request models)
├── elevator_api/ # Elevator API app (API views, serializers, etc.)
├── manage.py # Django management script
└── README.md # Project README file


## Database Modeling

The database modeling includes three main models: `ElevatorSystem`, `Elevator`, `Floor`, and `Request`. The `ElevatorSystem` model represents the overall elevator system, `Elevator` represents the details of individual elevators, `Floor` represents the floors in the building, and `Request` represents the user requests for an elevator.

## API Contracts

The API contracts include the following endpoints:

- `POST /api/elevator/initialize_system`: Initializes the elevator system with 'n' elevators.
- `GET /api/elevator/{id}/requests`: Fetches all requests for a given elevator.
- `GET /api/elevator/{id}/next_destination`: Fetches the next destination floor for a given elevator.
- `GET /api/elevator/{id}/moving_direction`: Fetches the current moving direction of a given elevator.
- `POST /api/elevator/{id}/add_request`: Adds a user request for a given optimal elevator.
- `POST /api/elevator/{id}/mark_maintenance`: Marks a given elevator as not working or in maintenance.
- `POST /api/elevator/{id}/open_door`: Opens the door of a given elevator.
- `POST /api/elevator/{id}/close_door`: Closes the door of a given elevator.
- `GET & POST /api/elevator-system/`:  Give the detail of elevator system.
- `GET & POST /api/elevator/`:  Give the list and detail of indivisual elevator system.
- `GET & POST /api/review/`:  User Feedback/ Review from particualar request with elevator.
- `GET & POST /api/request/`:  Give the detail of correspondent Request.
- `GET & POST /api/floor/`:  Give the detail of assosiated floor.


## Dependencies

The project has the following dependencies:

- asgiref==3.7.2
- Django==4.2.2
- djangorestframework==3.14.0
- exceptiongroup==1.1.1
- iniconfig==2.0.0
- model-bakery==1.12.0
- packaging==23.1
- pluggy==1.2.0
- psycopg2-binary==2.9.6
- pytest==7.4.0
- pytz==2023.3
- sqlparse==0.4.4
- tomli==2.0.1
- typing_extensions==4.6.3

## Plugins or Libraries

The following plugins or libraries are used in the project:

- [Django](https://www.djangoproject.com/): A Python web framework for building web applications.
- [Django Rest Framework](https://www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs.
- [model_bakery](https://github.com/model-bakers/model_bakery): A library for creating model instances for testing purposes.


## Setup and Deployment

To set up and deploy the elevator system, follow these steps:

1. Clone the repository:
2. Install the dependencies using pip:

    $ pip install -r requirements.txt
    
3. Set up the database (e.g., PostgreSQL or MySQL) and update the database configuration in `settings.py`.
4. Run the database migrations:
    
    $ python manage.py migrate

5. Start the development server

6. Access the APIs at `http://localhost:8000/api/`.

## Testing

To run the tests for the elevator system, use the following command:

    $ python manage.py test

