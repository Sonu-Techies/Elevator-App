# Elevator System

This is a Django-based elevator system that allows the management of elevators in a building. It provides APIs for initializing the elevator system, managing elevators, handling user requests, and monitoring elevator status.

## Table of Contents

- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Database Modeling](#database-modeling)
- [API Contracts](#api-contracts)
- [Setup and Deployment](#setup-and-deployment)
- [Testing](#testing)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

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
- `POST /api/elevator/{id}/add_request`: Adds a user request for a given elevator.
- `POST /api/elevator/{id}/mark_maintenance`: Marks a given elevator as not working or in maintenance.
- `POST /api/elevator/{id}/open_door`: Opens the door of a given elevator.
- `POST /api/elevator/{id}/close_door`: Closes the door of a given elevator.


## Database Modeling

The database modeling includes three main models: `ElevatorSystem`, `Elevator`, `Floor`, and `Request`. The `ElevatorSystem` model represents the overall elevator system, `Elevator` represents the details of individual elevators, `Floor` represents the floors in the building, and `Request` represents the user requests for an elevator.

## API Contracts

The API contracts include the following endpoints:

- `POST /api/elevator/initialize_system`: Initializes the elevator system with 'n' elevators.
- `GET /api/elevator/{id}/requests`: Fetches all requests for a given elevator.
- `GET /api/elevator/{id}/next_destination`: Fetches the next destination floor for a given elevator.
- `GET /api/elevator/{id}/moving_direction`: Fetches the current moving direction of a given elevator.
- `POST /api/elevator/{id}/add_request`: Adds a user request for a given elevator.
- `POST /api/elevator/{id}/mark_maintenance`: Marks a given elevator as not working or in maintenance.
- `POST /api/elevator/{id}/open_door`: Opens the door of a given elevator.
- `POST /api/elevator/{id}/close_door`: Closes the door of a given elevator.

## Setup and Deployment

To set up and deploy the elevator system, follow these steps:

1. Clone the repository:
2. Install the dependencies using pip:

    $ pip install -r requirements/dev.txt
    
3. Set up the database (e.g., PostgreSQL or MySQL) and update the database configuration in `settings.py`.
4. Run the database migrations:
    
    $ python manage.py migrate

5. Start the development server

6. Access the APIs at `http://localhost:8000/api/elevator/`.

## Testing

To run the tests for the elevator system, use the following command:

    $ python manage.py test

